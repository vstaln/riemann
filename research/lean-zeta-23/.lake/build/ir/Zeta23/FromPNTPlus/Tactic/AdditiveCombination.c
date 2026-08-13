// Lean compiler output
// Module: Zeta23.FromPNTPlus.Tactic.AdditiveCombination
// Imports: public import Init public meta import Init public import Mathlib.Tactic.Abel public import Mathlib.Tactic.LinearCombinationPrime
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
lean_object* l_Lean_Name_mkStr4(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Name_mkStr1(lean_object*);
lean_object* l_Lean_stringToMessageData(lean_object*);
uint8_t l_Lean_Syntax_isOfKind(lean_object*, lean_object*);
lean_object* l_Lean_replaceRef(lean_object*, lean_object*);
lean_object* l_Lean_Elab_Term_elabTerm___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeLightImp___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lean_infer_type(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Meta_whnfR(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t l_Lean_Expr_isEq(lean_object*);
lean_object* lp_batteries_Lean_Expr_toSyntax(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(lean_object*, uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_getArg(lean_object*, lean_object*);
lean_object* l_Lean_SourceInfo_fromRef(lean_object*, uint8_t);
lean_object* l_String_toRawSubstring_x27(lean_object*);
lean_object* l_Lean_addMacroScope(lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node2(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node3(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Name_mkStr2(lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node1(lean_object*, lean_object*, lean_object*);
uint8_t l_Lean_Syntax_matchesIdent(lean_object*, lean_object*);
lean_object* lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_expandLinearCombo(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_TSyntax_getNat(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_Array_mkArray0(lean_object*);
lean_object* l_Lean_Syntax_node4(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node5(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
lean_object* l_Lean_Core_withFreshMacroScope___redArg(lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Elab_Tactic_evalTactic___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Lean_Elab_Term_withoutErrToSorry___at___00Mathlib_Tactic_LinearCombinationPrime_elabLinearCombination_x27_spec__0___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_node6(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Elab_Tactic_getMainGoal___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_MVarId_getType_x27(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t l_Lean_Expr_isAppOfArity(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Lean_throwError___at___00Mathlib_Tactic_LinearCombinationPrime_elabLinearCombination_x27_spec__1___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Expr_appFn_x21(lean_object*);
lean_object* l_Lean_Expr_appArg_x21(lean_object*);
lean_object* l_Lean_Elab_Tactic_withMainContext___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_Lean_Syntax_getOptional_x3f(lean_object*);
uint8_t l_Lean_Syntax_isNone(lean_object*);
uint8_t l_Lean_Syntax_matchesNull(lean_object*, lean_object*);
extern lean_object* lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_normStx;
extern lean_object* lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_expStx;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "Lean"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "Parser"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "Term"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 5, .m_data = "paren"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__3 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__3_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__3_value),LEAN_SCALAR_PTR_LITERAL(124, 9, 161, 194, 227, 100, 20, 110)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "term_+_"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__5 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__5_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__5_value),LEAN_SCALAR_PTR_LITERAL(57, 160, 89, 154, 247, 230, 95, 119)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__6 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__6_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "term_-_"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__7 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__7_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__7_value),LEAN_SCALAR_PTR_LITERAL(92, 98, 183, 241, 65, 154, 192, 109)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__8 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__8_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "term-_"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__9 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__9_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__9_value),LEAN_SCALAR_PTR_LITERAL(77, 127, 37, 42, 155, 196, 209, 131)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__10 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__10_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 13, .m_capacity = 13, .m_length = 12, .m_data = "nestedAction"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__11 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__11_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__11_value),LEAN_SCALAR_PTR_LITERAL(115, 27, 24, 243, 204, 49, 153, 202)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 7, .m_data = "term_•_"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__13 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__13_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__13_value),LEAN_SCALAR_PTR_LITERAL(39, 170, 60, 237, 168, 151, 8, 86)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__14 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__14_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 3, .m_data = "app"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__15 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__15_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__15_value),LEAN_SCALAR_PTR_LITERAL(69, 118, 10, 41, 220, 156, 243, 179)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "smul_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17_value),LEAN_SCALAR_PTR_LITERAL(245, 108, 136, 98, 157, 165, 125, 9)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__19 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__19_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "Mathlib"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "Tactic"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 23, .m_capacity = 23, .m_length = 22, .m_data = "LinearCombinationPrime"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17_value),LEAN_SCALAR_PTR_LITERAL(100, 59, 88, 175, 109, 166, 188, 32)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__23_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__24 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__24_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__24_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__25 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__25_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "null"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__26 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__26_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__26_value),LEAN_SCALAR_PTR_LITERAL(24, 58, 49, 223, 146, 207, 197, 136)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "pf_smul_c"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__30_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28_value),LEAN_SCALAR_PTR_LITERAL(163, 131, 115, 236, 168, 159, 239, 9)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__30 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__30_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28_value),LEAN_SCALAR_PTR_LITERAL(10, 226, 228, 213, 196, 21, 219, 23)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__31_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__32 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__32_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__32_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__33 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__33_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "c_smul_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34_value),LEAN_SCALAR_PTR_LITERAL(231, 178, 94, 189, 15, 226, 50, 239)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__36 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__36_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34_value),LEAN_SCALAR_PTR_LITERAL(150, 102, 230, 142, 214, 24, 234, 180)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__38_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__37_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__38 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__38_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__39_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__38_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__39 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__39_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__40_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 1, .m_data = "•"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__40 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__40_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__41_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "doExpr"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__41 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__41_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__41_value),LEAN_SCALAR_PTR_LITERAL(130, 168, 60, 255, 153, 218, 88, 77)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__43_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "Eq.symm"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__43 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__43_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 3, .m_capacity = 3, .m_length = 2, .m_data = "Eq"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__46_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "symm"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__46 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__46_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45_value),LEAN_SCALAR_PTR_LITERAL(143, 37, 101, 248, 9, 246, 191, 223)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__46_value),LEAN_SCALAR_PTR_LITERAL(220, 149, 144, 59, 77, 93, 25, 217)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__48_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__48 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__48_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__49_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__48_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__49 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__49_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "neg_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__52_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50_value),LEAN_SCALAR_PTR_LITERAL(209, 55, 26, 213, 241, 162, 45, 8)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__52 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__52_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50_value),LEAN_SCALAR_PTR_LITERAL(216, 200, 97, 190, 64, 172, 89, 213)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__54_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__53_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__54 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__54_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__55_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__54_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__55 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__55_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__56_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "-"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__56 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__56_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "sub_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__59_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57_value),LEAN_SCALAR_PTR_LITERAL(251, 124, 25, 14, 254, 28, 162, 249)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__59 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__59_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57_value),LEAN_SCALAR_PTR_LITERAL(2, 142, 196, 253, 31, 132, 215, 230)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__61_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__60_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__61 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__61_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__62_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__61_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__62 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__62_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "pf_sub_c"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__65_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63_value),LEAN_SCALAR_PTR_LITERAL(244, 12, 129, 160, 44, 202, 42, 130)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__65 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__65_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63_value),LEAN_SCALAR_PTR_LITERAL(229, 139, 58, 145, 64, 250, 7, 194)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__67_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__66_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__67 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__67_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__68_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__67_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__68 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__68_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "c_sub_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__71_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69_value),LEAN_SCALAR_PTR_LITERAL(20, 128, 60, 67, 183, 151, 115, 243)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__71 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__71_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69_value),LEAN_SCALAR_PTR_LITERAL(69, 228, 81, 231, 64, 211, 184, 91)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__73_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__72_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__73 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__73_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__74_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__73_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__74 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__74_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "add_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__77_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75_value),LEAN_SCALAR_PTR_LITERAL(152, 151, 47, 0, 60, 60, 23, 79)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__77 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__77_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75_value),LEAN_SCALAR_PTR_LITERAL(145, 6, 127, 60, 171, 71, 211, 238)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__79_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__78_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__79 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__79_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__80_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__79_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__80 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__80_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "pf_add_c"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__83_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81_value),LEAN_SCALAR_PTR_LITERAL(157, 55, 239, 191, 165, 108, 153, 14)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__83 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__83_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81_value),LEAN_SCALAR_PTR_LITERAL(12, 6, 195, 52, 242, 149, 186, 59)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__85_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__84_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__85 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__85_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__86_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__85_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__86 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__86_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "c_add_pf"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__89_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87_value),LEAN_SCALAR_PTR_LITERAL(106, 189, 212, 24, 57, 228, 240, 200)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__89 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__89_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87_value),LEAN_SCALAR_PTR_LITERAL(67, 68, 233, 118, 66, 201, 248, 56)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__91_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__90_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__91 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__91_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__92_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__91_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__92 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__92_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__93_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "+"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__93 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__93_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__94_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 15, .m_capacity = 15, .m_length = 14, .m_data = "hygienicLParen"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__94 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__94_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__94_value),LEAN_SCALAR_PTR_LITERAL(41, 104, 206, 51, 21, 254, 100, 101)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__96_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "hygieneInfo"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__96 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__96_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__97_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__96_value),LEAN_SCALAR_PTR_LITERAL(27, 64, 36, 144, 170, 151, 255, 136)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__97 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__97_value;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__3_value),LEAN_SCALAR_PTR_LITERAL(117, 253, 122, 28, 77, 248, 149, 120)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "("};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "tacticSeq"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__2 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__2_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__2_value),LEAN_SCALAR_PTR_LITERAL(212, 140, 85, 215, 241, 69, 7, 118)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 19, .m_capacity = 19, .m_length = 18, .m_data = "tacticSeq1Indented"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__4 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__4_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__4_value),LEAN_SCALAR_PTR_LITERAL(223, 90, 160, 238, 133, 180, 23, 239)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "refine"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6_value),LEAN_SCALAR_PTR_LITERAL(49, 130, 130, 160, 131, 48, 178, 245)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 14, .m_capacity = 14, .m_length = 13, .m_data = "eq_of_add_pow"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8_value),LEAN_SCALAR_PTR_LITERAL(57, 141, 124, 145, 18, 144, 130, 174)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__10 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__10_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8_value),LEAN_SCALAR_PTR_LITERAL(160, 107, 12, 123, 46, 63, 138, 15)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__11_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__12 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__12_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__12_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__13 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__13_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 14, .m_capacity = 14, .m_length = 13, .m_data = "syntheticHole"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__14 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__14_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__2_value),LEAN_SCALAR_PTR_LITERAL(75, 170, 162, 138, 136, 204, 251, 229)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__14_value),LEAN_SCALAR_PTR_LITERAL(218, 189, 67, 60, 211, 196, 112, 165)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "\?"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "a"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__17 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__17_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__17_value),LEAN_SCALAR_PTR_LITERAL(247, 80, 99, 121, 74, 33, 203, 108)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = ";"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 5, .m_data = "case'"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21_value),LEAN_SCALAR_PTR_LITERAL(134, 21, 185, 205, 238, 88, 7, 106)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "caseArg"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__23 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__23_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__23_value),LEAN_SCALAR_PTR_LITERAL(151, 119, 254, 229, 232, 21, 225, 201)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 11, .m_data = "binderIdent"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__25 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__25_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__25_value),LEAN_SCALAR_PTR_LITERAL(37, 194, 68, 106, 254, 181, 31, 191)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 3, .m_capacity = 3, .m_length = 2, .m_data = "=>"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = ")"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "eq_of_add"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30_value),LEAN_SCALAR_PTR_LITERAL(137, 248, 140, 95, 132, 224, 134, 120)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__32 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__32_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30_value),LEAN_SCALAR_PTR_LITERAL(80, 164, 59, 15, 44, 161, 225, 106)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__33_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__34 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__34_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__35_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__34_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__35 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__35_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 12, .m_capacity = 12, .m_length = 9, .m_data = "eq_trans₃"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__38_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36_value),LEAN_SCALAR_PTR_LITERAL(91, 163, 54, 164, 184, 224, 80, 112)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__38 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__38_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36_value),LEAN_SCALAR_PTR_LITERAL(34, 37, 247, 50, 143, 128, 197, 163)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__40_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__39_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__40 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__40_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__41_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__40_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__41 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__41_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__42_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "b"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__42 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__42_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__44_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__42_value),LEAN_SCALAR_PTR_LITERAL(47, 22, 244, 233, 226, 169, 241, 142)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__44 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__44_value;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0(uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 15, .m_capacity = 15, .m_length = 14, .m_data = "UnhygienicMain"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__0 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__0_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(124, 169, 242, 144, 140, 56, 85, 78)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__1 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__1_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 11, .m_capacity = 11, .m_length = 10, .m_data = "tacticTry_"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__2 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__2_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__2_value),LEAN_SCALAR_PTR_LITERAL(34, 109, 187, 155, 23, 130, 33, 152)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 3, .m_data = "try"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__4 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__4_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "simp"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__5 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__5_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__5_value),LEAN_SCALAR_PTR_LITERAL(50, 13, 241, 145, 67, 153, 105, 177)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "optConfig"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__7 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__7_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__7_value),LEAN_SCALAR_PTR_LITERAL(137, 208, 10, 74, 108, 50, 106, 48)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "only"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__9 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__9_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "["};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__10 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__10_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 10, .m_capacity = 10, .m_length = 9, .m_data = "simpLemma"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__11 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__11_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__0_value),LEAN_SCALAR_PTR_LITERAL(70, 193, 83, 126, 233, 67, 208, 165)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__1_value),LEAN_SCALAR_PTR_LITERAL(103, 136, 125, 166, 167, 98, 71, 111)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(166, 58, 35, 182, 187, 130, 147, 254)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__11_value),LEAN_SCALAR_PTR_LITERAL(38, 215, 101, 250, 181, 108, 118, 102)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "smul_add"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__13 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__13_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__13_value),LEAN_SCALAR_PTR_LITERAL(165, 42, 232, 187, 143, 16, 187, 237)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__15 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__15_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = ","};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__17 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__17_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "smul_sub"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__18 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__18_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__18_value),LEAN_SCALAR_PTR_LITERAL(124, 49, 137, 217, 117, 19, 43, 133)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__20 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__20_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "]"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__22 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__22_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "Abel"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__23 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__23_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "abel"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__24 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__24_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__23_value),LEAN_SCALAR_PTR_LITERAL(127, 220, 84, 140, 79, 41, 205, 100)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__24_value),LEAN_SCALAR_PTR_LITERAL(55, 207, 94, 79, 28, 196, 87, 177)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45_value),LEAN_SCALAR_PTR_LITERAL(143, 37, 101, 248, 9, 246, 191, 223)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__26 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__26_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__27_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 46, .m_capacity = 46, .m_length = 45, .m_data = "'additive_combination' only proves equalities"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__27 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__27_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__29_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "Eq.refl"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__29 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__29_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__31_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "refl"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__31 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__31_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__45_value),LEAN_SCALAR_PTR_LITERAL(143, 37, 101, 248, 9, 246, 191, 223)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__31_value),LEAN_SCALAR_PTR_LITERAL(72, 6, 107, 181, 0, 125, 21, 187)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__33 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__33_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__33_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__34 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__34_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__35_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 4, .m_capacity = 4, .m_length = 3, .m_data = "num"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__35 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__35_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__35_value),LEAN_SCALAR_PTR_LITERAL(227, 68, 22, 222, 47, 51, 204, 84)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__36 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__36_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__37_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 2, .m_capacity = 2, .m_length = 1, .m_data = "0"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__37 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__37_value;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1(uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination(lean_object*, lean_object*, lean_object*, lean_object*, uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 20, .m_capacity = 20, .m_length = 19, .m_data = "AdditiveCombination"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__0 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__0_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__0_value),LEAN_SCALAR_PTR_LITERAL(107, 187, 248, 112, 56, 166, 70, 220)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "andthen"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__2 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__2_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__2_value),LEAN_SCALAR_PTR_LITERAL(40, 255, 78, 30, 143, 119, 117, 174)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 21, .m_capacity = 21, .m_length = 20, .m_data = "additive_combination"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__4 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__4_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 8, .m_other = 1, .m_tag = 6}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__4_value),LEAN_SCALAR_PTR_LITERAL(0, 0, 0, 0, 0, 0, 0, 0)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__5 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__5_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 9, .m_capacity = 9, .m_length = 8, .m_data = "optional"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__6 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__6_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__6_value),LEAN_SCALAR_PTR_LITERAL(233, 141, 154, 50, 143, 135, 42, 252)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "ppSpace"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__12 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__12_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__12_value),LEAN_SCALAR_PTR_LITERAL(207, 47, 58, 43, 30, 240, 125, 246)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__13 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__13_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 0}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__13_value)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__14 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__14_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 6, .m_capacity = 6, .m_length = 5, .m_data = "colGt"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__15 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__15_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__15_value),LEAN_SCALAR_PTR_LITERAL(185, 236, 32, 153, 169, 213, 53, 244)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__16 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__16_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 0}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__16_value)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__17 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__17_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 2}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3_value),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__14_value),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__17_value)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__18 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__18_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 5, .m_capacity = 5, .m_length = 4, .m_data = "term"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__19 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__19_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__19_value),LEAN_SCALAR_PTR_LITERAL(187, 230, 181, 162, 253, 146, 122, 119)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__20 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__20_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 7}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__20_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__21 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__21_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*3 + 0, .m_other = 3, .m_tag = 2}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3_value),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__18_value),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__21_value)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__22 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__22_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7_value),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__22_value)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__23 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__23_value;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24;
static lean_once_cell_t lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 7, .m_capacity = 7, .m_length = 6, .m_data = "expStx"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__0 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__0_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__0_value),LEAN_SCALAR_PTR_LITERAL(210, 86, 211, 90, 64, 112, 83, 83)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1_value;
static const lean_string_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 8, .m_capacity = 8, .m_length = 7, .m_data = "normStx"};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__2 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__2_value;
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_0 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__20_value),LEAN_SCALAR_PTR_LITERAL(118, 213, 161, 2, 73, 184, 31, 228)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_1 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_0),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__21_value),LEAN_SCALAR_PTR_LITERAL(139, 222, 98, 232, 116, 132, 69, 249)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_2 = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_1),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__22_value),LEAN_SCALAR_PTR_LITERAL(142, 199, 207, 73, 87, 45, 84, 242)}};
static const lean_ctor_object lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 8, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value_aux_2),((lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__2_value),LEAN_SCALAR_PTR_LITERAL(69, 210, 34, 3, 14, 114, 7, 205)}};
static const lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3 = (const lean_object*)&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3_value;
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0(lean_object* v___x_1_, lean_object* v___y_2_, lean_object* v___y_3_, lean_object* v___y_4_, lean_object* v___y_5_, lean_object* v___y_6_, lean_object* v___y_7_){
_start:
{
lean_object* v___x_9_; 
v___x_9_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeLightImp___redArg(v___x_1_, v___y_2_, v___y_3_, v___y_4_, v___y_5_, v___y_6_, v___y_7_);
if (lean_obj_tag(v___x_9_) == 0)
{
lean_object* v_a_10_; lean_object* v___x_11_; 
v_a_10_ = lean_ctor_get(v___x_9_, 0);
lean_inc_n(v_a_10_, 2);
lean_dec_ref_known(v___x_9_, 1);
lean_inc(v___y_7_);
lean_inc_ref(v___y_6_);
lean_inc(v___y_5_);
lean_inc_ref(v___y_4_);
v___x_11_ = lean_infer_type(v_a_10_, v___y_4_, v___y_5_, v___y_6_, v___y_7_);
if (lean_obj_tag(v___x_11_) == 0)
{
lean_object* v_a_12_; lean_object* v___x_13_; 
v_a_12_ = lean_ctor_get(v___x_11_, 0);
lean_inc(v_a_12_);
lean_dec_ref_known(v___x_11_, 1);
v___x_13_ = l_Lean_Meta_whnfR(v_a_12_, v___y_4_, v___y_5_, v___y_6_, v___y_7_);
if (lean_obj_tag(v___x_13_) == 0)
{
lean_object* v_a_14_; uint8_t v___x_15_; 
v_a_14_ = lean_ctor_get(v___x_13_, 0);
lean_inc(v_a_14_);
lean_dec_ref_known(v___x_13_, 1);
v___x_15_ = l_Lean_Expr_isEq(v_a_14_);
lean_dec(v_a_14_);
if (v___x_15_ == 0)
{
lean_object* v___x_16_; 
v___x_16_ = lp_batteries_Lean_Expr_toSyntax(v_a_10_, v___y_2_, v___y_3_, v___y_4_, v___y_5_, v___y_6_, v___y_7_);
lean_dec(v___y_7_);
lean_dec_ref(v___y_6_);
lean_dec(v___y_5_);
lean_dec_ref(v___y_4_);
if (lean_obj_tag(v___x_16_) == 0)
{
lean_object* v_a_17_; lean_object* v___x_19_; uint8_t v_isShared_20_; uint8_t v_isSharedCheck_25_; 
v_a_17_ = lean_ctor_get(v___x_16_, 0);
v_isSharedCheck_25_ = !lean_is_exclusive(v___x_16_);
if (v_isSharedCheck_25_ == 0)
{
v___x_19_ = v___x_16_;
v_isShared_20_ = v_isSharedCheck_25_;
goto v_resetjp_18_;
}
else
{
lean_inc(v_a_17_);
lean_dec(v___x_16_);
v___x_19_ = lean_box(0);
v_isShared_20_ = v_isSharedCheck_25_;
goto v_resetjp_18_;
}
v_resetjp_18_:
{
lean_object* v___x_21_; lean_object* v___x_23_; 
v___x_21_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_21_, 0, v_a_17_);
if (v_isShared_20_ == 0)
{
lean_ctor_set(v___x_19_, 0, v___x_21_);
v___x_23_ = v___x_19_;
goto v_reusejp_22_;
}
else
{
lean_object* v_reuseFailAlloc_24_; 
v_reuseFailAlloc_24_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_24_, 0, v___x_21_);
v___x_23_ = v_reuseFailAlloc_24_;
goto v_reusejp_22_;
}
v_reusejp_22_:
{
return v___x_23_;
}
}
}
else
{
lean_object* v_a_26_; lean_object* v___x_28_; uint8_t v_isShared_29_; uint8_t v_isSharedCheck_33_; 
v_a_26_ = lean_ctor_get(v___x_16_, 0);
v_isSharedCheck_33_ = !lean_is_exclusive(v___x_16_);
if (v_isSharedCheck_33_ == 0)
{
v___x_28_ = v___x_16_;
v_isShared_29_ = v_isSharedCheck_33_;
goto v_resetjp_27_;
}
else
{
lean_inc(v_a_26_);
lean_dec(v___x_16_);
v___x_28_ = lean_box(0);
v_isShared_29_ = v_isSharedCheck_33_;
goto v_resetjp_27_;
}
v_resetjp_27_:
{
lean_object* v___x_31_; 
if (v_isShared_29_ == 0)
{
v___x_31_ = v___x_28_;
goto v_reusejp_30_;
}
else
{
lean_object* v_reuseFailAlloc_32_; 
v_reuseFailAlloc_32_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_32_, 0, v_a_26_);
v___x_31_ = v_reuseFailAlloc_32_;
goto v_reusejp_30_;
}
v_reusejp_30_:
{
return v___x_31_;
}
}
}
}
else
{
lean_object* v___x_34_; 
v___x_34_ = lp_batteries_Lean_Expr_toSyntax(v_a_10_, v___y_2_, v___y_3_, v___y_4_, v___y_5_, v___y_6_, v___y_7_);
lean_dec(v___y_7_);
lean_dec_ref(v___y_6_);
lean_dec(v___y_5_);
lean_dec_ref(v___y_4_);
if (lean_obj_tag(v___x_34_) == 0)
{
lean_object* v_a_35_; lean_object* v___x_37_; uint8_t v_isShared_38_; uint8_t v_isSharedCheck_43_; 
v_a_35_ = lean_ctor_get(v___x_34_, 0);
v_isSharedCheck_43_ = !lean_is_exclusive(v___x_34_);
if (v_isSharedCheck_43_ == 0)
{
v___x_37_ = v___x_34_;
v_isShared_38_ = v_isSharedCheck_43_;
goto v_resetjp_36_;
}
else
{
lean_inc(v_a_35_);
lean_dec(v___x_34_);
v___x_37_ = lean_box(0);
v_isShared_38_ = v_isSharedCheck_43_;
goto v_resetjp_36_;
}
v_resetjp_36_:
{
lean_object* v___x_39_; lean_object* v___x_41_; 
v___x_39_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v___x_39_, 0, v_a_35_);
if (v_isShared_38_ == 0)
{
lean_ctor_set(v___x_37_, 0, v___x_39_);
v___x_41_ = v___x_37_;
goto v_reusejp_40_;
}
else
{
lean_object* v_reuseFailAlloc_42_; 
v_reuseFailAlloc_42_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_42_, 0, v___x_39_);
v___x_41_ = v_reuseFailAlloc_42_;
goto v_reusejp_40_;
}
v_reusejp_40_:
{
return v___x_41_;
}
}
}
else
{
lean_object* v_a_44_; lean_object* v___x_46_; uint8_t v_isShared_47_; uint8_t v_isSharedCheck_51_; 
v_a_44_ = lean_ctor_get(v___x_34_, 0);
v_isSharedCheck_51_ = !lean_is_exclusive(v___x_34_);
if (v_isSharedCheck_51_ == 0)
{
v___x_46_ = v___x_34_;
v_isShared_47_ = v_isSharedCheck_51_;
goto v_resetjp_45_;
}
else
{
lean_inc(v_a_44_);
lean_dec(v___x_34_);
v___x_46_ = lean_box(0);
v_isShared_47_ = v_isSharedCheck_51_;
goto v_resetjp_45_;
}
v_resetjp_45_:
{
lean_object* v___x_49_; 
if (v_isShared_47_ == 0)
{
v___x_49_ = v___x_46_;
goto v_reusejp_48_;
}
else
{
lean_object* v_reuseFailAlloc_50_; 
v_reuseFailAlloc_50_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_50_, 0, v_a_44_);
v___x_49_ = v_reuseFailAlloc_50_;
goto v_reusejp_48_;
}
v_reusejp_48_:
{
return v___x_49_;
}
}
}
}
}
else
{
lean_object* v_a_52_; lean_object* v___x_54_; uint8_t v_isShared_55_; uint8_t v_isSharedCheck_59_; 
lean_dec(v_a_10_);
lean_dec(v___y_7_);
lean_dec_ref(v___y_6_);
lean_dec(v___y_5_);
lean_dec_ref(v___y_4_);
v_a_52_ = lean_ctor_get(v___x_13_, 0);
v_isSharedCheck_59_ = !lean_is_exclusive(v___x_13_);
if (v_isSharedCheck_59_ == 0)
{
v___x_54_ = v___x_13_;
v_isShared_55_ = v_isSharedCheck_59_;
goto v_resetjp_53_;
}
else
{
lean_inc(v_a_52_);
lean_dec(v___x_13_);
v___x_54_ = lean_box(0);
v_isShared_55_ = v_isSharedCheck_59_;
goto v_resetjp_53_;
}
v_resetjp_53_:
{
lean_object* v___x_57_; 
if (v_isShared_55_ == 0)
{
v___x_57_ = v___x_54_;
goto v_reusejp_56_;
}
else
{
lean_object* v_reuseFailAlloc_58_; 
v_reuseFailAlloc_58_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_58_, 0, v_a_52_);
v___x_57_ = v_reuseFailAlloc_58_;
goto v_reusejp_56_;
}
v_reusejp_56_:
{
return v___x_57_;
}
}
}
}
else
{
lean_object* v_a_60_; lean_object* v___x_62_; uint8_t v_isShared_63_; uint8_t v_isSharedCheck_67_; 
lean_dec(v_a_10_);
lean_dec(v___y_7_);
lean_dec_ref(v___y_6_);
lean_dec(v___y_5_);
lean_dec_ref(v___y_4_);
v_a_60_ = lean_ctor_get(v___x_11_, 0);
v_isSharedCheck_67_ = !lean_is_exclusive(v___x_11_);
if (v_isSharedCheck_67_ == 0)
{
v___x_62_ = v___x_11_;
v_isShared_63_ = v_isSharedCheck_67_;
goto v_resetjp_61_;
}
else
{
lean_inc(v_a_60_);
lean_dec(v___x_11_);
v___x_62_ = lean_box(0);
v_isShared_63_ = v_isSharedCheck_67_;
goto v_resetjp_61_;
}
v_resetjp_61_:
{
lean_object* v___x_65_; 
if (v_isShared_63_ == 0)
{
v___x_65_ = v___x_62_;
goto v_reusejp_64_;
}
else
{
lean_object* v_reuseFailAlloc_66_; 
v_reuseFailAlloc_66_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_66_, 0, v_a_60_);
v___x_65_ = v_reuseFailAlloc_66_;
goto v_reusejp_64_;
}
v_reusejp_64_:
{
return v___x_65_;
}
}
}
}
else
{
lean_object* v_a_68_; lean_object* v___x_70_; uint8_t v_isShared_71_; uint8_t v_isSharedCheck_75_; 
lean_dec(v___y_7_);
lean_dec_ref(v___y_6_);
lean_dec(v___y_5_);
lean_dec_ref(v___y_4_);
v_a_68_ = lean_ctor_get(v___x_9_, 0);
v_isSharedCheck_75_ = !lean_is_exclusive(v___x_9_);
if (v_isSharedCheck_75_ == 0)
{
v___x_70_ = v___x_9_;
v_isShared_71_ = v_isSharedCheck_75_;
goto v_resetjp_69_;
}
else
{
lean_inc(v_a_68_);
lean_dec(v___x_9_);
v___x_70_ = lean_box(0);
v_isShared_71_ = v_isSharedCheck_75_;
goto v_resetjp_69_;
}
v_resetjp_69_:
{
lean_object* v___x_73_; 
if (v_isShared_71_ == 0)
{
v___x_73_ = v___x_70_;
goto v_reusejp_72_;
}
else
{
lean_object* v_reuseFailAlloc_74_; 
v_reuseFailAlloc_74_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_74_, 0, v_a_68_);
v___x_73_ = v_reuseFailAlloc_74_;
goto v_reusejp_72_;
}
v_reusejp_72_:
{
return v___x_73_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed(lean_object* v___x_76_, lean_object* v___y_77_, lean_object* v___y_78_, lean_object* v___y_79_, lean_object* v___y_80_, lean_object* v___y_81_, lean_object* v___y_82_, lean_object* v___y_83_){
_start:
{
lean_object* v_res_84_; 
v_res_84_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0(v___x_76_, v___y_77_, v___y_78_, v___y_79_, v___y_80_, v___y_81_, v___y_82_);
lean_dec(v___y_78_);
lean_dec_ref(v___y_77_);
return v_res_84_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18(void){
_start:
{
lean_object* v___x_119_; lean_object* v___x_120_; 
v___x_119_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__17));
v___x_120_ = l_String_toRawSubstring_x27(v___x_119_);
return v___x_120_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29(void){
_start:
{
lean_object* v___x_141_; lean_object* v___x_142_; 
v___x_141_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__28));
v___x_142_ = l_String_toRawSubstring_x27(v___x_141_);
return v___x_142_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35(void){
_start:
{
lean_object* v___x_157_; lean_object* v___x_158_; 
v___x_157_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__34));
v___x_158_ = l_String_toRawSubstring_x27(v___x_157_);
return v___x_158_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44(void){
_start:
{
lean_object* v___x_180_; lean_object* v___x_181_; 
v___x_180_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__43));
v___x_181_ = l_String_toRawSubstring_x27(v___x_180_);
return v___x_181_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51(void){
_start:
{
lean_object* v___x_194_; lean_object* v___x_195_; 
v___x_194_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__50));
v___x_195_ = l_String_toRawSubstring_x27(v___x_194_);
return v___x_195_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58(void){
_start:
{
lean_object* v___x_211_; lean_object* v___x_212_; 
v___x_211_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__57));
v___x_212_ = l_String_toRawSubstring_x27(v___x_211_);
return v___x_212_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64(void){
_start:
{
lean_object* v___x_227_; lean_object* v___x_228_; 
v___x_227_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__63));
v___x_228_ = l_String_toRawSubstring_x27(v___x_227_);
return v___x_228_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70(void){
_start:
{
lean_object* v___x_243_; lean_object* v___x_244_; 
v___x_243_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__69));
v___x_244_ = l_String_toRawSubstring_x27(v___x_243_);
return v___x_244_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76(void){
_start:
{
lean_object* v___x_259_; lean_object* v___x_260_; 
v___x_259_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__75));
v___x_260_ = l_String_toRawSubstring_x27(v___x_259_);
return v___x_260_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82(void){
_start:
{
lean_object* v___x_275_; lean_object* v___x_276_; 
v___x_275_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__81));
v___x_276_ = l_String_toRawSubstring_x27(v___x_275_);
return v___x_276_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88(void){
_start:
{
lean_object* v___x_291_; lean_object* v___x_292_; 
v___x_291_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__87));
v___x_292_ = l_String_toRawSubstring_x27(v___x_291_);
return v___x_292_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(lean_object* v_ty_316_, lean_object* v_stx_317_, lean_object* v_a_318_, lean_object* v_a_319_, lean_object* v_a_320_, lean_object* v_a_321_, lean_object* v_a_322_, lean_object* v_a_323_){
_start:
{
lean_object* v_fileName_325_; lean_object* v_fileMap_326_; lean_object* v_options_327_; lean_object* v_currRecDepth_328_; lean_object* v_maxRecDepth_329_; lean_object* v_ref_330_; lean_object* v_currNamespace_331_; lean_object* v_openDecls_332_; lean_object* v_initHeartbeats_333_; lean_object* v_maxHeartbeats_334_; lean_object* v_quotContext_335_; lean_object* v_currMacroScope_336_; uint8_t v_diag_337_; lean_object* v_cancelTk_x3f_338_; uint8_t v_suppressElabErrors_339_; lean_object* v_inheritedTraceOptions_340_; lean_object* v___x_341_; uint8_t v___x_342_; uint8_t v___x_343_; lean_object* v_ref_344_; lean_object* v___x_345_; 
v_fileName_325_ = lean_ctor_get(v_a_322_, 0);
v_fileMap_326_ = lean_ctor_get(v_a_322_, 1);
v_options_327_ = lean_ctor_get(v_a_322_, 2);
v_currRecDepth_328_ = lean_ctor_get(v_a_322_, 3);
v_maxRecDepth_329_ = lean_ctor_get(v_a_322_, 4);
v_ref_330_ = lean_ctor_get(v_a_322_, 5);
v_currNamespace_331_ = lean_ctor_get(v_a_322_, 6);
v_openDecls_332_ = lean_ctor_get(v_a_322_, 7);
v_initHeartbeats_333_ = lean_ctor_get(v_a_322_, 8);
v_maxHeartbeats_334_ = lean_ctor_get(v_a_322_, 9);
v_quotContext_335_ = lean_ctor_get(v_a_322_, 10);
v_currMacroScope_336_ = lean_ctor_get(v_a_322_, 11);
v_diag_337_ = lean_ctor_get_uint8(v_a_322_, sizeof(void*)*14);
v_cancelTk_x3f_338_ = lean_ctor_get(v_a_322_, 12);
v_suppressElabErrors_339_ = lean_ctor_get_uint8(v_a_322_, sizeof(void*)*14 + 1);
v_inheritedTraceOptions_340_ = lean_ctor_get(v_a_322_, 13);
v___x_341_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__4));
lean_inc(v_stx_317_);
v___x_342_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_341_);
v___x_343_ = 1;
v_ref_344_ = l_Lean_replaceRef(v_stx_317_, v_ref_330_);
lean_inc_ref(v_inheritedTraceOptions_340_);
lean_inc(v_cancelTk_x3f_338_);
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
lean_inc(v_maxHeartbeats_334_);
lean_inc(v_initHeartbeats_333_);
lean_inc(v_openDecls_332_);
lean_inc(v_currNamespace_331_);
lean_inc(v_ref_344_);
lean_inc(v_maxRecDepth_329_);
lean_inc(v_currRecDepth_328_);
lean_inc_ref(v_options_327_);
lean_inc_ref(v_fileMap_326_);
lean_inc_ref(v_fileName_325_);
v___x_345_ = lean_alloc_ctor(0, 14, 2);
lean_ctor_set(v___x_345_, 0, v_fileName_325_);
lean_ctor_set(v___x_345_, 1, v_fileMap_326_);
lean_ctor_set(v___x_345_, 2, v_options_327_);
lean_ctor_set(v___x_345_, 3, v_currRecDepth_328_);
lean_ctor_set(v___x_345_, 4, v_maxRecDepth_329_);
lean_ctor_set(v___x_345_, 5, v_ref_344_);
lean_ctor_set(v___x_345_, 6, v_currNamespace_331_);
lean_ctor_set(v___x_345_, 7, v_openDecls_332_);
lean_ctor_set(v___x_345_, 8, v_initHeartbeats_333_);
lean_ctor_set(v___x_345_, 9, v_maxHeartbeats_334_);
lean_ctor_set(v___x_345_, 10, v_quotContext_335_);
lean_ctor_set(v___x_345_, 11, v_currMacroScope_336_);
lean_ctor_set(v___x_345_, 12, v_cancelTk_x3f_338_);
lean_ctor_set(v___x_345_, 13, v_inheritedTraceOptions_340_);
lean_ctor_set_uint8(v___x_345_, sizeof(void*)*14, v_diag_337_);
lean_ctor_set_uint8(v___x_345_, sizeof(void*)*14 + 1, v_suppressElabErrors_339_);
if (v___x_342_ == 0)
{
lean_object* v___x_346_; uint8_t v___x_347_; 
v___x_346_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__6));
lean_inc(v_stx_317_);
v___x_347_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_346_);
if (v___x_347_ == 0)
{
lean_object* v___x_348_; uint8_t v___x_349_; 
v___x_348_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__8));
lean_inc(v_stx_317_);
v___x_349_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_348_);
if (v___x_349_ == 0)
{
lean_object* v___x_350_; uint8_t v___x_351_; 
v___x_350_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__10));
lean_inc(v_stx_317_);
v___x_351_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_350_);
if (v___x_351_ == 0)
{
lean_object* v___x_352_; uint8_t v___x_353_; 
v___x_352_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__12));
lean_inc(v_stx_317_);
v___x_353_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_352_);
if (v___x_353_ == 0)
{
lean_object* v___x_354_; uint8_t v___x_355_; 
v___x_354_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__14));
lean_inc(v_stx_317_);
v___x_355_ = l_Lean_Syntax_isOfKind(v_stx_317_, v___x_354_);
if (v___x_355_ == 0)
{
lean_object* v___x_356_; lean_object* v___x_357_; lean_object* v___x_358_; lean_object* v___x_359_; lean_object* v___f_360_; uint8_t v___x_361_; lean_object* v___x_362_; 
lean_dec(v_ref_344_);
v___x_356_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_356_, 0, v_ty_316_);
v___x_357_ = lean_box(v___x_343_);
v___x_358_ = lean_box(v___x_343_);
v___x_359_ = lean_alloc_closure((void*)(l_Lean_Elab_Term_elabTerm___boxed), 11, 4);
lean_closure_set(v___x_359_, 0, v_stx_317_);
lean_closure_set(v___x_359_, 1, v___x_356_);
lean_closure_set(v___x_359_, 2, v___x_357_);
lean_closure_set(v___x_359_, 3, v___x_358_);
v___f_360_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed), 8, 1);
lean_closure_set(v___f_360_, 0, v___x_359_);
v___x_361_ = 1;
v___x_362_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(v___f_360_, v___x_361_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
return v___x_362_;
}
else
{
lean_object* v___x_363_; lean_object* v_e_u2081_364_; lean_object* v___x_365_; 
v___x_363_ = lean_unsigned_to_nat(0u);
v_e_u2081_364_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_363_);
lean_inc_ref(v_ty_316_);
v___x_365_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2081_364_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
if (lean_obj_tag(v___x_365_) == 0)
{
lean_object* v_a_366_; lean_object* v___x_367_; lean_object* v_e_u2082_368_; lean_object* v___x_369_; 
v_a_366_ = lean_ctor_get(v___x_365_, 0);
lean_inc(v_a_366_);
lean_dec_ref_known(v___x_365_, 1);
v___x_367_ = lean_unsigned_to_nat(2u);
v_e_u2082_368_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_367_);
lean_dec(v_stx_317_);
v___x_369_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2082_368_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
if (lean_obj_tag(v___x_369_) == 0)
{
if (lean_obj_tag(v_a_366_) == 0)
{
lean_object* v_a_370_; lean_object* v___x_372_; uint8_t v_isShared_373_; uint8_t v_isSharedCheck_418_; 
v_a_370_ = lean_ctor_get(v___x_369_, 0);
v_isSharedCheck_418_ = !lean_is_exclusive(v___x_369_);
if (v_isSharedCheck_418_ == 0)
{
v___x_372_ = v___x_369_;
v_isShared_373_ = v_isSharedCheck_418_;
goto v_resetjp_371_;
}
else
{
lean_inc(v_a_370_);
lean_dec(v___x_369_);
v___x_372_ = lean_box(0);
v_isShared_373_ = v_isSharedCheck_418_;
goto v_resetjp_371_;
}
v_resetjp_371_:
{
if (lean_obj_tag(v_a_370_) == 0)
{
lean_object* v_pf_374_; lean_object* v_pf_375_; lean_object* v___x_377_; uint8_t v_isShared_378_; uint8_t v_isSharedCheck_395_; 
v_pf_374_ = lean_ctor_get(v_a_366_, 0);
lean_inc(v_pf_374_);
lean_dec_ref_known(v_a_366_, 1);
v_pf_375_ = lean_ctor_get(v_a_370_, 0);
v_isSharedCheck_395_ = !lean_is_exclusive(v_a_370_);
if (v_isSharedCheck_395_ == 0)
{
v___x_377_ = v_a_370_;
v_isShared_378_ = v_isSharedCheck_395_;
goto v_resetjp_376_;
}
else
{
lean_inc(v_pf_375_);
lean_dec(v_a_370_);
v___x_377_ = lean_box(0);
v_isShared_378_ = v_isSharedCheck_395_;
goto v_resetjp_376_;
}
v_resetjp_376_:
{
lean_object* v___x_379_; lean_object* v___x_380_; lean_object* v___x_381_; lean_object* v___x_382_; lean_object* v___x_383_; lean_object* v___x_384_; lean_object* v___x_385_; lean_object* v___x_386_; lean_object* v___x_387_; lean_object* v___x_388_; lean_object* v___x_390_; 
v___x_379_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_353_);
lean_dec(v_ref_344_);
v___x_380_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_381_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__18);
v___x_382_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__19));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_383_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_382_, v_currMacroScope_336_);
v___x_384_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__25));
lean_inc_n(v___x_379_, 2);
v___x_385_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_385_, 0, v___x_379_);
lean_ctor_set(v___x_385_, 1, v___x_381_);
lean_ctor_set(v___x_385_, 2, v___x_383_);
lean_ctor_set(v___x_385_, 3, v___x_384_);
v___x_386_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_387_ = l_Lean_Syntax_node2(v___x_379_, v___x_386_, v_pf_374_, v_pf_375_);
v___x_388_ = l_Lean_Syntax_node2(v___x_379_, v___x_380_, v___x_385_, v___x_387_);
if (v_isShared_378_ == 0)
{
lean_ctor_set(v___x_377_, 0, v___x_388_);
v___x_390_ = v___x_377_;
goto v_reusejp_389_;
}
else
{
lean_object* v_reuseFailAlloc_394_; 
v_reuseFailAlloc_394_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_394_, 0, v___x_388_);
v___x_390_ = v_reuseFailAlloc_394_;
goto v_reusejp_389_;
}
v_reusejp_389_:
{
lean_object* v___x_392_; 
if (v_isShared_373_ == 0)
{
lean_ctor_set(v___x_372_, 0, v___x_390_);
v___x_392_ = v___x_372_;
goto v_reusejp_391_;
}
else
{
lean_object* v_reuseFailAlloc_393_; 
v_reuseFailAlloc_393_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_393_, 0, v___x_390_);
v___x_392_ = v_reuseFailAlloc_393_;
goto v_reusejp_391_;
}
v_reusejp_391_:
{
return v___x_392_;
}
}
}
}
else
{
lean_object* v_pf_396_; lean_object* v_c_397_; lean_object* v___x_399_; uint8_t v_isShared_400_; uint8_t v_isSharedCheck_417_; 
v_pf_396_ = lean_ctor_get(v_a_366_, 0);
lean_inc(v_pf_396_);
lean_dec_ref_known(v_a_366_, 1);
v_c_397_ = lean_ctor_get(v_a_370_, 0);
v_isSharedCheck_417_ = !lean_is_exclusive(v_a_370_);
if (v_isSharedCheck_417_ == 0)
{
v___x_399_ = v_a_370_;
v_isShared_400_ = v_isSharedCheck_417_;
goto v_resetjp_398_;
}
else
{
lean_inc(v_c_397_);
lean_dec(v_a_370_);
v___x_399_ = lean_box(0);
v_isShared_400_ = v_isSharedCheck_417_;
goto v_resetjp_398_;
}
v_resetjp_398_:
{
lean_object* v___x_401_; lean_object* v___x_402_; lean_object* v___x_403_; lean_object* v___x_404_; lean_object* v___x_405_; lean_object* v___x_406_; lean_object* v___x_407_; lean_object* v___x_408_; lean_object* v___x_409_; lean_object* v___x_410_; lean_object* v___x_412_; 
v___x_401_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_353_);
lean_dec(v_ref_344_);
v___x_402_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_403_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__29);
v___x_404_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__30));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_405_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_404_, v_currMacroScope_336_);
v___x_406_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__33));
lean_inc_n(v___x_401_, 2);
v___x_407_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_407_, 0, v___x_401_);
lean_ctor_set(v___x_407_, 1, v___x_403_);
lean_ctor_set(v___x_407_, 2, v___x_405_);
lean_ctor_set(v___x_407_, 3, v___x_406_);
v___x_408_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_409_ = l_Lean_Syntax_node2(v___x_401_, v___x_408_, v_pf_396_, v_c_397_);
v___x_410_ = l_Lean_Syntax_node2(v___x_401_, v___x_402_, v___x_407_, v___x_409_);
if (v_isShared_400_ == 0)
{
lean_ctor_set_tag(v___x_399_, 0);
lean_ctor_set(v___x_399_, 0, v___x_410_);
v___x_412_ = v___x_399_;
goto v_reusejp_411_;
}
else
{
lean_object* v_reuseFailAlloc_416_; 
v_reuseFailAlloc_416_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_416_, 0, v___x_410_);
v___x_412_ = v_reuseFailAlloc_416_;
goto v_reusejp_411_;
}
v_reusejp_411_:
{
lean_object* v___x_414_; 
if (v_isShared_373_ == 0)
{
lean_ctor_set(v___x_372_, 0, v___x_412_);
v___x_414_ = v___x_372_;
goto v_reusejp_413_;
}
else
{
lean_object* v_reuseFailAlloc_415_; 
v_reuseFailAlloc_415_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_415_, 0, v___x_412_);
v___x_414_ = v_reuseFailAlloc_415_;
goto v_reusejp_413_;
}
v_reusejp_413_:
{
return v___x_414_;
}
}
}
}
}
}
else
{
lean_object* v_a_419_; lean_object* v___x_421_; uint8_t v_isShared_422_; uint8_t v_isSharedCheck_461_; 
v_a_419_ = lean_ctor_get(v___x_369_, 0);
v_isSharedCheck_461_ = !lean_is_exclusive(v___x_369_);
if (v_isSharedCheck_461_ == 0)
{
v___x_421_ = v___x_369_;
v_isShared_422_ = v_isSharedCheck_461_;
goto v_resetjp_420_;
}
else
{
lean_inc(v_a_419_);
lean_dec(v___x_369_);
v___x_421_ = lean_box(0);
v_isShared_422_ = v_isSharedCheck_461_;
goto v_resetjp_420_;
}
v_resetjp_420_:
{
if (lean_obj_tag(v_a_419_) == 0)
{
lean_object* v_c_423_; lean_object* v_pf_424_; lean_object* v___x_426_; uint8_t v_isShared_427_; uint8_t v_isSharedCheck_444_; 
v_c_423_ = lean_ctor_get(v_a_366_, 0);
lean_inc(v_c_423_);
lean_dec_ref_known(v_a_366_, 1);
v_pf_424_ = lean_ctor_get(v_a_419_, 0);
v_isSharedCheck_444_ = !lean_is_exclusive(v_a_419_);
if (v_isSharedCheck_444_ == 0)
{
v___x_426_ = v_a_419_;
v_isShared_427_ = v_isSharedCheck_444_;
goto v_resetjp_425_;
}
else
{
lean_inc(v_pf_424_);
lean_dec(v_a_419_);
v___x_426_ = lean_box(0);
v_isShared_427_ = v_isSharedCheck_444_;
goto v_resetjp_425_;
}
v_resetjp_425_:
{
lean_object* v___x_428_; lean_object* v___x_429_; lean_object* v___x_430_; lean_object* v___x_431_; lean_object* v___x_432_; lean_object* v___x_433_; lean_object* v___x_434_; lean_object* v___x_435_; lean_object* v___x_436_; lean_object* v___x_437_; lean_object* v___x_439_; 
v___x_428_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_353_);
lean_dec(v_ref_344_);
v___x_429_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_430_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__35);
v___x_431_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__36));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_432_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_431_, v_currMacroScope_336_);
v___x_433_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__39));
lean_inc_n(v___x_428_, 2);
v___x_434_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_434_, 0, v___x_428_);
lean_ctor_set(v___x_434_, 1, v___x_430_);
lean_ctor_set(v___x_434_, 2, v___x_432_);
lean_ctor_set(v___x_434_, 3, v___x_433_);
v___x_435_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_436_ = l_Lean_Syntax_node2(v___x_428_, v___x_435_, v_pf_424_, v_c_423_);
v___x_437_ = l_Lean_Syntax_node2(v___x_428_, v___x_429_, v___x_434_, v___x_436_);
if (v_isShared_427_ == 0)
{
lean_ctor_set(v___x_426_, 0, v___x_437_);
v___x_439_ = v___x_426_;
goto v_reusejp_438_;
}
else
{
lean_object* v_reuseFailAlloc_443_; 
v_reuseFailAlloc_443_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_443_, 0, v___x_437_);
v___x_439_ = v_reuseFailAlloc_443_;
goto v_reusejp_438_;
}
v_reusejp_438_:
{
lean_object* v___x_441_; 
if (v_isShared_422_ == 0)
{
lean_ctor_set(v___x_421_, 0, v___x_439_);
v___x_441_ = v___x_421_;
goto v_reusejp_440_;
}
else
{
lean_object* v_reuseFailAlloc_442_; 
v_reuseFailAlloc_442_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_442_, 0, v___x_439_);
v___x_441_ = v_reuseFailAlloc_442_;
goto v_reusejp_440_;
}
v_reusejp_440_:
{
return v___x_441_;
}
}
}
}
else
{
lean_object* v_c_445_; lean_object* v_c_446_; lean_object* v___x_448_; uint8_t v_isShared_449_; uint8_t v_isSharedCheck_460_; 
v_c_445_ = lean_ctor_get(v_a_366_, 0);
lean_inc(v_c_445_);
lean_dec_ref_known(v_a_366_, 1);
v_c_446_ = lean_ctor_get(v_a_419_, 0);
v_isSharedCheck_460_ = !lean_is_exclusive(v_a_419_);
if (v_isSharedCheck_460_ == 0)
{
v___x_448_ = v_a_419_;
v_isShared_449_ = v_isSharedCheck_460_;
goto v_resetjp_447_;
}
else
{
lean_inc(v_c_446_);
lean_dec(v_a_419_);
v___x_448_ = lean_box(0);
v_isShared_449_ = v_isSharedCheck_460_;
goto v_resetjp_447_;
}
v_resetjp_447_:
{
lean_object* v___x_450_; lean_object* v___x_451_; lean_object* v___x_452_; lean_object* v___x_453_; lean_object* v___x_455_; 
v___x_450_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_353_);
lean_dec(v_ref_344_);
v___x_451_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__40));
lean_inc(v___x_450_);
v___x_452_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_452_, 0, v___x_450_);
lean_ctor_set(v___x_452_, 1, v___x_451_);
v___x_453_ = l_Lean_Syntax_node3(v___x_450_, v___x_354_, v_c_445_, v___x_452_, v_c_446_);
if (v_isShared_449_ == 0)
{
lean_ctor_set(v___x_448_, 0, v___x_453_);
v___x_455_ = v___x_448_;
goto v_reusejp_454_;
}
else
{
lean_object* v_reuseFailAlloc_459_; 
v_reuseFailAlloc_459_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_459_, 0, v___x_453_);
v___x_455_ = v_reuseFailAlloc_459_;
goto v_reusejp_454_;
}
v_reusejp_454_:
{
lean_object* v___x_457_; 
if (v_isShared_422_ == 0)
{
lean_ctor_set(v___x_421_, 0, v___x_455_);
v___x_457_ = v___x_421_;
goto v_reusejp_456_;
}
else
{
lean_object* v_reuseFailAlloc_458_; 
v_reuseFailAlloc_458_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_458_, 0, v___x_455_);
v___x_457_ = v_reuseFailAlloc_458_;
goto v_reusejp_456_;
}
v_reusejp_456_:
{
return v___x_457_;
}
}
}
}
}
}
}
else
{
lean_dec(v_a_366_);
lean_dec(v_ref_344_);
return v___x_369_;
}
}
else
{
lean_dec_ref_known(v___x_345_, 14);
lean_dec(v_ref_344_);
lean_dec(v_stx_317_);
lean_dec_ref(v_ty_316_);
return v___x_365_;
}
}
}
else
{
lean_object* v___x_462_; lean_object* v___x_463_; lean_object* v___x_464_; uint8_t v___x_465_; 
v___x_462_ = lean_unsigned_to_nat(1u);
v___x_463_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_462_);
v___x_464_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__42));
lean_inc(v___x_463_);
v___x_465_ = l_Lean_Syntax_isOfKind(v___x_463_, v___x_464_);
if (v___x_465_ == 0)
{
lean_object* v___x_466_; lean_object* v___x_467_; lean_object* v___x_468_; lean_object* v___x_469_; lean_object* v___f_470_; uint8_t v___x_471_; lean_object* v___x_472_; 
lean_dec(v___x_463_);
lean_dec(v_ref_344_);
v___x_466_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_466_, 0, v_ty_316_);
v___x_467_ = lean_box(v___x_343_);
v___x_468_ = lean_box(v___x_343_);
v___x_469_ = lean_alloc_closure((void*)(l_Lean_Elab_Term_elabTerm___boxed), 11, 4);
lean_closure_set(v___x_469_, 0, v_stx_317_);
lean_closure_set(v___x_469_, 1, v___x_466_);
lean_closure_set(v___x_469_, 2, v___x_467_);
lean_closure_set(v___x_469_, 3, v___x_468_);
v___f_470_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed), 8, 1);
lean_closure_set(v___f_470_, 0, v___x_469_);
v___x_471_ = 1;
v___x_472_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(v___f_470_, v___x_471_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
return v___x_472_;
}
else
{
lean_object* v___x_473_; lean_object* v_e_474_; lean_object* v___x_475_; 
lean_dec(v_stx_317_);
v___x_473_ = lean_unsigned_to_nat(0u);
v_e_474_ = l_Lean_Syntax_getArg(v___x_463_, v___x_473_);
lean_dec(v___x_463_);
v___x_475_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_474_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
if (lean_obj_tag(v___x_475_) == 0)
{
lean_object* v_a_476_; 
v_a_476_ = lean_ctor_get(v___x_475_, 0);
lean_inc(v_a_476_);
if (lean_obj_tag(v_a_476_) == 0)
{
lean_object* v___x_478_; uint8_t v_isShared_479_; uint8_t v_isSharedCheck_501_; 
v_isSharedCheck_501_ = !lean_is_exclusive(v___x_475_);
if (v_isSharedCheck_501_ == 0)
{
lean_object* v_unused_502_; 
v_unused_502_ = lean_ctor_get(v___x_475_, 0);
lean_dec(v_unused_502_);
v___x_478_ = v___x_475_;
v_isShared_479_ = v_isSharedCheck_501_;
goto v_resetjp_477_;
}
else
{
lean_dec(v___x_475_);
v___x_478_ = lean_box(0);
v_isShared_479_ = v_isSharedCheck_501_;
goto v_resetjp_477_;
}
v_resetjp_477_:
{
lean_object* v_pf_480_; lean_object* v___x_482_; uint8_t v_isShared_483_; uint8_t v_isSharedCheck_500_; 
v_pf_480_ = lean_ctor_get(v_a_476_, 0);
v_isSharedCheck_500_ = !lean_is_exclusive(v_a_476_);
if (v_isSharedCheck_500_ == 0)
{
v___x_482_ = v_a_476_;
v_isShared_483_ = v_isSharedCheck_500_;
goto v_resetjp_481_;
}
else
{
lean_inc(v_pf_480_);
lean_dec(v_a_476_);
v___x_482_ = lean_box(0);
v_isShared_483_ = v_isSharedCheck_500_;
goto v_resetjp_481_;
}
v_resetjp_481_:
{
lean_object* v___x_484_; lean_object* v___x_485_; lean_object* v___x_486_; lean_object* v___x_487_; lean_object* v___x_488_; lean_object* v___x_489_; lean_object* v___x_490_; lean_object* v___x_491_; lean_object* v___x_492_; lean_object* v___x_493_; lean_object* v___x_495_; 
v___x_484_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_351_);
lean_dec(v_ref_344_);
v___x_485_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_486_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__44);
v___x_487_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__47));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_488_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_487_, v_currMacroScope_336_);
v___x_489_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__49));
lean_inc_n(v___x_484_, 2);
v___x_490_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_490_, 0, v___x_484_);
lean_ctor_set(v___x_490_, 1, v___x_486_);
lean_ctor_set(v___x_490_, 2, v___x_488_);
lean_ctor_set(v___x_490_, 3, v___x_489_);
v___x_491_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_492_ = l_Lean_Syntax_node1(v___x_484_, v___x_491_, v_pf_480_);
v___x_493_ = l_Lean_Syntax_node2(v___x_484_, v___x_485_, v___x_490_, v___x_492_);
if (v_isShared_483_ == 0)
{
lean_ctor_set(v___x_482_, 0, v___x_493_);
v___x_495_ = v___x_482_;
goto v_reusejp_494_;
}
else
{
lean_object* v_reuseFailAlloc_499_; 
v_reuseFailAlloc_499_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_499_, 0, v___x_493_);
v___x_495_ = v_reuseFailAlloc_499_;
goto v_reusejp_494_;
}
v_reusejp_494_:
{
lean_object* v___x_497_; 
if (v_isShared_479_ == 0)
{
lean_ctor_set(v___x_478_, 0, v___x_495_);
v___x_497_ = v___x_478_;
goto v_reusejp_496_;
}
else
{
lean_object* v_reuseFailAlloc_498_; 
v_reuseFailAlloc_498_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_498_, 0, v___x_495_);
v___x_497_ = v_reuseFailAlloc_498_;
goto v_reusejp_496_;
}
v_reusejp_496_:
{
return v___x_497_;
}
}
}
}
}
else
{
lean_dec_ref_known(v_a_476_, 1);
lean_dec(v_ref_344_);
return v___x_475_;
}
}
else
{
lean_dec(v_ref_344_);
return v___x_475_;
}
}
}
}
else
{
lean_object* v___x_503_; lean_object* v_e_504_; lean_object* v___x_505_; 
v___x_503_ = lean_unsigned_to_nat(1u);
v_e_504_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_503_);
lean_dec(v_stx_317_);
v___x_505_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_504_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
if (lean_obj_tag(v___x_505_) == 0)
{
lean_object* v_a_506_; lean_object* v___x_508_; uint8_t v_isShared_509_; uint8_t v_isSharedCheck_546_; 
v_a_506_ = lean_ctor_get(v___x_505_, 0);
v_isSharedCheck_546_ = !lean_is_exclusive(v___x_505_);
if (v_isSharedCheck_546_ == 0)
{
v___x_508_ = v___x_505_;
v_isShared_509_ = v_isSharedCheck_546_;
goto v_resetjp_507_;
}
else
{
lean_inc(v_a_506_);
lean_dec(v___x_505_);
v___x_508_ = lean_box(0);
v_isShared_509_ = v_isSharedCheck_546_;
goto v_resetjp_507_;
}
v_resetjp_507_:
{
if (lean_obj_tag(v_a_506_) == 0)
{
lean_object* v_pf_510_; lean_object* v___x_512_; uint8_t v_isShared_513_; uint8_t v_isSharedCheck_530_; 
v_pf_510_ = lean_ctor_get(v_a_506_, 0);
v_isSharedCheck_530_ = !lean_is_exclusive(v_a_506_);
if (v_isSharedCheck_530_ == 0)
{
v___x_512_ = v_a_506_;
v_isShared_513_ = v_isSharedCheck_530_;
goto v_resetjp_511_;
}
else
{
lean_inc(v_pf_510_);
lean_dec(v_a_506_);
v___x_512_ = lean_box(0);
v_isShared_513_ = v_isSharedCheck_530_;
goto v_resetjp_511_;
}
v_resetjp_511_:
{
lean_object* v___x_514_; lean_object* v___x_515_; lean_object* v___x_516_; lean_object* v___x_517_; lean_object* v___x_518_; lean_object* v___x_519_; lean_object* v___x_520_; lean_object* v___x_521_; lean_object* v___x_522_; lean_object* v___x_523_; lean_object* v___x_525_; 
v___x_514_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_349_);
lean_dec(v_ref_344_);
v___x_515_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_516_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__51);
v___x_517_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__52));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_518_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_517_, v_currMacroScope_336_);
v___x_519_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__55));
lean_inc_n(v___x_514_, 2);
v___x_520_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_520_, 0, v___x_514_);
lean_ctor_set(v___x_520_, 1, v___x_516_);
lean_ctor_set(v___x_520_, 2, v___x_518_);
lean_ctor_set(v___x_520_, 3, v___x_519_);
v___x_521_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_522_ = l_Lean_Syntax_node1(v___x_514_, v___x_521_, v_pf_510_);
v___x_523_ = l_Lean_Syntax_node2(v___x_514_, v___x_515_, v___x_520_, v___x_522_);
if (v_isShared_513_ == 0)
{
lean_ctor_set(v___x_512_, 0, v___x_523_);
v___x_525_ = v___x_512_;
goto v_reusejp_524_;
}
else
{
lean_object* v_reuseFailAlloc_529_; 
v_reuseFailAlloc_529_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_529_, 0, v___x_523_);
v___x_525_ = v_reuseFailAlloc_529_;
goto v_reusejp_524_;
}
v_reusejp_524_:
{
lean_object* v___x_527_; 
if (v_isShared_509_ == 0)
{
lean_ctor_set(v___x_508_, 0, v___x_525_);
v___x_527_ = v___x_508_;
goto v_reusejp_526_;
}
else
{
lean_object* v_reuseFailAlloc_528_; 
v_reuseFailAlloc_528_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_528_, 0, v___x_525_);
v___x_527_ = v_reuseFailAlloc_528_;
goto v_reusejp_526_;
}
v_reusejp_526_:
{
return v___x_527_;
}
}
}
}
else
{
lean_object* v_c_531_; lean_object* v___x_533_; uint8_t v_isShared_534_; uint8_t v_isSharedCheck_545_; 
v_c_531_ = lean_ctor_get(v_a_506_, 0);
v_isSharedCheck_545_ = !lean_is_exclusive(v_a_506_);
if (v_isSharedCheck_545_ == 0)
{
v___x_533_ = v_a_506_;
v_isShared_534_ = v_isSharedCheck_545_;
goto v_resetjp_532_;
}
else
{
lean_inc(v_c_531_);
lean_dec(v_a_506_);
v___x_533_ = lean_box(0);
v_isShared_534_ = v_isSharedCheck_545_;
goto v_resetjp_532_;
}
v_resetjp_532_:
{
lean_object* v___x_535_; lean_object* v___x_536_; lean_object* v___x_537_; lean_object* v___x_538_; lean_object* v___x_540_; 
v___x_535_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_349_);
lean_dec(v_ref_344_);
v___x_536_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__56));
lean_inc(v___x_535_);
v___x_537_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_537_, 0, v___x_535_);
lean_ctor_set(v___x_537_, 1, v___x_536_);
v___x_538_ = l_Lean_Syntax_node2(v___x_535_, v___x_350_, v___x_537_, v_c_531_);
if (v_isShared_534_ == 0)
{
lean_ctor_set(v___x_533_, 0, v___x_538_);
v___x_540_ = v___x_533_;
goto v_reusejp_539_;
}
else
{
lean_object* v_reuseFailAlloc_544_; 
v_reuseFailAlloc_544_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_544_, 0, v___x_538_);
v___x_540_ = v_reuseFailAlloc_544_;
goto v_reusejp_539_;
}
v_reusejp_539_:
{
lean_object* v___x_542_; 
if (v_isShared_509_ == 0)
{
lean_ctor_set(v___x_508_, 0, v___x_540_);
v___x_542_ = v___x_508_;
goto v_reusejp_541_;
}
else
{
lean_object* v_reuseFailAlloc_543_; 
v_reuseFailAlloc_543_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_543_, 0, v___x_540_);
v___x_542_ = v_reuseFailAlloc_543_;
goto v_reusejp_541_;
}
v_reusejp_541_:
{
return v___x_542_;
}
}
}
}
}
}
else
{
lean_dec(v_ref_344_);
return v___x_505_;
}
}
}
else
{
lean_object* v___x_547_; lean_object* v_e_u2081_548_; lean_object* v___x_549_; 
v___x_547_ = lean_unsigned_to_nat(0u);
v_e_u2081_548_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_547_);
lean_inc_ref(v_ty_316_);
v___x_549_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2081_548_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
if (lean_obj_tag(v___x_549_) == 0)
{
lean_object* v_a_550_; lean_object* v___x_551_; lean_object* v_e_u2082_552_; lean_object* v___x_553_; 
v_a_550_ = lean_ctor_get(v___x_549_, 0);
lean_inc(v_a_550_);
lean_dec_ref_known(v___x_549_, 1);
v___x_551_ = lean_unsigned_to_nat(2u);
v_e_u2082_552_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_551_);
lean_dec(v_stx_317_);
v___x_553_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2082_552_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
if (lean_obj_tag(v___x_553_) == 0)
{
if (lean_obj_tag(v_a_550_) == 0)
{
lean_object* v_a_554_; lean_object* v___x_556_; uint8_t v_isShared_557_; uint8_t v_isSharedCheck_602_; 
v_a_554_ = lean_ctor_get(v___x_553_, 0);
v_isSharedCheck_602_ = !lean_is_exclusive(v___x_553_);
if (v_isSharedCheck_602_ == 0)
{
v___x_556_ = v___x_553_;
v_isShared_557_ = v_isSharedCheck_602_;
goto v_resetjp_555_;
}
else
{
lean_inc(v_a_554_);
lean_dec(v___x_553_);
v___x_556_ = lean_box(0);
v_isShared_557_ = v_isSharedCheck_602_;
goto v_resetjp_555_;
}
v_resetjp_555_:
{
if (lean_obj_tag(v_a_554_) == 0)
{
lean_object* v_pf_558_; lean_object* v_pf_559_; lean_object* v___x_561_; uint8_t v_isShared_562_; uint8_t v_isSharedCheck_579_; 
v_pf_558_ = lean_ctor_get(v_a_550_, 0);
lean_inc(v_pf_558_);
lean_dec_ref_known(v_a_550_, 1);
v_pf_559_ = lean_ctor_get(v_a_554_, 0);
v_isSharedCheck_579_ = !lean_is_exclusive(v_a_554_);
if (v_isSharedCheck_579_ == 0)
{
v___x_561_ = v_a_554_;
v_isShared_562_ = v_isSharedCheck_579_;
goto v_resetjp_560_;
}
else
{
lean_inc(v_pf_559_);
lean_dec(v_a_554_);
v___x_561_ = lean_box(0);
v_isShared_562_ = v_isSharedCheck_579_;
goto v_resetjp_560_;
}
v_resetjp_560_:
{
lean_object* v___x_563_; lean_object* v___x_564_; lean_object* v___x_565_; lean_object* v___x_566_; lean_object* v___x_567_; lean_object* v___x_568_; lean_object* v___x_569_; lean_object* v___x_570_; lean_object* v___x_571_; lean_object* v___x_572_; lean_object* v___x_574_; 
v___x_563_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_347_);
lean_dec(v_ref_344_);
v___x_564_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_565_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__58);
v___x_566_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__59));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_567_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_566_, v_currMacroScope_336_);
v___x_568_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__62));
lean_inc_n(v___x_563_, 2);
v___x_569_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_569_, 0, v___x_563_);
lean_ctor_set(v___x_569_, 1, v___x_565_);
lean_ctor_set(v___x_569_, 2, v___x_567_);
lean_ctor_set(v___x_569_, 3, v___x_568_);
v___x_570_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_571_ = l_Lean_Syntax_node2(v___x_563_, v___x_570_, v_pf_558_, v_pf_559_);
v___x_572_ = l_Lean_Syntax_node2(v___x_563_, v___x_564_, v___x_569_, v___x_571_);
if (v_isShared_562_ == 0)
{
lean_ctor_set(v___x_561_, 0, v___x_572_);
v___x_574_ = v___x_561_;
goto v_reusejp_573_;
}
else
{
lean_object* v_reuseFailAlloc_578_; 
v_reuseFailAlloc_578_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_578_, 0, v___x_572_);
v___x_574_ = v_reuseFailAlloc_578_;
goto v_reusejp_573_;
}
v_reusejp_573_:
{
lean_object* v___x_576_; 
if (v_isShared_557_ == 0)
{
lean_ctor_set(v___x_556_, 0, v___x_574_);
v___x_576_ = v___x_556_;
goto v_reusejp_575_;
}
else
{
lean_object* v_reuseFailAlloc_577_; 
v_reuseFailAlloc_577_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_577_, 0, v___x_574_);
v___x_576_ = v_reuseFailAlloc_577_;
goto v_reusejp_575_;
}
v_reusejp_575_:
{
return v___x_576_;
}
}
}
}
else
{
lean_object* v_pf_580_; lean_object* v_c_581_; lean_object* v___x_583_; uint8_t v_isShared_584_; uint8_t v_isSharedCheck_601_; 
v_pf_580_ = lean_ctor_get(v_a_550_, 0);
lean_inc(v_pf_580_);
lean_dec_ref_known(v_a_550_, 1);
v_c_581_ = lean_ctor_get(v_a_554_, 0);
v_isSharedCheck_601_ = !lean_is_exclusive(v_a_554_);
if (v_isSharedCheck_601_ == 0)
{
v___x_583_ = v_a_554_;
v_isShared_584_ = v_isSharedCheck_601_;
goto v_resetjp_582_;
}
else
{
lean_inc(v_c_581_);
lean_dec(v_a_554_);
v___x_583_ = lean_box(0);
v_isShared_584_ = v_isSharedCheck_601_;
goto v_resetjp_582_;
}
v_resetjp_582_:
{
lean_object* v___x_585_; lean_object* v___x_586_; lean_object* v___x_587_; lean_object* v___x_588_; lean_object* v___x_589_; lean_object* v___x_590_; lean_object* v___x_591_; lean_object* v___x_592_; lean_object* v___x_593_; lean_object* v___x_594_; lean_object* v___x_596_; 
v___x_585_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_347_);
lean_dec(v_ref_344_);
v___x_586_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_587_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__64);
v___x_588_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__65));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_589_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_588_, v_currMacroScope_336_);
v___x_590_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__68));
lean_inc_n(v___x_585_, 2);
v___x_591_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_591_, 0, v___x_585_);
lean_ctor_set(v___x_591_, 1, v___x_587_);
lean_ctor_set(v___x_591_, 2, v___x_589_);
lean_ctor_set(v___x_591_, 3, v___x_590_);
v___x_592_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_593_ = l_Lean_Syntax_node2(v___x_585_, v___x_592_, v_pf_580_, v_c_581_);
v___x_594_ = l_Lean_Syntax_node2(v___x_585_, v___x_586_, v___x_591_, v___x_593_);
if (v_isShared_584_ == 0)
{
lean_ctor_set_tag(v___x_583_, 0);
lean_ctor_set(v___x_583_, 0, v___x_594_);
v___x_596_ = v___x_583_;
goto v_reusejp_595_;
}
else
{
lean_object* v_reuseFailAlloc_600_; 
v_reuseFailAlloc_600_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_600_, 0, v___x_594_);
v___x_596_ = v_reuseFailAlloc_600_;
goto v_reusejp_595_;
}
v_reusejp_595_:
{
lean_object* v___x_598_; 
if (v_isShared_557_ == 0)
{
lean_ctor_set(v___x_556_, 0, v___x_596_);
v___x_598_ = v___x_556_;
goto v_reusejp_597_;
}
else
{
lean_object* v_reuseFailAlloc_599_; 
v_reuseFailAlloc_599_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_599_, 0, v___x_596_);
v___x_598_ = v_reuseFailAlloc_599_;
goto v_reusejp_597_;
}
v_reusejp_597_:
{
return v___x_598_;
}
}
}
}
}
}
else
{
lean_object* v_a_603_; lean_object* v___x_605_; uint8_t v_isShared_606_; uint8_t v_isSharedCheck_645_; 
v_a_603_ = lean_ctor_get(v___x_553_, 0);
v_isSharedCheck_645_ = !lean_is_exclusive(v___x_553_);
if (v_isSharedCheck_645_ == 0)
{
v___x_605_ = v___x_553_;
v_isShared_606_ = v_isSharedCheck_645_;
goto v_resetjp_604_;
}
else
{
lean_inc(v_a_603_);
lean_dec(v___x_553_);
v___x_605_ = lean_box(0);
v_isShared_606_ = v_isSharedCheck_645_;
goto v_resetjp_604_;
}
v_resetjp_604_:
{
if (lean_obj_tag(v_a_603_) == 0)
{
lean_object* v_c_607_; lean_object* v_pf_608_; lean_object* v___x_610_; uint8_t v_isShared_611_; uint8_t v_isSharedCheck_628_; 
v_c_607_ = lean_ctor_get(v_a_550_, 0);
lean_inc(v_c_607_);
lean_dec_ref_known(v_a_550_, 1);
v_pf_608_ = lean_ctor_get(v_a_603_, 0);
v_isSharedCheck_628_ = !lean_is_exclusive(v_a_603_);
if (v_isSharedCheck_628_ == 0)
{
v___x_610_ = v_a_603_;
v_isShared_611_ = v_isSharedCheck_628_;
goto v_resetjp_609_;
}
else
{
lean_inc(v_pf_608_);
lean_dec(v_a_603_);
v___x_610_ = lean_box(0);
v_isShared_611_ = v_isSharedCheck_628_;
goto v_resetjp_609_;
}
v_resetjp_609_:
{
lean_object* v___x_612_; lean_object* v___x_613_; lean_object* v___x_614_; lean_object* v___x_615_; lean_object* v___x_616_; lean_object* v___x_617_; lean_object* v___x_618_; lean_object* v___x_619_; lean_object* v___x_620_; lean_object* v___x_621_; lean_object* v___x_623_; 
v___x_612_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_347_);
lean_dec(v_ref_344_);
v___x_613_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_614_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__70);
v___x_615_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__71));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_616_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_615_, v_currMacroScope_336_);
v___x_617_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__74));
lean_inc_n(v___x_612_, 2);
v___x_618_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_618_, 0, v___x_612_);
lean_ctor_set(v___x_618_, 1, v___x_614_);
lean_ctor_set(v___x_618_, 2, v___x_616_);
lean_ctor_set(v___x_618_, 3, v___x_617_);
v___x_619_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_620_ = l_Lean_Syntax_node2(v___x_612_, v___x_619_, v_pf_608_, v_c_607_);
v___x_621_ = l_Lean_Syntax_node2(v___x_612_, v___x_613_, v___x_618_, v___x_620_);
if (v_isShared_611_ == 0)
{
lean_ctor_set(v___x_610_, 0, v___x_621_);
v___x_623_ = v___x_610_;
goto v_reusejp_622_;
}
else
{
lean_object* v_reuseFailAlloc_627_; 
v_reuseFailAlloc_627_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_627_, 0, v___x_621_);
v___x_623_ = v_reuseFailAlloc_627_;
goto v_reusejp_622_;
}
v_reusejp_622_:
{
lean_object* v___x_625_; 
if (v_isShared_606_ == 0)
{
lean_ctor_set(v___x_605_, 0, v___x_623_);
v___x_625_ = v___x_605_;
goto v_reusejp_624_;
}
else
{
lean_object* v_reuseFailAlloc_626_; 
v_reuseFailAlloc_626_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_626_, 0, v___x_623_);
v___x_625_ = v_reuseFailAlloc_626_;
goto v_reusejp_624_;
}
v_reusejp_624_:
{
return v___x_625_;
}
}
}
}
else
{
lean_object* v_c_629_; lean_object* v_c_630_; lean_object* v___x_632_; uint8_t v_isShared_633_; uint8_t v_isSharedCheck_644_; 
v_c_629_ = lean_ctor_get(v_a_550_, 0);
lean_inc(v_c_629_);
lean_dec_ref_known(v_a_550_, 1);
v_c_630_ = lean_ctor_get(v_a_603_, 0);
v_isSharedCheck_644_ = !lean_is_exclusive(v_a_603_);
if (v_isSharedCheck_644_ == 0)
{
v___x_632_ = v_a_603_;
v_isShared_633_ = v_isSharedCheck_644_;
goto v_resetjp_631_;
}
else
{
lean_inc(v_c_630_);
lean_dec(v_a_603_);
v___x_632_ = lean_box(0);
v_isShared_633_ = v_isSharedCheck_644_;
goto v_resetjp_631_;
}
v_resetjp_631_:
{
lean_object* v___x_634_; lean_object* v___x_635_; lean_object* v___x_636_; lean_object* v___x_637_; lean_object* v___x_639_; 
v___x_634_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_347_);
lean_dec(v_ref_344_);
v___x_635_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__56));
lean_inc(v___x_634_);
v___x_636_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_636_, 0, v___x_634_);
lean_ctor_set(v___x_636_, 1, v___x_635_);
v___x_637_ = l_Lean_Syntax_node3(v___x_634_, v___x_348_, v_c_629_, v___x_636_, v_c_630_);
if (v_isShared_633_ == 0)
{
lean_ctor_set(v___x_632_, 0, v___x_637_);
v___x_639_ = v___x_632_;
goto v_reusejp_638_;
}
else
{
lean_object* v_reuseFailAlloc_643_; 
v_reuseFailAlloc_643_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_643_, 0, v___x_637_);
v___x_639_ = v_reuseFailAlloc_643_;
goto v_reusejp_638_;
}
v_reusejp_638_:
{
lean_object* v___x_641_; 
if (v_isShared_606_ == 0)
{
lean_ctor_set(v___x_605_, 0, v___x_639_);
v___x_641_ = v___x_605_;
goto v_reusejp_640_;
}
else
{
lean_object* v_reuseFailAlloc_642_; 
v_reuseFailAlloc_642_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_642_, 0, v___x_639_);
v___x_641_ = v_reuseFailAlloc_642_;
goto v_reusejp_640_;
}
v_reusejp_640_:
{
return v___x_641_;
}
}
}
}
}
}
}
else
{
lean_dec(v_a_550_);
lean_dec(v_ref_344_);
return v___x_553_;
}
}
else
{
lean_dec_ref_known(v___x_345_, 14);
lean_dec(v_ref_344_);
lean_dec(v_stx_317_);
lean_dec_ref(v_ty_316_);
return v___x_549_;
}
}
}
else
{
lean_object* v___x_646_; lean_object* v_e_u2081_647_; lean_object* v___x_648_; 
v___x_646_ = lean_unsigned_to_nat(0u);
v_e_u2081_647_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_646_);
lean_inc_ref(v_ty_316_);
v___x_648_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2081_647_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
if (lean_obj_tag(v___x_648_) == 0)
{
lean_object* v_a_649_; lean_object* v___x_650_; lean_object* v_e_u2082_651_; lean_object* v___x_652_; 
v_a_649_ = lean_ctor_get(v___x_648_, 0);
lean_inc(v_a_649_);
lean_dec_ref_known(v___x_648_, 1);
v___x_650_ = lean_unsigned_to_nat(2u);
v_e_u2082_651_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_650_);
lean_dec(v_stx_317_);
v___x_652_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_316_, v_e_u2082_651_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
if (lean_obj_tag(v___x_652_) == 0)
{
if (lean_obj_tag(v_a_649_) == 0)
{
lean_object* v_a_653_; lean_object* v___x_655_; uint8_t v_isShared_656_; uint8_t v_isSharedCheck_701_; 
v_a_653_ = lean_ctor_get(v___x_652_, 0);
v_isSharedCheck_701_ = !lean_is_exclusive(v___x_652_);
if (v_isSharedCheck_701_ == 0)
{
v___x_655_ = v___x_652_;
v_isShared_656_ = v_isSharedCheck_701_;
goto v_resetjp_654_;
}
else
{
lean_inc(v_a_653_);
lean_dec(v___x_652_);
v___x_655_ = lean_box(0);
v_isShared_656_ = v_isSharedCheck_701_;
goto v_resetjp_654_;
}
v_resetjp_654_:
{
if (lean_obj_tag(v_a_653_) == 0)
{
lean_object* v_pf_657_; lean_object* v_pf_658_; lean_object* v___x_660_; uint8_t v_isShared_661_; uint8_t v_isSharedCheck_678_; 
v_pf_657_ = lean_ctor_get(v_a_649_, 0);
lean_inc(v_pf_657_);
lean_dec_ref_known(v_a_649_, 1);
v_pf_658_ = lean_ctor_get(v_a_653_, 0);
v_isSharedCheck_678_ = !lean_is_exclusive(v_a_653_);
if (v_isSharedCheck_678_ == 0)
{
v___x_660_ = v_a_653_;
v_isShared_661_ = v_isSharedCheck_678_;
goto v_resetjp_659_;
}
else
{
lean_inc(v_pf_658_);
lean_dec(v_a_653_);
v___x_660_ = lean_box(0);
v_isShared_661_ = v_isSharedCheck_678_;
goto v_resetjp_659_;
}
v_resetjp_659_:
{
lean_object* v___x_662_; lean_object* v___x_663_; lean_object* v___x_664_; lean_object* v___x_665_; lean_object* v___x_666_; lean_object* v___x_667_; lean_object* v___x_668_; lean_object* v___x_669_; lean_object* v___x_670_; lean_object* v___x_671_; lean_object* v___x_673_; 
v___x_662_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_342_);
lean_dec(v_ref_344_);
v___x_663_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_664_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__76);
v___x_665_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__77));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_666_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_665_, v_currMacroScope_336_);
v___x_667_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__80));
lean_inc_n(v___x_662_, 2);
v___x_668_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_668_, 0, v___x_662_);
lean_ctor_set(v___x_668_, 1, v___x_664_);
lean_ctor_set(v___x_668_, 2, v___x_666_);
lean_ctor_set(v___x_668_, 3, v___x_667_);
v___x_669_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_670_ = l_Lean_Syntax_node2(v___x_662_, v___x_669_, v_pf_657_, v_pf_658_);
v___x_671_ = l_Lean_Syntax_node2(v___x_662_, v___x_663_, v___x_668_, v___x_670_);
if (v_isShared_661_ == 0)
{
lean_ctor_set(v___x_660_, 0, v___x_671_);
v___x_673_ = v___x_660_;
goto v_reusejp_672_;
}
else
{
lean_object* v_reuseFailAlloc_677_; 
v_reuseFailAlloc_677_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_677_, 0, v___x_671_);
v___x_673_ = v_reuseFailAlloc_677_;
goto v_reusejp_672_;
}
v_reusejp_672_:
{
lean_object* v___x_675_; 
if (v_isShared_656_ == 0)
{
lean_ctor_set(v___x_655_, 0, v___x_673_);
v___x_675_ = v___x_655_;
goto v_reusejp_674_;
}
else
{
lean_object* v_reuseFailAlloc_676_; 
v_reuseFailAlloc_676_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_676_, 0, v___x_673_);
v___x_675_ = v_reuseFailAlloc_676_;
goto v_reusejp_674_;
}
v_reusejp_674_:
{
return v___x_675_;
}
}
}
}
else
{
lean_object* v_pf_679_; lean_object* v_c_680_; lean_object* v___x_682_; uint8_t v_isShared_683_; uint8_t v_isSharedCheck_700_; 
v_pf_679_ = lean_ctor_get(v_a_649_, 0);
lean_inc(v_pf_679_);
lean_dec_ref_known(v_a_649_, 1);
v_c_680_ = lean_ctor_get(v_a_653_, 0);
v_isSharedCheck_700_ = !lean_is_exclusive(v_a_653_);
if (v_isSharedCheck_700_ == 0)
{
v___x_682_ = v_a_653_;
v_isShared_683_ = v_isSharedCheck_700_;
goto v_resetjp_681_;
}
else
{
lean_inc(v_c_680_);
lean_dec(v_a_653_);
v___x_682_ = lean_box(0);
v_isShared_683_ = v_isSharedCheck_700_;
goto v_resetjp_681_;
}
v_resetjp_681_:
{
lean_object* v___x_684_; lean_object* v___x_685_; lean_object* v___x_686_; lean_object* v___x_687_; lean_object* v___x_688_; lean_object* v___x_689_; lean_object* v___x_690_; lean_object* v___x_691_; lean_object* v___x_692_; lean_object* v___x_693_; lean_object* v___x_695_; 
v___x_684_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_342_);
lean_dec(v_ref_344_);
v___x_685_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_686_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__82);
v___x_687_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__83));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_688_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_687_, v_currMacroScope_336_);
v___x_689_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__86));
lean_inc_n(v___x_684_, 2);
v___x_690_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_690_, 0, v___x_684_);
lean_ctor_set(v___x_690_, 1, v___x_686_);
lean_ctor_set(v___x_690_, 2, v___x_688_);
lean_ctor_set(v___x_690_, 3, v___x_689_);
v___x_691_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_692_ = l_Lean_Syntax_node2(v___x_684_, v___x_691_, v_pf_679_, v_c_680_);
v___x_693_ = l_Lean_Syntax_node2(v___x_684_, v___x_685_, v___x_690_, v___x_692_);
if (v_isShared_683_ == 0)
{
lean_ctor_set_tag(v___x_682_, 0);
lean_ctor_set(v___x_682_, 0, v___x_693_);
v___x_695_ = v___x_682_;
goto v_reusejp_694_;
}
else
{
lean_object* v_reuseFailAlloc_699_; 
v_reuseFailAlloc_699_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_699_, 0, v___x_693_);
v___x_695_ = v_reuseFailAlloc_699_;
goto v_reusejp_694_;
}
v_reusejp_694_:
{
lean_object* v___x_697_; 
if (v_isShared_656_ == 0)
{
lean_ctor_set(v___x_655_, 0, v___x_695_);
v___x_697_ = v___x_655_;
goto v_reusejp_696_;
}
else
{
lean_object* v_reuseFailAlloc_698_; 
v_reuseFailAlloc_698_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_698_, 0, v___x_695_);
v___x_697_ = v_reuseFailAlloc_698_;
goto v_reusejp_696_;
}
v_reusejp_696_:
{
return v___x_697_;
}
}
}
}
}
}
else
{
lean_object* v_a_702_; lean_object* v___x_704_; uint8_t v_isShared_705_; uint8_t v_isSharedCheck_744_; 
v_a_702_ = lean_ctor_get(v___x_652_, 0);
v_isSharedCheck_744_ = !lean_is_exclusive(v___x_652_);
if (v_isSharedCheck_744_ == 0)
{
v___x_704_ = v___x_652_;
v_isShared_705_ = v_isSharedCheck_744_;
goto v_resetjp_703_;
}
else
{
lean_inc(v_a_702_);
lean_dec(v___x_652_);
v___x_704_ = lean_box(0);
v_isShared_705_ = v_isSharedCheck_744_;
goto v_resetjp_703_;
}
v_resetjp_703_:
{
if (lean_obj_tag(v_a_702_) == 0)
{
lean_object* v_c_706_; lean_object* v_pf_707_; lean_object* v___x_709_; uint8_t v_isShared_710_; uint8_t v_isSharedCheck_727_; 
v_c_706_ = lean_ctor_get(v_a_649_, 0);
lean_inc(v_c_706_);
lean_dec_ref_known(v_a_649_, 1);
v_pf_707_ = lean_ctor_get(v_a_702_, 0);
v_isSharedCheck_727_ = !lean_is_exclusive(v_a_702_);
if (v_isSharedCheck_727_ == 0)
{
v___x_709_ = v_a_702_;
v_isShared_710_ = v_isSharedCheck_727_;
goto v_resetjp_708_;
}
else
{
lean_inc(v_pf_707_);
lean_dec(v_a_702_);
v___x_709_ = lean_box(0);
v_isShared_710_ = v_isSharedCheck_727_;
goto v_resetjp_708_;
}
v_resetjp_708_:
{
lean_object* v___x_711_; lean_object* v___x_712_; lean_object* v___x_713_; lean_object* v___x_714_; lean_object* v___x_715_; lean_object* v___x_716_; lean_object* v___x_717_; lean_object* v___x_718_; lean_object* v___x_719_; lean_object* v___x_720_; lean_object* v___x_722_; 
v___x_711_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_342_);
lean_dec(v_ref_344_);
v___x_712_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_713_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__88);
v___x_714_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__89));
lean_inc(v_currMacroScope_336_);
lean_inc(v_quotContext_335_);
v___x_715_ = l_Lean_addMacroScope(v_quotContext_335_, v___x_714_, v_currMacroScope_336_);
v___x_716_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__92));
lean_inc_n(v___x_711_, 2);
v___x_717_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_717_, 0, v___x_711_);
lean_ctor_set(v___x_717_, 1, v___x_713_);
lean_ctor_set(v___x_717_, 2, v___x_715_);
lean_ctor_set(v___x_717_, 3, v___x_716_);
v___x_718_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_719_ = l_Lean_Syntax_node2(v___x_711_, v___x_718_, v_pf_707_, v_c_706_);
v___x_720_ = l_Lean_Syntax_node2(v___x_711_, v___x_712_, v___x_717_, v___x_719_);
if (v_isShared_710_ == 0)
{
lean_ctor_set(v___x_709_, 0, v___x_720_);
v___x_722_ = v___x_709_;
goto v_reusejp_721_;
}
else
{
lean_object* v_reuseFailAlloc_726_; 
v_reuseFailAlloc_726_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_726_, 0, v___x_720_);
v___x_722_ = v_reuseFailAlloc_726_;
goto v_reusejp_721_;
}
v_reusejp_721_:
{
lean_object* v___x_724_; 
if (v_isShared_705_ == 0)
{
lean_ctor_set(v___x_704_, 0, v___x_722_);
v___x_724_ = v___x_704_;
goto v_reusejp_723_;
}
else
{
lean_object* v_reuseFailAlloc_725_; 
v_reuseFailAlloc_725_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_725_, 0, v___x_722_);
v___x_724_ = v_reuseFailAlloc_725_;
goto v_reusejp_723_;
}
v_reusejp_723_:
{
return v___x_724_;
}
}
}
}
else
{
lean_object* v_c_728_; lean_object* v_c_729_; lean_object* v___x_731_; uint8_t v_isShared_732_; uint8_t v_isSharedCheck_743_; 
v_c_728_ = lean_ctor_get(v_a_649_, 0);
lean_inc(v_c_728_);
lean_dec_ref_known(v_a_649_, 1);
v_c_729_ = lean_ctor_get(v_a_702_, 0);
v_isSharedCheck_743_ = !lean_is_exclusive(v_a_702_);
if (v_isSharedCheck_743_ == 0)
{
v___x_731_ = v_a_702_;
v_isShared_732_ = v_isSharedCheck_743_;
goto v_resetjp_730_;
}
else
{
lean_inc(v_c_729_);
lean_dec(v_a_702_);
v___x_731_ = lean_box(0);
v_isShared_732_ = v_isSharedCheck_743_;
goto v_resetjp_730_;
}
v_resetjp_730_:
{
lean_object* v___x_733_; lean_object* v___x_734_; lean_object* v___x_735_; lean_object* v___x_736_; lean_object* v___x_738_; 
v___x_733_ = l_Lean_SourceInfo_fromRef(v_ref_344_, v___x_342_);
lean_dec(v_ref_344_);
v___x_734_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__93));
lean_inc(v___x_733_);
v___x_735_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_735_, 0, v___x_733_);
lean_ctor_set(v___x_735_, 1, v___x_734_);
v___x_736_ = l_Lean_Syntax_node3(v___x_733_, v___x_346_, v_c_728_, v___x_735_, v_c_729_);
if (v_isShared_732_ == 0)
{
lean_ctor_set(v___x_731_, 0, v___x_736_);
v___x_738_ = v___x_731_;
goto v_reusejp_737_;
}
else
{
lean_object* v_reuseFailAlloc_742_; 
v_reuseFailAlloc_742_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_742_, 0, v___x_736_);
v___x_738_ = v_reuseFailAlloc_742_;
goto v_reusejp_737_;
}
v_reusejp_737_:
{
lean_object* v___x_740_; 
if (v_isShared_705_ == 0)
{
lean_ctor_set(v___x_704_, 0, v___x_738_);
v___x_740_ = v___x_704_;
goto v_reusejp_739_;
}
else
{
lean_object* v_reuseFailAlloc_741_; 
v_reuseFailAlloc_741_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_741_, 0, v___x_738_);
v___x_740_ = v_reuseFailAlloc_741_;
goto v_reusejp_739_;
}
v_reusejp_739_:
{
return v___x_740_;
}
}
}
}
}
}
}
else
{
lean_dec(v_a_649_);
lean_dec(v_ref_344_);
return v___x_652_;
}
}
else
{
lean_dec_ref_known(v___x_345_, 14);
lean_dec(v_ref_344_);
lean_dec(v_stx_317_);
lean_dec_ref(v_ty_316_);
return v___x_648_;
}
}
}
else
{
lean_object* v___x_745_; lean_object* v___x_746_; lean_object* v___x_747_; uint8_t v___x_748_; 
lean_dec(v_ref_344_);
v___x_745_ = lean_unsigned_to_nat(0u);
v___x_746_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_745_);
v___x_747_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__95));
lean_inc(v___x_746_);
v___x_748_ = l_Lean_Syntax_isOfKind(v___x_746_, v___x_747_);
if (v___x_748_ == 0)
{
lean_object* v___x_749_; lean_object* v___x_750_; lean_object* v___x_751_; lean_object* v___x_752_; lean_object* v___f_753_; uint8_t v___x_754_; lean_object* v___x_755_; 
lean_dec(v___x_746_);
v___x_749_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_749_, 0, v_ty_316_);
v___x_750_ = lean_box(v___x_343_);
v___x_751_ = lean_box(v___x_343_);
v___x_752_ = lean_alloc_closure((void*)(l_Lean_Elab_Term_elabTerm___boxed), 11, 4);
lean_closure_set(v___x_752_, 0, v_stx_317_);
lean_closure_set(v___x_752_, 1, v___x_749_);
lean_closure_set(v___x_752_, 2, v___x_750_);
lean_closure_set(v___x_752_, 3, v___x_751_);
v___f_753_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed), 8, 1);
lean_closure_set(v___f_753_, 0, v___x_752_);
v___x_754_ = 1;
v___x_755_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(v___f_753_, v___x_754_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
return v___x_755_;
}
else
{
lean_object* v___x_756_; lean_object* v___x_757_; lean_object* v___x_758_; uint8_t v___x_759_; 
v___x_756_ = lean_unsigned_to_nat(1u);
v___x_757_ = l_Lean_Syntax_getArg(v___x_746_, v___x_756_);
lean_dec(v___x_746_);
v___x_758_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__97));
lean_inc(v___x_757_);
v___x_759_ = l_Lean_Syntax_isOfKind(v___x_757_, v___x_758_);
if (v___x_759_ == 0)
{
lean_object* v___x_760_; lean_object* v___x_761_; lean_object* v___x_762_; lean_object* v___x_763_; lean_object* v___f_764_; uint8_t v___x_765_; lean_object* v___x_766_; 
lean_dec(v___x_757_);
v___x_760_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_760_, 0, v_ty_316_);
v___x_761_ = lean_box(v___x_343_);
v___x_762_ = lean_box(v___x_343_);
v___x_763_ = lean_alloc_closure((void*)(l_Lean_Elab_Term_elabTerm___boxed), 11, 4);
lean_closure_set(v___x_763_, 0, v_stx_317_);
lean_closure_set(v___x_763_, 1, v___x_760_);
lean_closure_set(v___x_763_, 2, v___x_761_);
lean_closure_set(v___x_763_, 3, v___x_762_);
v___f_764_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed), 8, 1);
lean_closure_set(v___f_764_, 0, v___x_763_);
v___x_765_ = 1;
v___x_766_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(v___f_764_, v___x_765_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
return v___x_766_;
}
else
{
lean_object* v___x_767_; lean_object* v___x_768_; uint8_t v___x_769_; 
v___x_767_ = l_Lean_Syntax_getArg(v___x_757_, v___x_745_);
lean_dec(v___x_757_);
v___x_768_ = lean_box(0);
v___x_769_ = l_Lean_Syntax_matchesIdent(v___x_767_, v___x_768_);
lean_dec(v___x_767_);
if (v___x_769_ == 0)
{
lean_object* v___x_770_; lean_object* v___x_771_; lean_object* v___x_772_; lean_object* v___x_773_; lean_object* v___f_774_; uint8_t v___x_775_; lean_object* v___x_776_; 
v___x_770_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_770_, 0, v_ty_316_);
v___x_771_ = lean_box(v___x_343_);
v___x_772_ = lean_box(v___x_343_);
v___x_773_ = lean_alloc_closure((void*)(l_Lean_Elab_Term_elabTerm___boxed), 11, 4);
lean_closure_set(v___x_773_, 0, v_stx_317_);
lean_closure_set(v___x_773_, 1, v___x_770_);
lean_closure_set(v___x_773_, 2, v___x_771_);
lean_closure_set(v___x_773_, 3, v___x_772_);
v___f_774_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___lam__0___boxed), 8, 1);
lean_closure_set(v___f_774_, 0, v___x_773_);
v___x_775_ = 1;
v___x_776_ = l___private_Lean_Elab_SyntheticMVars_0__Lean_Elab_Term_withSynthesizeImp___redArg(v___f_774_, v___x_775_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
lean_dec_ref_known(v___x_345_, 14);
return v___x_776_;
}
else
{
lean_object* v_e_777_; lean_object* v___x_778_; 
v_e_777_ = l_Lean_Syntax_getArg(v_stx_317_, v___x_756_);
lean_dec(v_stx_317_);
v___x_778_ = lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_expandLinearCombo(v_ty_316_, v_e_777_, v_a_318_, v_a_319_, v_a_320_, v_a_321_, v___x_345_, v_a_323_);
return v___x_778_;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___boxed(lean_object* v_ty_779_, lean_object* v_stx_780_, lean_object* v_a_781_, lean_object* v_a_782_, lean_object* v_a_783_, lean_object* v_a_784_, lean_object* v_a_785_, lean_object* v_a_786_, lean_object* v_a_787_){
_start:
{
lean_object* v_res_788_; 
v_res_788_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v_ty_779_, v_stx_780_, v_a_781_, v_a_782_, v_a_783_, v_a_784_, v_a_785_, v_a_786_);
lean_dec(v_a_786_);
lean_dec_ref(v_a_785_);
lean_dec(v_a_784_);
lean_dec_ref(v_a_783_);
lean_dec(v_a_782_);
lean_dec_ref(v_a_781_);
return v_res_788_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9(void){
_start:
{
lean_object* v___x_814_; lean_object* v___x_815_; 
v___x_814_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__8));
v___x_815_ = l_String_toRawSubstring_x27(v___x_814_);
return v___x_815_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18(void){
_start:
{
lean_object* v___x_837_; lean_object* v___x_838_; 
v___x_837_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__17));
v___x_838_ = l_String_toRawSubstring_x27(v___x_837_);
return v___x_838_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27(void){
_start:
{
lean_object* v___x_858_; 
v___x_858_ = l_Array_mkArray0(lean_box(0));
return v___x_858_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31(void){
_start:
{
lean_object* v___x_862_; lean_object* v___x_863_; 
v___x_862_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__30));
v___x_863_ = l_String_toRawSubstring_x27(v___x_862_);
return v___x_863_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37(void){
_start:
{
lean_object* v___x_878_; lean_object* v___x_879_; 
v___x_878_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__36));
v___x_879_ = l_String_toRawSubstring_x27(v___x_878_);
return v___x_879_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43(void){
_start:
{
lean_object* v___x_894_; lean_object* v___x_895_; 
v___x_894_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__42));
v___x_895_ = l_String_toRawSubstring_x27(v___x_894_);
return v___x_895_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0(uint8_t v_twoGoals_898_, lean_object* v_exp_x3f_899_, lean_object* v_p_900_, lean_object* v___y_901_, lean_object* v___y_902_, lean_object* v___y_903_){
_start:
{
if (v_twoGoals_898_ == 0)
{
if (lean_obj_tag(v_exp_x3f_899_) == 1)
{
lean_object* v_val_905_; lean_object* v___x_907_; uint8_t v_isShared_908_; uint8_t v_isSharedCheck_1028_; 
v_val_905_ = lean_ctor_get(v_exp_x3f_899_, 0);
v_isSharedCheck_1028_ = !lean_is_exclusive(v_exp_x3f_899_);
if (v_isSharedCheck_1028_ == 0)
{
v___x_907_ = v_exp_x3f_899_;
v_isShared_908_ = v_isSharedCheck_1028_;
goto v_resetjp_906_;
}
else
{
lean_inc(v_val_905_);
lean_dec(v_exp_x3f_899_);
v___x_907_ = lean_box(0);
v_isShared_908_ = v_isSharedCheck_1028_;
goto v_resetjp_906_;
}
v_resetjp_906_:
{
lean_object* v___x_909_; lean_object* v___x_910_; uint8_t v___x_911_; 
v___x_909_ = l_Lean_TSyntax_getNat(v_val_905_);
v___x_910_ = lean_unsigned_to_nat(1u);
v___x_911_ = lean_nat_dec_eq(v___x_909_, v___x_910_);
lean_dec(v___x_909_);
if (v___x_911_ == 0)
{
lean_object* v_ref_912_; lean_object* v_quotContext_913_; lean_object* v_currMacroScope_914_; lean_object* v___x_915_; lean_object* v___x_916_; lean_object* v___x_917_; lean_object* v___x_918_; lean_object* v___x_919_; lean_object* v___x_920_; lean_object* v___x_921_; lean_object* v___x_922_; lean_object* v___x_923_; lean_object* v___x_924_; lean_object* v___x_925_; lean_object* v___x_926_; lean_object* v___x_927_; lean_object* v___x_928_; lean_object* v___x_929_; lean_object* v___x_930_; lean_object* v___x_931_; lean_object* v___x_932_; lean_object* v___x_933_; lean_object* v___x_934_; lean_object* v___x_935_; lean_object* v___x_936_; lean_object* v___x_937_; lean_object* v___x_938_; lean_object* v___x_939_; lean_object* v___x_940_; lean_object* v___x_941_; lean_object* v___x_942_; lean_object* v___x_943_; lean_object* v___x_944_; lean_object* v___x_945_; lean_object* v___x_946_; lean_object* v___x_947_; lean_object* v___x_948_; lean_object* v___x_949_; lean_object* v___x_950_; lean_object* v___x_951_; lean_object* v___x_952_; lean_object* v___x_953_; lean_object* v___x_954_; lean_object* v___x_955_; lean_object* v___x_956_; lean_object* v___x_957_; lean_object* v___x_958_; lean_object* v___x_959_; lean_object* v___x_960_; lean_object* v___x_961_; lean_object* v___x_962_; lean_object* v___x_963_; lean_object* v___x_964_; lean_object* v___x_965_; lean_object* v___x_966_; lean_object* v___x_968_; 
v_ref_912_ = lean_ctor_get(v___y_902_, 5);
lean_inc(v_ref_912_);
v_quotContext_913_ = lean_ctor_get(v___y_902_, 10);
lean_inc_n(v_quotContext_913_, 2);
v_currMacroScope_914_ = lean_ctor_get(v___y_902_, 11);
lean_inc_n(v_currMacroScope_914_, 2);
lean_dec_ref(v___y_902_);
v___x_915_ = l_Lean_SourceInfo_fromRef(v_ref_912_, v___x_911_);
lean_dec(v_ref_912_);
v___x_916_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0));
v___x_917_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1));
lean_inc_n(v___x_915_, 24);
v___x_918_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_918_, 0, v___x_915_);
lean_ctor_set(v___x_918_, 1, v___x_917_);
v___x_919_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3));
v___x_920_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5));
v___x_921_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_922_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6));
v___x_923_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7));
v___x_924_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_924_, 0, v___x_915_);
lean_ctor_set(v___x_924_, 1, v___x_922_);
v___x_925_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_926_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__9);
v___x_927_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__10));
v___x_928_ = l_Lean_addMacroScope(v_quotContext_913_, v___x_927_, v_currMacroScope_914_);
v___x_929_ = lean_box(0);
v___x_930_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__13));
v___x_931_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_931_, 0, v___x_915_);
lean_ctor_set(v___x_931_, 1, v___x_926_);
lean_ctor_set(v___x_931_, 2, v___x_928_);
lean_ctor_set(v___x_931_, 3, v___x_930_);
v___x_932_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15));
v___x_933_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16));
v___x_934_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_934_, 0, v___x_915_);
lean_ctor_set(v___x_934_, 1, v___x_933_);
v___x_935_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18);
v___x_936_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19));
v___x_937_ = l_Lean_addMacroScope(v_quotContext_913_, v___x_936_, v_currMacroScope_914_);
v___x_938_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_938_, 0, v___x_915_);
lean_ctor_set(v___x_938_, 1, v___x_935_);
lean_ctor_set(v___x_938_, 2, v___x_937_);
lean_ctor_set(v___x_938_, 3, v___x_929_);
lean_inc_ref(v___x_938_);
v___x_939_ = l_Lean_Syntax_node2(v___x_915_, v___x_932_, v___x_934_, v___x_938_);
v___x_940_ = l_Lean_Syntax_node3(v___x_915_, v___x_921_, v_val_905_, v_p_900_, v___x_939_);
v___x_941_ = l_Lean_Syntax_node2(v___x_915_, v___x_925_, v___x_931_, v___x_940_);
v___x_942_ = l_Lean_Syntax_node2(v___x_915_, v___x_923_, v___x_924_, v___x_941_);
v___x_943_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20));
v___x_944_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_944_, 0, v___x_915_);
lean_ctor_set(v___x_944_, 1, v___x_943_);
v___x_945_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21));
v___x_946_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22));
v___x_947_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_947_, 0, v___x_915_);
lean_ctor_set(v___x_947_, 1, v___x_945_);
v___x_948_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24));
v___x_949_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26));
v___x_950_ = l_Lean_Syntax_node1(v___x_915_, v___x_949_, v___x_938_);
v___x_951_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27);
v___x_952_ = lean_alloc_ctor(1, 3, 0);
lean_ctor_set(v___x_952_, 0, v___x_915_);
lean_ctor_set(v___x_952_, 1, v___x_921_);
lean_ctor_set(v___x_952_, 2, v___x_951_);
v___x_953_ = l_Lean_Syntax_node2(v___x_915_, v___x_948_, v___x_950_, v___x_952_);
v___x_954_ = l_Lean_Syntax_node1(v___x_915_, v___x_921_, v___x_953_);
v___x_955_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28));
v___x_956_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_956_, 0, v___x_915_);
lean_ctor_set(v___x_956_, 1, v___x_955_);
v___x_957_ = l_Lean_Syntax_node1(v___x_915_, v___x_921_, v___y_901_);
v___x_958_ = l_Lean_Syntax_node1(v___x_915_, v___x_920_, v___x_957_);
v___x_959_ = l_Lean_Syntax_node1(v___x_915_, v___x_919_, v___x_958_);
v___x_960_ = l_Lean_Syntax_node4(v___x_915_, v___x_946_, v___x_947_, v___x_954_, v___x_956_, v___x_959_);
v___x_961_ = l_Lean_Syntax_node3(v___x_915_, v___x_921_, v___x_942_, v___x_944_, v___x_960_);
v___x_962_ = l_Lean_Syntax_node1(v___x_915_, v___x_920_, v___x_961_);
v___x_963_ = l_Lean_Syntax_node1(v___x_915_, v___x_919_, v___x_962_);
v___x_964_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29));
v___x_965_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_965_, 0, v___x_915_);
lean_ctor_set(v___x_965_, 1, v___x_964_);
v___x_966_ = l_Lean_Syntax_node3(v___x_915_, v___x_916_, v___x_918_, v___x_963_, v___x_965_);
if (v_isShared_908_ == 0)
{
lean_ctor_set_tag(v___x_907_, 0);
lean_ctor_set(v___x_907_, 0, v___x_966_);
v___x_968_ = v___x_907_;
goto v_reusejp_967_;
}
else
{
lean_object* v_reuseFailAlloc_969_; 
v_reuseFailAlloc_969_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_969_, 0, v___x_966_);
v___x_968_ = v_reuseFailAlloc_969_;
goto v_reusejp_967_;
}
v_reusejp_967_:
{
return v___x_968_;
}
}
else
{
lean_object* v_ref_970_; lean_object* v_quotContext_971_; lean_object* v_currMacroScope_972_; lean_object* v___x_973_; lean_object* v___x_974_; lean_object* v___x_975_; lean_object* v___x_976_; lean_object* v___x_977_; lean_object* v___x_978_; lean_object* v___x_979_; lean_object* v___x_980_; lean_object* v___x_981_; lean_object* v___x_982_; lean_object* v___x_983_; lean_object* v___x_984_; lean_object* v___x_985_; lean_object* v___x_986_; lean_object* v___x_987_; lean_object* v___x_988_; lean_object* v___x_989_; lean_object* v___x_990_; lean_object* v___x_991_; lean_object* v___x_992_; lean_object* v___x_993_; lean_object* v___x_994_; lean_object* v___x_995_; lean_object* v___x_996_; lean_object* v___x_997_; lean_object* v___x_998_; lean_object* v___x_999_; lean_object* v___x_1000_; lean_object* v___x_1001_; lean_object* v___x_1002_; lean_object* v___x_1003_; lean_object* v___x_1004_; lean_object* v___x_1005_; lean_object* v___x_1006_; lean_object* v___x_1007_; lean_object* v___x_1008_; lean_object* v___x_1009_; lean_object* v___x_1010_; lean_object* v___x_1011_; lean_object* v___x_1012_; lean_object* v___x_1013_; lean_object* v___x_1014_; lean_object* v___x_1015_; lean_object* v___x_1016_; lean_object* v___x_1017_; lean_object* v___x_1018_; lean_object* v___x_1019_; lean_object* v___x_1020_; lean_object* v___x_1021_; lean_object* v___x_1022_; lean_object* v___x_1023_; lean_object* v___x_1024_; lean_object* v___x_1026_; 
lean_dec(v_val_905_);
v_ref_970_ = lean_ctor_get(v___y_902_, 5);
lean_inc(v_ref_970_);
v_quotContext_971_ = lean_ctor_get(v___y_902_, 10);
lean_inc_n(v_quotContext_971_, 2);
v_currMacroScope_972_ = lean_ctor_get(v___y_902_, 11);
lean_inc_n(v_currMacroScope_972_, 2);
lean_dec_ref(v___y_902_);
v___x_973_ = l_Lean_SourceInfo_fromRef(v_ref_970_, v_twoGoals_898_);
lean_dec(v_ref_970_);
v___x_974_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0));
v___x_975_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1));
lean_inc_n(v___x_973_, 24);
v___x_976_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_976_, 0, v___x_973_);
lean_ctor_set(v___x_976_, 1, v___x_975_);
v___x_977_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3));
v___x_978_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5));
v___x_979_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_980_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6));
v___x_981_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7));
v___x_982_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_982_, 0, v___x_973_);
lean_ctor_set(v___x_982_, 1, v___x_980_);
v___x_983_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_984_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31);
v___x_985_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__32));
v___x_986_ = l_Lean_addMacroScope(v_quotContext_971_, v___x_985_, v_currMacroScope_972_);
v___x_987_ = lean_box(0);
v___x_988_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__35));
v___x_989_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_989_, 0, v___x_973_);
lean_ctor_set(v___x_989_, 1, v___x_984_);
lean_ctor_set(v___x_989_, 2, v___x_986_);
lean_ctor_set(v___x_989_, 3, v___x_988_);
v___x_990_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15));
v___x_991_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16));
v___x_992_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_992_, 0, v___x_973_);
lean_ctor_set(v___x_992_, 1, v___x_991_);
v___x_993_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18);
v___x_994_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19));
v___x_995_ = l_Lean_addMacroScope(v_quotContext_971_, v___x_994_, v_currMacroScope_972_);
v___x_996_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_996_, 0, v___x_973_);
lean_ctor_set(v___x_996_, 1, v___x_993_);
lean_ctor_set(v___x_996_, 2, v___x_995_);
lean_ctor_set(v___x_996_, 3, v___x_987_);
lean_inc_ref(v___x_996_);
v___x_997_ = l_Lean_Syntax_node2(v___x_973_, v___x_990_, v___x_992_, v___x_996_);
v___x_998_ = l_Lean_Syntax_node2(v___x_973_, v___x_979_, v_p_900_, v___x_997_);
v___x_999_ = l_Lean_Syntax_node2(v___x_973_, v___x_983_, v___x_989_, v___x_998_);
v___x_1000_ = l_Lean_Syntax_node2(v___x_973_, v___x_981_, v___x_982_, v___x_999_);
v___x_1001_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20));
v___x_1002_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1002_, 0, v___x_973_);
lean_ctor_set(v___x_1002_, 1, v___x_1001_);
v___x_1003_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21));
v___x_1004_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22));
v___x_1005_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1005_, 0, v___x_973_);
lean_ctor_set(v___x_1005_, 1, v___x_1003_);
v___x_1006_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24));
v___x_1007_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26));
v___x_1008_ = l_Lean_Syntax_node1(v___x_973_, v___x_1007_, v___x_996_);
v___x_1009_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27);
v___x_1010_ = lean_alloc_ctor(1, 3, 0);
lean_ctor_set(v___x_1010_, 0, v___x_973_);
lean_ctor_set(v___x_1010_, 1, v___x_979_);
lean_ctor_set(v___x_1010_, 2, v___x_1009_);
v___x_1011_ = l_Lean_Syntax_node2(v___x_973_, v___x_1006_, v___x_1008_, v___x_1010_);
v___x_1012_ = l_Lean_Syntax_node1(v___x_973_, v___x_979_, v___x_1011_);
v___x_1013_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28));
v___x_1014_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1014_, 0, v___x_973_);
lean_ctor_set(v___x_1014_, 1, v___x_1013_);
v___x_1015_ = l_Lean_Syntax_node1(v___x_973_, v___x_979_, v___y_901_);
v___x_1016_ = l_Lean_Syntax_node1(v___x_973_, v___x_978_, v___x_1015_);
v___x_1017_ = l_Lean_Syntax_node1(v___x_973_, v___x_977_, v___x_1016_);
v___x_1018_ = l_Lean_Syntax_node4(v___x_973_, v___x_1004_, v___x_1005_, v___x_1012_, v___x_1014_, v___x_1017_);
v___x_1019_ = l_Lean_Syntax_node3(v___x_973_, v___x_979_, v___x_1000_, v___x_1002_, v___x_1018_);
v___x_1020_ = l_Lean_Syntax_node1(v___x_973_, v___x_978_, v___x_1019_);
v___x_1021_ = l_Lean_Syntax_node1(v___x_973_, v___x_977_, v___x_1020_);
v___x_1022_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29));
v___x_1023_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1023_, 0, v___x_973_);
lean_ctor_set(v___x_1023_, 1, v___x_1022_);
v___x_1024_ = l_Lean_Syntax_node3(v___x_973_, v___x_974_, v___x_976_, v___x_1021_, v___x_1023_);
if (v_isShared_908_ == 0)
{
lean_ctor_set_tag(v___x_907_, 0);
lean_ctor_set(v___x_907_, 0, v___x_1024_);
v___x_1026_ = v___x_907_;
goto v_reusejp_1025_;
}
else
{
lean_object* v_reuseFailAlloc_1027_; 
v_reuseFailAlloc_1027_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1027_, 0, v___x_1024_);
v___x_1026_ = v_reuseFailAlloc_1027_;
goto v_reusejp_1025_;
}
v_reusejp_1025_:
{
return v___x_1026_;
}
}
}
}
else
{
lean_object* v_ref_1029_; lean_object* v_quotContext_1030_; lean_object* v_currMacroScope_1031_; lean_object* v___x_1032_; lean_object* v___x_1033_; lean_object* v___x_1034_; lean_object* v___x_1035_; lean_object* v___x_1036_; lean_object* v___x_1037_; lean_object* v___x_1038_; lean_object* v___x_1039_; lean_object* v___x_1040_; lean_object* v___x_1041_; lean_object* v___x_1042_; lean_object* v___x_1043_; lean_object* v___x_1044_; lean_object* v___x_1045_; lean_object* v___x_1046_; lean_object* v___x_1047_; lean_object* v___x_1048_; lean_object* v___x_1049_; lean_object* v___x_1050_; lean_object* v___x_1051_; lean_object* v___x_1052_; lean_object* v___x_1053_; lean_object* v___x_1054_; lean_object* v___x_1055_; lean_object* v___x_1056_; lean_object* v___x_1057_; lean_object* v___x_1058_; lean_object* v___x_1059_; lean_object* v___x_1060_; lean_object* v___x_1061_; lean_object* v___x_1062_; lean_object* v___x_1063_; lean_object* v___x_1064_; lean_object* v___x_1065_; lean_object* v___x_1066_; lean_object* v___x_1067_; lean_object* v___x_1068_; lean_object* v___x_1069_; lean_object* v___x_1070_; lean_object* v___x_1071_; lean_object* v___x_1072_; lean_object* v___x_1073_; lean_object* v___x_1074_; lean_object* v___x_1075_; lean_object* v___x_1076_; lean_object* v___x_1077_; lean_object* v___x_1078_; lean_object* v___x_1079_; lean_object* v___x_1080_; lean_object* v___x_1081_; lean_object* v___x_1082_; lean_object* v___x_1083_; lean_object* v___x_1084_; 
lean_dec(v_exp_x3f_899_);
v_ref_1029_ = lean_ctor_get(v___y_902_, 5);
lean_inc(v_ref_1029_);
v_quotContext_1030_ = lean_ctor_get(v___y_902_, 10);
lean_inc_n(v_quotContext_1030_, 2);
v_currMacroScope_1031_ = lean_ctor_get(v___y_902_, 11);
lean_inc_n(v_currMacroScope_1031_, 2);
lean_dec_ref(v___y_902_);
v___x_1032_ = l_Lean_SourceInfo_fromRef(v_ref_1029_, v_twoGoals_898_);
lean_dec(v_ref_1029_);
v___x_1033_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0));
v___x_1034_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1));
lean_inc_n(v___x_1032_, 24);
v___x_1035_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1035_, 0, v___x_1032_);
lean_ctor_set(v___x_1035_, 1, v___x_1034_);
v___x_1036_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3));
v___x_1037_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5));
v___x_1038_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_1039_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6));
v___x_1040_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7));
v___x_1041_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1041_, 0, v___x_1032_);
lean_ctor_set(v___x_1041_, 1, v___x_1039_);
v___x_1042_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_1043_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__31);
v___x_1044_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__32));
v___x_1045_ = l_Lean_addMacroScope(v_quotContext_1030_, v___x_1044_, v_currMacroScope_1031_);
v___x_1046_ = lean_box(0);
v___x_1047_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__35));
v___x_1048_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1048_, 0, v___x_1032_);
lean_ctor_set(v___x_1048_, 1, v___x_1043_);
lean_ctor_set(v___x_1048_, 2, v___x_1045_);
lean_ctor_set(v___x_1048_, 3, v___x_1047_);
v___x_1049_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15));
v___x_1050_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16));
v___x_1051_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1051_, 0, v___x_1032_);
lean_ctor_set(v___x_1051_, 1, v___x_1050_);
v___x_1052_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18);
v___x_1053_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19));
v___x_1054_ = l_Lean_addMacroScope(v_quotContext_1030_, v___x_1053_, v_currMacroScope_1031_);
v___x_1055_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1055_, 0, v___x_1032_);
lean_ctor_set(v___x_1055_, 1, v___x_1052_);
lean_ctor_set(v___x_1055_, 2, v___x_1054_);
lean_ctor_set(v___x_1055_, 3, v___x_1046_);
lean_inc_ref(v___x_1055_);
v___x_1056_ = l_Lean_Syntax_node2(v___x_1032_, v___x_1049_, v___x_1051_, v___x_1055_);
v___x_1057_ = l_Lean_Syntax_node2(v___x_1032_, v___x_1038_, v_p_900_, v___x_1056_);
v___x_1058_ = l_Lean_Syntax_node2(v___x_1032_, v___x_1042_, v___x_1048_, v___x_1057_);
v___x_1059_ = l_Lean_Syntax_node2(v___x_1032_, v___x_1040_, v___x_1041_, v___x_1058_);
v___x_1060_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20));
v___x_1061_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1061_, 0, v___x_1032_);
lean_ctor_set(v___x_1061_, 1, v___x_1060_);
v___x_1062_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21));
v___x_1063_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22));
v___x_1064_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1064_, 0, v___x_1032_);
lean_ctor_set(v___x_1064_, 1, v___x_1062_);
v___x_1065_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24));
v___x_1066_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26));
v___x_1067_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1066_, v___x_1055_);
v___x_1068_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27);
v___x_1069_ = lean_alloc_ctor(1, 3, 0);
lean_ctor_set(v___x_1069_, 0, v___x_1032_);
lean_ctor_set(v___x_1069_, 1, v___x_1038_);
lean_ctor_set(v___x_1069_, 2, v___x_1068_);
v___x_1070_ = l_Lean_Syntax_node2(v___x_1032_, v___x_1065_, v___x_1067_, v___x_1069_);
v___x_1071_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1038_, v___x_1070_);
v___x_1072_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28));
v___x_1073_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1073_, 0, v___x_1032_);
lean_ctor_set(v___x_1073_, 1, v___x_1072_);
v___x_1074_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1038_, v___y_901_);
v___x_1075_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1037_, v___x_1074_);
v___x_1076_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1036_, v___x_1075_);
v___x_1077_ = l_Lean_Syntax_node4(v___x_1032_, v___x_1063_, v___x_1064_, v___x_1071_, v___x_1073_, v___x_1076_);
v___x_1078_ = l_Lean_Syntax_node3(v___x_1032_, v___x_1038_, v___x_1059_, v___x_1061_, v___x_1077_);
v___x_1079_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1037_, v___x_1078_);
v___x_1080_ = l_Lean_Syntax_node1(v___x_1032_, v___x_1036_, v___x_1079_);
v___x_1081_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29));
v___x_1082_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1082_, 0, v___x_1032_);
lean_ctor_set(v___x_1082_, 1, v___x_1081_);
v___x_1083_ = l_Lean_Syntax_node3(v___x_1032_, v___x_1033_, v___x_1035_, v___x_1080_, v___x_1082_);
v___x_1084_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v___x_1084_, 0, v___x_1083_);
return v___x_1084_;
}
}
else
{
lean_object* v_ref_1085_; lean_object* v_quotContext_1086_; lean_object* v_currMacroScope_1087_; uint8_t v___x_1088_; lean_object* v___x_1089_; lean_object* v___x_1090_; lean_object* v___x_1091_; lean_object* v___x_1092_; lean_object* v___x_1093_; lean_object* v___x_1094_; lean_object* v___x_1095_; lean_object* v___x_1096_; lean_object* v___x_1097_; lean_object* v___x_1098_; lean_object* v___x_1099_; lean_object* v___x_1100_; lean_object* v___x_1101_; lean_object* v___x_1102_; lean_object* v___x_1103_; lean_object* v___x_1104_; lean_object* v___x_1105_; lean_object* v___x_1106_; lean_object* v___x_1107_; lean_object* v___x_1108_; lean_object* v___x_1109_; lean_object* v___x_1110_; lean_object* v___x_1111_; lean_object* v___x_1112_; lean_object* v___x_1113_; lean_object* v___x_1114_; lean_object* v___x_1115_; lean_object* v___x_1116_; lean_object* v___x_1117_; lean_object* v___x_1118_; lean_object* v___x_1119_; lean_object* v___x_1120_; lean_object* v___x_1121_; lean_object* v___x_1122_; lean_object* v___x_1123_; lean_object* v___x_1124_; lean_object* v___x_1125_; lean_object* v___x_1126_; lean_object* v___x_1127_; lean_object* v___x_1128_; lean_object* v___x_1129_; lean_object* v___x_1130_; lean_object* v___x_1131_; lean_object* v___x_1132_; lean_object* v___x_1133_; lean_object* v___x_1134_; lean_object* v___x_1135_; lean_object* v___x_1136_; lean_object* v___x_1137_; lean_object* v___x_1138_; lean_object* v___x_1139_; lean_object* v___x_1140_; lean_object* v___x_1141_; lean_object* v___x_1142_; lean_object* v___x_1143_; lean_object* v___x_1144_; lean_object* v___x_1145_; lean_object* v___x_1146_; lean_object* v___x_1147_; lean_object* v___x_1148_; 
lean_dec(v_exp_x3f_899_);
v_ref_1085_ = lean_ctor_get(v___y_902_, 5);
lean_inc(v_ref_1085_);
v_quotContext_1086_ = lean_ctor_get(v___y_902_, 10);
lean_inc_n(v_quotContext_1086_, 3);
v_currMacroScope_1087_ = lean_ctor_get(v___y_902_, 11);
lean_inc_n(v_currMacroScope_1087_, 3);
lean_dec_ref(v___y_902_);
v___x_1088_ = 0;
v___x_1089_ = l_Lean_SourceInfo_fromRef(v_ref_1085_, v___x_1088_);
lean_dec(v_ref_1085_);
v___x_1090_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0));
v___x_1091_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1));
lean_inc_n(v___x_1089_, 29);
v___x_1092_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1092_, 0, v___x_1089_);
lean_ctor_set(v___x_1092_, 1, v___x_1091_);
v___x_1093_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3));
v___x_1094_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5));
v___x_1095_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_1096_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__6));
v___x_1097_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__7));
v___x_1098_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1098_, 0, v___x_1089_);
lean_ctor_set(v___x_1098_, 1, v___x_1096_);
v___x_1099_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_1100_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__37);
v___x_1101_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__38));
v___x_1102_ = l_Lean_addMacroScope(v_quotContext_1086_, v___x_1101_, v_currMacroScope_1087_);
v___x_1103_ = lean_box(0);
v___x_1104_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__41));
v___x_1105_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1105_, 0, v___x_1089_);
lean_ctor_set(v___x_1105_, 1, v___x_1100_);
lean_ctor_set(v___x_1105_, 2, v___x_1102_);
lean_ctor_set(v___x_1105_, 3, v___x_1104_);
v___x_1106_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__15));
v___x_1107_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__16));
v___x_1108_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1108_, 0, v___x_1089_);
lean_ctor_set(v___x_1108_, 1, v___x_1107_);
v___x_1109_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__18);
v___x_1110_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__19));
v___x_1111_ = l_Lean_addMacroScope(v_quotContext_1086_, v___x_1110_, v_currMacroScope_1087_);
v___x_1112_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1112_, 0, v___x_1089_);
lean_ctor_set(v___x_1112_, 1, v___x_1109_);
lean_ctor_set(v___x_1112_, 2, v___x_1111_);
lean_ctor_set(v___x_1112_, 3, v___x_1103_);
lean_inc_ref(v___x_1112_);
lean_inc_ref(v___x_1108_);
v___x_1113_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1106_, v___x_1108_, v___x_1112_);
v___x_1114_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__43);
v___x_1115_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__44));
v___x_1116_ = l_Lean_addMacroScope(v_quotContext_1086_, v___x_1115_, v_currMacroScope_1087_);
v___x_1117_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1117_, 0, v___x_1089_);
lean_ctor_set(v___x_1117_, 1, v___x_1114_);
lean_ctor_set(v___x_1117_, 2, v___x_1116_);
lean_ctor_set(v___x_1117_, 3, v___x_1103_);
lean_inc_ref(v___x_1117_);
v___x_1118_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1106_, v___x_1108_, v___x_1117_);
v___x_1119_ = l_Lean_Syntax_node3(v___x_1089_, v___x_1095_, v_p_900_, v___x_1113_, v___x_1118_);
v___x_1120_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1099_, v___x_1105_, v___x_1119_);
v___x_1121_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1097_, v___x_1098_, v___x_1120_);
v___x_1122_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27);
v___x_1123_ = lean_alloc_ctor(1, 3, 0);
lean_ctor_set(v___x_1123_, 0, v___x_1089_);
lean_ctor_set(v___x_1123_, 1, v___x_1095_);
lean_ctor_set(v___x_1123_, 2, v___x_1122_);
v___x_1124_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__21));
v___x_1125_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__22));
v___x_1126_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1126_, 0, v___x_1089_);
lean_ctor_set(v___x_1126_, 1, v___x_1124_);
v___x_1127_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__24));
v___x_1128_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__26));
v___x_1129_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1128_, v___x_1112_);
lean_inc_ref_n(v___x_1123_, 3);
v___x_1130_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1127_, v___x_1129_, v___x_1123_);
v___x_1131_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1095_, v___x_1130_);
v___x_1132_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__28));
v___x_1133_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1133_, 0, v___x_1089_);
lean_ctor_set(v___x_1133_, 1, v___x_1132_);
v___x_1134_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1095_, v___y_901_);
v___x_1135_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1094_, v___x_1134_);
v___x_1136_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1093_, v___x_1135_);
lean_inc(v___x_1136_);
lean_inc_ref(v___x_1133_);
lean_inc_ref(v___x_1126_);
v___x_1137_ = l_Lean_Syntax_node4(v___x_1089_, v___x_1125_, v___x_1126_, v___x_1131_, v___x_1133_, v___x_1136_);
v___x_1138_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1128_, v___x_1117_);
v___x_1139_ = l_Lean_Syntax_node2(v___x_1089_, v___x_1127_, v___x_1138_, v___x_1123_);
v___x_1140_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1095_, v___x_1139_);
v___x_1141_ = l_Lean_Syntax_node4(v___x_1089_, v___x_1125_, v___x_1126_, v___x_1140_, v___x_1133_, v___x_1136_);
v___x_1142_ = l_Lean_Syntax_node5(v___x_1089_, v___x_1095_, v___x_1121_, v___x_1123_, v___x_1137_, v___x_1123_, v___x_1141_);
v___x_1143_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1094_, v___x_1142_);
v___x_1144_ = l_Lean_Syntax_node1(v___x_1089_, v___x_1093_, v___x_1143_);
v___x_1145_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29));
v___x_1146_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1146_, 0, v___x_1089_);
lean_ctor_set(v___x_1146_, 1, v___x_1145_);
v___x_1147_ = l_Lean_Syntax_node3(v___x_1089_, v___x_1090_, v___x_1092_, v___x_1144_, v___x_1146_);
v___x_1148_ = lean_alloc_ctor(0, 1, 0);
lean_ctor_set(v___x_1148_, 0, v___x_1147_);
return v___x_1148_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___boxed(lean_object* v_twoGoals_1149_, lean_object* v_exp_x3f_1150_, lean_object* v_p_1151_, lean_object* v___y_1152_, lean_object* v___y_1153_, lean_object* v___y_1154_, lean_object* v___y_1155_){
_start:
{
uint8_t v_twoGoals_boxed_1156_; lean_object* v_res_1157_; 
v_twoGoals_boxed_1156_ = lean_unbox(v_twoGoals_1149_);
v_res_1157_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0(v_twoGoals_boxed_1156_, v_exp_x3f_1150_, v_p_1151_, v___y_1152_, v___y_1153_, v___y_1154_);
lean_dec(v___y_1154_);
return v_res_1157_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14(void){
_start:
{
lean_object* v___x_1189_; lean_object* v___x_1190_; 
v___x_1189_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__13));
v___x_1190_ = l_String_toRawSubstring_x27(v___x_1189_);
return v___x_1190_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16(void){
_start:
{
lean_object* v___x_1193_; lean_object* v___x_1194_; lean_object* v___x_1195_; lean_object* v___x_1196_; 
v___x_1193_ = lean_unsigned_to_nat(1u);
v___x_1194_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__15));
v___x_1195_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__1));
v___x_1196_ = l_Lean_addMacroScope(v___x_1195_, v___x_1194_, v___x_1193_);
return v___x_1196_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19(void){
_start:
{
lean_object* v___x_1199_; lean_object* v___x_1200_; 
v___x_1199_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__18));
v___x_1200_ = l_String_toRawSubstring_x27(v___x_1199_);
return v___x_1200_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21(void){
_start:
{
lean_object* v___x_1203_; lean_object* v___x_1204_; lean_object* v___x_1205_; lean_object* v___x_1206_; 
v___x_1203_ = lean_unsigned_to_nat(1u);
v___x_1204_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__20));
v___x_1205_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__1));
v___x_1206_ = l_Lean_addMacroScope(v___x_1205_, v___x_1204_, v___x_1203_);
return v___x_1206_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28(void){
_start:
{
lean_object* v___x_1218_; lean_object* v___x_1219_; 
v___x_1218_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__27));
v___x_1219_ = l_Lean_stringToMessageData(v___x_1218_);
return v___x_1219_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30(void){
_start:
{
lean_object* v___x_1221_; lean_object* v___x_1222_; 
v___x_1221_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__29));
v___x_1222_ = l_String_toRawSubstring_x27(v___x_1221_);
return v___x_1222_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1(uint8_t v_twoGoals_1237_, lean_object* v_exp_x3f_1238_, lean_object* v_norm_x3f_1239_, lean_object* v_tk_1240_, lean_object* v_input_1241_, lean_object* v___y_1242_, lean_object* v___y_1243_, lean_object* v___y_1244_, lean_object* v___y_1245_, lean_object* v___y_1246_, lean_object* v___y_1247_, lean_object* v___y_1248_, lean_object* v___y_1249_){
_start:
{
lean_object* v___y_1252_; lean_object* v___y_1253_; lean_object* v___y_1254_; lean_object* v___y_1255_; lean_object* v___y_1256_; lean_object* v___y_1257_; lean_object* v___y_1258_; lean_object* v___y_1259_; lean_object* v___y_1260_; lean_object* v___y_1261_; lean_object* v_p_1277_; lean_object* v___y_1278_; lean_object* v___y_1279_; lean_object* v___y_1280_; lean_object* v___y_1281_; lean_object* v___y_1282_; lean_object* v___y_1283_; lean_object* v___y_1284_; lean_object* v___y_1285_; lean_object* v___x_1349_; 
v___x_1349_ = l_Lean_Elab_Tactic_getMainGoal___redArg(v___y_1243_, v___y_1246_, v___y_1247_, v___y_1248_, v___y_1249_);
if (lean_obj_tag(v___x_1349_) == 0)
{
lean_object* v_a_1350_; lean_object* v___x_1351_; 
v_a_1350_ = lean_ctor_get(v___x_1349_, 0);
lean_inc(v_a_1350_);
lean_dec_ref_known(v___x_1349_, 1);
v___x_1351_ = l_Lean_MVarId_getType_x27(v_a_1350_, v___y_1246_, v___y_1247_, v___y_1248_, v___y_1249_);
if (lean_obj_tag(v___x_1351_) == 0)
{
lean_object* v_a_1352_; lean_object* v___x_1353_; lean_object* v___x_1354_; uint8_t v___x_1355_; 
v_a_1352_ = lean_ctor_get(v___x_1351_, 0);
lean_inc(v_a_1352_);
lean_dec_ref_known(v___x_1351_, 1);
v___x_1353_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__26));
v___x_1354_ = lean_unsigned_to_nat(3u);
v___x_1355_ = l_Lean_Expr_isAppOfArity(v_a_1352_, v___x_1353_, v___x_1354_);
if (v___x_1355_ == 0)
{
lean_object* v___x_1356_; lean_object* v___x_1357_; 
lean_dec(v_a_1352_);
lean_dec(v_input_1241_);
lean_dec(v_norm_x3f_1239_);
lean_dec(v_exp_x3f_1238_);
v___x_1356_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__28);
v___x_1357_ = lp_mathlib_Lean_throwError___at___00Mathlib_Tactic_LinearCombinationPrime_elabLinearCombination_x27_spec__1___redArg(v___x_1356_, v___y_1246_, v___y_1247_, v___y_1248_, v___y_1249_);
lean_dec_ref(v___y_1248_);
return v___x_1357_;
}
else
{
if (lean_obj_tag(v_input_1241_) == 0)
{
lean_object* v_ref_1358_; lean_object* v_quotContext_1359_; lean_object* v_currMacroScope_1360_; uint8_t v___x_1361_; lean_object* v___x_1362_; lean_object* v___x_1363_; lean_object* v___x_1364_; lean_object* v___x_1365_; lean_object* v___x_1366_; lean_object* v___x_1367_; lean_object* v___x_1368_; lean_object* v___x_1369_; lean_object* v___x_1370_; lean_object* v___x_1371_; lean_object* v___x_1372_; lean_object* v___x_1373_; lean_object* v___x_1374_; lean_object* v___x_1375_; 
lean_dec(v_a_1352_);
v_ref_1358_ = lean_ctor_get(v___y_1248_, 5);
v_quotContext_1359_ = lean_ctor_get(v___y_1248_, 10);
v_currMacroScope_1360_ = lean_ctor_get(v___y_1248_, 11);
v___x_1361_ = 0;
v___x_1362_ = l_Lean_SourceInfo_fromRef(v_ref_1358_, v___x_1361_);
v___x_1363_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_1364_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30);
v___x_1365_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32));
lean_inc(v_currMacroScope_1360_);
lean_inc(v_quotContext_1359_);
v___x_1366_ = l_Lean_addMacroScope(v_quotContext_1359_, v___x_1365_, v_currMacroScope_1360_);
v___x_1367_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__34));
lean_inc_n(v___x_1362_, 4);
v___x_1368_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1368_, 0, v___x_1362_);
lean_ctor_set(v___x_1368_, 1, v___x_1364_);
lean_ctor_set(v___x_1368_, 2, v___x_1366_);
lean_ctor_set(v___x_1368_, 3, v___x_1367_);
v___x_1369_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_1370_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__36));
v___x_1371_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__37));
v___x_1372_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1372_, 0, v___x_1362_);
lean_ctor_set(v___x_1372_, 1, v___x_1371_);
v___x_1373_ = l_Lean_Syntax_node1(v___x_1362_, v___x_1370_, v___x_1372_);
v___x_1374_ = l_Lean_Syntax_node1(v___x_1362_, v___x_1369_, v___x_1373_);
v___x_1375_ = l_Lean_Syntax_node2(v___x_1362_, v___x_1363_, v___x_1368_, v___x_1374_);
v_p_1277_ = v___x_1375_;
v___y_1278_ = v___y_1242_;
v___y_1279_ = v___y_1243_;
v___y_1280_ = v___y_1244_;
v___y_1281_ = v___y_1245_;
v___y_1282_ = v___y_1246_;
v___y_1283_ = v___y_1247_;
v___y_1284_ = v___y_1248_;
v___y_1285_ = v___y_1249_;
goto v___jp_1276_;
}
else
{
lean_object* v_val_1376_; lean_object* v___x_1377_; lean_object* v___x_1378_; lean_object* v___x_1379_; lean_object* v___x_1380_; 
v_val_1376_ = lean_ctor_get(v_input_1241_, 0);
lean_inc(v_val_1376_);
lean_dec_ref_known(v_input_1241_, 1);
v___x_1377_ = l_Lean_Expr_appFn_x21(v_a_1352_);
lean_dec(v_a_1352_);
v___x_1378_ = l_Lean_Expr_appFn_x21(v___x_1377_);
lean_dec_ref(v___x_1377_);
v___x_1379_ = l_Lean_Expr_appArg_x21(v___x_1378_);
lean_dec_ref(v___x_1378_);
v___x_1380_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo(v___x_1379_, v_val_1376_, v___y_1244_, v___y_1245_, v___y_1246_, v___y_1247_, v___y_1248_, v___y_1249_);
if (lean_obj_tag(v___x_1380_) == 0)
{
lean_object* v_a_1381_; 
v_a_1381_ = lean_ctor_get(v___x_1380_, 0);
lean_inc(v_a_1381_);
lean_dec_ref_known(v___x_1380_, 1);
if (lean_obj_tag(v_a_1381_) == 0)
{
lean_object* v_pf_1382_; 
v_pf_1382_ = lean_ctor_get(v_a_1381_, 0);
lean_inc(v_pf_1382_);
lean_dec_ref_known(v_a_1381_, 1);
v_p_1277_ = v_pf_1382_;
v___y_1278_ = v___y_1242_;
v___y_1279_ = v___y_1243_;
v___y_1280_ = v___y_1244_;
v___y_1281_ = v___y_1245_;
v___y_1282_ = v___y_1246_;
v___y_1283_ = v___y_1247_;
v___y_1284_ = v___y_1248_;
v___y_1285_ = v___y_1249_;
goto v___jp_1276_;
}
else
{
lean_object* v_c_1383_; lean_object* v_ref_1384_; lean_object* v_quotContext_1385_; lean_object* v_currMacroScope_1386_; uint8_t v___x_1387_; lean_object* v___x_1388_; lean_object* v___x_1389_; lean_object* v___x_1390_; lean_object* v___x_1391_; lean_object* v___x_1392_; lean_object* v___x_1393_; lean_object* v___x_1394_; lean_object* v___x_1395_; lean_object* v___x_1396_; lean_object* v___x_1397_; 
v_c_1383_ = lean_ctor_get(v_a_1381_, 0);
lean_inc(v_c_1383_);
lean_dec_ref_known(v_a_1381_, 1);
v_ref_1384_ = lean_ctor_get(v___y_1248_, 5);
v_quotContext_1385_ = lean_ctor_get(v___y_1248_, 10);
v_currMacroScope_1386_ = lean_ctor_get(v___y_1248_, 11);
v___x_1387_ = 0;
v___x_1388_ = l_Lean_SourceInfo_fromRef(v_ref_1384_, v___x_1387_);
v___x_1389_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__16));
v___x_1390_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__30);
v___x_1391_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__32));
lean_inc(v_currMacroScope_1386_);
lean_inc(v_quotContext_1385_);
v___x_1392_ = l_Lean_addMacroScope(v_quotContext_1385_, v___x_1391_, v_currMacroScope_1386_);
v___x_1393_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__34));
lean_inc_n(v___x_1388_, 2);
v___x_1394_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1394_, 0, v___x_1388_);
lean_ctor_set(v___x_1394_, 1, v___x_1390_);
lean_ctor_set(v___x_1394_, 2, v___x_1392_);
lean_ctor_set(v___x_1394_, 3, v___x_1393_);
v___x_1395_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_1396_ = l_Lean_Syntax_node1(v___x_1388_, v___x_1395_, v_c_1383_);
v___x_1397_ = l_Lean_Syntax_node2(v___x_1388_, v___x_1389_, v___x_1394_, v___x_1396_);
v_p_1277_ = v___x_1397_;
v___y_1278_ = v___y_1242_;
v___y_1279_ = v___y_1243_;
v___y_1280_ = v___y_1244_;
v___y_1281_ = v___y_1245_;
v___y_1282_ = v___y_1246_;
v___y_1283_ = v___y_1247_;
v___y_1284_ = v___y_1248_;
v___y_1285_ = v___y_1249_;
goto v___jp_1276_;
}
}
else
{
lean_object* v_a_1398_; lean_object* v___x_1400_; uint8_t v_isShared_1401_; uint8_t v_isSharedCheck_1405_; 
lean_dec_ref(v___y_1248_);
lean_dec(v_norm_x3f_1239_);
lean_dec(v_exp_x3f_1238_);
v_a_1398_ = lean_ctor_get(v___x_1380_, 0);
v_isSharedCheck_1405_ = !lean_is_exclusive(v___x_1380_);
if (v_isSharedCheck_1405_ == 0)
{
v___x_1400_ = v___x_1380_;
v_isShared_1401_ = v_isSharedCheck_1405_;
goto v_resetjp_1399_;
}
else
{
lean_inc(v_a_1398_);
lean_dec(v___x_1380_);
v___x_1400_ = lean_box(0);
v_isShared_1401_ = v_isSharedCheck_1405_;
goto v_resetjp_1399_;
}
v_resetjp_1399_:
{
lean_object* v___x_1403_; 
if (v_isShared_1401_ == 0)
{
v___x_1403_ = v___x_1400_;
goto v_reusejp_1402_;
}
else
{
lean_object* v_reuseFailAlloc_1404_; 
v_reuseFailAlloc_1404_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1404_, 0, v_a_1398_);
v___x_1403_ = v_reuseFailAlloc_1404_;
goto v_reusejp_1402_;
}
v_reusejp_1402_:
{
return v___x_1403_;
}
}
}
}
}
}
else
{
lean_object* v_a_1406_; lean_object* v___x_1408_; uint8_t v_isShared_1409_; uint8_t v_isSharedCheck_1413_; 
lean_dec_ref(v___y_1248_);
lean_dec(v_input_1241_);
lean_dec(v_norm_x3f_1239_);
lean_dec(v_exp_x3f_1238_);
v_a_1406_ = lean_ctor_get(v___x_1351_, 0);
v_isSharedCheck_1413_ = !lean_is_exclusive(v___x_1351_);
if (v_isSharedCheck_1413_ == 0)
{
v___x_1408_ = v___x_1351_;
v_isShared_1409_ = v_isSharedCheck_1413_;
goto v_resetjp_1407_;
}
else
{
lean_inc(v_a_1406_);
lean_dec(v___x_1351_);
v___x_1408_ = lean_box(0);
v_isShared_1409_ = v_isSharedCheck_1413_;
goto v_resetjp_1407_;
}
v_resetjp_1407_:
{
lean_object* v___x_1411_; 
if (v_isShared_1409_ == 0)
{
v___x_1411_ = v___x_1408_;
goto v_reusejp_1410_;
}
else
{
lean_object* v_reuseFailAlloc_1412_; 
v_reuseFailAlloc_1412_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1412_, 0, v_a_1406_);
v___x_1411_ = v_reuseFailAlloc_1412_;
goto v_reusejp_1410_;
}
v_reusejp_1410_:
{
return v___x_1411_;
}
}
}
}
else
{
lean_object* v_a_1414_; lean_object* v___x_1416_; uint8_t v_isShared_1417_; uint8_t v_isSharedCheck_1421_; 
lean_dec_ref(v___y_1248_);
lean_dec(v_input_1241_);
lean_dec(v_norm_x3f_1239_);
lean_dec(v_exp_x3f_1238_);
v_a_1414_ = lean_ctor_get(v___x_1349_, 0);
v_isSharedCheck_1421_ = !lean_is_exclusive(v___x_1349_);
if (v_isSharedCheck_1421_ == 0)
{
v___x_1416_ = v___x_1349_;
v_isShared_1417_ = v_isSharedCheck_1421_;
goto v_resetjp_1415_;
}
else
{
lean_inc(v_a_1414_);
lean_dec(v___x_1349_);
v___x_1416_ = lean_box(0);
v_isShared_1417_ = v_isSharedCheck_1421_;
goto v_resetjp_1415_;
}
v_resetjp_1415_:
{
lean_object* v___x_1419_; 
if (v_isShared_1417_ == 0)
{
v___x_1419_ = v___x_1416_;
goto v_reusejp_1418_;
}
else
{
lean_object* v_reuseFailAlloc_1420_; 
v_reuseFailAlloc_1420_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1420_, 0, v_a_1414_);
v___x_1419_ = v_reuseFailAlloc_1420_;
goto v_reusejp_1418_;
}
v_reusejp_1418_:
{
return v___x_1419_;
}
}
}
v___jp_1251_:
{
lean_object* v___x_1262_; lean_object* v___f_1263_; lean_object* v___x_1264_; 
v___x_1262_ = lean_box(v_twoGoals_1237_);
v___f_1263_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___boxed), 7, 4);
lean_closure_set(v___f_1263_, 0, v___x_1262_);
lean_closure_set(v___f_1263_, 1, v_exp_x3f_1238_);
lean_closure_set(v___f_1263_, 2, v___y_1253_);
lean_closure_set(v___f_1263_, 3, v___y_1261_);
v___x_1264_ = l_Lean_Core_withFreshMacroScope___redArg(v___f_1263_, v___y_1259_, v___y_1258_);
if (lean_obj_tag(v___x_1264_) == 0)
{
lean_object* v_a_1265_; lean_object* v___x_1266_; lean_object* v___x_1267_; 
v_a_1265_ = lean_ctor_get(v___x_1264_, 0);
lean_inc(v_a_1265_);
lean_dec_ref_known(v___x_1264_, 1);
v___x_1266_ = lean_alloc_closure((void*)(l_Lean_Elab_Tactic_evalTactic___boxed), 10, 1);
lean_closure_set(v___x_1266_, 0, v_a_1265_);
v___x_1267_ = lp_mathlib_Lean_Elab_Term_withoutErrToSorry___at___00Mathlib_Tactic_LinearCombinationPrime_elabLinearCombination_x27_spec__0___redArg(v___x_1266_, v___y_1257_, v___y_1255_, v___y_1252_, v___y_1254_, v___y_1260_, v___y_1256_, v___y_1259_, v___y_1258_);
lean_dec_ref(v___y_1259_);
return v___x_1267_;
}
else
{
lean_object* v_a_1268_; lean_object* v___x_1270_; uint8_t v_isShared_1271_; uint8_t v_isSharedCheck_1275_; 
lean_dec_ref(v___y_1259_);
v_a_1268_ = lean_ctor_get(v___x_1264_, 0);
v_isSharedCheck_1275_ = !lean_is_exclusive(v___x_1264_);
if (v_isSharedCheck_1275_ == 0)
{
v___x_1270_ = v___x_1264_;
v_isShared_1271_ = v_isSharedCheck_1275_;
goto v_resetjp_1269_;
}
else
{
lean_inc(v_a_1268_);
lean_dec(v___x_1264_);
v___x_1270_ = lean_box(0);
v_isShared_1271_ = v_isSharedCheck_1275_;
goto v_resetjp_1269_;
}
v_resetjp_1269_:
{
lean_object* v___x_1273_; 
if (v_isShared_1271_ == 0)
{
v___x_1273_ = v___x_1270_;
goto v_reusejp_1272_;
}
else
{
lean_object* v_reuseFailAlloc_1274_; 
v_reuseFailAlloc_1274_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1274_, 0, v_a_1268_);
v___x_1273_ = v_reuseFailAlloc_1274_;
goto v_reusejp_1272_;
}
v_reusejp_1272_:
{
return v___x_1273_;
}
}
}
}
v___jp_1276_:
{
if (lean_obj_tag(v_norm_x3f_1239_) == 0)
{
lean_object* v___x_1286_; lean_object* v_ref_1287_; uint8_t v___x_1288_; lean_object* v___x_1289_; lean_object* v___x_1290_; lean_object* v___x_1291_; lean_object* v___x_1292_; lean_object* v___x_1293_; lean_object* v___x_1294_; lean_object* v___x_1295_; lean_object* v___x_1296_; lean_object* v___x_1297_; lean_object* v___x_1298_; lean_object* v___x_1299_; lean_object* v___x_1300_; lean_object* v___x_1301_; lean_object* v___x_1302_; lean_object* v___x_1303_; lean_object* v___x_1304_; lean_object* v___x_1305_; lean_object* v___x_1306_; lean_object* v___x_1307_; lean_object* v___x_1308_; lean_object* v___x_1309_; lean_object* v___x_1310_; lean_object* v___x_1311_; lean_object* v___x_1312_; lean_object* v___x_1313_; lean_object* v___x_1314_; lean_object* v___x_1315_; lean_object* v___x_1316_; lean_object* v___x_1317_; lean_object* v___x_1318_; lean_object* v___x_1319_; lean_object* v___x_1320_; lean_object* v___x_1321_; lean_object* v___x_1322_; lean_object* v___x_1323_; lean_object* v___x_1324_; lean_object* v___x_1325_; lean_object* v___x_1326_; lean_object* v___x_1327_; lean_object* v___x_1328_; lean_object* v___x_1329_; lean_object* v___x_1330_; lean_object* v___x_1331_; lean_object* v___x_1332_; lean_object* v___x_1333_; lean_object* v___x_1334_; lean_object* v___x_1335_; lean_object* v___x_1336_; lean_object* v___x_1337_; lean_object* v___x_1338_; lean_object* v___x_1339_; lean_object* v___x_1340_; lean_object* v___x_1341_; lean_object* v___x_1342_; lean_object* v___x_1343_; lean_object* v___x_1344_; lean_object* v___x_1345_; lean_object* v___x_1346_; lean_object* v___x_1347_; 
v___x_1286_ = lean_box(0);
v_ref_1287_ = l_Lean_replaceRef(v_tk_1240_, v___x_1286_);
v___x_1288_ = 0;
v___x_1289_ = l_Lean_SourceInfo_fromRef(v_ref_1287_, v___x_1288_);
lean_dec(v_ref_1287_);
v___x_1290_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__0));
v___x_1291_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__1));
lean_inc_n(v___x_1289_, 32);
v___x_1292_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1292_, 0, v___x_1289_);
lean_ctor_set(v___x_1292_, 1, v___x_1291_);
v___x_1293_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__3));
v___x_1294_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__5));
v___x_1295_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_expandAdditiveCombo___closed__27));
v___x_1296_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__3));
v___x_1297_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__4));
v___x_1298_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1298_, 0, v___x_1289_);
lean_ctor_set(v___x_1298_, 1, v___x_1297_);
v___x_1299_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__5));
v___x_1300_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__6));
v___x_1301_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1301_, 0, v___x_1289_);
lean_ctor_set(v___x_1301_, 1, v___x_1299_);
v___x_1302_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__8));
v___x_1303_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__27);
v___x_1304_ = lean_alloc_ctor(1, 3, 0);
lean_ctor_set(v___x_1304_, 0, v___x_1289_);
lean_ctor_set(v___x_1304_, 1, v___x_1295_);
lean_ctor_set(v___x_1304_, 2, v___x_1303_);
lean_inc_ref_n(v___x_1304_, 7);
v___x_1305_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1302_, v___x_1304_);
v___x_1306_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__9));
v___x_1307_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1307_, 0, v___x_1289_);
lean_ctor_set(v___x_1307_, 1, v___x_1306_);
v___x_1308_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1295_, v___x_1307_);
v___x_1309_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__10));
v___x_1310_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1310_, 0, v___x_1289_);
lean_ctor_set(v___x_1310_, 1, v___x_1309_);
v___x_1311_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__12));
v___x_1312_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__14);
v___x_1313_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__16);
v___x_1314_ = lean_box(0);
v___x_1315_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1315_, 0, v___x_1289_);
lean_ctor_set(v___x_1315_, 1, v___x_1312_);
lean_ctor_set(v___x_1315_, 2, v___x_1313_);
lean_ctor_set(v___x_1315_, 3, v___x_1314_);
v___x_1316_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1311_, v___x_1304_, v___x_1304_, v___x_1315_);
v___x_1317_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__17));
v___x_1318_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1318_, 0, v___x_1289_);
lean_ctor_set(v___x_1318_, 1, v___x_1317_);
v___x_1319_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__19);
v___x_1320_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__21);
v___x_1321_ = lean_alloc_ctor(3, 4, 0);
lean_ctor_set(v___x_1321_, 0, v___x_1289_);
lean_ctor_set(v___x_1321_, 1, v___x_1319_);
lean_ctor_set(v___x_1321_, 2, v___x_1320_);
lean_ctor_set(v___x_1321_, 3, v___x_1314_);
v___x_1322_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1311_, v___x_1304_, v___x_1304_, v___x_1321_);
v___x_1323_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1295_, v___x_1316_, v___x_1318_, v___x_1322_);
v___x_1324_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__22));
v___x_1325_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1325_, 0, v___x_1289_);
lean_ctor_set(v___x_1325_, 1, v___x_1324_);
v___x_1326_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1295_, v___x_1310_, v___x_1323_, v___x_1325_);
v___x_1327_ = l_Lean_Syntax_node6(v___x_1289_, v___x_1300_, v___x_1301_, v___x_1305_, v___x_1304_, v___x_1308_, v___x_1326_, v___x_1304_);
v___x_1328_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1295_, v___x_1327_);
v___x_1329_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1294_, v___x_1328_);
v___x_1330_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1293_, v___x_1329_);
v___x_1331_ = l_Lean_Syntax_node2(v___x_1289_, v___x_1296_, v___x_1298_, v___x_1330_);
v___x_1332_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1295_, v___x_1331_);
v___x_1333_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1294_, v___x_1332_);
v___x_1334_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1293_, v___x_1333_);
v___x_1335_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__29));
v___x_1336_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1336_, 0, v___x_1289_);
lean_ctor_set(v___x_1336_, 1, v___x_1335_);
lean_inc_ref(v___x_1336_);
lean_inc_ref(v___x_1292_);
v___x_1337_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1290_, v___x_1292_, v___x_1334_, v___x_1336_);
v___x_1338_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__0___closed__20));
v___x_1339_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1339_, 0, v___x_1289_);
lean_ctor_set(v___x_1339_, 1, v___x_1338_);
v___x_1340_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__24));
v___x_1341_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___closed__25));
v___x_1342_ = lean_alloc_ctor(2, 2, 0);
lean_ctor_set(v___x_1342_, 0, v___x_1289_);
lean_ctor_set(v___x_1342_, 1, v___x_1340_);
v___x_1343_ = l_Lean_Syntax_node2(v___x_1289_, v___x_1341_, v___x_1342_, v___x_1304_);
v___x_1344_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1295_, v___x_1337_, v___x_1339_, v___x_1343_);
v___x_1345_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1294_, v___x_1344_);
v___x_1346_ = l_Lean_Syntax_node1(v___x_1289_, v___x_1293_, v___x_1345_);
v___x_1347_ = l_Lean_Syntax_node3(v___x_1289_, v___x_1290_, v___x_1292_, v___x_1346_, v___x_1336_);
v___y_1252_ = v___y_1280_;
v___y_1253_ = v_p_1277_;
v___y_1254_ = v___y_1281_;
v___y_1255_ = v___y_1279_;
v___y_1256_ = v___y_1283_;
v___y_1257_ = v___y_1278_;
v___y_1258_ = v___y_1285_;
v___y_1259_ = v___y_1284_;
v___y_1260_ = v___y_1282_;
v___y_1261_ = v___x_1347_;
goto v___jp_1251_;
}
else
{
lean_object* v_val_1348_; 
v_val_1348_ = lean_ctor_get(v_norm_x3f_1239_, 0);
lean_inc(v_val_1348_);
lean_dec_ref_known(v_norm_x3f_1239_, 1);
v___y_1252_ = v___y_1280_;
v___y_1253_ = v_p_1277_;
v___y_1254_ = v___y_1281_;
v___y_1255_ = v___y_1279_;
v___y_1256_ = v___y_1283_;
v___y_1257_ = v___y_1278_;
v___y_1258_ = v___y_1285_;
v___y_1259_ = v___y_1284_;
v___y_1260_ = v___y_1282_;
v___y_1261_ = v_val_1348_;
goto v___jp_1251_;
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___boxed(lean_object* v_twoGoals_1422_, lean_object* v_exp_x3f_1423_, lean_object* v_norm_x3f_1424_, lean_object* v_tk_1425_, lean_object* v_input_1426_, lean_object* v___y_1427_, lean_object* v___y_1428_, lean_object* v___y_1429_, lean_object* v___y_1430_, lean_object* v___y_1431_, lean_object* v___y_1432_, lean_object* v___y_1433_, lean_object* v___y_1434_, lean_object* v___y_1435_){
_start:
{
uint8_t v_twoGoals_boxed_1436_; lean_object* v_res_1437_; 
v_twoGoals_boxed_1436_ = lean_unbox(v_twoGoals_1422_);
v_res_1437_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1(v_twoGoals_boxed_1436_, v_exp_x3f_1423_, v_norm_x3f_1424_, v_tk_1425_, v_input_1426_, v___y_1427_, v___y_1428_, v___y_1429_, v___y_1430_, v___y_1431_, v___y_1432_, v___y_1433_, v___y_1434_);
lean_dec(v___y_1434_);
lean_dec(v___y_1432_);
lean_dec_ref(v___y_1431_);
lean_dec(v___y_1430_);
lean_dec_ref(v___y_1429_);
lean_dec(v___y_1428_);
lean_dec_ref(v___y_1427_);
lean_dec(v_tk_1425_);
return v_res_1437_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination(lean_object* v_tk_1438_, lean_object* v_norm_x3f_1439_, lean_object* v_exp_x3f_1440_, lean_object* v_input_1441_, uint8_t v_twoGoals_1442_, lean_object* v_a_1443_, lean_object* v_a_1444_, lean_object* v_a_1445_, lean_object* v_a_1446_, lean_object* v_a_1447_, lean_object* v_a_1448_, lean_object* v_a_1449_, lean_object* v_a_1450_){
_start:
{
lean_object* v___x_1452_; lean_object* v___f_1453_; lean_object* v___x_1454_; 
v___x_1452_ = lean_box(v_twoGoals_1442_);
v___f_1453_ = lean_alloc_closure((void*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___lam__1___boxed), 14, 5);
lean_closure_set(v___f_1453_, 0, v___x_1452_);
lean_closure_set(v___f_1453_, 1, v_exp_x3f_1440_);
lean_closure_set(v___f_1453_, 2, v_norm_x3f_1439_);
lean_closure_set(v___f_1453_, 3, v_tk_1438_);
lean_closure_set(v___f_1453_, 4, v_input_1441_);
v___x_1454_ = l_Lean_Elab_Tactic_withMainContext___redArg(v___f_1453_, v_a_1443_, v_a_1444_, v_a_1445_, v_a_1446_, v_a_1447_, v_a_1448_, v_a_1449_, v_a_1450_);
return v___x_1454_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination___boxed(lean_object* v_tk_1455_, lean_object* v_norm_x3f_1456_, lean_object* v_exp_x3f_1457_, lean_object* v_input_1458_, lean_object* v_twoGoals_1459_, lean_object* v_a_1460_, lean_object* v_a_1461_, lean_object* v_a_1462_, lean_object* v_a_1463_, lean_object* v_a_1464_, lean_object* v_a_1465_, lean_object* v_a_1466_, lean_object* v_a_1467_, lean_object* v_a_1468_){
_start:
{
uint8_t v_twoGoals_boxed_1469_; lean_object* v_res_1470_; 
v_twoGoals_boxed_1469_ = lean_unbox(v_twoGoals_1459_);
v_res_1470_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination(v_tk_1455_, v_norm_x3f_1456_, v_exp_x3f_1457_, v_input_1458_, v_twoGoals_boxed_1469_, v_a_1460_, v_a_1461_, v_a_1462_, v_a_1463_, v_a_1464_, v_a_1465_, v_a_1466_, v_a_1467_);
lean_dec(v_a_1467_);
lean_dec_ref(v_a_1466_);
lean_dec(v_a_1465_);
lean_dec_ref(v_a_1464_);
lean_dec(v_a_1463_);
lean_dec_ref(v_a_1462_);
lean_dec(v_a_1461_);
lean_dec_ref(v_a_1460_);
return v_res_1470_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8(void){
_start:
{
lean_object* v___x_1487_; lean_object* v___x_1488_; lean_object* v___x_1489_; 
v___x_1487_ = lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_normStx;
v___x_1488_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7));
v___x_1489_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_1489_, 0, v___x_1488_);
lean_ctor_set(v___x_1489_, 1, v___x_1487_);
return v___x_1489_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9(void){
_start:
{
lean_object* v___x_1490_; lean_object* v___x_1491_; lean_object* v___x_1492_; lean_object* v___x_1493_; 
v___x_1490_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__8);
v___x_1491_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__5));
v___x_1492_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3));
v___x_1493_ = lean_alloc_ctor(2, 3, 0);
lean_ctor_set(v___x_1493_, 0, v___x_1492_);
lean_ctor_set(v___x_1493_, 1, v___x_1491_);
lean_ctor_set(v___x_1493_, 2, v___x_1490_);
return v___x_1493_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10(void){
_start:
{
lean_object* v___x_1494_; lean_object* v___x_1495_; lean_object* v___x_1496_; 
v___x_1494_ = lp_mathlib_Mathlib_Tactic_LinearCombinationPrime_expStx;
v___x_1495_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__7));
v___x_1496_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_1496_, 0, v___x_1495_);
lean_ctor_set(v___x_1496_, 1, v___x_1494_);
return v___x_1496_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11(void){
_start:
{
lean_object* v___x_1497_; lean_object* v___x_1498_; lean_object* v___x_1499_; lean_object* v___x_1500_; 
v___x_1497_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__10);
v___x_1498_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__9);
v___x_1499_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3));
v___x_1500_ = lean_alloc_ctor(2, 3, 0);
lean_ctor_set(v___x_1500_, 0, v___x_1499_);
lean_ctor_set(v___x_1500_, 1, v___x_1498_);
lean_ctor_set(v___x_1500_, 2, v___x_1497_);
return v___x_1500_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24(void){
_start:
{
lean_object* v___x_1528_; lean_object* v___x_1529_; lean_object* v___x_1530_; lean_object* v___x_1531_; 
v___x_1528_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__23));
v___x_1529_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__11);
v___x_1530_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__3));
v___x_1531_ = lean_alloc_ctor(2, 3, 0);
lean_ctor_set(v___x_1531_, 0, v___x_1530_);
lean_ctor_set(v___x_1531_, 1, v___x_1529_);
lean_ctor_set(v___x_1531_, 2, v___x_1528_);
return v___x_1531_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25(void){
_start:
{
lean_object* v___x_1532_; lean_object* v___x_1533_; lean_object* v___x_1534_; lean_object* v___x_1535_; 
v___x_1532_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__24);
v___x_1533_ = lean_unsigned_to_nat(1022u);
v___x_1534_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1));
v___x_1535_ = lean_alloc_ctor(3, 3, 0);
lean_ctor_set(v___x_1535_, 0, v___x_1534_);
lean_ctor_set(v___x_1535_, 1, v___x_1533_);
lean_ctor_set(v___x_1535_, 2, v___x_1532_);
return v___x_1535_;
}
}
static lean_object* _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination(void){
_start:
{
lean_object* v___x_1536_; 
v___x_1536_ = lean_obj_once(&lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25, &lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25_once, _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__25);
return v___x_1536_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1(lean_object* v_x_1549_, lean_object* v_a_1550_, lean_object* v_a_1551_, lean_object* v_a_1552_, lean_object* v_a_1553_, lean_object* v_a_1554_, lean_object* v_a_1555_, lean_object* v_a_1556_, lean_object* v_a_1557_){
_start:
{
lean_object* v___x_1559_; uint8_t v___x_1560_; 
v___x_1559_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination___closed__1));
lean_inc(v_x_1549_);
v___x_1560_ = l_Lean_Syntax_isOfKind(v_x_1549_, v___x_1559_);
if (v___x_1560_ == 0)
{
lean_object* v___x_1561_; 
lean_dec(v_x_1549_);
v___x_1561_ = lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
return v___x_1561_;
}
else
{
lean_object* v___x_1562_; lean_object* v_tk_1563_; lean_object* v___y_1565_; lean_object* v___y_1566_; lean_object* v___y_1567_; lean_object* v___y_1568_; lean_object* v___y_1569_; lean_object* v___y_1570_; lean_object* v___y_1571_; lean_object* v___y_1572_; lean_object* v___y_1573_; lean_object* v___y_1574_; lean_object* v___y_1575_; lean_object* v___y_1579_; lean_object* v_n_1580_; lean_object* v___y_1581_; lean_object* v___y_1582_; lean_object* v___y_1583_; lean_object* v___y_1584_; lean_object* v___y_1585_; lean_object* v___y_1586_; lean_object* v___y_1587_; lean_object* v___y_1588_; lean_object* v___x_1601_; lean_object* v_tac_1603_; lean_object* v___y_1604_; lean_object* v___y_1605_; lean_object* v___y_1606_; lean_object* v___y_1607_; lean_object* v___y_1608_; lean_object* v___y_1609_; lean_object* v___y_1610_; lean_object* v___y_1611_; lean_object* v___x_1625_; uint8_t v___x_1626_; 
v___x_1562_ = lean_unsigned_to_nat(0u);
v_tk_1563_ = l_Lean_Syntax_getArg(v_x_1549_, v___x_1562_);
v___x_1601_ = lean_unsigned_to_nat(1u);
v___x_1625_ = l_Lean_Syntax_getArg(v_x_1549_, v___x_1601_);
v___x_1626_ = l_Lean_Syntax_isNone(v___x_1625_);
if (v___x_1626_ == 0)
{
uint8_t v___x_1627_; 
lean_inc(v___x_1625_);
v___x_1627_ = l_Lean_Syntax_matchesNull(v___x_1625_, v___x_1601_);
if (v___x_1627_ == 0)
{
lean_object* v___x_1628_; 
lean_dec(v___x_1625_);
lean_dec(v_tk_1563_);
lean_dec(v_x_1549_);
v___x_1628_ = lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
return v___x_1628_;
}
else
{
lean_object* v___x_1629_; lean_object* v___x_1630_; uint8_t v___x_1631_; 
v___x_1629_ = l_Lean_Syntax_getArg(v___x_1625_, v___x_1562_);
lean_dec(v___x_1625_);
v___x_1630_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__3));
lean_inc(v___x_1629_);
v___x_1631_ = l_Lean_Syntax_isOfKind(v___x_1629_, v___x_1630_);
if (v___x_1631_ == 0)
{
lean_object* v___x_1632_; 
lean_dec(v___x_1629_);
lean_dec(v_tk_1563_);
lean_dec(v_x_1549_);
v___x_1632_ = lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
return v___x_1632_;
}
else
{
lean_object* v___x_1633_; lean_object* v_tac_1634_; lean_object* v___x_1635_; 
v___x_1633_ = lean_unsigned_to_nat(3u);
v_tac_1634_ = l_Lean_Syntax_getArg(v___x_1629_, v___x_1633_);
lean_dec(v___x_1629_);
v___x_1635_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_1635_, 0, v_tac_1634_);
v_tac_1603_ = v___x_1635_;
v___y_1604_ = v_a_1550_;
v___y_1605_ = v_a_1551_;
v___y_1606_ = v_a_1552_;
v___y_1607_ = v_a_1553_;
v___y_1608_ = v_a_1554_;
v___y_1609_ = v_a_1555_;
v___y_1610_ = v_a_1556_;
v___y_1611_ = v_a_1557_;
goto v___jp_1602_;
}
}
}
else
{
lean_object* v___x_1636_; 
lean_dec(v___x_1625_);
v___x_1636_ = lean_box(0);
v_tac_1603_ = v___x_1636_;
v___y_1604_ = v_a_1550_;
v___y_1605_ = v_a_1551_;
v___y_1606_ = v_a_1552_;
v___y_1607_ = v_a_1553_;
v___y_1608_ = v_a_1554_;
v___y_1609_ = v_a_1555_;
v___y_1610_ = v_a_1556_;
v___y_1611_ = v_a_1557_;
goto v___jp_1602_;
}
v___jp_1564_:
{
uint8_t v___x_1576_; lean_object* v___x_1577_; 
v___x_1576_ = 0;
v___x_1577_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_elabAdditiveCombination(v_tk_1563_, v___y_1573_, v___y_1566_, v___y_1575_, v___x_1576_, v___y_1570_, v___y_1572_, v___y_1565_, v___y_1574_, v___y_1569_, v___y_1568_, v___y_1567_, v___y_1571_);
return v___x_1577_;
}
v___jp_1578_:
{
lean_object* v___x_1589_; lean_object* v___x_1590_; lean_object* v___x_1591_; 
v___x_1589_ = lean_unsigned_to_nat(3u);
v___x_1590_ = l_Lean_Syntax_getArg(v_x_1549_, v___x_1589_);
lean_dec(v_x_1549_);
v___x_1591_ = l_Lean_Syntax_getOptional_x3f(v___x_1590_);
lean_dec(v___x_1590_);
if (lean_obj_tag(v___x_1591_) == 0)
{
lean_object* v___x_1592_; 
v___x_1592_ = lean_box(0);
v___y_1565_ = v___y_1583_;
v___y_1566_ = v_n_1580_;
v___y_1567_ = v___y_1587_;
v___y_1568_ = v___y_1586_;
v___y_1569_ = v___y_1585_;
v___y_1570_ = v___y_1581_;
v___y_1571_ = v___y_1588_;
v___y_1572_ = v___y_1582_;
v___y_1573_ = v___y_1579_;
v___y_1574_ = v___y_1584_;
v___y_1575_ = v___x_1592_;
goto v___jp_1564_;
}
else
{
lean_object* v_val_1593_; lean_object* v___x_1595_; uint8_t v_isShared_1596_; uint8_t v_isSharedCheck_1600_; 
v_val_1593_ = lean_ctor_get(v___x_1591_, 0);
v_isSharedCheck_1600_ = !lean_is_exclusive(v___x_1591_);
if (v_isSharedCheck_1600_ == 0)
{
v___x_1595_ = v___x_1591_;
v_isShared_1596_ = v_isSharedCheck_1600_;
goto v_resetjp_1594_;
}
else
{
lean_inc(v_val_1593_);
lean_dec(v___x_1591_);
v___x_1595_ = lean_box(0);
v_isShared_1596_ = v_isSharedCheck_1600_;
goto v_resetjp_1594_;
}
v_resetjp_1594_:
{
lean_object* v___x_1598_; 
if (v_isShared_1596_ == 0)
{
v___x_1598_ = v___x_1595_;
goto v_reusejp_1597_;
}
else
{
lean_object* v_reuseFailAlloc_1599_; 
v_reuseFailAlloc_1599_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v_reuseFailAlloc_1599_, 0, v_val_1593_);
v___x_1598_ = v_reuseFailAlloc_1599_;
goto v_reusejp_1597_;
}
v_reusejp_1597_:
{
v___y_1565_ = v___y_1583_;
v___y_1566_ = v_n_1580_;
v___y_1567_ = v___y_1587_;
v___y_1568_ = v___y_1586_;
v___y_1569_ = v___y_1585_;
v___y_1570_ = v___y_1581_;
v___y_1571_ = v___y_1588_;
v___y_1572_ = v___y_1582_;
v___y_1573_ = v___y_1579_;
v___y_1574_ = v___y_1584_;
v___y_1575_ = v___x_1598_;
goto v___jp_1564_;
}
}
}
}
v___jp_1602_:
{
lean_object* v___x_1612_; lean_object* v___x_1613_; uint8_t v___x_1614_; 
v___x_1612_ = lean_unsigned_to_nat(2u);
v___x_1613_ = l_Lean_Syntax_getArg(v_x_1549_, v___x_1612_);
v___x_1614_ = l_Lean_Syntax_isNone(v___x_1613_);
if (v___x_1614_ == 0)
{
uint8_t v___x_1615_; 
lean_inc(v___x_1613_);
v___x_1615_ = l_Lean_Syntax_matchesNull(v___x_1613_, v___x_1601_);
if (v___x_1615_ == 0)
{
lean_object* v___x_1616_; 
lean_dec(v___x_1613_);
lean_dec(v_tac_1603_);
lean_dec(v_tk_1563_);
lean_dec(v_x_1549_);
v___x_1616_ = lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
return v___x_1616_;
}
else
{
lean_object* v___x_1617_; lean_object* v___x_1618_; uint8_t v___x_1619_; 
v___x_1617_ = l_Lean_Syntax_getArg(v___x_1613_, v___x_1562_);
lean_dec(v___x_1613_);
v___x_1618_ = ((lean_object*)(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___closed__1));
lean_inc(v___x_1617_);
v___x_1619_ = l_Lean_Syntax_isOfKind(v___x_1617_, v___x_1618_);
if (v___x_1619_ == 0)
{
lean_object* v___x_1620_; 
lean_dec(v___x_1617_);
lean_dec(v_tac_1603_);
lean_dec(v_tk_1563_);
lean_dec(v_x_1549_);
v___x_1620_ = lp_mathlib_Lean_Elab_throwUnsupportedSyntax___at___00Mathlib_Tactic_LinearCombinationPrime___aux__Mathlib__Tactic__LinearCombinationPrime______elabRules__Mathlib__Tactic__LinearCombinationPrime__linearCombination_x27__1_spec__0___redArg();
return v___x_1620_;
}
else
{
lean_object* v___x_1621_; lean_object* v_n_1622_; lean_object* v___x_1623_; 
v___x_1621_ = lean_unsigned_to_nat(3u);
v_n_1622_ = l_Lean_Syntax_getArg(v___x_1617_, v___x_1621_);
lean_dec(v___x_1617_);
v___x_1623_ = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(v___x_1623_, 0, v_n_1622_);
v___y_1579_ = v_tac_1603_;
v_n_1580_ = v___x_1623_;
v___y_1581_ = v___y_1604_;
v___y_1582_ = v___y_1605_;
v___y_1583_ = v___y_1606_;
v___y_1584_ = v___y_1607_;
v___y_1585_ = v___y_1608_;
v___y_1586_ = v___y_1609_;
v___y_1587_ = v___y_1610_;
v___y_1588_ = v___y_1611_;
goto v___jp_1578_;
}
}
}
else
{
lean_object* v___x_1624_; 
lean_dec(v___x_1613_);
v___x_1624_ = lean_box(0);
v___y_1579_ = v_tac_1603_;
v_n_1580_ = v___x_1624_;
v___y_1581_ = v___y_1604_;
v___y_1582_ = v___y_1605_;
v___y_1583_ = v___y_1606_;
v___y_1584_ = v___y_1607_;
v___y_1585_ = v___y_1608_;
v___y_1586_ = v___y_1609_;
v___y_1587_ = v___y_1610_;
v___y_1588_ = v___y_1611_;
goto v___jp_1578_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1___boxed(lean_object* v_x_1637_, lean_object* v_a_1638_, lean_object* v_a_1639_, lean_object* v_a_1640_, lean_object* v_a_1641_, lean_object* v_a_1642_, lean_object* v_a_1643_, lean_object* v_a_1644_, lean_object* v_a_1645_, lean_object* v_a_1646_){
_start:
{
lean_object* v_res_1647_; 
v_res_1647_ = lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime___aux__Zeta23__FromPNTPlus__Tactic__AdditiveCombination______elabRules__Mathlib__Tactic__LinearCombinationPrime__AdditiveCombination__1(v_x_1637_, v_a_1638_, v_a_1639_, v_a_1640_, v_a_1641_, v_a_1642_, v_a_1643_, v_a_1644_, v_a_1645_);
lean_dec(v_a_1645_);
lean_dec_ref(v_a_1644_);
lean_dec(v_a_1643_);
lean_dec_ref(v_a_1642_);
lean_dec(v_a_1641_);
lean_dec_ref(v_a_1640_);
lean_dec(v_a_1639_);
lean_dec_ref(v_a_1638_);
return v_res_1647_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Abel(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_LinearCombinationPrime(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Tactic_AdditiveCombination(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Abel(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_LinearCombinationPrime(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination = _init_lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination();
lean_mark_persistent(lp_Zeta23_Mathlib_Tactic_LinearCombinationPrime_AdditiveCombination);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
