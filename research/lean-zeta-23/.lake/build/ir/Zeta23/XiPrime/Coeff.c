// Lean compiler output
// Module: Zeta23.XiPrime.Coeff
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Statement public import Zeta23.XiPrime.Coeff.Upper public import Zeta23.XiPrime.Coeff.H3 public import Zeta23.XiPrime.Coeff.LSeries public import Zeta23.XiPrime.Coeff.LT public import Zeta23.XiPrime.Certificate.D1
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_Upper(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_H3(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_LSeries(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_LT(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff(uint8_t builtin) {
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
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_Upper(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_H3(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_LSeries(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_LT(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
