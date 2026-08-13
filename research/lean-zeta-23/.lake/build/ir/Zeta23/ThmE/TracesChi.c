// Lean compiler output
// Module: Zeta23.ThmE.TracesChi
// Imports: public import Init public meta import Init public import Zeta23.ThmE.TracesHypChi public import Zeta23.ThmE.PrimeSideChi public import Zeta23.ThmE.PPChi public import Zeta23.ThmE.MuMuChi public import Zeta23.ThmE.CrossMuPChi public import Zeta23.PrimeSideB public import Zeta23.PrimeSideB.Concrete public import Zeta23.PrimeSideA.Bridge
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
lean_object* initialize_Zeta23_Zeta23_ThmE_TracesHypChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_PrimeSideChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_PPChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_MuMuChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_CrossMuPChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideB(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideB_Concrete(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideA_Bridge(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_TracesChi(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_TracesHypChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_PrimeSideChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_PPChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_MuMuChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_CrossMuPChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideB(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideB_Concrete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideA_Bridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
