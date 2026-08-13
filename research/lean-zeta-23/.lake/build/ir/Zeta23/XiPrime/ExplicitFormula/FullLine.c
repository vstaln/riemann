// Lean compiler output
// Module: Zeta23.XiPrime.ExplicitFormula.FullLine
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.ExplicitFormula.Contour public import Zeta23.XiPrime.ZeroCount.GoodHeights public import Zeta23.XiPrime.ExplicitFormula.LineBound public import Zeta23.WeilEF.ZeroSummabilityGen
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_mulSubOne(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(lean_object* v_re_1_, lean_object* v_im_2_, lean_object* v_z_3_){
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
static lean_object* _init_lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0(void){
_start:
{
lean_object* v___x_20_; lean_object* v___x_21_; 
v___x_20_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_21_ = lp_mathlib_Complex_ofReal(v___x_20_);
return v___x_21_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_XiPrime_mulSubOne(lean_object* v_s_22_){
_start:
{
lean_object* v_re_23_; lean_object* v_im_24_; lean_object* v___x_26_; uint8_t v_isShared_27_; uint8_t v_isSharedCheck_39_; 
v_re_23_ = lean_ctor_get(v_s_22_, 0);
v_im_24_ = lean_ctor_get(v_s_22_, 1);
v_isSharedCheck_39_ = !lean_is_exclusive(v_s_22_);
if (v_isSharedCheck_39_ == 0)
{
v___x_26_ = v_s_22_;
v_isShared_27_ = v_isSharedCheck_39_;
goto v_resetjp_25_;
}
else
{
lean_inc(v_im_24_);
lean_inc(v_re_23_);
lean_dec(v_s_22_);
v___x_26_ = lean_box(0);
v_isShared_27_ = v_isSharedCheck_39_;
goto v_resetjp_25_;
}
v_resetjp_25_:
{
lean_object* v___x_28_; lean_object* v_re_29_; lean_object* v_im_30_; lean_object* v___f_31_; lean_object* v___f_32_; lean_object* v___f_33_; lean_object* v___f_34_; lean_object* v___x_36_; 
v___x_28_ = lean_obj_once(&lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0, &lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0_once, _init_lp_Zeta23_Zeta23_XiPrime_mulSubOne___closed__0);
v_re_29_ = lean_ctor_get(v___x_28_, 0);
v_im_30_ = lean_ctor_get(v___x_28_, 1);
lean_inc(v_re_29_);
v___f_31_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_31_, 0, v_re_29_);
lean_inc(v_re_23_);
v___f_32_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_32_, 0, v_re_23_);
lean_closure_set(v___f_32_, 1, v___f_31_);
lean_inc(v_im_30_);
v___f_33_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_33_, 0, v_im_30_);
lean_inc(v_im_24_);
v___f_34_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_34_, 0, v_im_24_);
lean_closure_set(v___f_34_, 1, v___f_33_);
if (v_isShared_27_ == 0)
{
lean_ctor_set(v___x_26_, 1, v___f_34_);
lean_ctor_set(v___x_26_, 0, v___f_32_);
v___x_36_ = v___x_26_;
goto v_reusejp_35_;
}
else
{
lean_object* v_reuseFailAlloc_38_; 
v_reuseFailAlloc_38_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_38_, 0, v___f_32_);
lean_ctor_set(v_reuseFailAlloc_38_, 1, v___f_34_);
v___x_36_ = v_reuseFailAlloc_38_;
goto v_reusejp_35_;
}
v_reusejp_35_:
{
lean_object* v___x_37_; 
v___x_37_ = lp_Zeta23_Complex_mulAux___at___00Zeta23_XiPrime_mulSubOne_spec__0(v_re_23_, v_im_24_, v___x_36_);
return v___x_37_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Contour(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ZeroCount_GoodHeights(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_LineBound(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_ZeroSummabilityGen(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_FullLine(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Contour(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ZeroCount_GoodHeights(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_LineBound(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_ZeroSummabilityGen(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
