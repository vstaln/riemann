#include <array>
#include <bit>
#include <cfenv>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

#pragma STDC FENV_ACCESS ON

namespace {
constexpr int kGrid = 4000;
constexpr int kPressureDenominator = 1920;
constexpr int kTargetNumerator = 563;
constexpr int kTargetDenominator = 100000;
constexpr int kPressureCutoffCells = 43239;
constexpr int kTableCells = kPressureCutoffCells + 8;
constexpr double kNegativeInfinity = -std::numeric_limits<double>::infinity();
constexpr double kPositiveInfinity = std::numeric_limits<double>::infinity();

static_assert(std::numeric_limits<double>::is_iec559,
              "the verifier requires IEEE-754 binary64");

inline double DownAdd(double left, double right) {
  return std::nextafter(left + right, kNegativeInfinity);
}
inline double DownMultiply(double left, double right) {
  return std::nextafter(left * right, kNegativeInfinity);
}
inline double DownRatio(std::uint64_t numerator, std::uint64_t denominator) {
  return std::nextafter(static_cast<double>(numerator) /
                            static_cast<double>(denominator),
                        kNegativeInfinity);
}
inline double UpRatio(std::uint64_t numerator, std::uint64_t denominator) {
  return std::nextafter(static_cast<double>(numerator) /
                            static_cast<double>(denominator),
                        kPositiveInfinity);
}

std::uint32_t ReadBigEndian32(std::istream& input) {
  unsigned char bytes[4];
  input.read(reinterpret_cast<char*>(bytes), 4);
  if (!input) throw std::runtime_error("truncated table header");
  return (std::uint32_t(bytes[0]) << 24) |
         (std::uint32_t(bytes[1]) << 16) |
         (std::uint32_t(bytes[2]) << 8) | std::uint32_t(bytes[3]);
}

double ReadBigEndianDouble(std::istream& input) {
  unsigned char bytes[8];
  input.read(reinterpret_cast<char*>(bytes), 8);
  if (!input) throw std::runtime_error("truncated table data");
  std::uint64_t bits = 0;
  for (unsigned char byte : bytes) bits = (bits << 8) | byte;
  double value;
  std::memcpy(&value, &bits, sizeof(value));
  return value;
}

std::vector<double> ReadTable(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open table: " + path);
  char magic[4];
  input.read(magic, 4);
  if (!input || std::string(magic, 4) != "CWK2") {
    throw std::runtime_error("bad table magic");
  }
  const auto grid = ReadBigEndian32(input);
  const auto cells = ReadBigEndian32(input);
  if (grid != kGrid || cells != kTableCells) {
    throw std::runtime_error("unexpected table dimensions");
  }
  std::vector<double> table(cells);
  for (double& value : table) {
    value = ReadBigEndianDouble(input);
    if (!(value >= 0.0) || !std::isfinite(value)) {
      throw std::runtime_error("invalid table entry");
    }
  }
  char extra;
  if (input.read(&extra, 1)) throw std::runtime_error("trailing table bytes");
  return table;
}

class RangeMinimum {
 public:
  explicit RangeMinimum(std::vector<double> values)
      : length_(static_cast<int>(values.size())) {
    levels_.push_back(std::move(values));
    for (int width = 1; 2 * width <= length_; width *= 2) {
      const auto& previous = levels_.back();
      std::vector<double> next(length_ - 2 * width + 1);
      for (int index = 0; index + 2 * width <= length_; ++index) {
        next[index] = std::min(previous[index], previous[index + width]);
      }
      levels_.push_back(std::move(next));
    }
  }

  double Query(int left, int right) const {
    if (left < 0 || right < left) throw std::runtime_error("invalid RMQ");
    if (right >= length_) return 0.0;  // w is nonnegative beyond the table.
    const int count = right - left + 1;
    const int level = std::bit_width(static_cast<unsigned>(count)) - 1;
    const int width = 1 << level;
    const auto& row = levels_[level];
    return std::min(row[left], row[right - width + 1]);
  }

