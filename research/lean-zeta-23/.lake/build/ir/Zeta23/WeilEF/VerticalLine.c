// Lean compiler output
// Module: Zeta23.WeilEF.VerticalLine
// Imports: public import Init public meta import Init public import Zeta23.WeilEF.XiLogDeriv public import Zeta23.GammaFacts.StirlingVert public import Mathlib.NumberTheory.LSeries.Dirichlet public import Zeta23.ExplicitFormula public import Zeta23.ExplicitFormula.Bridge public import Zeta23.WeilEF.GammaRBracket public import Zeta23.Poisson.PaperFT public import Mathlib.Analysis.SpecialFunctions.JapaneseBracket
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
lean_object* initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_StirlingVert(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_Dirichlet(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ExplicitFormula(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_GammaRBracket(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Poisson_PaperFT(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_JapaneseBracket(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_WeilEF_VerticalLine(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_XiLogDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_StirlingVert(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_Dirichlet(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ExplicitFormula(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_GammaRBracket(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Poisson_PaperFT(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_JapaneseBracket(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
