// Lean compiler output
// Module: Zeta23.XiPrime.Hardy.Basic
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Statement public import Zeta23.ZetaReflect public import Zeta23.RvM.Fold public import Zeta23.RvM.GammaSide public import Zeta23.RvM.CountByIntegral public import Zeta23.WeilEF.XiLogDeriv public import Mathlib.Analysis.SpecialFunctions.Gamma.Deligne public import Mathlib.Analysis.Complex.CauchyIntegral public import Mathlib.Analysis.Calculus.Deriv.Shift
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZetaReflect(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Fold(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_GammaSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_CountByIntegral(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Gamma_Deligne(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Complex_CauchyIntegral(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Calculus_Deriv_Shift(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_Basic(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZetaReflect(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Fold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_GammaSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_CountByIntegral(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Gamma_Deligne(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Complex_CauchyIntegral(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Calculus_Deriv_Shift(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
