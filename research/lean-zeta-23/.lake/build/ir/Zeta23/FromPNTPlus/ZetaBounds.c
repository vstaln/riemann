// Lean compiler output
// Module: Zeta23.FromPNTPlus.ZetaBounds
// Imports: public import Init public meta import Init public import Batteries.Tactic.Lemma public import Mathlib.MeasureTheory.Function.Floor public import Mathlib.MeasureTheory.Order.Group.Lattice public import Mathlib.NumberTheory.Harmonic.Bounds public import Mathlib.NumberTheory.LSeries.Nonvanishing public import Zeta23.FromPNTPlus.Auxiliary public import Zeta23.FromPNTPlus.Fourier public import Zeta23.FromPNTPlus.Mathlib.Analysis.SpecialFunctions.Log.Basic public import Zeta23.FromPNTPlus.ResidueCalcOnRectangles public import Zeta23.FromPNTPlus.EulerMaclaurin
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
lean_object* l_Lean_Name_mkStr1(lean_object*);
lean_object* l_Lean_Name_str___override(lean_object*, lean_object*);
lean_object* l_Lean_Name_num___override(lean_object*, lean_object*);
uint8_t l_Lean_Syntax_isOfKind(lean_object*, lean_object*);
lean_object* l_Lean_SourceInfo_fromRef(lean_object*, uint8_t);
lean_object* l_String_toRawSubstring_x27(lean_object*);
lean_object* l_Lean_addMacroScope(lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Name_mkStr2(lean_object*, lean_object*);
lean_object* l_Lean_replaceRef(lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node1(lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Name_mkStr4(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_getArg(lean_object*, lean_object*);
uint8_t l_Lean_Syntax_matchesNull(lean_object*, lean_object*);
uint8_t l_Lean_Syntax_matchesIdent(lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node2(lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "_private"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__0_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__0_value),LEAN_SCALAR_PTR_LITERAL(103, 214, 75, 80, 34, 198, 193, 153)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__1_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "Zeta23"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__1_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__2_value),LEAN_SCALAR_PTR_LITERAL(49, 198, 4, 56, 221, 160, 221, 117)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__3_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "FromPNTPlus"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__4_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__3_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__4_value),LEAN_SCALAR_PTR_LITERAL(89, 25, 118, 72, 198, 149, 10, 183)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__5 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__5_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 11, .m_capacity = 11, .m_length = 10, .m_data = "ZetaBounds"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__6 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__6_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__5_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__6_value),LEAN_SCALAR_PTR_LITERAL(115, 123, 189, 217, 244, 25, 242, 130)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__7 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__7_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 2}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__7_value),((lean_object*)(((size_t)(0) << 1) | 1)),LEAN_SCALAR_PTR_LITERAL(222, 213, 170, 106, 225, 126, 43, 175)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "riemannzeta"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__9 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__9_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__9_value),LEAN_SCALAR_PTR_LITERAL(248, 215, 135, 242, 125, 25, 218, 120)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 3, .m_capacity = 3, .m_length = 1, .m_data = "ζ"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__11 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__11_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 5}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__11_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__12 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__12_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 3}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10_value),((lean_object*)(((size_t)(1024) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__12_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__13 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__13_value;
LEAN_EXPORT const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__13_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "riemannZeta"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__0_value;
static lean_once_cell_t lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(248, 217, 109, 20, 67, 112, 68, 23)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__3_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__4_value;
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___boxed(lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 5, .m_data = "ident"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__0_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(52, 159, 208, 51, 14, 60, 6, 71)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1_value;
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___boxed(lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 17, .m_capacity = 17, .m_length = 16, .m_data = "derivriemannzeta"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__0_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__0_value),LEAN_SCALAR_PTR_LITERAL(91, 15, 99, 241, 202, 210, 189, 157)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 2, .m_data = "ζ'"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 5}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__2_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 3}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1_value),((lean_object*)(((size_t)(1024) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__3_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__4_value;
LEAN_EXPORT const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__4_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "Lean"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__0_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "Parser"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__1_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "Term"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__2_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 3, .m_data = "app"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_0),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_1),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value_aux_2),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__3_value),LEAN_SCALAR_PTR_LITERAL(69, 118, 10, 41, 220, 156, 243, 179)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 5, .m_data = "deriv"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__5 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__5_value;
static lean_once_cell_t lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__5_value),LEAN_SCALAR_PTR_LITERAL(137, 149, 173, 56, 89, 170, 71, 44)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__8 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__8_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 0}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__9 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__9_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__9_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__10 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__10_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__8_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__10_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__11 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__11_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "null"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__12 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__12_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__12_value),LEAN_SCALAR_PTR_LITERAL(24, 58, 49, 223, 146, 207, 197, 136)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__13 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__13_value;
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__deriv__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__deriv__1___boxed(lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 13, .m_capacity = 13, .m_length = 12, .m_data = "riemannzeta0"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__0_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__0_value),LEAN_SCALAR_PTR_LITERAL(184, 28, 4, 51, 215, 128, 3, 81)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 2, .m_data = "ζ₀"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 5}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__2_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 3}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1_value),((lean_object*)(((size_t)(1024) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__3_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__4_value;
LEAN_EXPORT const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__4_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 13, .m_capacity = 13, .m_length = 12, .m_data = "riemannZeta0"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__0_value;
static lean_once_cell_t lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(128, 92, 173, 66, 54, 120, 80, 235)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__2_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__3_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__4_value;
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta0__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta0__1___boxed(lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "zb_Lambda"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__0_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__8_value),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__0_value),LEAN_SCALAR_PTR_LITERAL(107, 190, 197, 63, 207, 182, 7, 209)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 3, .m_capacity = 3, .m_length = 1, .m_data = "Λ"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__2_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 5}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__2_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 3}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1_value),((lean_object*)(((size_t)(1024) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__3_value)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__4_value;
LEAN_EXPORT const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__4_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "vonMangoldt"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0_value;
static lean_once_cell_t lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(63, 143, 255, 231, 66, 208, 157, 247)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__2 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__2_value;
static const lean_string_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 19, .m_capacity = 19, .m_length = 18, .m_data = "ArithmeticFunction"};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__3 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__3_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__3_value),LEAN_SCALAR_PTR_LITERAL(157, 18, 60, 192, 61, 131, 187, 171)}};
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4_value_aux_0),((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(9, 57, 20, 153, 154, 150, 147, 1)}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__4_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__5 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__5_value;
static const lean_ctor_object lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__5_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__6 = (const lean_object*)&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__6_value;
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__ArithmeticFunction__vonMangoldt__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__ArithmeticFunction__vonMangoldt__1___boxed(lean_object*, lean_object*, lean_object*);
static lean_object* _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1(void){
_start:
{
lean_object* v___x_33_; lean_object* v___x_34_; 
v___x_33_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__0));
v___x_34_ = l_String_toRawSubstring_x27(v___x_33_);
return v___x_34_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1(lean_object* v_x_43_, lean_object* v_a_44_, lean_object* v_a_45_){
_start:
{
lean_object* v___x_46_; uint8_t v___x_47_; 
v___x_46_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10));
v___x_47_ = l_Lean_Syntax_isOfKind(v_x_43_, v___x_46_);
if (v___x_47_ == 0)
{
lean_object* v___x_48_; lean_object* v___x_49_; 
v___x_48_ = lean_box(1);
v___x_49_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_49_, 0, v___x_48_);
lean_ctor_set(v___x_49_, 1, v_a_45_);
return v___x_49_;
}
else
{
lean_object* v_quotContext_50_; lean_object* v_currMacroScope_51_; lean_object* v_ref_52_; uint8_t v___x_53_; lean_object* v___x_54_; lean_object* v___x_55_; lean_object* v___x_56_; lean_object* v___x_57_; lean_object* v___x_58_; lean_object* v___x_59_; lean_object* v___x_60_; 
v_quotContext_50_ = lean_ctor_get(v_a_44_, 1);
v_currMacroScope_51_ = lean_ctor_get(v_a_44_, 2);
v_ref_52_ = lean_ctor_get(v_a_44_, 5);
v___x_53_ = 0;
v___x_54_ = l_Lean_SourceInfo_fromRef(v_ref_52_, v___x_53_);
v___x_55_ = lean_obj_once(&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1, &lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1_once, _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1);
v___x_56_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2));
lean_inc(v_currMacroScope_51_);
lean_inc(v_quotContext_50_);
v___x_57_ = l_Lean_addMacroScope(v_quotContext_50_, v___x_56_, v_currMacroScope_51_);
v___x_58_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__4));
v___x_59_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_59_, 0, v___x_54_);
lean_ctor_set(v___x_59_, 1, v___x_55_);
lean_ctor_set(v___x_59_, 2, v___x_57_);
lean_ctor_set(v___x_59_, 3, v___x_58_);
v___x_60_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_60_, 0, v___x_59_);
lean_ctor_set(v___x_60_, 1, v_a_45_);
return v___x_60_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___boxed(lean_object* v_x_61_, lean_object* v_a_62_, lean_object* v_a_63_){
_start:
{
lean_object* v_res_64_; 
v_res_64_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1(v_x_61_, v_a_62_, v_a_63_);
lean_dec_ref(v_a_62_);
return v_res_64_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1(lean_object* v_x_68_, lean_object* v_a_69_, lean_object* v_a_70_){
_start:
{
lean_object* v___x_71_; uint8_t v___x_72_; 
v___x_71_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1));
lean_inc(v_x_68_);
v___x_72_ = l_Lean_Syntax_isOfKind(v_x_68_, v___x_71_);
if (v___x_72_ == 0)
{
lean_object* v___x_73_; lean_object* v___x_74_; 
lean_dec(v_x_68_);
v___x_73_ = lean_box(0);
v___x_74_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_74_, 0, v___x_73_);
lean_ctor_set(v___x_74_, 1, v_a_70_);
return v___x_74_;
}
else
{
lean_object* v_ref_75_; uint8_t v___x_76_; lean_object* v___x_77_; lean_object* v___x_78_; lean_object* v___x_79_; lean_object* v___x_80_; lean_object* v___x_81_; lean_object* v___x_82_; 
v_ref_75_ = l_Lean_replaceRef(v_x_68_, v_a_69_);
lean_dec(v_x_68_);
v___x_76_ = 0;
v___x_77_ = l_Lean_SourceInfo_fromRef(v_ref_75_, v___x_76_);
lean_dec(v_ref_75_);
v___x_78_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__10));
v___x_79_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta___closed__11));
lean_inc(v___x_77_);
v___x_80_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_80_, 0, v___x_77_);
lean_ctor_set(v___x_80_, 1, v___x_79_);
v___x_81_ = l_Lean_Syntax_node1(v___x_77_, v___x_78_, v___x_80_);
v___x_82_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_82_, 0, v___x_81_);
lean_ctor_set(v___x_82_, 1, v_a_70_);
return v___x_82_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___boxed(lean_object* v_x_83_, lean_object* v_a_84_, lean_object* v_a_85_){
_start:
{
lean_object* v_res_86_; 
v_res_86_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1(v_x_83_, v_a_84_, v_a_85_);
lean_dec(v_a_84_);
return v_res_86_;
}
}
static lean_object* _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6(void){
_start:
{
lean_object* v___x_109_; lean_object* v___x_110_; 
v___x_109_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__5));
v___x_110_ = l_String_toRawSubstring_x27(v___x_109_);
return v___x_110_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1(lean_object* v_x_127_, lean_object* v_a_128_, lean_object* v_a_129_){
_start:
{
lean_object* v___x_130_; uint8_t v___x_131_; 
v___x_130_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1));
v___x_131_ = l_Lean_Syntax_isOfKind(v_x_127_, v___x_130_);
if (v___x_131_ == 0)
{
lean_object* v___x_132_; lean_object* v___x_133_; 
v___x_132_ = lean_box(1);
v___x_133_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_133_, 0, v___x_132_);
lean_ctor_set(v___x_133_, 1, v_a_129_);
return v___x_133_;
}
else
{
lean_object* v_quotContext_134_; lean_object* v_currMacroScope_135_; lean_object* v_ref_136_; uint8_t v___x_137_; lean_object* v___x_138_; lean_object* v___x_139_; lean_object* v___x_140_; lean_object* v___x_141_; lean_object* v___x_142_; lean_object* v___x_143_; lean_object* v___x_144_; lean_object* v___x_145_; lean_object* v___x_146_; lean_object* v___x_147_; lean_object* v___x_148_; lean_object* v___x_149_; lean_object* v___x_150_; lean_object* v___x_151_; lean_object* v___x_152_; lean_object* v___x_153_; 
v_quotContext_134_ = lean_ctor_get(v_a_128_, 1);
v_currMacroScope_135_ = lean_ctor_get(v_a_128_, 2);
v_ref_136_ = lean_ctor_get(v_a_128_, 5);
v___x_137_ = 0;
v___x_138_ = l_Lean_SourceInfo_fromRef(v_ref_136_, v___x_137_);
v___x_139_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4));
v___x_140_ = lean_obj_once(&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6, &lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6_once, _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__6);
v___x_141_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__7));
lean_inc_n(v_currMacroScope_135_, 2);
lean_inc_n(v_quotContext_134_, 2);
v___x_142_ = l_Lean_addMacroScope(v_quotContext_134_, v___x_141_, v_currMacroScope_135_);
v___x_143_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__11));
lean_inc_n(v___x_138_, 3);
v___x_144_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_144_, 0, v___x_138_);
lean_ctor_set(v___x_144_, 1, v___x_140_);
lean_ctor_set(v___x_144_, 2, v___x_142_);
lean_ctor_set(v___x_144_, 3, v___x_143_);
v___x_145_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__13));
v___x_146_ = lean_obj_once(&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1, &lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1_once, _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__1);
v___x_147_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2));
v___x_148_ = l_Lean_addMacroScope(v_quotContext_134_, v___x_147_, v_currMacroScope_135_);
v___x_149_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__4));
v___x_150_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_150_, 0, v___x_138_);
lean_ctor_set(v___x_150_, 1, v___x_146_);
lean_ctor_set(v___x_150_, 2, v___x_148_);
lean_ctor_set(v___x_150_, 3, v___x_149_);
v___x_151_ = l_Lean_Syntax_node1(v___x_138_, v___x_145_, v___x_150_);
v___x_152_ = l_Lean_Syntax_node2(v___x_138_, v___x_139_, v___x_144_, v___x_151_);
v___x_153_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_153_, 0, v___x_152_);
lean_ctor_set(v___x_153_, 1, v_a_129_);
return v___x_153_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___boxed(lean_object* v_x_154_, lean_object* v_a_155_, lean_object* v_a_156_){
_start:
{
lean_object* v_res_157_; 
v_res_157_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1(v_x_154_, v_a_155_, v_a_156_);
lean_dec_ref(v_a_155_);
return v_res_157_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__deriv__1(lean_object* v_x_158_, lean_object* v_a_159_, lean_object* v_a_160_){
_start:
{
lean_object* v___x_161_; uint8_t v___x_162_; 
v___x_161_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__derivriemannzeta__1___closed__4));
lean_inc(v_x_158_);
v___x_162_ = l_Lean_Syntax_isOfKind(v_x_158_, v___x_161_);
if (v___x_162_ == 0)
{
lean_object* v___x_163_; lean_object* v___x_164_; 
lean_dec(v_x_158_);
v___x_163_ = lean_box(0);
v___x_164_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_164_, 0, v___x_163_);
lean_ctor_set(v___x_164_, 1, v_a_160_);
return v___x_164_;
}
else
{
lean_object* v___x_165_; lean_object* v___x_166_; lean_object* v___x_167_; uint8_t v___x_168_; 
v___x_165_ = lean_unsigned_to_nat(0u);
v___x_166_ = l_Lean_Syntax_getArg(v_x_158_, v___x_165_);
v___x_167_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1));
lean_inc(v___x_166_);
v___x_168_ = l_Lean_Syntax_isOfKind(v___x_166_, v___x_167_);
if (v___x_168_ == 0)
{
lean_object* v___x_169_; lean_object* v___x_170_; 
lean_dec(v___x_166_);
lean_dec(v_x_158_);
v___x_169_ = lean_box(0);
v___x_170_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_170_, 0, v___x_169_);
lean_ctor_set(v___x_170_, 1, v_a_160_);
return v___x_170_;
}
else
{
lean_object* v___x_171_; lean_object* v___x_172_; uint8_t v___x_173_; 
v___x_171_ = lean_unsigned_to_nat(1u);
v___x_172_ = l_Lean_Syntax_getArg(v_x_158_, v___x_171_);
lean_dec(v_x_158_);
lean_inc(v___x_172_);
v___x_173_ = l_Lean_Syntax_matchesNull(v___x_172_, v___x_171_);
if (v___x_173_ == 0)
{
lean_object* v___x_174_; lean_object* v___x_175_; 
lean_dec(v___x_172_);
lean_dec(v___x_166_);
v___x_174_ = lean_box(0);
v___x_175_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_175_, 0, v___x_174_);
lean_ctor_set(v___x_175_, 1, v_a_160_);
return v___x_175_;
}
else
{
lean_object* v___x_176_; lean_object* v___x_177_; uint8_t v___x_178_; 
v___x_176_ = l_Lean_Syntax_getArg(v___x_172_, v___x_165_);
lean_dec(v___x_172_);
v___x_177_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta__1___closed__2));
v___x_178_ = l_Lean_Syntax_matchesIdent(v___x_176_, v___x_177_);
lean_dec(v___x_176_);
if (v___x_178_ == 0)
{
lean_object* v___x_179_; lean_object* v___x_180_; 
lean_dec(v___x_166_);
v___x_179_ = lean_box(0);
v___x_180_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_180_, 0, v___x_179_);
lean_ctor_set(v___x_180_, 1, v_a_160_);
return v___x_180_;
}
else
{
lean_object* v_ref_181_; uint8_t v___x_182_; lean_object* v___x_183_; lean_object* v___x_184_; lean_object* v___x_185_; lean_object* v___x_186_; lean_object* v___x_187_; lean_object* v___x_188_; 
v_ref_181_ = l_Lean_replaceRef(v___x_166_, v_a_159_);
lean_dec(v___x_166_);
v___x_182_ = 0;
v___x_183_ = l_Lean_SourceInfo_fromRef(v_ref_181_, v___x_182_);
lean_dec(v_ref_181_);
v___x_184_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__1));
v___x_185_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__derivriemannzeta___closed__2));
lean_inc(v___x_183_);
v___x_186_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_186_, 0, v___x_183_);
lean_ctor_set(v___x_186_, 1, v___x_185_);
v___x_187_ = l_Lean_Syntax_node1(v___x_183_, v___x_184_, v___x_186_);
v___x_188_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_188_, 0, v___x_187_);
lean_ctor_set(v___x_188_, 1, v_a_160_);
return v___x_188_;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__deriv__1___boxed(lean_object* v_x_189_, lean_object* v_a_190_, lean_object* v_a_191_){
_start:
{
lean_object* v_res_192_; 
v_res_192_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__deriv__1(v_x_189_, v_a_190_, v_a_191_);
lean_dec(v_a_190_);
return v_res_192_;
}
}
static lean_object* _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1(void){
_start:
{
lean_object* v___x_206_; lean_object* v___x_207_; 
v___x_206_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__0));
v___x_207_ = l_String_toRawSubstring_x27(v___x_206_);
return v___x_207_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1(lean_object* v_x_216_, lean_object* v_a_217_, lean_object* v_a_218_){
_start:
{
lean_object* v___x_219_; uint8_t v___x_220_; 
v___x_219_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1));
v___x_220_ = l_Lean_Syntax_isOfKind(v_x_216_, v___x_219_);
if (v___x_220_ == 0)
{
lean_object* v___x_221_; lean_object* v___x_222_; 
v___x_221_ = lean_box(1);
v___x_222_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_222_, 0, v___x_221_);
lean_ctor_set(v___x_222_, 1, v_a_218_);
return v___x_222_;
}
else
{
lean_object* v_quotContext_223_; lean_object* v_currMacroScope_224_; lean_object* v_ref_225_; uint8_t v___x_226_; lean_object* v___x_227_; lean_object* v___x_228_; lean_object* v___x_229_; lean_object* v___x_230_; lean_object* v___x_231_; lean_object* v___x_232_; lean_object* v___x_233_; 
v_quotContext_223_ = lean_ctor_get(v_a_217_, 1);
v_currMacroScope_224_ = lean_ctor_get(v_a_217_, 2);
v_ref_225_ = lean_ctor_get(v_a_217_, 5);
v___x_226_ = 0;
v___x_227_ = l_Lean_SourceInfo_fromRef(v_ref_225_, v___x_226_);
v___x_228_ = lean_obj_once(&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1, &lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1_once, _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__1);
v___x_229_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__2));
lean_inc(v_currMacroScope_224_);
lean_inc(v_quotContext_223_);
v___x_230_ = l_Lean_addMacroScope(v_quotContext_223_, v___x_229_, v_currMacroScope_224_);
v___x_231_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___closed__4));
v___x_232_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_232_, 0, v___x_227_);
lean_ctor_set(v___x_232_, 1, v___x_228_);
lean_ctor_set(v___x_232_, 2, v___x_230_);
lean_ctor_set(v___x_232_, 3, v___x_231_);
v___x_233_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_233_, 0, v___x_232_);
lean_ctor_set(v___x_233_, 1, v_a_218_);
return v___x_233_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1___boxed(lean_object* v_x_234_, lean_object* v_a_235_, lean_object* v_a_236_){
_start:
{
lean_object* v_res_237_; 
v_res_237_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__riemannzeta0__1(v_x_234_, v_a_235_, v_a_236_);
lean_dec_ref(v_a_235_);
return v_res_237_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta0__1(lean_object* v_x_238_, lean_object* v_a_239_, lean_object* v_a_240_){
_start:
{
lean_object* v___x_241_; uint8_t v___x_242_; 
v___x_241_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1));
lean_inc(v_x_238_);
v___x_242_ = l_Lean_Syntax_isOfKind(v_x_238_, v___x_241_);
if (v___x_242_ == 0)
{
lean_object* v___x_243_; lean_object* v___x_244_; 
lean_dec(v_x_238_);
v___x_243_ = lean_box(0);
v___x_244_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_244_, 0, v___x_243_);
lean_ctor_set(v___x_244_, 1, v_a_240_);
return v___x_244_;
}
else
{
lean_object* v_ref_245_; uint8_t v___x_246_; lean_object* v___x_247_; lean_object* v___x_248_; lean_object* v___x_249_; lean_object* v___x_250_; lean_object* v___x_251_; lean_object* v___x_252_; 
v_ref_245_ = l_Lean_replaceRef(v_x_238_, v_a_239_);
lean_dec(v_x_238_);
v___x_246_ = 0;
v___x_247_ = l_Lean_SourceInfo_fromRef(v_ref_245_, v___x_246_);
lean_dec(v_ref_245_);
v___x_248_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__1));
v___x_249_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__riemannzeta0___closed__2));
lean_inc(v___x_247_);
v___x_250_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_250_, 0, v___x_247_);
lean_ctor_set(v___x_250_, 1, v___x_249_);
v___x_251_ = l_Lean_Syntax_node1(v___x_247_, v___x_248_, v___x_250_);
v___x_252_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_252_, 0, v___x_251_);
lean_ctor_set(v___x_252_, 1, v_a_240_);
return v___x_252_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta0__1___boxed(lean_object* v_x_253_, lean_object* v_a_254_, lean_object* v_a_255_){
_start:
{
lean_object* v_res_256_; 
v_res_256_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta0__1(v_x_253_, v_a_254_, v_a_255_);
lean_dec(v_a_254_);
return v_res_256_;
}
}
static lean_object* _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1(void){
_start:
{
lean_object* v___x_270_; lean_object* v___x_271_; 
v___x_270_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__0));
v___x_271_ = l_String_toRawSubstring_x27(v___x_270_);
return v___x_271_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1(lean_object* v_x_284_, lean_object* v_a_285_, lean_object* v_a_286_){
_start:
{
lean_object* v___x_287_; uint8_t v___x_288_; 
v___x_287_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1));
v___x_288_ = l_Lean_Syntax_isOfKind(v_x_284_, v___x_287_);
if (v___x_288_ == 0)
{
lean_object* v___x_289_; lean_object* v___x_290_; 
v___x_289_ = lean_box(1);
v___x_290_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_290_, 0, v___x_289_);
lean_ctor_set(v___x_290_, 1, v_a_286_);
return v___x_290_;
}
else
{
lean_object* v_quotContext_291_; lean_object* v_currMacroScope_292_; lean_object* v_ref_293_; uint8_t v___x_294_; lean_object* v___x_295_; lean_object* v___x_296_; lean_object* v___x_297_; lean_object* v___x_298_; lean_object* v___x_299_; lean_object* v___x_300_; lean_object* v___x_301_; 
v_quotContext_291_ = lean_ctor_get(v_a_285_, 1);
v_currMacroScope_292_ = lean_ctor_get(v_a_285_, 2);
v_ref_293_ = lean_ctor_get(v_a_285_, 5);
v___x_294_ = 0;
v___x_295_ = l_Lean_SourceInfo_fromRef(v_ref_293_, v___x_294_);
v___x_296_ = lean_obj_once(&lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1, &lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1_once, _init_lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__1);
v___x_297_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__2));
lean_inc(v_currMacroScope_292_);
lean_inc(v_quotContext_291_);
v___x_298_ = l_Lean_addMacroScope(v_quotContext_291_, v___x_297_, v_currMacroScope_292_);
v___x_299_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___closed__6));
v___x_300_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_300_, 0, v___x_295_);
lean_ctor_set(v___x_300_, 1, v___x_296_);
lean_ctor_set(v___x_300_, 2, v___x_298_);
lean_ctor_set(v___x_300_, 3, v___x_299_);
v___x_301_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_301_, 0, v___x_300_);
lean_ctor_set(v___x_301_, 1, v_a_286_);
return v___x_301_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1___boxed(lean_object* v_x_302_, lean_object* v_a_303_, lean_object* v_a_304_){
_start:
{
lean_object* v_res_305_; 
v_res_305_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______macroRules____private__Zeta23__FromPNTPlus__ZetaBounds__0__zb__Lambda__1(v_x_302_, v_a_303_, v_a_304_);
lean_dec_ref(v_a_303_);
return v_res_305_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__ArithmeticFunction__vonMangoldt__1(lean_object* v_x_306_, lean_object* v_a_307_, lean_object* v_a_308_){
_start:
{
lean_object* v___x_309_; uint8_t v___x_310_; 
v___x_309_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__riemannZeta__1___closed__1));
lean_inc(v_x_306_);
v___x_310_ = l_Lean_Syntax_isOfKind(v_x_306_, v___x_309_);
if (v___x_310_ == 0)
{
lean_object* v___x_311_; lean_object* v___x_312_; 
lean_dec(v_x_306_);
v___x_311_ = lean_box(0);
v___x_312_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_312_, 0, v___x_311_);
lean_ctor_set(v___x_312_, 1, v_a_308_);
return v___x_312_;
}
else
{
lean_object* v_ref_313_; uint8_t v___x_314_; lean_object* v___x_315_; lean_object* v___x_316_; lean_object* v___x_317_; lean_object* v___x_318_; lean_object* v___x_319_; lean_object* v___x_320_; 
v_ref_313_ = l_Lean_replaceRef(v_x_306_, v_a_307_);
lean_dec(v_x_306_);
v___x_314_ = 0;
v___x_315_ = l_Lean_SourceInfo_fromRef(v_ref_313_, v___x_314_);
lean_dec(v_ref_313_);
v___x_316_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__1));
v___x_317_ = ((lean_object*)(lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0__zb__Lambda___closed__2));
lean_inc(v___x_315_);
v___x_318_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_318_, 0, v___x_315_);
lean_ctor_set(v___x_318_, 1, v___x_317_);
v___x_319_ = l_Lean_Syntax_node1(v___x_315_, v___x_316_, v___x_318_);
v___x_320_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_320_, 0, v___x_319_);
lean_ctor_set(v___x_320_, 1, v_a_308_);
return v___x_320_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__ArithmeticFunction__vonMangoldt__1___boxed(lean_object* v_x_321_, lean_object* v_a_322_, lean_object* v_a_323_){
_start:
{
lean_object* v_res_324_; 
v_res_324_ = lp_Zeta23___private_Zeta23_FromPNTPlus_ZetaBounds_0____aux__Zeta23__FromPNTPlus__ZetaBounds______unexpand__ArithmeticFunction__vonMangoldt__1(v_x_321_, v_a_322_, v_a_323_);
lean_dec(v_a_322_);
return v_res_324_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_batteries_Batteries_Tactic_Lemma(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Function_Floor(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_MeasureTheory_Order_Group_Lattice(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_Harmonic_Bounds(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_NumberTheory_LSeries_Nonvanishing(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Auxiliary(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Fourier(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Mathlib_Analysis_SpecialFunctions_Log_Basic(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_ResidueCalcOnRectangles(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_EulerMaclaurin(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_ZetaBounds(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_batteries_Batteries_Tactic_Lemma(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Function_Floor(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_MeasureTheory_Order_Group_Lattice(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_Harmonic_Bounds(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_NumberTheory_LSeries_Nonvanishing(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_Auxiliary(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_Fourier(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_Mathlib_Analysis_SpecialFunctions_Log_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_ResidueCalcOnRectangles(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_FromPNTPlus_EulerMaclaurin(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
