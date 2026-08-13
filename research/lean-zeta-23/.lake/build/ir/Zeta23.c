// Lean compiler output
// Module: Zeta23
// Imports: public import Init public meta import Init public import Zeta23.Unconditional public import Zeta23.ThmD.Final public import Zeta23.ThmE.Final public import Zeta23.ThmDE.Final public import Zeta23.FinalMult public import Zeta23.ThmD.Mult public import Zeta23.ThmE.Mult public import Zeta23.ThmDE.Mult public import Zeta23.ZeroSide.TightMult public import Zeta23.XiPrime.Final public import Zeta23.PairCeiling.CeilingLaw256 public import Zeta23.PairCeiling.Signed
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
lean_object* initialize_Zeta23_Zeta23_Unconditional(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmD_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmDE_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FinalMult(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmD_Mult(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_Mult(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmDE_Mult(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ZeroSide_TightMult(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PairCeiling_CeilingLaw256(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PairCeiling_Signed(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Unconditional(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmD_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmDE_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FinalMult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmD_Mult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Mult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmDE_Mult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ZeroSide_TightMult(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PairCeiling_CeilingLaw256(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PairCeiling_Signed(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
