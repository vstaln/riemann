// Lean compiler output
// Module: Zeta23.FromPNTPlus.Mertens
// Imports: public import Init public meta import Init public import Mathlib.Algebra.Order.Field.GeomSum public import Mathlib.Analysis.SumIntegralComparisons public import Mathlib.NumberTheory.Chebyshev public import Mathlib.NumberTheory.Harmonic.EulerMascheroni public import Mathlib.NumberTheory.LSeries.RiemannZeta public import Mathlib.NumberTheory.Harmonic.GammaDeriv public import Mathlib.Analysis.Asymptotics.Lemmas public import Mathlib.Algebra.Group.Submonoid.BigOperators public import Zeta23.FromPNTPlus.EulerMaclaurin
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
lean_object* initialize_mathlib_Mathlib_Algebra_Order_Field_GeomSum(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SumIntegralComparisons(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_Chebyshev(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_Harmonic_EulerMascheroni(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_RiemannZeta(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_Harmonic_GammaDeriv(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Asymptotics_Lemmas(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Group_Submonoid_BigOperators(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_EulerMaclaurin(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Mertens(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Order_Field_GeomSum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SumIntegralComparisons(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_Chebyshev(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_Harmonic_EulerMascheroni(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_RiemannZeta(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_Harmonic_GammaDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Asymptotics_Lemmas(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Group_Submonoid_BigOperators(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_EulerMaclaurin(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
