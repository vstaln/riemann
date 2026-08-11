# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf"]
# ///
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
out = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    out.append(f"\n\n===== PAGE {i+1} =====\n\n" + t)
open(sys.argv[2], "w").write("".join(out))
print(f"extracted {len(r.pages)} pages -> {sys.argv[2]}")
