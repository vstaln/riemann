// Lean compiler output
// Module: Zeta23.GammaFacts.StirlingVert
// Imports: public import Init public meta import Init public import Zeta23.GammaFacts.Mu public import Mathlib.NumberTheory.Harmonic.EulerMascheroni public import Mathlib.Analysis.SpecialFunctions.Integrals.Basic public import Mathlib.Analysis.SumIntegralComparisons public import Mathlib.Analysis.PSeries
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
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Mu(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_Harmonic_EulerMascheroni(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SumIntegralComparisons(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_PSeries(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_GammaFacts_StirlingVert(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Mu(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_Harmonic_EulerMascheroni(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SumIntegralComparisons(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_PSeries(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
