// Lean compiler output
// Module: Zeta23.XiPrime.Defs
// Imports: public import Init public meta import Init public import Zeta23.Defs public import Mathlib.NumberTheory.LSeries.RiemannZeta public import Mathlib.NumberTheory.ArithmeticFunction.Misc public import Mathlib.Analysis.Analytic.Order public import Mathlib.Analysis.Calculus.LogDeriv public import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
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
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_vFlat(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_vFlat___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_vFlat(lean_object* v_x_1_){
_start:
{
lean_object* v___x_2_; 
v___x_2_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
return v___x_2_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_vFlat___boxed(lean_object* v_x_3_){
_start:
{
lean_object* v_res_4_; 
v_res_4_ = lp_Zeta23_Zeta23_XiPrime_vFlat(v_x_3_);
lean_dec(v_x_3_);
return v_res_4_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_RiemannZeta(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_ArithmeticFunction_Misc(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Analytic_Order(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Calculus_LogDeriv(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Integral_IntervalIntegral_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Defs(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_RiemannZeta(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_ArithmeticFunction_Misc(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Analytic_Order(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Calculus_LogDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Integral_IntervalIntegral_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
