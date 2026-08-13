// Lean compiler output
// Module: Zeta23.ThmE.Main
// Imports: public import Init public meta import Init public import Zeta23.ThmE.Statement public import Zeta23.ThmE.AssemblyQ public import Zeta23.ThmE.SeamL public import Zeta23.ThmE.GzGpChi public import Zeta23.ThmE.RvMChi public import Zeta23.ThmE.TracesChi public import Zeta23.ThmE.ChebCoprime public import Zeta23.ThmE.GammaFactsChiProof public import Zeta23.MV.Final public import Zeta23.PrimeSideA.Bridge public import Mathlib.NumberTheory.DirichletCharacter.Bounds public import Zeta23.Main
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
lean_object* initialize_Zeta23_Zeta23_ThmE_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_AssemblyQ(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_SeamL(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_GzGpChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_RvMChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_TracesChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_ChebCoprime(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_GammaFactsChiProof(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_MV_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideA_Bridge(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_DirichletCharacter_Bounds(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Main(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_Main(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_AssemblyQ(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_SeamL(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_GzGpChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_RvMChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_TracesChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_ChebCoprime(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_GammaFactsChiProof(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_MV_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideA_Bridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_DirichletCharacter_Bounds(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Main(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
