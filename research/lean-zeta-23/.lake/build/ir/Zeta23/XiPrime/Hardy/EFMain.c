// Lean compiler output
// Module: Zeta23.XiPrime.Hardy.EFMain
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Hardy.EFJTermW public import Zeta23.XiPrime.Hardy.EFWeights public import Zeta23.XiPrime.ExplicitFormula.GramBridge public import Zeta23.XiPrime.ExplicitFormula.PrimeTermJ public import Zeta23.XiPrime.ExplicitFormula.FamilyFacts public import Zeta23.XiPrime.ExplicitFormula.XiEFAssembly
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFJTermW(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFWeights(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_GramBridge(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_PrimeTermJ(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_FamilyFacts(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_XiEFAssembly(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFMain(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFJTermW(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFWeights(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_GramBridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_PrimeTermJ(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_FamilyFacts(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_XiEFAssembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
