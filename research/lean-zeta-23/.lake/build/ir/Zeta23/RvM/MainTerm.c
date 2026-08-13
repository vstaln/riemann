// Lean compiler output
// Module: Zeta23.RvM.MainTerm
// Imports: public import Init public meta import Init public import Zeta23.RvM.Defs public import Zeta23.RvM.LocalCount public import Zeta23.Hypotheses public import Zeta23.WeilEF.XiLogDeriv public import Zeta23.Analytic.RectangleLogDeriv public import Zeta23.RvM.GammaSide public import Zeta23.RvM.Backlund public import Zeta23.RvM.Fold public import Zeta23.RvM.NcountWindow
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
lean_object* initialize_Zeta23_Zeta23_RvM_Defs(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_LocalCount(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Hypotheses(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Analytic_RectangleLogDeriv(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_GammaSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Backlund(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Fold(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_NcountWindow(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_RvM_MainTerm(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_LocalCount(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Hypotheses(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Analytic_RectangleLogDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_GammaSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Backlund(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Fold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_NcountWindow(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
