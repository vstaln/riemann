// Lean compiler output
// Module: Zeta23.XiPrime.Final
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Assembly public import Zeta23.XiPrime.Inputs public import Zeta23.XiPrime.Certificate public import Zeta23.XiPrime.Window public import Zeta23.XiPrime.QuarticWindow.ZeroSide public import Zeta23.XiPrime.Seam public import Zeta23.XiPrime.ZeroCount public import Zeta23.XiPrime.ExplicitFormula.ZeroFree public import Zeta23.XiPrime.ExplicitFormula.Main public import Zeta23.XiPrime.Coeff public import Zeta23.XiPrime.Coeff.Reexpansion public import Zeta23.XiPrime.FamilyFlat public import Zeta23.XiPrime.FamilyHyps public import Zeta23.XiPrime.FamilyHypsV public import Zeta23.XiPrime.Hardy.ZeroFree public import Zeta23.XiPrime.Hardy.Seam public import Zeta23.XiPrime.Hardy.Count public import Zeta23.XiPrime.Hardy.EFFinal public import Zeta23.XiPrime.Hardy.ZFunction public import Zeta23.Taper.Gevrey public import Zeta23.Defs.Profile public import Zeta23.RvM.Statement public import Zeta23.Statement.SeamClosed
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
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Assembly(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Inputs(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Certificate(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Window(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ZeroSide(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Seam(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ZeroCount(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_ZeroFree(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Main(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Coeff_Reexpansion(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_FamilyFlat(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_FamilyHyps(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_FamilyHypsV(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_ZeroFree(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_Seam(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_Count(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_EFFinal(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Hardy_ZFunction(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Taper_Gevrey(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs_Profile(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Statement_SeamClosed(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_Final(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Assembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Inputs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Certificate(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Window(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_QuarticWindow_ZeroSide(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Seam(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ZeroCount(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_ZeroFree(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_ExplicitFormula_Main(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Coeff_Reexpansion(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_FamilyFlat(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_FamilyHyps(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_FamilyHypsV(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_ZeroFree(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_Seam(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_Count(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_EFFinal(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Hardy_ZFunction(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Taper_Gevrey(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs_Profile(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Statement_SeamClosed(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
