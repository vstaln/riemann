// Lean compiler output
// Module: Zeta23.ZeroSide.Mult
// Imports: public import Init public meta import Init public import Zeta23.ZeroSide public import Zeta23.ZeroSide.RankTraceMult
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
extern lean_object* lp_mathlib_Real_instNatCast;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat___redArg(lean_object* v_D_1_, lean_object* v_z_2_){
_start:
{
lean_object* v_m_3_; lean_object* v___x_4_; lean_object* v___x_9__overap_5_; lean_object* v___x_6_; 
v_m_3_ = lean_ctor_get(v_D_1_, 0);
lean_inc_ref(v_m_3_);
lean_dec_ref(v_D_1_);
v___x_4_ = lean_apply_1(v_m_3_, v_z_2_);
v___x_9__overap_5_ = lp_mathlib_Real_instNatCast;
v___x_6_ = lean_apply_1(v___x_9__overap_5_, v___x_4_);
return v___x_6_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat(lean_object* v_00_u03b9_7_, lean_object* v_d_8_, lean_object* v_inst_9_, lean_object* v_inst_10_, lean_object* v_D_11_, lean_object* v_z_12_){
_start:
{
lean_object* v___x_13_; 
v___x_13_ = lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat___redArg(v_D_11_, v_z_12_);
return v___x_13_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat___boxed(lean_object* v_00_u03b9_14_, lean_object* v_d_15_, lean_object* v_inst_16_, lean_object* v_inst_17_, lean_object* v_D_18_, lean_object* v_z_19_){
_start:
{
lean_object* v_res_20_; 
v_res_20_ = lp_Zeta23_Zeta23_ZeroSide_ZeroBlockData_mhat(v_00_u03b9_14_, v_d_15_, v_inst_16_, v_inst_17_, v_D_18_, v_z_19_);
lean_dec_ref(v_inst_17_);
lean_dec(v_inst_16_);
return v_res_20_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZeroSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZeroSide_RankTraceMult(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ZeroSide_Mult(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZeroSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZeroSide_RankTraceMult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
