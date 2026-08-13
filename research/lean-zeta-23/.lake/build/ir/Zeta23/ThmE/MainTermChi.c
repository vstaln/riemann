// Lean compiler output
// Module: Zeta23.ThmE.MainTermChi
// Imports: public import Init public meta import Init public import Zeta23.ThmE.LGrowth public import Zeta23.ThmE.Statement public import Zeta23.ThmE.Hypotheses public import Zeta23.ThmE.LocalCountChi public import Zeta23.ThmE.GammaSideChi public import Zeta23.ThmE.CountByIntegralChi public import Zeta23.ThmE.FoldChi public import Zeta23.ThmE.RvMChiDefs public import Zeta23.Assembly public import Zeta23.ThmE.ReZeroCountChi public import Zeta23.ThmE.GammaFactsChiProof
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
lean_object* initialize_Zeta23_Zeta23_ThmE_LGrowth(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_Hypotheses(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_LocalCountChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_GammaSideChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_CountByIntegralChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_FoldChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_RvMChiDefs(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_Assembly(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_ReZeroCountChi(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmE_GammaFactsChiProof(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_ThmE_MainTermChi(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_LGrowth(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_Hypotheses(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_LocalCountChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_GammaSideChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_CountByIntegralChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_FoldChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_RvMChiDefs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_Assembly(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_ReZeroCountChi(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmE_GammaFactsChiProof(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
