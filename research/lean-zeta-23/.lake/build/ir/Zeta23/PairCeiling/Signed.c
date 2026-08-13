// Lean compiler output
// Module: Zeta23.PairCeiling.Signed
// Imports: public import Init public meta import Init public import Zeta23.PairCeiling.CeilingLaw256
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
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_to_int(lean_object*);
lean_object* lean_int_mul(lean_object*, lean_object*);
lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo(lean_object*);
uint8_t lean_int_dec_le(lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0;
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_edgeNonneg(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___boxed(lean_object*);
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lean_unsigned_to_nat(2u);
v___x_2_ = lean_nat_to_int(v___x_1_);
return v___x_2_;
}
}
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_edgeNonneg(lean_object* v_d_3_){
_start:
{
lean_object* v_N_4_; lean_object* v_K_5_; lean_object* v_encl_6_; uint8_t v___y_8_; lean_object* v___x_13_; lean_object* v___x_14_; lean_object* v___x_15_; lean_object* v___x_16_; lean_object* v___x_17_; lean_object* v___x_18_; uint8_t v___x_19_; 
v_N_4_ = lean_ctor_get(v_d_3_, 0);
lean_inc_n(v_N_4_, 2);
v_K_5_ = lean_ctor_get(v_d_3_, 1);
lean_inc_n(v_K_5_, 2);
v_encl_6_ = lean_ctor_get(v_d_3_, 2);
lean_inc(v_encl_6_);
lean_dec_ref(v_d_3_);
v___x_13_ = lean_nat_to_int(v_K_5_);
v___x_14_ = lean_nat_to_int(v_N_4_);
v___x_15_ = lean_int_mul(v___x_13_, v___x_14_);
lean_dec(v___x_14_);
lean_dec(v___x_13_);
v___x_16_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0, &lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___closed__0);
v___x_17_ = lp_Zeta23_Zeta23_PairCeiling_sumLo(v_encl_6_);
v___x_18_ = lean_int_mul(v___x_16_, v___x_17_);
lean_dec(v___x_17_);
v___x_19_ = lean_int_dec_le(v___x_15_, v___x_18_);
lean_dec(v___x_18_);
lean_dec(v___x_15_);
if (v___x_19_ == 0)
{
lean_dec(v_K_5_);
v___y_8_ = v___x_19_;
goto v___jp_7_;
}
else
{
lean_object* v___x_20_; uint8_t v___x_21_; 
v___x_20_ = lean_unsigned_to_nat(0u);
v___x_21_ = lean_nat_dec_lt(v___x_20_, v_K_5_);
lean_dec(v_K_5_);
v___y_8_ = v___x_21_;
goto v___jp_7_;
}
v___jp_7_:
{
if (v___y_8_ == 0)
{
lean_dec(v_encl_6_);
lean_dec(v_N_4_);
return v___y_8_;
}
else
{
lean_object* v___x_9_; uint8_t v___x_10_; 
v___x_9_ = lean_unsigned_to_nat(0u);
v___x_10_ = lean_nat_dec_lt(v___x_9_, v_N_4_);
if (v___x_10_ == 0)
{
lean_dec(v_encl_6_);
lean_dec(v_N_4_);
return v___x_10_;
}
else
{
lean_object* v___x_11_; uint8_t v___x_12_; 
v___x_11_ = l_List_lengthTR___redArg(v_encl_6_);
lean_dec(v_encl_6_);
v___x_12_ = lean_nat_dec_eq(v___x_11_, v_N_4_);
lean_dec(v_N_4_);
lean_dec(v___x_11_);
return v___x_12_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_edgeNonneg___boxed(lean_object* v_d_22_){
_start:
{
uint8_t v_res_23_; lean_object* v_r_24_; 
v_res_23_ = lp_Zeta23_Zeta23_PairCeiling_edgeNonneg(v_d_22_);
v_r_24_ = lean_box(v_res_23_);
return v_r_24_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PairCeiling_CeilingLaw256(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PairCeiling_Signed(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PairCeiling_CeilingLaw256(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
