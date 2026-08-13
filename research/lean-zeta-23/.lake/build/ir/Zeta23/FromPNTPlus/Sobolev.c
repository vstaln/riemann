// Lean compiler output
// Module: Zeta23.FromPNTPlus.Sobolev
// Imports: public import Init public meta import Init public import Mathlib.Analysis.Calculus.Deriv.Support public import Mathlib.Analysis.Distribution.SchwartzSpace.Deriv public import Mathlib.Order.Filter.ZeroAndBoundedAtFilter
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
lean_object* lp_mathlib___private_Mathlib_Data_Real_Basic_0__Real_mul(lean_object*, lean_object*);
lean_object* l_instSMulOfMul___redArg___lam__0(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
lean_object* lp_mathlib_Complex_mulAux___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_SubNegZeroMonoid_toNegZeroClass___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_CS_instCoeFunForallReal___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_CS_instCoeFunForallReal___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_CS_instCoeFunForallReal___closed__0 = (const lean_object*)&lp_Zeta23_CS_instCoeFunForallReal___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_CS_instCoeRealComplex___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_CS_instCoeRealComplex___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_CS_instCoeRealComplex___closed__0 = (const lean_object*)&lp_Zeta23_CS_instCoeRealComplex___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instNeg___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instNeg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___redArg___lam__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instHSMulReal___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_CS_instHSMulReal(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_trunc_instCoeFunForallReal___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_trunc_instCoeFunForallReal___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_trunc_instCoeFunForallReal___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_trunc_instCoeFunForallReal___closed__0 = (const lean_object*)&lp_Zeta23_trunc_instCoeFunForallReal___closed__0_value;
LEAN_EXPORT const lean_object* lp_Zeta23_trunc_instCoeFunForallReal = (const lean_object*)&lp_Zeta23_trunc_instCoeFunForallReal___closed__0_value;
LEAN_EXPORT const lean_object* lp_Zeta23_trunc_instCoeCSOfNatNatReal = (const lean_object*)&lp_Zeta23_CS_instCoeFunForallReal___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_W1_instCoeFunForallReal(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_instCoeFunForallReal___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___redArg___lam__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_instSub___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W1_instSub(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W21_ofCS2(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_W21_ofCS2___boxed(lean_object*);
static const lean_closure_object lp_Zeta23_W21_instCoeCSOfNatNatComplex___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_W21_ofCS2___boxed, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_W21_instCoeCSOfNatNatComplex___closed__0 = (const lean_object*)&lp_Zeta23_W21_instCoeCSOfNatNatComplex___closed__0_value;
LEAN_EXPORT const lean_object* lp_Zeta23_W21_instCoeCSOfNatNatComplex = (const lean_object*)&lp_Zeta23_W21_instCoeCSOfNatNatComplex___closed__0_value;
static const lean_closure_object lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_mathlib___private_Mathlib_Data_Real_Basic_0__Real_mul, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__0 = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__0_value;
static const lean_closure_object lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*1, .m_other = 0, .m_tag = 245}, .m_fun = (void*)l_instSMulOfMul___redArg___lam__0, .m_arity = 3, .m_num_fixed = 1, .m_objs = {((lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__0_value)} };
static const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__1 = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__1_value;
LEAN_EXPORT lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0(lean_object*, lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_W21_instHMulCSOfNatNatComplex___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex___closed__0 = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatComplex___closed__0_value;
LEAN_EXPORT const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatComplex___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___lam__0(lean_object*, lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___lam__0, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___closed__0 = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___closed__0_value;
LEAN_EXPORT const lean_object* lp_Zeta23_W21_instHMulCSOfNatNatRealComplex = (const lean_object*)&lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal___lam__0(lean_object* v_self_1_, lean_object* v___y_2_){
_start:
{
lean_object* v___x_3_; 
v___x_3_ = lean_apply_1(v_self_1_, v___y_2_);
return v___x_3_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal(lean_object* v_E_5_, lean_object* v_inst_6_, lean_object* v_inst_7_, lean_object* v_n_8_){
_start:
{
lean_object* v___f_9_; 
v___f_9_ = ((lean_object*)(lp_Zeta23_CS_instCoeFunForallReal___closed__0));
return v___f_9_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeFunForallReal___boxed(lean_object* v_E_10_, lean_object* v_inst_11_, lean_object* v_inst_12_, lean_object* v_n_13_){
_start:
{
lean_object* v_res_14_; 
v_res_14_ = lp_Zeta23_CS_instCoeFunForallReal(v_E_10_, v_inst_11_, v_inst_12_, v_n_13_);
lean_dec(v_n_13_);
lean_dec(v_inst_12_);
lean_dec_ref(v_inst_11_);
return v_res_14_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex___lam__0(lean_object* v_f_15_, lean_object* v___y_16_){
_start:
{
lean_object* v___x_17_; lean_object* v___x_18_; 
v___x_17_ = lean_apply_1(v_f_15_, v___y_16_);
v___x_18_ = lp_mathlib_Complex_ofReal(v___x_17_);
return v___x_18_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex(lean_object* v_n_20_){
_start:
{
lean_object* v___f_21_; 
v___f_21_ = ((lean_object*)(lp_Zeta23_CS_instCoeRealComplex___closed__0));
return v___f_21_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instCoeRealComplex___boxed(lean_object* v_n_22_){
_start:
{
lean_object* v_res_23_; 
v_res_23_ = lp_Zeta23_CS_instCoeRealComplex(v_n_22_);
lean_dec(v_n_22_);
return v_res_23_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg___lam__0(lean_object* v_f_24_, lean_object* v_toNeg_25_, lean_object* v___y_26_){
_start:
{
lean_object* v___x_27_; lean_object* v___x_28_; 
v___x_27_ = lean_apply_1(v_f_24_, v___y_26_);
v___x_28_ = lean_apply_1(v_toNeg_25_, v___x_27_);
return v___x_28_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg(lean_object* v_inst_29_, lean_object* v_f_30_){
_start:
{
lean_object* v_toAddCommGroup_31_; lean_object* v___x_32_; lean_object* v_toNeg_33_; lean_object* v___f_34_; 
v_toAddCommGroup_31_ = lean_ctor_get(v_inst_29_, 1);
v___x_32_ = lp_mathlib_SubNegZeroMonoid_toNegZeroClass___redArg(v_toAddCommGroup_31_);
v_toNeg_33_ = lean_ctor_get(v___x_32_, 1);
lean_inc(v_toNeg_33_);
lean_dec_ref(v___x_32_);
v___f_34_ = lean_alloc_closure((void*)(lp_Zeta23_CS_neg___redArg___lam__0), 3, 2);
lean_closure_set(v___f_34_, 0, v_f_30_);
lean_closure_set(v___f_34_, 1, v_toNeg_33_);
return v___f_34_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___redArg___boxed(lean_object* v_inst_35_, lean_object* v_f_36_){
_start:
{
lean_object* v_res_37_; 
v_res_37_ = lp_Zeta23_CS_neg___redArg(v_inst_35_, v_f_36_);
lean_dec_ref(v_inst_35_);
return v_res_37_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg(lean_object* v_E_38_, lean_object* v_inst_39_, lean_object* v_inst_40_, lean_object* v_n_41_, lean_object* v_f_42_){
_start:
{
lean_object* v___x_43_; 
v___x_43_ = lp_Zeta23_CS_neg___redArg(v_inst_39_, v_f_42_);
return v___x_43_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_neg___boxed(lean_object* v_E_44_, lean_object* v_inst_45_, lean_object* v_inst_46_, lean_object* v_n_47_, lean_object* v_f_48_){
_start:
{
lean_object* v_res_49_; 
v_res_49_ = lp_Zeta23_CS_neg(v_E_44_, v_inst_45_, v_inst_46_, v_n_47_, v_f_48_);
lean_dec(v_n_47_);
lean_dec(v_inst_46_);
lean_dec_ref(v_inst_45_);
return v_res_49_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instNeg___redArg(lean_object* v_inst_50_, lean_object* v_inst_51_, lean_object* v_n_52_){
_start:
{
lean_object* v___x_53_; 
v___x_53_ = lean_alloc_closure((void*)(lp_Zeta23_CS_neg___boxed), 5, 4);
lean_closure_set(v___x_53_, 0, lean_box(0));
lean_closure_set(v___x_53_, 1, v_inst_50_);
lean_closure_set(v___x_53_, 2, v_inst_51_);
lean_closure_set(v___x_53_, 3, v_n_52_);
return v___x_53_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instNeg(lean_object* v_E_54_, lean_object* v_inst_55_, lean_object* v_inst_56_, lean_object* v_n_57_){
_start:
{
lean_object* v___x_58_; 
v___x_58_ = lean_alloc_closure((void*)(lp_Zeta23_CS_neg___boxed), 5, 4);
lean_closure_set(v___x_58_, 0, lean_box(0));
lean_closure_set(v___x_58_, 1, v_inst_55_);
lean_closure_set(v___x_58_, 2, v_inst_56_);
lean_closure_set(v___x_58_, 3, v_n_57_);
return v___x_58_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___redArg___lam__0(lean_object* v_f_59_, lean_object* v_inst_60_, lean_object* v_R_61_, lean_object* v___y_62_){
_start:
{
lean_object* v___x_63_; lean_object* v___x_64_; 
v___x_63_ = lean_apply_1(v_f_59_, v___y_62_);
v___x_64_ = lean_apply_2(v_inst_60_, v_R_61_, v___x_63_);
return v___x_64_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___redArg(lean_object* v_inst_65_, lean_object* v_R_66_, lean_object* v_f_67_){
_start:
{
lean_object* v___f_68_; 
v___f_68_ = lean_alloc_closure((void*)(lp_Zeta23_CS_smul___redArg___lam__0), 4, 3);
lean_closure_set(v___f_68_, 0, v_f_67_);
lean_closure_set(v___f_68_, 1, v_inst_65_);
lean_closure_set(v___f_68_, 2, v_R_66_);
return v___f_68_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul(lean_object* v_E_69_, lean_object* v_inst_70_, lean_object* v_inst_71_, lean_object* v_n_72_, lean_object* v_R_73_, lean_object* v_f_74_){
_start:
{
lean_object* v___f_75_; 
v___f_75_ = lean_alloc_closure((void*)(lp_Zeta23_CS_smul___redArg___lam__0), 4, 3);
lean_closure_set(v___f_75_, 0, v_f_74_);
lean_closure_set(v___f_75_, 1, v_inst_71_);
lean_closure_set(v___f_75_, 2, v_R_73_);
return v___f_75_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_smul___boxed(lean_object* v_E_76_, lean_object* v_inst_77_, lean_object* v_inst_78_, lean_object* v_n_79_, lean_object* v_R_80_, lean_object* v_f_81_){
_start:
{
lean_object* v_res_82_; 
v_res_82_ = lp_Zeta23_CS_smul(v_E_76_, v_inst_77_, v_inst_78_, v_n_79_, v_R_80_, v_f_81_);
lean_dec(v_n_79_);
lean_dec_ref(v_inst_77_);
return v_res_82_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instHSMulReal___redArg(lean_object* v_inst_83_, lean_object* v_inst_84_, lean_object* v_n_85_){
_start:
{
lean_object* v___x_86_; 
v___x_86_ = lean_alloc_closure((void*)(lp_Zeta23_CS_smul___boxed), 6, 4);
lean_closure_set(v___x_86_, 0, lean_box(0));
lean_closure_set(v___x_86_, 1, v_inst_83_);
lean_closure_set(v___x_86_, 2, v_inst_84_);
lean_closure_set(v___x_86_, 3, v_n_85_);
return v___x_86_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_CS_instHSMulReal(lean_object* v_E_87_, lean_object* v_inst_88_, lean_object* v_inst_89_, lean_object* v_n_90_){
_start:
{
lean_object* v___x_91_; 
v___x_91_ = lean_alloc_closure((void*)(lp_Zeta23_CS_smul___boxed), 6, 4);
lean_closure_set(v___x_91_, 0, lean_box(0));
lean_closure_set(v___x_91_, 1, v_inst_88_);
lean_closure_set(v___x_91_, 2, v_inst_89_);
lean_closure_set(v___x_91_, 3, v_n_90_);
return v___x_91_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_trunc_instCoeFunForallReal___lam__0(lean_object* v_f_92_, lean_object* v___y_93_){
_start:
{
lean_object* v___x_94_; 
v___x_94_ = lean_apply_1(v_f_92_, v___y_93_);
return v___x_94_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_instCoeFunForallReal(lean_object* v_E_98_, lean_object* v_inst_99_, lean_object* v_inst_100_, lean_object* v_n_101_){
_start:
{
lean_object* v___f_102_; 
v___f_102_ = ((lean_object*)(lp_Zeta23_CS_instCoeFunForallReal___closed__0));
return v___f_102_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_instCoeFunForallReal___boxed(lean_object* v_E_103_, lean_object* v_inst_104_, lean_object* v_inst_105_, lean_object* v_n_106_){
_start:
{
lean_object* v_res_107_; 
v_res_107_ = lp_Zeta23_W1_instCoeFunForallReal(v_E_103_, v_inst_104_, v_inst_105_, v_n_106_);
lean_dec(v_n_106_);
lean_dec(v_inst_105_);
lean_dec_ref(v_inst_104_);
return v_res_107_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___redArg___lam__0(lean_object* v_f_108_, lean_object* v_g_109_, lean_object* v_toSub_110_, lean_object* v___y_111_){
_start:
{
lean_object* v___x_112_; lean_object* v___x_113_; lean_object* v___x_114_; 
lean_inc(v___y_111_);
v___x_112_ = lean_apply_1(v_f_108_, v___y_111_);
v___x_113_ = lean_apply_1(v_g_109_, v___y_111_);
v___x_114_ = lean_apply_2(v_toSub_110_, v___x_112_, v___x_113_);
return v___x_114_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___redArg(lean_object* v_inst_115_, lean_object* v_f_116_, lean_object* v_g_117_){
_start:
{
lean_object* v_toAddCommGroup_118_; lean_object* v_toSub_119_; lean_object* v___f_120_; 
v_toAddCommGroup_118_ = lean_ctor_get(v_inst_115_, 1);
lean_inc_ref(v_toAddCommGroup_118_);
lean_dec_ref(v_inst_115_);
v_toSub_119_ = lean_ctor_get(v_toAddCommGroup_118_, 2);
lean_inc(v_toSub_119_);
lean_dec_ref(v_toAddCommGroup_118_);
v___f_120_ = lean_alloc_closure((void*)(lp_Zeta23_W1_sub___redArg___lam__0), 4, 3);
lean_closure_set(v___f_120_, 0, v_f_116_);
lean_closure_set(v___f_120_, 1, v_g_117_);
lean_closure_set(v___f_120_, 2, v_toSub_119_);
return v___f_120_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub(lean_object* v_E_121_, lean_object* v_inst_122_, lean_object* v_inst_123_, lean_object* v_n_124_, lean_object* v_f_125_, lean_object* v_g_126_){
_start:
{
lean_object* v___x_127_; 
v___x_127_ = lp_Zeta23_W1_sub___redArg(v_inst_122_, v_f_125_, v_g_126_);
return v___x_127_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_sub___boxed(lean_object* v_E_128_, lean_object* v_inst_129_, lean_object* v_inst_130_, lean_object* v_n_131_, lean_object* v_f_132_, lean_object* v_g_133_){
_start:
{
lean_object* v_res_134_; 
v_res_134_ = lp_Zeta23_W1_sub(v_E_128_, v_inst_129_, v_inst_130_, v_n_131_, v_f_132_, v_g_133_);
lean_dec(v_n_131_);
lean_dec(v_inst_130_);
return v_res_134_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_instSub___redArg(lean_object* v_inst_135_, lean_object* v_inst_136_, lean_object* v_n_137_){
_start:
{
lean_object* v___x_138_; 
v___x_138_ = lean_alloc_closure((void*)(lp_Zeta23_W1_sub___boxed), 6, 4);
lean_closure_set(v___x_138_, 0, lean_box(0));
lean_closure_set(v___x_138_, 1, v_inst_135_);
lean_closure_set(v___x_138_, 2, v_inst_136_);
lean_closure_set(v___x_138_, 3, v_n_137_);
return v___x_138_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W1_instSub(lean_object* v_E_139_, lean_object* v_inst_140_, lean_object* v_inst_141_, lean_object* v_n_142_){
_start:
{
lean_object* v___x_143_; 
v___x_143_ = lean_alloc_closure((void*)(lp_Zeta23_W1_sub___boxed), 6, 4);
lean_closure_set(v___x_143_, 0, lean_box(0));
lean_closure_set(v___x_143_, 1, v_inst_140_);
lean_closure_set(v___x_143_, 2, v_inst_141_);
lean_closure_set(v___x_143_, 3, v_n_142_);
return v___x_143_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W21_ofCS2(lean_object* v_f_144_){
_start:
{
lean_inc_ref(v_f_144_);
return v_f_144_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W21_ofCS2___boxed(lean_object* v_f_145_){
_start:
{
lean_object* v_res_146_; 
v_res_146_ = lp_Zeta23_W21_ofCS2(v_f_145_);
lean_dec_ref(v_f_145_);
return v_res_146_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0(lean_object* v_g_152_, lean_object* v_f_153_, lean_object* v___y_154_){
_start:
{
lean_object* v___x_155_; lean_object* v_re_156_; lean_object* v_im_157_; lean_object* v___x_158_; lean_object* v___f_159_; lean_object* v___x_160_; 
lean_inc(v___y_154_);
v___x_155_ = lean_apply_1(v_g_152_, v___y_154_);
v_re_156_ = lean_ctor_get(v___x_155_, 0);
lean_inc(v_re_156_);
v_im_157_ = lean_ctor_get(v___x_155_, 1);
lean_inc(v_im_157_);
lean_dec_ref(v___x_155_);
v___x_158_ = lean_apply_1(v_f_153_, v___y_154_);
v___f_159_ = ((lean_object*)(lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__1));
v___x_160_ = lp_mathlib_Complex_mulAux___redArg(v___f_159_, v_re_156_, v_im_157_, v___x_158_);
return v___x_160_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_W21_instHMulCSOfNatNatRealComplex___lam__0(lean_object* v_g_163_, lean_object* v_f_164_, lean_object* v___y_165_){
_start:
{
lean_object* v___x_166_; lean_object* v___x_167_; lean_object* v_re_168_; lean_object* v_im_169_; lean_object* v___x_170_; lean_object* v___f_171_; lean_object* v___x_172_; 
lean_inc(v___y_165_);
v___x_166_ = lean_apply_1(v_g_163_, v___y_165_);
v___x_167_ = lp_mathlib_Complex_ofReal(v___x_166_);
v_re_168_ = lean_ctor_get(v___x_167_, 0);
lean_inc(v_re_168_);
v_im_169_ = lean_ctor_get(v___x_167_, 1);
lean_inc(v_im_169_);
lean_dec_ref(v___x_167_);
v___x_170_ = lean_apply_1(v_f_164_, v___y_165_);
v___f_171_ = ((lean_object*)(lp_Zeta23_W21_instHMulCSOfNatNatComplex___lam__0___closed__1));
v___x_172_ = lp_mathlib_Complex_mulAux___redArg(v___f_171_, v_re_168_, v_im_169_, v___x_170_);
return v___x_172_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Calculus_Deriv_Support(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_Distribution_SchwartzSpace_Deriv(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Order_Filter_ZeroAndBoundedAtFilter(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_FromPNTPlus_Sobolev(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Calculus_Deriv_Support(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_Distribution_SchwartzSpace_Deriv(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Order_Filter_ZeroAndBoundedAtFilter(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
