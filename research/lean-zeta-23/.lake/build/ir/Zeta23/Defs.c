// Lean compiler output
// Module: Zeta23.Defs
// Imports: public import Init public meta import Init public import Mathlib.Analysis.CStarAlgebra.Classes public import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma public import Mathlib.Analysis.SpecialFunctions.Pow.Complex public import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt public import Mathlib.MeasureTheory.Integral.Bochner.Basic public import Mathlib.MeasureTheory.Measure.Lebesgue.Basic public import Mathlib.Algebra.BigOperators.Finprod public import Mathlib.Data.Set.Card public import Mathlib.Data.Matrix.Basic
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
lean_object* lp_mathlib_starRingEnd___at___00Complex_conjAe_spec__0___lam__0(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_reflect___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_reflect___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_reflect(lean_object*);
static lean_object* _init_lp_Zeta23_Zeta23_reflect___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_2_ = lp_mathlib_Complex_ofReal(v___x_1_);
return v___x_2_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_reflect(lean_object* v_00_u03c1_3_){
_start:
{
lean_object* v___x_4_; lean_object* v_re_5_; lean_object* v_im_6_; lean_object* v___x_7_; lean_object* v_re_8_; lean_object* v_im_9_; lean_object* v___x_11_; uint8_t v_isShared_12_; uint8_t v_isSharedCheck_20_; 
v___x_4_ = lean_obj_once(&lp_Zeta23_Zeta23_reflect___closed__0, &lp_Zeta23_Zeta23_reflect___closed__0_once, _init_lp_Zeta23_Zeta23_reflect___closed__0);
v_re_5_ = lean_ctor_get(v___x_4_, 0);
v_im_6_ = lean_ctor_get(v___x_4_, 1);
v___x_7_ = lp_mathlib_starRingEnd___at___00Complex_conjAe_spec__0___lam__0(v_00_u03c1_3_);
v_re_8_ = lean_ctor_get(v___x_7_, 0);
v_im_9_ = lean_ctor_get(v___x_7_, 1);
v_isSharedCheck_20_ = !lean_is_exclusive(v___x_7_);
if (v_isSharedCheck_20_ == 0)
{
v___x_11_ = v___x_7_;
v_isShared_12_ = v_isSharedCheck_20_;
goto v_resetjp_10_;
}
else
{
lean_inc(v_im_9_);
lean_inc(v_re_8_);
lean_dec(v___x_7_);
v___x_11_ = lean_box(0);
v_isShared_12_ = v_isSharedCheck_20_;
goto v_resetjp_10_;
}
v_resetjp_10_:
{
lean_object* v___f_13_; lean_object* v___f_14_; lean_object* v___f_15_; lean_object* v___f_16_; lean_object* v___x_18_; 
v___f_13_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_13_, 0, v_re_8_);
lean_inc(v_re_5_);
v___f_14_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_14_, 0, v_re_5_);
lean_closure_set(v___f_14_, 1, v___f_13_);
v___f_15_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_15_, 0, v_im_9_);
lean_inc(v_im_6_);
v___f_16_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_16_, 0, v_im_6_);
lean_closure_set(v___f_16_, 1, v___f_15_);
if (v_isShared_12_ == 0)
{
lean_ctor_set(v___x_11_, 1, v___f_16_);
lean_ctor_set(v___x_11_, 0, v___f_14_);
v___x_18_ = v___x_11_;
goto v_reusejp_17_;
}
else
{
lean_object* v_reuseFailAlloc_19_; 
v_reuseFailAlloc_19_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_19_, 0, v___f_14_);
lean_ctor_set(v_reuseFailAlloc_19_, 1, v___f_16_);
v___x_18_ = v_reuseFailAlloc_19_;
goto v_reusejp_17_;
}
v_reusejp_17_:
{
return v___x_18_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_CStarAlgebra_Classes(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Gamma_Digamma(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Pow_Complex(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_ArithmeticFunction_VonMangoldt(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Integral_Bochner_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Measure_Lebesgue_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_BigOperators_Finprod(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Set_Card(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Matrix_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_Defs(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_CStarAlgebra_Classes(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Gamma_Digamma(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Pow_Complex(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_ArithmeticFunction_VonMangoldt(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Integral_Bochner_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Measure_Lebesgue_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_BigOperators_Finprod(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Set_Card(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Matrix_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
