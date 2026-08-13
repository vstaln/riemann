// Lean compiler output
// Module: Zeta23.FromPNTPlus.Fourier
// Imports: public import Init public meta import Init public import Mathlib.Analysis.Distribution.SchwartzSpace.Deriv public import Mathlib.MeasureTheory.Integral.IntegralEqImproper public import Mathlib.Topology.ContinuousMap.Bounded.Basic public import Mathlib.Order.Filter.ZeroAndBoundedAtFilter public import Mathlib.Analysis.Fourier.FourierTransformDeriv public import Zeta23.FromPNTPlus.Sobolev
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
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_instCoeForallRealForallComplex__zeta23___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_instCoeForallRealForallComplex__zeta23___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_instCoeForallRealForallComplex__zeta23___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_instCoeForallRealForallComplex__zeta23___closed__0 = (const lean_object*)&lp_Zeta23_instCoeForallRealForallComplex__zeta23___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_instCoeForallRealForallComplex__zeta23(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_instCoeForallRealForallComplex__zeta23___lam__0(lean_object* v_f_1_, lean_object* v_n_2_){
_start:
{
lean_object* v___x_3_; lean_object* v___x_4_; 
v___x_3_ = lean_apply_1(v_f_1_, v_n_2_);
v___x_4_ = lp_mathlib_Complex_ofReal(v___x_3_);
return v___x_4_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_instCoeForallRealForallComplex__zeta23(lean_object* v_E_6_){
_start:
{
lean_object* v___f_7_; 
v___f_7_ = ((lean_object*)(lp_Zeta23_instCoeForallRealForallComplex__zeta23___closed__0));
return v___f_7_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Distribution_SchwartzSpace_Deriv(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Integral_IntegralEqImproper(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Topology_ContinuousMap_Bounded_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Order_Filter_ZeroAndBoundedAtFilter(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Fourier_FourierTransformDeriv(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Sobolev(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Fourier(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Distribution_SchwartzSpace_Deriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Integral_IntegralEqImproper(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Topology_ContinuousMap_Bounded_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Order_Filter_ZeroAndBoundedAtFilter(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Fourier_FourierTransformDeriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_Sobolev(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
