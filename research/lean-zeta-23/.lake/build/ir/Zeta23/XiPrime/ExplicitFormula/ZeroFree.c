// Lean compiler output
// Module: Zeta23.XiPrime.ExplicitFormula.ZeroFree
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.ExplicitFormula public import Zeta23.WeilEF.ZeroSumLimit public import Zeta23.GammaFacts.StirlingVert public import Zeta23.GammaFacts.Series public import Zeta23.GammaFacts.Complete public import Zeta23.RvM.Statement public import Zeta23.Assembly
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
extern lean_object* lp_mathlib_Complex_I;
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_Zeta23_Zeta23_reflect(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_ZeroFree_zc_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_zc(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_wc(lean_object*);
static const lean_closure_object lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_Zeta23_reflect, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__0 = (const lean_object*)&lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__0_value;
static const lean_ctor_object lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 0}, .m_objs = {((lean_object*)&lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__0_value),((lean_object*)&lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__0_value)}};
static const lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__1 = (const lean_object*)&lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__1_value;
LEAN_EXPORT const lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv = (const lean_object*)&lp_Zeta23_Zeta23_XiPrime_ZeroFree_reflectEquiv___closed__1_value;
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_ZeroFree_zc_spec__0(lean_object* v_re_1_, lean_object* v_im_2_, lean_object* v_z_3_){
_start:
{
lean_object* v_re_4_; lean_object* v_im_5_; lean_object* v___x_7_; uint8_t v_isShared_8_; uint8_t v_isSharedCheck_19_; 
v_re_4_ = lean_ctor_get(v_z_3_, 0);
v_im_5_ = lean_ctor_get(v_z_3_, 1);
v_isSharedCheck_19_ = !lean_is_exclusive(v_z_3_);
if (v_isSharedCheck_19_ == 0)
{
v___x_7_ = v_z_3_;
v_isShared_8_ = v_isSharedCheck_19_;
goto v_resetjp_6_;
}
else
{
lean_inc(v_im_5_);
lean_inc(v_re_4_);
lean_dec(v_z_3_);
v___x_7_ = lean_box(0);
v_isShared_8_ = v_isSharedCheck_19_;
goto v_resetjp_6_;
}
v_resetjp_6_:
{
lean_object* v___f_9_; lean_object* v___f_10_; lean_object* v___f_11_; lean_object* v___f_12_; lean_object* v___f_13_; lean_object* v___f_14_; lean_object* v___f_15_; lean_object* v___x_17_; 
lean_inc(v_re_4_);
lean_inc(v_re_1_);
v___f_9_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_9_, 0, v_re_1_);
lean_closure_set(v___f_9_, 1, v_re_4_);
lean_inc(v_im_5_);
lean_inc(v_im_2_);
v___f_10_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_10_, 0, v_im_2_);
lean_closure_set(v___f_10_, 1, v_im_5_);
v___f_11_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_11_, 0, v___f_10_);
v___f_12_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_12_, 0, v___f_9_);
lean_closure_set(v___f_12_, 1, v___f_11_);
v___f_13_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_13_, 0, v_re_1_);
lean_closure_set(v___f_13_, 1, v_im_5_);
v___f_14_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_14_, 0, v_im_2_);
lean_closure_set(v___f_14_, 1, v_re_4_);
v___f_15_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_15_, 0, v___f_13_);
lean_closure_set(v___f_15_, 1, v___f_14_);
if (v_isShared_8_ == 0)
{
lean_ctor_set(v___x_7_, 1, v___f_15_);
lean_ctor_set(v___x_7_, 0, v___f_12_);
v___x_17_ = v___x_7_;
goto v_reusejp_16_;
}
else
{
lean_object* v_reuseFailAlloc_18_; 
v_reuseFailAlloc_18_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_18_, 0, v___f_12_);
lean_ctor_set(v_reuseFailAlloc_18_, 1, v___f_15_);
v___x_17_ = v_reuseFailAlloc_18_;
goto v_reusejp_16_;
}
v_reusejp_16_:
{
return v___x_17_;
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_zc(lean_object* v_R_20_){
_start:
{
lean_object* v___x_21_; lean_object* v___f_22_; lean_object* v___f_23_; lean_object* v___x_24_; lean_object* v_re_25_; lean_object* v_im_26_; lean_object* v___x_27_; lean_object* v_re_28_; lean_object* v_im_29_; lean_object* v___x_30_; lean_object* v___x_31_; lean_object* v_re_32_; lean_object* v_im_33_; lean_object* v___x_35_; uint8_t v_isShared_36_; uint8_t v_isSharedCheck_42_; 
v___x_21_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___f_22_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_22_, 0, v_R_20_);
lean_inc_ref(v___f_22_);
v___f_23_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_23_, 0, v___x_21_);
lean_closure_set(v___f_23_, 1, v___f_22_);
v___x_24_ = lp_mathlib_Complex_ofReal(v___f_22_);
v_re_25_ = lean_ctor_get(v___x_24_, 0);
lean_inc(v_re_25_);
v_im_26_ = lean_ctor_get(v___x_24_, 1);
lean_inc(v_im_26_);
lean_dec_ref(v___x_24_);
v___x_27_ = lp_mathlib_Complex_ofReal(v___f_23_);
v_re_28_ = lean_ctor_get(v___x_27_, 0);
lean_inc(v_re_28_);
v_im_29_ = lean_ctor_get(v___x_27_, 1);
lean_inc(v_im_29_);
lean_dec_ref(v___x_27_);
v___x_30_ = lp_mathlib_Complex_I;
v___x_31_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_ZeroFree_zc_spec__0(v_re_25_, v_im_26_, v___x_30_);
v_re_32_ = lean_ctor_get(v___x_31_, 0);
v_im_33_ = lean_ctor_get(v___x_31_, 1);
v_isSharedCheck_42_ = !lean_is_exclusive(v___x_31_);
if (v_isSharedCheck_42_ == 0)
{
v___x_35_ = v___x_31_;
v_isShared_36_ = v_isSharedCheck_42_;
goto v_resetjp_34_;
}
else
{
lean_inc(v_im_33_);
lean_inc(v_re_32_);
lean_dec(v___x_31_);
v___x_35_ = lean_box(0);
v_isShared_36_ = v_isSharedCheck_42_;
goto v_resetjp_34_;
}
v_resetjp_34_:
{
lean_object* v___f_37_; lean_object* v___f_38_; lean_object* v___x_40_; 
v___f_37_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_37_, 0, v_re_28_);
lean_closure_set(v___f_37_, 1, v_re_32_);
v___f_38_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_38_, 0, v_im_29_);
lean_closure_set(v___f_38_, 1, v_im_33_);
if (v_isShared_36_ == 0)
{
lean_ctor_set(v___x_35_, 1, v___f_38_);
lean_ctor_set(v___x_35_, 0, v___f_37_);
v___x_40_ = v___x_35_;
goto v_reusejp_39_;
}
else
{
lean_object* v_reuseFailAlloc_41_; 
v_reuseFailAlloc_41_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_41_, 0, v___f_37_);
lean_ctor_set(v_reuseFailAlloc_41_, 1, v___f_38_);
v___x_40_ = v_reuseFailAlloc_41_;
goto v_reusejp_39_;
}
v_reusejp_39_:
{
return v___x_40_;
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_ZeroFree_wc(lean_object* v_R_43_){
_start:
{
lean_object* v___x_44_; lean_object* v_re_45_; lean_object* v_im_46_; lean_object* v___x_47_; lean_object* v___x_48_; lean_object* v_re_49_; lean_object* v_im_50_; lean_object* v___x_52_; uint8_t v_isShared_53_; uint8_t v_isSharedCheck_59_; 
v___x_44_ = lp_mathlib_Complex_ofReal(v_R_43_);
v_re_45_ = lean_ctor_get(v___x_44_, 0);
lean_inc_n(v_re_45_, 2);
v_im_46_ = lean_ctor_get(v___x_44_, 1);
lean_inc_n(v_im_46_, 2);
lean_dec_ref(v___x_44_);
v___x_47_ = lp_mathlib_Complex_I;
v___x_48_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_ZeroFree_zc_spec__0(v_re_45_, v_im_46_, v___x_47_);
v_re_49_ = lean_ctor_get(v___x_48_, 0);
v_im_50_ = lean_ctor_get(v___x_48_, 1);
v_isSharedCheck_59_ = !lean_is_exclusive(v___x_48_);
if (v_isSharedCheck_59_ == 0)
{
v___x_52_ = v___x_48_;
v_isShared_53_ = v_isSharedCheck_59_;
goto v_resetjp_51_;
}
else
{
lean_inc(v_im_50_);
lean_inc(v_re_49_);
lean_dec(v___x_48_);
v___x_52_ = lean_box(0);
v_isShared_53_ = v_isSharedCheck_59_;
goto v_resetjp_51_;
}
v_resetjp_51_:
{
lean_object* v___f_54_; lean_object* v___f_55_; lean_object* v___x_57_; 
v___f_54_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_54_, 0, v_re_45_);
lean_closure_set(v___f_54_, 1, v_re_49_);
v___f_55_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_55_, 0, v_im_46_);
lean_closure_set(v___f_55_, 1, v_im_50_);
if (v_isShared_53_ == 0)
{
lean_ctor_set(v___x_52_, 1, v___f_55_);
lean_ctor_set(v___x_52_, 0, v___f_54_);
v___x_57_ = v___x_52_;
goto v_reusejp_56_;
}
else
{
lean_object* v_reuseFailAlloc_58_; 
v_reuseFailAlloc_58_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_58_, 0, v___f_54_);
lean_ctor_set(v_reuseFailAlloc_58_, 1, v___f_55_);
v___x_57_ = v_reuseFailAlloc_58_;
goto v_reusejp_56_;
}
v_reusejp_56_:
{
return v___x_57_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_ZeroSumLimit(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_StirlingVert(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Series(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Complete(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Assembly(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_ZeroFree(uint8_t builtin) {
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
res = initialize_Zeta23_Zeta23_WeilEF_ZeroSumLimit(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_StirlingVert(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Series(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Complete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Assembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
