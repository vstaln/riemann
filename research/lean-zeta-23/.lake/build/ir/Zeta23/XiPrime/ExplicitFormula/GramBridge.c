// Lean compiler output
// Module: Zeta23.XiPrime.ExplicitFormula.GramBridge
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.ExplicitFormula public import Zeta23.Hypotheses.GzGp public import Zeta23.ExplicitFormula.Bridge public import Zeta23.GammaFacts.Complete public import Zeta23.WeilEF.VerticalLine
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Hypotheses_GzGp(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Complete(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_VerticalLine(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_GramBridge(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Hypotheses_GzGp(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Complete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_VerticalLine(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
