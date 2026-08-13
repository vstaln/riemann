// Lean compiler output
// Module: Zeta23.Main
// Imports: public import Init public meta import Init public import Zeta23.Statement.Seam public import Zeta23.Assembly public import Zeta23.Hypotheses.GzGp public import Zeta23.Statement.SeamClosed public import Zeta23.Defs.Profile public import Zeta23.Taper.Params public import Zeta23.Tail public import Zeta23.Tail.Package public import Zeta23.ZeroSide public import Zeta23.Poisson public import Zeta23.PrimeSideTemp public import Zeta23.ExplicitFormula.Bridge public import Zeta23.Chebyshev
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
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_paramsOf(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_paramsOf(lean_object* v_00_u03f1_1_, lean_object* v_lam_2_){
_start:
{
lean_object* v___x_3_; lean_object* v___x_4_; 
v___x_3_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
v___x_4_ = lean_alloc_ctor(0, 3, 0);
lean_ctor_set(v___x_4_, 0, v_00_u03f1_1_);
lean_ctor_set(v___x_4_, 1, v_lam_2_);
lean_ctor_set(v___x_4_, 2, v___x_3_);
return v___x_4_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Statement_Seam(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Assembly(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Hypotheses_GzGp(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Statement_SeamClosed(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs_Profile(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Taper_Params(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Tail(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Tail_Package(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZeroSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Poisson(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideTemp(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Chebyshev(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_Main(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Statement_Seam(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Assembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Hypotheses_GzGp(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Statement_SeamClosed(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs_Profile(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Taper_Params(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Tail(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Tail_Package(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZeroSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Poisson(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideTemp(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ExplicitFormula_Bridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Chebyshev(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
