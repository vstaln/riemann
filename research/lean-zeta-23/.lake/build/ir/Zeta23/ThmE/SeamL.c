// Lean compiler output
// Module: Zeta23.ThmE.SeamL
// Imports: public import Init public meta import Init public import Zeta23.ThmE.Statement public import Zeta23.ZetaReflect public import Mathlib.NumberTheory.LSeries.Nonvanishing public import Mathlib.NumberTheory.MulChar.Lemmas public import Mathlib.Analysis.Complex.ReImTopology public import Mathlib.Analysis.Normed.Module.Connected public import Mathlib.LinearAlgebra.Complex.FiniteDimensional
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
lean_object* initialize_Zeta23_Zeta23_ThmE_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZetaReflect(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_Nonvanishing(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_MulChar_Lemmas(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Complex_ReImTopology(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Normed_Module_Connected(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_LinearAlgebra_Complex_FiniteDimensional(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_SeamL(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZetaReflect(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_Nonvanishing(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_MulChar_Lemmas(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Complex_ReImTopology(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Normed_Module_Connected(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_LinearAlgebra_Complex_FiniteDimensional(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
