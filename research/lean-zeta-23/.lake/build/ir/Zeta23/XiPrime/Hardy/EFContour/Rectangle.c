// Lean compiler output
// Module: Zeta23.XiPrime.Hardy.EFContour.Rectangle
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Hardy.EFContour.Poles public import Zeta23.XiPrime.ExplicitFormula.FullLine
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
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
extern lean_object* lp_mathlib_Complex_I;
lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_zc(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_wc(lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_zc(lean_object* v_c_1_, lean_object* v_R_2_){
_start:
{
lean_object* v___x_3_; lean_object* v_re_4_; lean_object* v_im_5_; lean_object* v___x_6_; lean_object* v___f_7_; lean_object* v___f_8_; lean_object* v___x_9_; lean_object* v_re_10_; lean_object* v_im_11_; lean_object* v___x_12_; lean_object* v___x_13_; lean_object* v_re_14_; lean_object* v_im_15_; lean_object* v___x_17_; uint8_t v_isShared_18_; uint8_t v_isSharedCheck_26_; 
v___x_3_ = lp_mathlib_Complex_ofReal(v_R_2_);
v_re_4_ = lean_ctor_get(v___x_3_, 0);
lean_inc(v_re_4_);
v_im_5_ = lean_ctor_get(v___x_3_, 1);
lean_inc(v_im_5_);
lean_dec_ref(v___x_3_);
v___x_6_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___f_7_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_7_, 0, v_c_1_);
v___f_8_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_8_, 0, v___x_6_);
lean_closure_set(v___f_8_, 1, v___f_7_);
v___x_9_ = lp_mathlib_Complex_ofReal(v___f_8_);
v_re_10_ = lean_ctor_get(v___x_9_, 0);
lean_inc(v_re_10_);
v_im_11_ = lean_ctor_get(v___x_9_, 1);
lean_inc(v_im_11_);
lean_dec_ref(v___x_9_);
v___x_12_ = lp_mathlib_Complex_I;
v___x_13_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(v_re_4_, v_im_5_, v___x_12_);
v_re_14_ = lean_ctor_get(v___x_13_, 0);
v_im_15_ = lean_ctor_get(v___x_13_, 1);
v_isSharedCheck_26_ = !lean_is_exclusive(v___x_13_);
if (v_isSharedCheck_26_ == 0)
{
v___x_17_ = v___x_13_;
v_isShared_18_ = v_isSharedCheck_26_;
goto v_resetjp_16_;
}
else
{
lean_inc(v_im_15_);
lean_inc(v_re_14_);
lean_dec(v___x_13_);
v___x_17_ = lean_box(0);
v_isShared_18_ = v_isSharedCheck_26_;
goto v_resetjp_16_;
}
v_resetjp_16_:
{
lean_object* v___f_19_; lean_object* v___f_20_; lean_object* v___f_21_; lean_object* v___f_22_; lean_object* v___x_24_; 
v___f_19_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_19_, 0, v_re_14_);
v___f_20_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_20_, 0, v_re_10_);
lean_closure_set(v___f_20_, 1, v___f_19_);
v___f_21_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_21_, 0, v_im_15_);
v___f_22_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_22_, 0, v_im_11_);
lean_closure_set(v___f_22_, 1, v___f_21_);
if (v_isShared_18_ == 0)
{
lean_ctor_set(v___x_17_, 1, v___f_22_);
lean_ctor_set(v___x_17_, 0, v___f_20_);
v___x_24_ = v___x_17_;
goto v_reusejp_23_;
}
else
{
lean_object* v_reuseFailAlloc_25_; 
v_reuseFailAlloc_25_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_25_, 0, v___f_20_);
lean_ctor_set(v_reuseFailAlloc_25_, 1, v___f_22_);
v___x_24_ = v_reuseFailAlloc_25_;
goto v_reusejp_23_;
}
v_reusejp_23_:
{
return v___x_24_;
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_wc(lean_object* v_c_27_, lean_object* v_R_28_){
_start:
{
lean_object* v___x_29_; lean_object* v_re_30_; lean_object* v_im_31_; lean_object* v___x_32_; lean_object* v_re_33_; lean_object* v_im_34_; lean_object* v___x_35_; lean_object* v___x_36_; lean_object* v_re_37_; lean_object* v_im_38_; lean_object* v___x_40_; uint8_t v_isShared_41_; uint8_t v_isSharedCheck_47_; 
v___x_29_ = lp_mathlib_Complex_ofReal(v_R_28_);
v_re_30_ = lean_ctor_get(v___x_29_, 0);
lean_inc(v_re_30_);
v_im_31_ = lean_ctor_get(v___x_29_, 1);
lean_inc(v_im_31_);
lean_dec_ref(v___x_29_);
v___x_32_ = lp_mathlib_Complex_ofReal(v_c_27_);
v_re_33_ = lean_ctor_get(v___x_32_, 0);
lean_inc(v_re_33_);
v_im_34_ = lean_ctor_get(v___x_32_, 1);
lean_inc(v_im_34_);
lean_dec_ref(v___x_32_);
v___x_35_ = lp_mathlib_Complex_I;
v___x_36_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(v_re_30_, v_im_31_, v___x_35_);
v_re_37_ = lean_ctor_get(v___x_36_, 0);
v_im_38_ = lean_ctor_get(v___x_36_, 1);
v_isSharedCheck_47_ = !lean_is_exclusive(v___x_36_);
if (v_isSharedCheck_47_ == 0)
{
v___x_40_ = v___x_36_;
v_isShared_41_ = v_isSharedCheck_47_;
goto v_resetjp_39_;
}
else
{
lean_inc(v_im_38_);
lean_inc(v_re_37_);
lean_dec(v___x_36_);
v___x_40_ = lean_box(0);
v_isShared_41_ = v_isSharedCheck_47_;
goto v_resetjp_39_;
}
v_resetjp_39_:
{
lean_object* v___f_42_; lean_object* v___f_43_; lean_object* v___x_45_; 
v___f_42_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_42_, 0, v_re_33_);
lean_closure_set(v___f_42_, 1, v_re_37_);
v___f_43_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_43_, 0, v_im_34_);
lean_closure_set(v___f_43_, 1, v_im_38_);
if (v_isShared_41_ == 0)
{
lean_ctor_set(v___x_40_, 1, v___f_43_);
lean_ctor_set(v___x_40_, 0, v___f_42_);
v___x_45_ = v___x_40_;
goto v_reusejp_44_;
}
else
{
lean_object* v_reuseFailAlloc_46_; 
v_reuseFailAlloc_46_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_46_, 0, v___f_42_);
lean_ctor_set(v_reuseFailAlloc_46_, 1, v___f_43_);
v___x_45_ = v_reuseFailAlloc_46_;
goto v_reusejp_44_;
}
v_reusejp_44_:
{
return v___x_45_;
}
}
}
}
static lean_object* _init_lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0(void){
_start:
{
lean_object* v___x_48_; lean_object* v___x_49_; 
v___x_48_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_49_ = lp_mathlib_Complex_ofReal(v___x_48_);
return v___x_49_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne(lean_object* v_s_50_){
_start:
{
lean_object* v_re_51_; lean_object* v_im_52_; lean_object* v___x_54_; uint8_t v_isShared_55_; uint8_t v_isSharedCheck_66_; 
v_re_51_ = lean_ctor_get(v_s_50_, 0);
v_im_52_ = lean_ctor_get(v_s_50_, 1);
v_isSharedCheck_66_ = !lean_is_exclusive(v_s_50_);
if (v_isSharedCheck_66_ == 0)
{
v___x_54_ = v_s_50_;
v_isShared_55_ = v_isSharedCheck_66_;
goto v_resetjp_53_;
}
else
{
lean_inc(v_im_52_);
lean_inc(v_re_51_);
lean_dec(v_s_50_);
v___x_54_ = lean_box(0);
v_isShared_55_ = v_isSharedCheck_66_;
goto v_resetjp_53_;
}
v_resetjp_53_:
{
lean_object* v___x_56_; lean_object* v_re_57_; lean_object* v_im_58_; lean_object* v___f_59_; lean_object* v___f_60_; lean_object* v___f_61_; lean_object* v___f_62_; lean_object* v___x_64_; 
v___x_56_ = lean_obj_once(&lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0, &lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0_once, _init_lp_Zeta23_Zeta23_XiPrime_Hardy_EFContour_subOne___closed__0);
v_re_57_ = lean_ctor_get(v___x_56_, 0);
v_im_58_ = lean_ctor_get(v___x_56_, 1);
lean_inc(v_re_57_);
v___f_59_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_59_, 0, v_re_57_);
v___f_60_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_60_, 0, v_re_51_);
lean_closure_set(v___f_60_, 1, v___f_59_);
lean_inc(v_im_58_);
v___f_61_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_61_, 0, v_im_58_);
v___f_62_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_62_, 0, v_im_52_);
lean_closure_set(v___f_62_, 1, v___f_61_);
if (v_isShared_55_ == 0)
{
lean_ctor_set(v___x_54_, 1, v___f_62_);
lean_ctor_set(v___x_54_, 0, v___f_60_);
v___x_64_ = v___x_54_;
goto v_reusejp_63_;
}
else
{
lean_object* v_reuseFailAlloc_65_; 
v_reuseFailAlloc_65_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_65_, 0, v___f_60_);
lean_ctor_set(v_reuseFailAlloc_65_, 1, v___f_62_);
v___x_64_ = v_reuseFailAlloc_65_;
goto v_reusejp_63_;
}
v_reusejp_63_:
{
return v___x_64_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Poles(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_FullLine(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Rectangle(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFContour_Poles(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_FullLine(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
