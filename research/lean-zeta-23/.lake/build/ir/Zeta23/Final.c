// Lean compiler output
// Module: Zeta23.Final
// Imports: public import Init public meta import Init public import Zeta23.Main public import Zeta23.Defs.Profile public import Zeta23.PrimeSideB.Final public import Zeta23.MV public import Zeta23.MV.Final public import Zeta23.GammaFacts.Complete public import Zeta23.RvM.Statement public import Zeta23.WeilEF.Main
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
lean_object* initialize_Zeta23_Zeta23_Main(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Defs_Profile(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideB_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_MV(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_MV_Final(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_GammaFacts_Complete(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_RvM_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_Main(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_Final(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Main(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Defs_Profile(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideB_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_MV(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_MV_Final(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_GammaFacts_Complete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_RvM_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_Main(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
