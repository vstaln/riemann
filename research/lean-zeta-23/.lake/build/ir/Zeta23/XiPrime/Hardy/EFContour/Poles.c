// Lean compiler output
// Module: Zeta23.XiPrime.Hardy.EFContour.Poles
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Hardy.EFContour.Analytic
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
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__0(lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_polarPoly(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__0(lean_object* v_re_1_, lean_object* v_im_2_, lean_object* v_z_3_){
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
static lean_object* _init_lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0(void){
_start:
{
lean_object* v___x_20_; lean_object* v___x_21_; 
v___x_20_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_21_ = lp_mathlib_Complex_ofReal(v___x_20_);
return v___x_21_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1(lean_object* v_x_22_, lean_object* v_x_23_){
_start:
{
lean_object* v_zero_24_; uint8_t v_isZero_25_; 
v_zero_24_ = lean_unsigned_to_nat(0u);
v_isZero_25_ = lean_nat_dec_eq(v_x_22_, v_zero_24_);
if (v_isZero_25_ == 1)
{
lean_object* v___x_26_; 
lean_dec_ref(v_x_23_);
v___x_26_ = lean_obj_once(&lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0, &lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0_once, _init_lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0);
return v___x_26_;
}
else
{
lean_object* v_one_27_; lean_object* v_n_28_; lean_object* v___x_29_; lean_object* v_re_30_; lean_object* v_im_31_; lean_object* v___x_32_; 
v_one_27_ = lean_unsigned_to_nat(1u);
v_n_28_ = lean_nat_sub(v_x_22_, v_one_27_);
lean_inc_ref(v_x_23_);
v___x_29_ = lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1(v_n_28_, v_x_23_);
lean_dec(v_n_28_);
v_re_30_ = lean_ctor_get(v___x_29_, 0);
lean_inc(v_re_30_);
v_im_31_ = lean_ctor_get(v___x_29_, 1);
lean_inc(v_im_31_);
lean_dec_ref(v___x_29_);
v___x_32_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__0(v_re_30_, v_im_31_, v_x_23_);
return v___x_32_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___boxed(lean_object* v_x_33_, lean_object* v_x_34_){
_start:
{
lean_object* v_res_35_; 
v_res_35_ = lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1(v_x_33_, v_x_34_);
lean_dec(v_x_33_);
return v_res_35_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_polarPoly(lean_object* v_s_36_){
_start:
{
lean_object* v_re_37_; lean_object* v_im_38_; lean_object* v___x_40_; uint8_t v_isShared_41_; uint8_t v_isSharedCheck_55_; 
v_re_37_ = lean_ctor_get(v_s_36_, 0);
v_im_38_ = lean_ctor_get(v_s_36_, 1);
v_isSharedCheck_55_ = !lean_is_exclusive(v_s_36_);
if (v_isSharedCheck_55_ == 0)
{
v___x_40_ = v_s_36_;
v_isShared_41_ = v_isSharedCheck_55_;
goto v_resetjp_39_;
}
else
{
lean_inc(v_im_38_);
lean_inc(v_re_37_);
lean_dec(v_s_36_);
v___x_40_ = lean_box(0);
v_isShared_41_ = v_isSharedCheck_55_;
goto v_resetjp_39_;
}
v_resetjp_39_:
{
lean_object* v___x_42_; lean_object* v_re_43_; lean_object* v_im_44_; lean_object* v___f_45_; lean_object* v___f_46_; lean_object* v___f_47_; lean_object* v___f_48_; lean_object* v___x_50_; 
v___x_42_ = lean_obj_once(&lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0, &lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0_once, _init_lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1___closed__0);
v_re_43_ = lean_ctor_get(v___x_42_, 0);
v_im_44_ = lean_ctor_get(v___x_42_, 1);
lean_inc(v_re_43_);
v___f_45_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_45_, 0, v_re_43_);
lean_inc(v_re_37_);
v___f_46_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_46_, 0, v_re_37_);
lean_closure_set(v___f_46_, 1, v___f_45_);
lean_inc(v_im_44_);
v___f_47_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_47_, 0, v_im_44_);
lean_inc(v_im_38_);
v___f_48_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_48_, 0, v_im_38_);
lean_closure_set(v___f_48_, 1, v___f_47_);
if (v_isShared_41_ == 0)
{
lean_ctor_set(v___x_40_, 1, v___f_48_);
lean_ctor_set(v___x_40_, 0, v___f_46_);
v___x_50_ = v___x_40_;
goto v_reusejp_49_;
}
else
{
lean_object* v_reuseFailAlloc_54_; 
v_reuseFailAlloc_54_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_54_, 0, v___f_46_);
lean_ctor_set(v_reuseFailAlloc_54_, 1, v___f_48_);
v___x_50_ = v_reuseFailAlloc_54_;
goto v_reusejp_49_;
}
v_reusejp_49_:
{
lean_object* v___x_51_; lean_object* v___x_52_; lean_object* v___x_53_; 
v___x_51_ = lean_unsigned_to_nat(2u);
v___x_52_ = lp_Zeta23_npowRec___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__1(v___x_51_, v___x_50_);
v___x_53_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_Hardy_EFContour_polarPoly_spec__0(v_re_37_, v_im_38_, v___x_52_);
return v___x_53_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Analytic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Poles(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Analytic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
