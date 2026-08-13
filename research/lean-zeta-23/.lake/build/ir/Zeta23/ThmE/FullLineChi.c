// Lean compiler output
// Module: Zeta23.ThmE.FullLineChi
// Imports: public import Init public meta import Init public import Zeta23.ThmE.ContourChi public import Zeta23.ThmE.LocalCountChi public import Zeta23.ThmE.GzGpChi public import Zeta23.WeilEF.GoodHeights public import Zeta23.ThmE.LandauChi public import Zeta23.WeilEF.ZeroSummabilityGen
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
lean_object* initialize_Zeta23_Zeta23_ThmE_ContourChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_LocalCountChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_GzGpChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_GoodHeights(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_LandauChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_WeilEF_ZeroSummabilityGen(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_FullLineChi(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_ContourChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_LocalCountChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_GzGpChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_GoodHeights(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_LandauChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_WeilEF_ZeroSummabilityGen(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
