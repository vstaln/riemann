// Lean compiler output
// Module: Zeta23.XiPrime.FamilyHypsV
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.FamilyHyps public import Zeta23.XiPrime.QuarticWindow.Params public import Zeta23.XiPrime.QuarticWindow.ModWindow public import Mathlib.Analysis.Calculus.BumpFunction.InnerProduct public import Mathlib.Analysis.SpecialFunctions.Sqrt public import Mathlib.Topology.MetricSpace.Thickening
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_FamilyHyps(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Params(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ModWindow(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Calculus_BumpFunction_InnerProduct(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Sqrt(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Topology_MetricSpace_Thickening(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_FamilyHypsV(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_FamilyHyps(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Params(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ModWindow(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Calculus_BumpFunction_InnerProduct(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Sqrt(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Topology_MetricSpace_Thickening(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
