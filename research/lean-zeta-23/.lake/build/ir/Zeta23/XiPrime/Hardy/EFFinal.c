// Lean compiler output
// Module: Zeta23.XiPrime.Hardy.EFFinal
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Hardy.EFMain public import Zeta23.XiPrime.Hardy.EFExpansion public import Zeta23.XiPrime.Hardy.EFContour public import Zeta23.XiPrime.Coeff.LSeries public import Zeta23.XiPrime.ExplicitFormula.Main
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFMain(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFExpansion(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_LSeries(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Main(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFFinal(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFMain(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFExpansion(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_LSeries(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Main(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
