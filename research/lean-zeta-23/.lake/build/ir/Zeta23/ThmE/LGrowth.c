// Lean compiler output
// Module: Zeta23.ThmE.LGrowth
// Imports: public import Init public meta import Init public import Zeta23.ThmE.SeamL public import Mathlib.Analysis.MellinTransform public import Zeta23.RvM.ZetaGrowth public import Mathlib.NumberTheory.LSeries.SumCoeff
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
lean_object* initialize_Zeta23_Zeta23_ThmE_SeamL(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_MellinTransform(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_ZetaGrowth(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_SumCoeff(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_LGrowth(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_SeamL(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_MellinTransform(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_ZetaGrowth(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_SumCoeff(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