 private:
  int length_;
  std::vector<std::vector<double>> levels_;
};

struct CellRange {
  int left;
  int right;
};
struct Box {
  std::array<CellRange, 6> coordinates;
  int depth;
};
struct Statistics {
  std::uint64_t nodes = 0;
  std::uint64_t splits = 0;
  std::uint64_t pressure_pruned = 0;
  std::uint64_t interval_pruned = 0;
  int maximum_depth = 0;
};

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc < 2 || argc > 3) {
      std::cerr << "usage: verify_seven_joint KERNEL_TABLE.bin [BOX_CODE]\n";
      return 2;
    }
    if (std::fesetround(FE_TONEAREST) != 0) {
      throw std::runtime_error("could not select round-to-nearest mode");
    }

    auto table = ReadTable(argv[1]);
    const RangeMinimum ranges(table);
    const std::array<double, 7> coefficients = {
        0.0, DownRatio(1, 3), DownRatio(2, 5), DownRatio(1, 2),
        DownRatio(2, 3), 1.0, 2.0};
    const double target_upper = UpRatio(kTargetNumerator, kTargetDenominator);

    std::vector<int> surviving_cells;
    for (int index = 0; index < kPressureCutoffCells; ++index) {
      double one_body = DownRatio(
          index, std::uint64_t(kGrid) * kPressureDenominator);
      one_body = DownAdd(
          one_body, DownMultiply(coefficients[1], table[index]));
      if (one_body < target_upper) surviving_cells.push_back(index);
    }

    std::vector<CellRange> components;
    for (int index : surviving_cells) {
      if (components.empty() || index > components.back().right + 1) {
        components.push_back({index, index});
      } else {
        components.back().right = index;
      }
    }
    if (components.size() != 2) {
      throw std::runtime_error("unexpected surviving-component count");
    }

    std::uint64_t initial_box_count = 1;
    for (int coordinate = 0; coordinate < 6; ++coordinate) {
      initial_box_count *= components.size();
    }
    std::uint64_t code_begin = 0;
    std::uint64_t code_end = initial_box_count;
    if (argc == 3) {
      code_begin = std::stoull(argv[2]);
      code_end = code_begin + 1;
      if (code_begin >= initial_box_count) {
        throw std::runtime_error("box code must lie in [0,63]");
      }
    }

    std::vector<Box> stack;
    stack.reserve(256);
    for (std::uint64_t code = code_begin; code < code_end; ++code) {
      std::uint64_t quotient = code;
      Box box{};
      box.depth = 0;
      for (int coordinate = 0; coordinate < 6; ++coordinate) {
        box.coordinates[coordinate] =
            components[quotient % components.size()];
        quotient /= components.size();
      }
      stack.push_back(box);
    }

    Statistics statistics;
    while (!stack.empty()) {
      const Box box = stack.back();
      stack.pop_back();
      ++statistics.nodes;
      statistics.maximum_depth =
          std::max(statistics.maximum_depth, box.depth);

      std::array<int, 7> low_prefix{};
      std::array<int, 7> high_prefix{};
      for (int coordinate = 0; coordinate < 6; ++coordinate) {
        low_prefix[coordinate + 1] =
            low_prefix[coordinate] + box.coordinates[coordinate].left;
        high_prefix[coordinate + 1] =
            high_prefix[coordinate] + box.coordinates[coordinate].right;
      }

      if (low_prefix[6] >= kPressureCutoffCells) {
        ++statistics.pressure_pruned;
        continue;
      }

      double lower = DownRatio(
          low_prefix[6], std::uint64_t(kGrid) * kPressureDenominator);
      for (int span = 1; span <= 6; ++span) {
        for (int start = 0; start < 7 - span; ++start) {
          const int left = low_prefix[start + span] - low_prefix[start];
          const int right = high_prefix[start + span] - high_prefix[start]
                            + span - 1;
          lower = DownAdd(
              lower,
              DownMultiply(coefficients[span], ranges.Query(left, right)));
        }
      }
      if (lower >= target_upper) {
        ++statistics.interval_pruned;
        continue;
      }

      int split_coordinate = 0;
      int widest = -1;
      for (int coordinate = 0; coordinate < 6; ++coordinate) {
        const int width = box.coordinates[coordinate].right -
                          box.coordinates[coordinate].left;
        if (width > widest) {
          widest = width;
          split_coordinate = coordinate;
        }
      }
      if (widest == 0) {
        std::cerr << std::setprecision(17)
                  << "verified=false terminal_lower=" << lower
                  << " box_code=" << code_begin << " cells=";
        for (const auto cell : box.coordinates) {
          std::cerr << '[' << cell.left << ',' << cell.right << ']';
        }
        std::cerr << '\n';
        return 1;
      }

      const int midpoint =
          (box.coordinates[split_coordinate].left +
           box.coordinates[split_coordinate].right) /
          2;
      Box lower_half = box;
      Box upper_half = box;
      lower_half.depth = upper_half.depth = box.depth + 1;
      lower_half.coordinates[split_coordinate].right = midpoint;
      upper_half.coordinates[split_coordinate].left = midpoint + 1;
      stack.push_back(lower_half);
      stack.push_back(upper_half);
      ++statistics.splits;
    }

    std::cout << "verified=true"
              << " box_begin=" << code_begin
              << " box_end=" << code_end
              << " components=dynamic"
              << " nodes=" << statistics.nodes
              << " splits=" << statistics.splits
              << " pressure_pruned=" << statistics.pressure_pruned
              << " interval_pruned=" << statistics.interval_pruned
              << " maximum_depth=" << statistics.maximum_depth << '\n';
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}
