// Lean compiler output
// Module: Zeta23.LinAlg.PosIndex
// Imports: public import Init public meta import Init public import Mathlib.Analysis.Matrix.PosDef
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
lean_object* lp_mathlib_Field_toSemifield___redArg(lean_object*);
lean_object* lp_mathlib_Semifield_toDivisionSemiring___redArg(lean_object*);
lean_object* lp_mathlib_instDistribOfSemiring___redArg(lean_object*);
lean_object* lp_mathlib_Matrix_conjTranspose___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_dotProduct___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Matrix_trace___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_rtrace___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_rtrace(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__1(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__2(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__2___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_rtrace___redArg(lean_object* v_inst_1_, lean_object* v_inst_2_, lean_object* v_A_3_){
_start:
{
lean_object* v_toDenselyNormedField_4_; lean_object* v_re_5_; lean_object* v_toField_6_; lean_object* v___x_7_; lean_object* v___x_8_; lean_object* v_toSemiring_9_; lean_object* v_toAddCommMonoid_10_; lean_object* v___x_11_; lean_object* v___x_12_; 
v_toDenselyNormedField_4_ = lean_ctor_get(v_inst_1_, 0);
lean_inc_ref(v_toDenselyNormedField_4_);
v_re_5_ = lean_ctor_get(v_inst_1_, 3);
lean_inc(v_re_5_);
lean_dec_ref(v_inst_1_);
v_toField_6_ = lean_ctor_get(v_toDenselyNormedField_4_, 1);
lean_inc_ref(v_toField_6_);
lean_dec_ref(v_toDenselyNormedField_4_);
v___x_7_ = lp_mathlib_Field_toSemifield___redArg(v_toField_6_);
lean_dec_ref(v_toField_6_);
v___x_8_ = lp_mathlib_Semifield_toDivisionSemiring___redArg(v___x_7_);
v_toSemiring_9_ = lean_ctor_get(v___x_8_, 0);
lean_inc_ref(v_toSemiring_9_);
lean_dec_ref(v___x_8_);
v_toAddCommMonoid_10_ = lean_ctor_get(v_toSemiring_9_, 0);
lean_inc_ref(v_toAddCommMonoid_10_);
lean_dec_ref(v_toSemiring_9_);
v___x_11_ = lp_mathlib_Matrix_trace___redArg(v_inst_2_, v_toAddCommMonoid_10_, v_A_3_);
lean_dec_ref(v_toAddCommMonoid_10_);
v___x_12_ = lean_apply_1(v_re_5_, v___x_11_);
return v___x_12_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_rtrace(lean_object* v_00_U0001d55c_13_, lean_object* v_inst_14_, lean_object* v_n_15_, lean_object* v_inst_16_, lean_object* v_A_17_){
_start:
{
lean_object* v___x_18_; 
v___x_18_ = lp_Zeta23_RHLinalg_rtrace___redArg(v_inst_14_, v_inst_16_, v_A_17_);
return v___x_18_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__0(lean_object* v_A_19_, lean_object* v___y_20_, lean_object* v_j_21_){
_start:
{
lean_object* v___x_22_; 
v___x_22_ = lean_apply_2(v_A_19_, v_j_21_, v___y_20_);
return v___x_22_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__1(lean_object* v_toStarRing_23_, lean_object* v_A_24_, lean_object* v___y_25_, lean_object* v_j_26_){
_start:
{
lean_object* v___x_27_; 
v___x_27_ = lp_mathlib_Matrix_conjTranspose___redArg(v_toStarRing_23_, v_A_24_, v___y_25_, v_j_26_);
return v___x_27_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__2(lean_object* v_A_28_, lean_object* v_toStarRing_29_, lean_object* v_inst_30_, lean_object* v_toMul_31_, lean_object* v_toAddCommMonoid_32_, lean_object* v___y_33_, lean_object* v___y_34_){
_start:
{
lean_object* v___f_35_; lean_object* v___f_36_; lean_object* v___x_37_; 
lean_inc(v_A_28_);
v___f_35_ = lean_alloc_closure((void*)(lp_Zeta23_RHLinalg_frobSq___redArg___lam__0), 3, 2);
lean_closure_set(v___f_35_, 0, v_A_28_);
lean_closure_set(v___f_35_, 1, v___y_34_);
v___f_36_ = lean_alloc_closure((void*)(lp_Zeta23_RHLinalg_frobSq___redArg___lam__1), 4, 3);
lean_closure_set(v___f_36_, 0, v_toStarRing_29_);
lean_closure_set(v___f_36_, 1, v_A_28_);
lean_closure_set(v___f_36_, 2, v___y_33_);
v___x_37_ = lp_mathlib_dotProduct___redArg(v_inst_30_, v_toMul_31_, v_toAddCommMonoid_32_, v___f_36_, v___f_35_);
return v___x_37_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg___lam__2___boxed(lean_object* v_A_38_, lean_object* v_toStarRing_39_, lean_object* v_inst_40_, lean_object* v_toMul_41_, lean_object* v_toAddCommMonoid_42_, lean_object* v___y_43_, lean_object* v___y_44_){
_start:
{
lean_object* v_res_45_; 
v_res_45_ = lp_Zeta23_RHLinalg_frobSq___redArg___lam__2(v_A_38_, v_toStarRing_39_, v_inst_40_, v_toMul_41_, v_toAddCommMonoid_42_, v___y_43_, v___y_44_);
lean_dec_ref(v_toAddCommMonoid_42_);
return v_res_45_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq___redArg(lean_object* v_inst_46_, lean_object* v_inst_47_, lean_object* v_A_48_){
_start:
{
lean_object* v_toDenselyNormedField_49_; lean_object* v_toStarRing_50_; lean_object* v_re_51_; lean_object* v_toField_52_; lean_object* v___x_53_; lean_object* v___x_54_; lean_object* v_toSemiring_55_; lean_object* v_toAddCommMonoid_56_; lean_object* v___x_57_; lean_object* v_toMul_58_; lean_object* v___f_59_; lean_object* v___x_60_; lean_object* v___x_61_; 
v_toDenselyNormedField_49_ = lean_ctor_get(v_inst_46_, 0);
lean_inc_ref(v_toDenselyNormedField_49_);
v_toStarRing_50_ = lean_ctor_get(v_inst_46_, 1);
lean_inc(v_toStarRing_50_);
v_re_51_ = lean_ctor_get(v_inst_46_, 3);
lean_inc(v_re_51_);
lean_dec_ref(v_inst_46_);
v_toField_52_ = lean_ctor_get(v_toDenselyNormedField_49_, 1);
lean_inc_ref(v_toField_52_);
lean_dec_ref(v_toDenselyNormedField_49_);
v___x_53_ = lp_mathlib_Field_toSemifield___redArg(v_toField_52_);
lean_dec_ref(v_toField_52_);
v___x_54_ = lp_mathlib_Semifield_toDivisionSemiring___redArg(v___x_53_);
v_toSemiring_55_ = lean_ctor_get(v___x_54_, 0);
lean_inc_ref(v_toSemiring_55_);
lean_dec_ref(v___x_54_);
v_toAddCommMonoid_56_ = lean_ctor_get(v_toSemiring_55_, 0);
lean_inc_ref_n(v_toAddCommMonoid_56_, 2);
v___x_57_ = lp_mathlib_instDistribOfSemiring___redArg(v_toSemiring_55_);
v_toMul_58_ = lean_ctor_get(v___x_57_, 0);
lean_inc(v_toMul_58_);
lean_dec_ref(v___x_57_);
lean_inc(v_inst_47_);
v___f_59_ = lean_alloc_closure((void*)(lp_Zeta23_RHLinalg_frobSq___redArg___lam__2___boxed), 7, 5);
lean_closure_set(v___f_59_, 0, v_A_48_);
lean_closure_set(v___f_59_, 1, v_toStarRing_50_);
lean_closure_set(v___f_59_, 2, v_inst_47_);
lean_closure_set(v___f_59_, 3, v_toMul_58_);
lean_closure_set(v___f_59_, 4, v_toAddCommMonoid_56_);
v___x_60_ = lp_mathlib_Matrix_trace___redArg(v_inst_47_, v_toAddCommMonoid_56_, v___f_59_);
lean_dec_ref(v_toAddCommMonoid_56_);
v___x_61_ = lean_apply_1(v_re_51_, v___x_60_);
return v___x_61_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_frobSq(lean_object* v_00_U0001d55c_62_, lean_object* v_inst_63_, lean_object* v_n_64_, lean_object* v_inst_65_, lean_object* v_A_66_){
_start:
{
lean_object* v___x_67_; 
v___x_67_ = lp_Zeta23_RHLinalg_frobSq___redArg(v_inst_63_, v_inst_65_, v_A_66_);
return v___x_67_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Matrix_PosDef(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_LinAlg_PosIndex(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Matrix_PosDef(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
