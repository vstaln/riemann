// Lean compiler output
// Module: Zeta23.XiPrime.Inputs
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Assembly public import Zeta23.XiPrime.PrimeSide.Moments public import Zeta23.XiPrime.Window public import Zeta23.XiPrime.Window.FlatAdm public import Zeta23.XiPrime.Window.Quartic public import Zeta23.XiPrime.QuarticWindow public import Zeta23.XiPrime.Transfer public import Zeta23.XiPrime.PrimeSide.Final public import Zeta23.XiPrime.Transfer.W public import Zeta23.XiPrime.Coeff.ReexpansionW public import Zeta23.XiPrime.Certificate.D1 public import Zeta23.GammaFacts.Complete public import Zeta23.MV.Final
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Assembly(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Moments(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Window(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Window_FlatAdm(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Window_Quartic(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Transfer(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Transfer_W(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_ReexpansionW(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Complete(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_MV_Final(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Inputs(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Assembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Moments(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Window(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Window_FlatAdm(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Window_Quartic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Transfer(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Transfer_W(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_ReexpansionW(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Complete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_MV_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
