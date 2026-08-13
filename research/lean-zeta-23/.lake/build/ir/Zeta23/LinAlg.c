// Lean compiler output
// Module: Zeta23.LinAlg
// Imports: public import Init public meta import Init public import Zeta23.LinAlg.HermitianPosPart public import Zeta23.LinAlg.Inertia public import Zeta23.LinAlg.PosIndex public import Zeta23.LinAlg.RankTrace public import Zeta23.LinAlg.Sylvester public import Zeta23.LinAlg.VonNeumann public import Zeta23.LinAlg.Weyl
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
lean_object* initialize_Zeta23_Zeta23_LinAlg_HermitianPosPart(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_Inertia(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_PosIndex(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_RankTrace(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_Sylvester(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_VonNeumann(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_LinAlg_Weyl(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_LinAlg(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_HermitianPosPart(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_Inertia(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_PosIndex(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_RankTrace(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_Sylvester(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_VonNeumann(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_LinAlg_Weyl(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
