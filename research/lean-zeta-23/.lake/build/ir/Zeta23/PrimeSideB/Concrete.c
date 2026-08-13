// Lean compiler output
// Module: Zeta23.PrimeSideB.Concrete
// Imports: public import Init public meta import Init public import Zeta23.PrimeSideA.Basic public import Zeta23.PrimeSideTemp
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
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_Params_toSetting(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_Params_toSetting(lean_object* v_P_1_, lean_object* v_T_2_){
_start:
{
lean_object* v_lam_3_; lean_object* v_w_4_; lean_object* v___x_6_; uint8_t v_isShared_7_; uint8_t v_isSharedCheck_11_; 
v_lam_3_ = lean_ctor_get(v_P_1_, 1);
v_w_4_ = lean_ctor_get(v_P_1_, 2);
v_isSharedCheck_11_ = !lean_is_exclusive(v_P_1_);
if (v_isSharedCheck_11_ == 0)
{
lean_object* v_unused_12_; 
v_unused_12_ = lean_ctor_get(v_P_1_, 0);
lean_dec(v_unused_12_);
v___x_6_ = v_P_1_;
v_isShared_7_ = v_isSharedCheck_11_;
goto v_resetjp_5_;
}
else
{
lean_inc(v_w_4_);
lean_inc(v_lam_3_);
lean_dec(v_P_1_);
v___x_6_ = lean_box(0);
v_isShared_7_ = v_isSharedCheck_11_;
goto v_resetjp_5_;
}
v_resetjp_5_:
{
lean_object* v___x_9_; 
if (v_isShared_7_ == 0)
{
lean_ctor_set(v___x_6_, 0, v_T_2_);
v___x_9_ = v___x_6_;
goto v_reusejp_8_;
}
else
{
lean_object* v_reuseFailAlloc_10_; 
v_reuseFailAlloc_10_ = lean_alloc_ctor(0, 3, 0);
lean_ctor_set(v_reuseFailAlloc_10_, 0, v_T_2_);
lean_ctor_set(v_reuseFailAlloc_10_, 1, v_lam_3_);
lean_ctor_set(v_reuseFailAlloc_10_, 2, v_w_4_);
v___x_9_ = v_reuseFailAlloc_10_;
goto v_reusejp_8_;
}
v_reusejp_8_:
{
return v___x_9_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideA_Basic(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideTemp(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PrimeSideB_Concrete(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideA_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideTemp(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
