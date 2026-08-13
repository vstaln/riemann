// Lean compiler output
// Module: Zeta23.PairCeiling.Defs
// Imports: public import Init public meta import Init public import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Finset_Icc___at___00Nat_divisorsAntidiagonal_spec__0(lean_object*, lean_object*);
lean_object* lp_mathlib_Multiset_map___redArg(lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_object* l_List_foldrTR___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0___closed__0 = (const lean_object*)&lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum___lam__0(lean_object* v_s_1_, lean_object* v_j_2_){
_start:
{
lean_object* v___x_3_; 
v___x_3_ = lean_apply_1(v_s_1_, v_j_2_);
return v___x_3_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0(lean_object* v_s_5_){
_start:
{
lean_object* v___f_6_; lean_object* v___x_7_; lean_object* v___x_8_; 
v___f_6_ = ((lean_object*)(lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0___closed__0));
v___x_7_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
v___x_8_ = l_List_foldrTR___redArg(v___f_6_, v___x_7_, v_s_5_);
return v___x_8_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0___redArg(lean_object* v_s_9_, lean_object* v_f_10_){
_start:
{
lean_object* v___x_11_; lean_object* v___x_12_; 
v___x_11_ = lp_mathlib_Multiset_map___redArg(v_f_10_, v_s_9_);
v___x_12_ = lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0_spec__0(v___x_11_);
return v___x_12_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum(lean_object* v_s_13_, lean_object* v_m_14_){
_start:
{
lean_object* v___f_15_; lean_object* v___x_16_; lean_object* v___x_17_; lean_object* v___x_18_; 
v___f_15_ = lean_alloc_closure((void*)(lp_Zeta23_Zeta23_PairCeiling_Csum___lam__0), 2, 1);
lean_closure_set(v___f_15_, 0, v_s_13_);
v___x_16_ = lean_unsigned_to_nat(1u);
v___x_17_ = lp_mathlib_Finset_Icc___at___00Nat_divisorsAntidiagonal_spec__0(v___x_16_, v_m_14_);
v___x_18_ = lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0___redArg(v___x_17_, v___f_15_);
return v___x_18_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_Csum___boxed(lean_object* v_s_19_, lean_object* v_m_20_){
_start:
{
lean_object* v_res_21_; 
v_res_21_ = lp_Zeta23_Zeta23_PairCeiling_Csum(v_s_19_, v_m_20_);
lean_dec(v_m_20_);
return v_res_21_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0(lean_object* v_00_u03b9_22_, lean_object* v_s_23_, lean_object* v_f_24_){
_start:
{
lean_object* v___x_25_; 
v___x_25_ = lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_Csum_spec__0___redArg(v_s_23_, v_f_24_);
return v___x_25_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Integral_IntervalIntegral_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PairCeiling_Defs(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
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
