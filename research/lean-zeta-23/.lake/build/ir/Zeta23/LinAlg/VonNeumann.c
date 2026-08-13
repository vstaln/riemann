// Lean compiler output
// Module: Zeta23.LinAlg.VonNeumann
// Imports: public import Init public meta import Init public import Zeta23.LinAlg.PosIndex public import Mathlib.Analysis.Convex.Birkhoff public import Mathlib.Algebra.Order.Rearrangement
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
lean_object* l_npowRec___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Equiv_refl(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg___lam__0(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0;
static const lean_closure_object lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__1 = (const lean_object*)&lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__1_value;
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg___lam__0(lean_object* v_W_1_, lean_object* v_toNorm_2_, lean_object* v___f_3_, lean_object* v_i_4_, lean_object* v_j_5_){
_start:
{
lean_object* v___x_6_; lean_object* v___x_7_; lean_object* v___x_8_; lean_object* v___x_9_; lean_object* v___x_10_; 
v___x_6_ = lean_apply_2(v_W_1_, v_i_4_, v_j_5_);
v___x_7_ = lean_apply_1(v_toNorm_2_, v___x_6_);
v___x_8_ = lean_unsigned_to_nat(2u);
v___x_9_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_10_ = l_npowRec___redArg(v___x_9_, v___f_3_, v___x_8_, v___x_7_);
return v___x_10_;
}
}
static lean_object* _init_lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0(void){
_start:
{
lean_object* v___x_11_; 
v___x_11_ = lp_mathlib_Equiv_refl(lean_box(0));
return v___x_11_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix___redArg(lean_object* v_inst_13_, lean_object* v_W_14_, lean_object* v_a_15_, lean_object* v_a_16_){
_start:
{
lean_object* v_toDenselyNormedField_17_; lean_object* v_toNorm_18_; lean_object* v___x_19_; lean_object* v_toFun_20_; lean_object* v___f_21_; lean_object* v___f_22_; lean_object* v___x_23_; 
v_toDenselyNormedField_17_ = lean_ctor_get(v_inst_13_, 0);
lean_inc_ref(v_toDenselyNormedField_17_);
lean_dec_ref(v_inst_13_);
v_toNorm_18_ = lean_ctor_get(v_toDenselyNormedField_17_, 0);
lean_inc(v_toNorm_18_);
lean_dec_ref(v_toDenselyNormedField_17_);
v___x_19_ = lean_obj_once(&lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0, &lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0_once, _init_lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__0);
v_toFun_20_ = lean_ctor_get(v___x_19_, 0);
v___f_21_ = ((lean_object*)(lp_Zeta23_RHLinalg_normSqMatrix___redArg___closed__1));
v___f_22_ = lean_alloc_closure((void*)(lp_Zeta23_RHLinalg_normSqMatrix___redArg___lam__0), 5, 3);
lean_closure_set(v___f_22_, 0, v_W_14_);
lean_closure_set(v___f_22_, 1, v_toNorm_18_);
lean_closure_set(v___f_22_, 2, v___f_21_);
lean_inc(v_toFun_20_);
v___x_23_ = lean_apply_3(v_toFun_20_, v___f_22_, v_a_15_, v_a_16_);
return v___x_23_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_RHLinalg_normSqMatrix(lean_object* v_00_U0001d55c_24_, lean_object* v_inst_25_, lean_object* v_n_26_, lean_object* v_W_27_, lean_object* v_a_28_, lean_object* v_a_29_){
_start:
{
lean_object* v___x_30_; 
v___x_30_ = lp_Zeta23_RHLinalg_normSqMatrix___redArg(v_inst_25_, v_W_27_, v_a_28_, v_a_29_);
return v___x_30_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_PosIndex(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Convex_Birkhoff(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Order_Rearrangement(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_LinAlg_VonNeumann(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_PosIndex(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Convex_Birkhoff(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Order_Rearrangement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
