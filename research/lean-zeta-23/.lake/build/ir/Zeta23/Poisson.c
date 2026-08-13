// Lean compiler output
// Module: Zeta23.Poisson
// Imports: public import Init public meta import Init public import Mathlib.Analysis.Fourier.PoissonSummation public import Mathlib.MeasureTheory.Measure.Haar.NormedSpace public import Mathlib.MeasureTheory.Integral.Prod public import Zeta23.Defs public import Zeta23.Poisson.PaperFT public import Zeta23.Taper.Strip public import Zeta23.Taper.Fourier
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Fourier_PoissonSummation(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Measure_Haar_NormedSpace(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Integral_Prod(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Poisson_PaperFT(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Taper_Strip(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Taper_Fourier(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_Poisson(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Fourier_PoissonSummation(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Measure_Haar_NormedSpace(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Integral_Prod(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Poisson_PaperFT(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Taper_Strip(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Taper_Fourier(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
