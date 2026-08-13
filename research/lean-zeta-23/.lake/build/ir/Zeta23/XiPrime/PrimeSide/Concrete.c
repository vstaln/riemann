// Lean compiler output
// Module: Zeta23.XiPrime.PrimeSide.Concrete
// Imports: public import Init public meta import Init public import Zeta23.XiPrime.Statement public import Zeta23.XiPrime.PrimeSide.Traces public import Zeta23.XiPrime.PrimeSide.Density public import Zeta23.XiPrime.PrimeSide.Cross public import Zeta23.XiPrime.PrimeSide.Trace public import Zeta23.XiPrime.PrimeSide.Abel public import Zeta23.ThmD.WindowLocalHyps public import Zeta23.ThmD.Window public import Zeta23.PrimeSideB.Concrete
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
lean_object* initialize_Zeta23_Zeta23_XiPrime_Statement(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Traces(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Density(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Cross(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Trace(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Abel(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmD_WindowLocalHyps(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_ThmD_Window(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PrimeSideB_Concrete(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Concrete(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_Statement(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Traces(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Density(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Cross(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Trace(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_XiPrime_PrimeSide_Abel(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmD_WindowLocalHyps(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_ThmD_Window(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PrimeSideB_Concrete(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
