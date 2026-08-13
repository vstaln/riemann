// Lean compiler output
// Module: Zeta23.XiPrime.Certificate.Poly
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Certificate.D1 public import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
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
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_object* l_List_getD___redArg(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Multiset_map___redArg(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* l_List_foldrTR___redArg(lean_object*, lean_object*, lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
lean_object* l_List_range(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0___boxed(lean_object*, lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0___closed__0 = (const lean_object*)&lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0(lean_object* v_c_1_, lean_object* v_x_2_, lean_object* v_k_3_){
_start:
{
lean_object* v___x_4_; lean_object* v___x_5_; lean_object* v___x_6_; lean_object* v___f_7_; 
v___x_4_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_inc(v_k_3_);
v___x_5_ = l_List_getD___redArg(v_c_1_, v_k_3_, v___x_4_);
v___x_6_ = lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(v_k_3_, v_x_2_);
lean_dec(v_k_3_);
v___f_7_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_7_, 0, v___x_5_);
lean_closure_set(v___f_7_, 1, v___x_6_);
return v___f_7_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0___boxed(lean_object* v_c_8_, lean_object* v_x_9_, lean_object* v_k_10_){
_start:
{
lean_object* v_res_11_; 
v_res_11_ = lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0(v_c_8_, v_x_9_, v_k_10_);
lean_dec(v_c_8_);
return v_res_11_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0(lean_object* v_s_13_){
_start:
{
lean_object* v___f_14_; lean_object* v___x_15_; lean_object* v___x_16_; 
v___f_14_ = ((lean_object*)(lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0___closed__0));
v___x_15_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
v___x_16_ = l_List_foldrTR___redArg(v___f_14_, v___x_15_, v_s_13_);
return v___x_16_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0___redArg(lean_object* v_s_17_, lean_object* v_f_18_){
_start:
{
lean_object* v___x_19_; lean_object* v___x_20_; 
v___x_19_ = lp_mathlib_Multiset_map___redArg(v_f_18_, v_s_17_);
v___x_20_ = lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0_spec__0(v___x_19_);
return v___x_20_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_polyEval(lean_object* v_c_21_, lean_object* v_x_22_){
_start:
{
lean_object* v___f_23_; lean_object* v___x_24_; lean_object* v___x_25_; lean_object* v___x_26_; 
lean_inc(v_c_21_);
v___f_23_ = lean_alloc_closure((void*)(lp_Zeta23_Zeta23_XiPrime_polyEval___lam__0___boxed), 3, 2);
lean_closure_set(v___f_23_, 0, v_c_21_);
lean_closure_set(v___f_23_, 1, v_x_22_);
v___x_24_ = l_List_lengthTR___redArg(v_c_21_);
lean_dec(v_c_21_);
v___x_25_ = l_List_range(v___x_24_);
v___x_26_ = lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0___redArg(v___x_25_, v___f_23_);
return v___x_26_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0(lean_object* v_00_u03b9_27_, lean_object* v_s_28_, lean_object* v_f_29_){
_start:
{
lean_object* v___x_30_; 
v___x_30_ = lp_Zeta23_Finset_sum___at___00Zeta23_XiPrime_polyEval_spec__0___redArg(v_s_28_, v_f_29_);
return v___x_30_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Certificate_Poly(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Certificate_D1(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
