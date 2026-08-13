// Lean compiler output
// Module: Zeta23.ExplicitFormula
// Imports: public import Init public meta import Init public import Mathlib.Analysis.Fourier.Inversion public import Mathlib.Analysis.Fourier.Convolution public import Mathlib.Analysis.Calculus.ContDiff.Convolution public import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals public import Mathlib.Analysis.SpecialFunctions.Integrals.Basic public import Zeta23.Defs
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
lean_object* lp_mathlib_starRingEnd___at___00Complex_conjAe_spec__0___lam__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_EF_tilde(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_EF_tilde(lean_object* v_g_1_, lean_object* v_u_2_){
_start:
{
lean_object* v___f_3_; lean_object* v___x_4_; lean_object* v___x_5_; 
v___f_3_ = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(v___f_3_, 0, v_u_2_);
v___x_4_ = lean_apply_1(v_g_1_, v___f_3_);
v___x_5_ = lp_mathlib_starRingEnd___at___00Complex_conjAe_spec__0___lam__0(v___x_4_);
return v___x_5_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Fourier_Inversion(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Fourier_Convolution(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Calculus_ContDiff_Convolution(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_ImproperIntegrals(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ExplicitFormula(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Fourier_Inversion(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Fourier_Convolution(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Calculus_ContDiff_Convolution(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_ImproperIntegrals(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Integrals_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
