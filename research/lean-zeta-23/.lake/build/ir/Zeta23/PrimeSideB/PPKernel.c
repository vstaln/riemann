// Lean compiler output
// Module: Zeta23.PrimeSideB.PPKernel
// Imports: public import Init public meta import Init public import Zeta23.PrimeSideA.Defs
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
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__1(lean_object*);
static const lean_closure_object lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__0, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__0 = (const lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__0_value;
static const lean_closure_object lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__1, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__1 = (const lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__1_value;
static const lean_ctor_object lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 0}, .m_objs = {((lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__0_value),((lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__1_value)}};
static const lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__2 = (const lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__2_value;
LEAN_EXPORT const lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo = (const lean_object*)&lp_Zeta23_Zeta23_PrimeSide_shearHomeo___closed__2_value;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__0(lean_object* v_z_1_){
_start:
{
lean_object* v_fst_2_; lean_object* v_snd_3_; lean_object* v___x_5_; uint8_t v_isShared_6_; uint8_t v_isSharedCheck_11_; 
v_fst_2_ = lean_ctor_get(v_z_1_, 0);
v_snd_3_ = lean_ctor_get(v_z_1_, 1);
v_isSharedCheck_11_ = !lean_is_exclusive(v_z_1_);
if (v_isSharedCheck_11_ == 0)
{
v___x_5_ = v_z_1_;
v_isShared_6_ = v_isSharedCheck_11_;
goto v_resetjp_4_;
}
else
{
lean_inc(v_snd_3_);
lean_inc(v_fst_2_);
lean_dec(v_z_1_);
v___x_5_ = lean_box(0);
v_isShared_6_ = v_isSharedCheck_11_;
goto v_resetjp_4_;
}
v_resetjp_4_:
{
lean_object* v___f_7_; lean_object* v___x_9_; 
lean_inc(v_snd_3_);
v___f_7_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_7_, 0, v_fst_2_);
lean_closure_set(v___f_7_, 1, v_snd_3_);
if (v_isShared_6_ == 0)
{
lean_ctor_set(v___x_5_, 0, v___f_7_);
v___x_9_ = v___x_5_;
goto v_reusejp_8_;
}
else
{
lean_object* v_reuseFailAlloc_10_; 
v_reuseFailAlloc_10_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_10_, 0, v___f_7_);
lean_ctor_set(v_reuseFailAlloc_10_, 1, v_snd_3_);
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
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PrimeSide_shearHomeo___lam__1(lean_object* v_z_12_){
_start:
{
lean_object* v_fst_13_; lean_object* v_snd_14_; lean_object* v___x_16_; uint8_t v_isShared_17_; uint8_t v_isSharedCheck_23_; 
v_fst_13_ = lean_ctor_get(v_z_12_, 0);
v_snd_14_ = lean_ctor_get(v_z_12_, 1);
v_isSharedCheck_23_ = !lean_is_exclusive(v_z_12_);
if (v_isSharedCheck_23_ == 0)
{
v___x_16_ = v_z_12_;
v_isShared_17_ = v_isSharedCheck_23_;
goto v_resetjp_15_;
}
else
{
lean_inc(v_snd_14_);
lean_inc(v_fst_13_);
lean_dec(v_z_12_);
v___x_16_ = lean_box(0);
v_isShared_17_ = v_isSharedCheck_23_;
goto v_resetjp_15_;
}
v_resetjp_15_:
{
lean_object* v___f_18_; lean_object* v___f_19_; lean_object* v___x_21_; 
lean_inc(v_snd_14_);
v___f_18_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_18_, 0, v_snd_14_);
v___f_19_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(v___f_19_, 0, v_fst_13_);
lean_closure_set(v___f_19_, 1, v___f_18_);
if (v_isShared_17_ == 0)
{
lean_ctor_set(v___x_16_, 0, v___f_19_);
v___x_21_ = v___x_16_;
goto v_reusejp_20_;
}
else
{
lean_object* v_reuseFailAlloc_22_; 
v_reuseFailAlloc_22_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v_reuseFailAlloc_22_, 0, v___f_19_);
lean_ctor_set(v_reuseFailAlloc_22_, 1, v_snd_14_);
v___x_21_ = v_reuseFailAlloc_22_;
goto v_reusejp_20_;
}
v_reusejp_20_:
{
return v___x_21_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideA_Defs(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PrimeSideB_PPKernel(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideA_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
