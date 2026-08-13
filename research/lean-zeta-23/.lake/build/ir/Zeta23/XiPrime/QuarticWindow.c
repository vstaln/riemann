// Lean compiler output
// Module: Zeta23.XiPrime.QuarticWindow
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.QuarticWindow.Params public import Zeta23.XiPrime.QuarticWindow.ModWindow public import Zeta23.XiPrime.QuarticWindow.Quartic public import Zeta23.XiPrime.QuarticWindow.ZeroSide public import Zeta23.XiPrime.QuarticWindow.Moments public import Zeta23.XiPrime.QuarticWindow.Family
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Params(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ModWindow(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Quartic(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ZeroSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Moments(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Family(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Params(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ModWindow(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Quartic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ZeroSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Moments(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_Family(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
