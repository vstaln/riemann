// Lean compiler output
// Module: Zeta23.LinAlg.Sylvester
// Imports: public import Init public meta import Init public import Zeta23.LinAlg.HermitianPosPart public import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
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
lean_object* lp_mathlib_CommRing_toNonUnitalCommRing___redArg(lean_object*);
lean_object* lp_mathlib_NonUnitalNonAssocRing_toNonUnitalNonAssocSemiring___redArg(lean_object*);
lean_object* lp_mathlib_Matrix_mulVec(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_dotProduct___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm___redArg___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm___redArg___lam__0(lean_object* v_x_1_, lean_object* v_toStarRing_2_, lean_object* v___y_3_){
_start:
{
lean_object* v___x_4_; lean_object* v___x_5_; 
v___x_4_ = lean_apply_1(v_x_1_, v___y_3_);
v___x_5_ = lean_apply_1(v_toStarRing_2_, v___x_4_);
return v___x_5_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm___redArg(lean_object* v_inst_6_, lean_object* v_inst_7_, lean_object* v_A_8_, lean_object* v_x_9_){
_start:
{
lean_object* v_toDenselyNormedField_10_; lean_object* v_toField_11_; lean_object* v_toStarRing_12_; lean_object* v_re_13_; lean_object* v_toCommRing_14_; lean_object* v___x_15_; lean_object* v___x_16_; lean_object* v_toSemiring_17_; lean_object* v___x_18_; lean_object* v_toMul_19_; lean_object* v_toAddCommMonoid_20_; lean_object* v___f_21_; lean_object* v___x_22_; lean_object* v___x_23_; lean_object* v___x_24_; lean_object* v___x_25_; lean_object* v___x_26_; 
v_toDenselyNormedField_10_ = lean_ctor_get(v_inst_6_, 0);
v_toField_11_ = lean_ctor_get(v_toDenselyNormedField_10_, 1);
lean_inc_ref(v_toField_11_);
v_toStarRing_12_ = lean_ctor_get(v_inst_6_, 1);
lean_inc(v_toStarRing_12_);
v_re_13_ = lean_ctor_get(v_inst_6_, 3);
lean_inc(v_re_13_);
lean_dec_ref(v_inst_6_);
v_toCommRing_14_ = lean_ctor_get(v_toField_11_, 0);
lean_inc_ref(v_toCommRing_14_);
v___x_15_ = lp_mathlib_Field_toSemifield___redArg(v_toField_11_);
lean_dec_ref(v_toField_11_);
v___x_16_ = lp_mathlib_Semifield_toDivisionSemiring___redArg(v___x_15_);
v_toSemiring_17_ = lean_ctor_get(v___x_16_, 0);
lean_inc_ref_n(v_toSemiring_17_, 2);
lean_dec_ref(v___x_16_);
v___x_18_ = lp_mathlib_instDistribOfSemiring___redArg(v_toSemiring_17_);
v_toMul_19_ = lean_ctor_get(v___x_18_, 0);
lean_inc(v_toMul_19_);
lean_dec_ref(v___x_18_);
v_toAddCommMonoid_20_ = lean_ctor_get(v_toSemiring_17_, 0);
lean_inc_ref(v_toAddCommMonoid_20_);
lean_dec_ref(v_toSemiring_17_);
lean_inc(v_x_9_);
v___f_21_ = lean_alloc_closure((void*)(lp_Zeta23_RHLinalg_hermForm___redArg___lam__0), 3, 2);
lean_closure_set(v___f_21_, 0, v_x_9_);
lean_closure_set(v___f_21_, 1, v_toStarRing_12_);
v___x_22_ = lp_mathlib_CommRing_toNonUnitalCommRing___redArg(v_toCommRing_14_);
lean_dec_ref(v_toCommRing_14_);
v___x_23_ = lp_mathlib_NonUnitalNonAssocRing_toNonUnitalNonAssocSemiring___redArg(v___x_22_);
lean_inc(v_inst_7_);
v___x_24_ = lean_alloc_closure((void*)(lp_mathlib_Matrix_mulVec), 8, 7);
lean_closure_set(v___x_24_, 0, lean_box(0));
lean_closure_set(v___x_24_, 1, lean_box(0));
lean_closure_set(v___x_24_, 2, lean_box(0));
lean_closure_set(v___x_24_, 3, v___x_23_);
lean_closure_set(v___x_24_, 4, v_inst_7_);
lean_closure_set(v___x_24_, 5, v_A_8_);
lean_closure_set(v___x_24_, 6, v_x_9_);
v___x_25_ = lp_mathlib_dotProduct___redArg(v_inst_7_, v_toMul_19_, v_toAddCommMonoid_20_, v___f_21_, v___x_24_);
lean_dec_ref(v_toAddCommMonoid_20_);
v___x_26_ = lean_apply_1(v_re_13_, v___x_25_);
return v___x_26_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_hermForm(lean_object* v_00_U0001d55c_27_, lean_object* v_inst_28_, lean_object* v_n_29_, lean_object* v_inst_30_, lean_object* v_A_31_, lean_object* v_x_32_){
_start:
{
lean_object* v___x_33_; 
v___x_33_ = lp_Zeta23_RHLinalg_hermForm___redArg(v_inst_28_, v_inst_30_, v_A_31_, v_x_32_);
return v___x_33_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_HermitianPosPart(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_LinearAlgebra_FiniteDimensional_Lemmas(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_LinAlg_Sylvester(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_HermitianPosPart(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_LinearAlgebra_FiniteDimensional_Lemmas(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
