// Lean compiler output
// Module: Zeta23.FromPNTPlus.StrongPNTPrefix
// Imports: public import Init public meta import Init public import Zeta23.Prelude.InstancePriorities public import Mathlib.Algebra.Lie.OfAssociative public import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset public import Mathlib.Analysis.CStarAlgebra.Classes public import Mathlib.Analysis.Complex.HasPrimitives public import Mathlib.Data.Rat.Cast.OfScientific public import Mathlib.Algebra.Order.Star.Real public import Mathlib.RingTheory.SimpleRing.Principal public import Mathlib.Analysis.Complex.BorelCaratheodory public import Mathlib.Analysis.Analytic.Order public import Mathlib.Analysis.Normed.Module.Connected
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
lean_object* initialize_Zeta23_Zeta23_Prelude_InstancePriorities(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Lie_OfAssociative(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Order_BigOperators_GroupWithZero_Finset(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_CStarAlgebra_Classes(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Complex_HasPrimitives(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Rat_Cast_OfScientific(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Order_Star_Real(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_RingTheory_SimpleRing_Principal(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Complex_BorelCaratheodory(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Analytic_Order(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Normed_Module_Connected(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_StrongPNTPrefix(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Prelude_InstancePriorities(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Lie_OfAssociative(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Order_BigOperators_GroupWithZero_Finset(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_CStarAlgebra_Classes(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Complex_HasPrimitives(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Rat_Cast_OfScientific(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Order_Star_Real(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_RingTheory_SimpleRing_Principal(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Complex_BorelCaratheodory(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Analytic_Order(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Normed_Module_Connected(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
