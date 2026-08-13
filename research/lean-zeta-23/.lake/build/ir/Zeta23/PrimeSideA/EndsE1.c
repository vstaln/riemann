// Lean compiler output
// Module: Zeta23.PrimeSideA.EndsE1
// Imports: public import Init public meta import Init public import Zeta23.PrimeSideA.EndsCore public import Zeta23.Defs.LeafIntegrals public import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00__private_Mathlib_NumberTheory_ModularForms_EisensteinSeries_E2_Transform_0__EisensteinSeries_00_u03b4_spec__0_spec__0_spec__2_spec__3(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1934218611____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PrimeSide_distB___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PrimeSide_distB___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_distB(lean_object*, lean_object*);
static lean_object* _init_lp_Zeta23_Zeta23_PrimeSide_distB___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lean_unsigned_to_nat(2u);
v___x_2_ = lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00__private_Mathlib_NumberTheory_ModularForms_EisensteinSeries_E2_Transform_0__EisensteinSeries_00_u03b4_spec__0_spec__0_spec__2_spec__3(v___x_1_);
return v___x_2_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_distB(lean_object* v_p_3_, lean_object* v_00_u03c4_4_){
_start:
{
lean_object* v_T_5_; lean_object* v___f_6_; lean_object* v___f_7_; lean_object* v___x_8_; lean_object* v___f_9_; lean_object* v___f_10_; lean_object* v___f_11_; lean_object* v___f_12_; 
v_T_5_ = lean_ctor_get(v_p_3_, 0);
lean_inc_n(v_T_5_, 2);
lean_dec_ref(v_p_3_);
v___f_6_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_6_, 0, v_T_5_);
lean_inc(v_00_u03c4_4_);
v___f_7_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_7_, 0, v_00_u03c4_4_);
lean_closure_set(v___f_7_, 1, v___f_6_);
v___x_8_ = lean_obj_once(&lp_Zeta23_Zeta23_PrimeSide_distB___closed__0, &lp_Zeta23_Zeta23_PrimeSide_distB___closed__0_once, _init_lp_Zeta23_Zeta23_PrimeSide_distB___closed__0);
v___f_9_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_9_, 0, v___x_8_);
lean_closure_set(v___f_9_, 1, v_T_5_);
v___f_10_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_10_, 0, v_00_u03c4_4_);
v___f_11_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_11_, 0, v___f_9_);
lean_closure_set(v___f_11_, 1, v___f_10_);
v___f_12_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1934218611____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_12_, 0, v___f_7_);
lean_closure_set(v___f_12_, 1, v___f_11_);
return v___f_12_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideA_EndsCore(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs_LeafIntegrals(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PrimeSideA_EndsE1(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideA_EndsCore(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs_LeafIntegrals(builtin);
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
