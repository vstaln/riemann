// Lean compiler output
// Module: Zeta23.PairCeiling.NumericCert
// Imports: public import Init public meta import Init public import Mathlib.Analysis.SpecialFunctions.Pow.Real public import Mathlib.Algebra.Order.Floor.Defs public import Mathlib.Algebra.BigOperators.Intervals
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
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
lean_object* lp_mathlib_Multiset_map___redArg(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_object* l_List_foldrTR___redArg(lean_object*, lean_object*, lean_object*);
lean_object* lean_nat_to_int(lean_object*);
lean_object* lean_int_add(lean_object*, lean_object*);
uint8_t lean_int_dec_le(lean_object*, lean_object*);
lean_object* lean_int_mul(lean_object*, lean_object*);
lean_object* l_Int_pow(lean_object*, lean_object*);
lean_object* lean_int_sub(lean_object*, lean_object*);
lean_object* lean_int_neg(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T___lam__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T___lam__0___boxed(lean_object*, lean_object*);
static const lean_closure_object lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_, .m_arity = 3, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0___closed__0 = (const lean_object*)&lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0___closed__0_value;
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_U___lam__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_U(lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0;
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_St_init;
LEAN_EXPORT lean_object* lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_step___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_step___closed__0;
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_step___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_step___closed__1;
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_step___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_step___closed__2;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_step(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_step___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_run(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_run___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_check(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_check___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T___lam__0(lean_object* v_S_1_, lean_object* v_i_2_){
_start:
{
lean_object* v___x_3_; lean_object* v___x_4_; lean_object* v___x_5_; 
v___x_3_ = lean_unsigned_to_nat(1u);
v___x_4_ = lean_nat_add(v_i_2_, v___x_3_);
v___x_5_ = lean_apply_1(v_S_1_, v___x_4_);
return v___x_5_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T___lam__0___boxed(lean_object* v_S_6_, lean_object* v_i_7_){
_start:
{
lean_object* v_res_8_; 
v_res_8_ = lp_Zeta23_Zeta23_PairCeiling_T___lam__0(v_S_6_, v_i_7_);
lean_dec(v_i_7_);
return v_res_8_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0(lean_object* v_s_10_){
_start:
{
lean_object* v___f_11_; lean_object* v___x_12_; lean_object* v___x_13_; 
v___f_11_ = ((lean_object*)(lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0___closed__0));
v___x_12_ = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
v___x_13_ = l_List_foldrTR___redArg(v___f_11_, v___x_12_, v_s_10_);
return v___x_13_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0___redArg(lean_object* v_s_14_, lean_object* v_f_15_){
_start:
{
lean_object* v___x_16_; lean_object* v___x_17_; 
v___x_16_ = lp_mathlib_Multiset_map___redArg(v_f_15_, v_s_14_);
v___x_17_ = lp_Zeta23_Multiset_sum___at___00Finset_sum___at___00Zeta23_PairCeiling_T_spec__0_spec__0(v___x_16_);
return v___x_17_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_T(lean_object* v_S_18_, lean_object* v_j_19_){
_start:
{
lean_object* v___f_20_; lean_object* v___x_21_; lean_object* v___x_22_; 
v___f_20_ = lean_alloc_closure((void*)(lp_Zeta23_Zeta23_PairCeiling_T___lam__0___boxed), 2, 1);
lean_closure_set(v___f_20_, 0, v_S_18_);
v___x_21_ = l_List_range(v_j_19_);
v___x_22_ = lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0___redArg(v___x_21_, v___f_20_);
return v___x_22_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0(lean_object* v_00_u03b9_23_, lean_object* v_s_24_, lean_object* v_f_25_){
_start:
{
lean_object* v___x_26_; 
v___x_26_ = lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0___redArg(v_s_24_, v_f_25_);
return v___x_26_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_U___lam__0(lean_object* v_S_27_, lean_object* v_i_28_){
_start:
{
lean_object* v___x_29_; 
v___x_29_ = lp_Zeta23_Zeta23_PairCeiling_T(v_S_27_, v_i_28_);
return v___x_29_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_U(lean_object* v_S_30_, lean_object* v_j_31_){
_start:
{
lean_object* v___f_32_; lean_object* v___x_33_; lean_object* v___x_34_; 
v___f_32_ = lean_alloc_closure((void*)(lp_Zeta23_Zeta23_PairCeiling_U___lam__0), 2, 1);
lean_closure_set(v___f_32_, 0, v_S_30_);
v___x_33_ = l_List_range(v_j_31_);
v___x_34_ = lp_Zeta23_Finset_sum___at___00Zeta23_PairCeiling_T_spec__0___redArg(v___x_33_, v___f_32_);
return v___x_34_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0(void){
_start:
{
lean_object* v___x_35_; lean_object* v___x_36_; 
v___x_35_ = lean_unsigned_to_nat(0u);
v___x_36_ = lean_nat_to_int(v___x_35_);
return v___x_36_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1(void){
_start:
{
uint8_t v___x_37_; lean_object* v___x_38_; lean_object* v___x_39_; lean_object* v___x_40_; 
v___x_37_ = 1;
v___x_38_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0, &lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_St_init___closed__0);
v___x_39_ = lean_unsigned_to_nat(0u);
v___x_40_ = lean_alloc_ctor(0, 7, 1);
lean_ctor_set(v___x_40_, 0, v___x_39_);
lean_ctor_set(v___x_40_, 1, v___x_38_);
lean_ctor_set(v___x_40_, 2, v___x_38_);
lean_ctor_set(v___x_40_, 3, v___x_38_);
lean_ctor_set(v___x_40_, 4, v___x_38_);
lean_ctor_set(v___x_40_, 5, v___x_38_);
lean_ctor_set(v___x_40_, 6, v___x_38_);
lean_ctor_set_uint8(v___x_40_, sizeof(void*)*7, v___x_37_);
return v___x_40_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_St_init(void){
_start:
{
lean_object* v___x_41_; 
v___x_41_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1, &lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1_once, _init_lp_Zeta23_Zeta23_PairCeiling_St_init___closed__1);
return v___x_41_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(lean_object* v_a_42_){
_start:
{
lean_object* v___x_43_; uint8_t v___x_44_; 
v___x_43_ = lean_int_neg(v_a_42_);
v___x_44_ = lean_int_dec_le(v_a_42_, v___x_43_);
if (v___x_44_ == 0)
{
lean_dec(v___x_43_);
lean_inc(v_a_42_);
return v_a_42_;
}
else
{
return v___x_43_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0___boxed(lean_object* v_a_45_){
_start:
{
lean_object* v_res_46_; 
v_res_46_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v_a_45_);
lean_dec(v_a_45_);
return v_res_46_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__0(void){
_start:
{
lean_object* v___x_47_; lean_object* v___x_48_; 
v___x_47_ = lean_unsigned_to_nat(2u);
v___x_48_ = lean_nat_to_int(v___x_47_);
return v___x_48_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__1(void){
_start:
{
lean_object* v___x_49_; lean_object* v___x_50_; 
v___x_49_ = lean_unsigned_to_nat(1u);
v___x_50_ = lean_nat_to_int(v___x_49_);
return v___x_50_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__2(void){
_start:
{
lean_object* v___x_51_; lean_object* v___x_52_; 
v___x_51_ = lean_unsigned_to_nat(6u);
v___x_52_ = lean_nat_to_int(v___x_51_);
return v___x_52_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_step(lean_object* v_N_53_, lean_object* v_K_54_, lean_object* v_s_55_, lean_object* v_e_56_){
_start:
{
lean_object* v_j_57_; lean_object* v_Tlo_58_; lean_object* v_Thi_59_; lean_object* v_Ulo_60_; lean_object* v_Uhi_61_; lean_object* v_M1_62_; lean_object* v_M2_63_; uint8_t v_ok_64_; lean_object* v___x_66_; uint8_t v_isShared_67_; uint8_t v_isSharedCheck_137_; 
v_j_57_ = lean_ctor_get(v_s_55_, 0);
v_Tlo_58_ = lean_ctor_get(v_s_55_, 1);
v_Thi_59_ = lean_ctor_get(v_s_55_, 2);
v_Ulo_60_ = lean_ctor_get(v_s_55_, 3);
v_Uhi_61_ = lean_ctor_get(v_s_55_, 4);
v_M1_62_ = lean_ctor_get(v_s_55_, 5);
v_M2_63_ = lean_ctor_get(v_s_55_, 6);
v_ok_64_ = lean_ctor_get_uint8(v_s_55_, sizeof(void*)*7);
v_isSharedCheck_137_ = !lean_is_exclusive(v_s_55_);
if (v_isSharedCheck_137_ == 0)
{
v___x_66_ = v_s_55_;
v_isShared_67_ = v_isSharedCheck_137_;
goto v_resetjp_65_;
}
else
{
lean_inc(v_M2_63_);
lean_inc(v_M1_62_);
lean_inc(v_Uhi_61_);
lean_inc(v_Ulo_60_);
lean_inc(v_Thi_59_);
lean_inc(v_Tlo_58_);
lean_inc(v_j_57_);
lean_dec(v_s_55_);
v___x_66_ = lean_box(0);
v_isShared_67_ = v_isSharedCheck_137_;
goto v_resetjp_65_;
}
v_resetjp_65_:
{
lean_object* v_fst_68_; lean_object* v_snd_69_; lean_object* v___x_70_; lean_object* v___x_71_; lean_object* v___x_72_; lean_object* v___x_73_; lean_object* v___x_74_; lean_object* v___x_75_; lean_object* v___y_77_; lean_object* v___y_78_; lean_object* v___y_87_; lean_object* v___y_88_; lean_object* v___x_90_; lean_object* v___x_91_; lean_object* v___x_92_; lean_object* v___x_93_; lean_object* v___x_94_; lean_object* v___x_95_; lean_object* v___x_96_; lean_object* v___x_97_; lean_object* v___x_98_; lean_object* v___x_99_; lean_object* v___y_101_; lean_object* v___y_115_; lean_object* v___y_118_; lean_object* v___y_119_; lean_object* v___x_121_; lean_object* v___y_123_; lean_object* v___x_131_; lean_object* v___x_132_; lean_object* v___x_133_; lean_object* v___x_134_; lean_object* v___x_135_; uint8_t v___x_136_; 
v_fst_68_ = lean_ctor_get(v_e_56_, 0);
v_snd_69_ = lean_ctor_get(v_e_56_, 1);
v___x_70_ = lean_unsigned_to_nat(1u);
v___x_71_ = lean_nat_add(v_j_57_, v___x_70_);
v___x_72_ = lean_int_add(v_Tlo_58_, v_fst_68_);
v___x_73_ = lean_int_add(v_Thi_59_, v_snd_69_);
v___x_74_ = lean_int_add(v_Ulo_60_, v_Tlo_58_);
lean_dec(v_Ulo_60_);
v___x_75_ = lean_int_add(v_Uhi_61_, v_Thi_59_);
lean_dec(v_Uhi_61_);
v___x_90_ = lean_unsigned_to_nat(2u);
v___x_91_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_step___closed__0, &lp_Zeta23_Zeta23_PairCeiling_step___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__0);
v___x_92_ = lean_nat_to_int(v_N_53_);
v___x_93_ = lean_int_mul(v___x_91_, v___x_92_);
v___x_94_ = lean_int_mul(v___x_93_, v_Tlo_58_);
lean_dec(v_Tlo_58_);
v___x_95_ = lean_nat_to_int(v_j_57_);
v___x_96_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_step___closed__1, &lp_Zeta23_Zeta23_PairCeiling_step___closed__1_once, _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__1);
v___x_97_ = lean_int_add(v___x_95_, v___x_96_);
lean_dec(v___x_95_);
v___x_98_ = l_Int_pow(v___x_97_, v___x_90_);
v___x_99_ = lean_nat_to_int(v_K_54_);
v___x_121_ = lean_int_mul(v___x_98_, v___x_99_);
lean_dec(v___x_98_);
v___x_131_ = lean_int_sub(v___x_94_, v___x_121_);
lean_dec(v___x_94_);
v___x_132_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_131_);
lean_dec(v___x_131_);
v___x_133_ = lean_int_mul(v___x_93_, v_Thi_59_);
lean_dec(v_Thi_59_);
v___x_134_ = lean_int_sub(v___x_133_, v___x_121_);
lean_dec(v___x_133_);
v___x_135_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_134_);
lean_dec(v___x_134_);
v___x_136_ = lean_int_dec_le(v___x_132_, v___x_135_);
if (v___x_136_ == 0)
{
lean_dec(v___x_135_);
v___y_123_ = v___x_132_;
goto v___jp_122_;
}
else
{
lean_dec(v___x_132_);
v___y_123_ = v___x_135_;
goto v___jp_122_;
}
v___jp_76_:
{
if (v_ok_64_ == 0)
{
lean_object* v___x_80_; 
if (v_isShared_67_ == 0)
{
lean_ctor_set(v___x_66_, 6, v___y_78_);
lean_ctor_set(v___x_66_, 5, v___y_77_);
lean_ctor_set(v___x_66_, 4, v___x_75_);
lean_ctor_set(v___x_66_, 3, v___x_74_);
lean_ctor_set(v___x_66_, 2, v___x_73_);
lean_ctor_set(v___x_66_, 1, v___x_72_);
lean_ctor_set(v___x_66_, 0, v___x_71_);
v___x_80_ = v___x_66_;
goto v_reusejp_79_;
}
else
{
lean_object* v_reuseFailAlloc_81_; 
v_reuseFailAlloc_81_ = lean_alloc_ctor(0, 7, 1);
lean_ctor_set(v_reuseFailAlloc_81_, 0, v___x_71_);
lean_ctor_set(v_reuseFailAlloc_81_, 1, v___x_72_);
lean_ctor_set(v_reuseFailAlloc_81_, 2, v___x_73_);
lean_ctor_set(v_reuseFailAlloc_81_, 3, v___x_74_);
lean_ctor_set(v_reuseFailAlloc_81_, 4, v___x_75_);
lean_ctor_set(v_reuseFailAlloc_81_, 5, v___y_77_);
lean_ctor_set(v_reuseFailAlloc_81_, 6, v___y_78_);
lean_ctor_set_uint8(v_reuseFailAlloc_81_, sizeof(void*)*7, v_ok_64_);
v___x_80_ = v_reuseFailAlloc_81_;
goto v_reusejp_79_;
}
v_reusejp_79_:
{
return v___x_80_;
}
}
else
{
uint8_t v___x_82_; lean_object* v___x_84_; 
v___x_82_ = lean_int_dec_le(v_fst_68_, v_snd_69_);
if (v_isShared_67_ == 0)
{
lean_ctor_set(v___x_66_, 6, v___y_78_);
lean_ctor_set(v___x_66_, 5, v___y_77_);
lean_ctor_set(v___x_66_, 4, v___x_75_);
lean_ctor_set(v___x_66_, 3, v___x_74_);
lean_ctor_set(v___x_66_, 2, v___x_73_);
lean_ctor_set(v___x_66_, 1, v___x_72_);
lean_ctor_set(v___x_66_, 0, v___x_71_);
v___x_84_ = v___x_66_;
goto v_reusejp_83_;
}
else
{
lean_object* v_reuseFailAlloc_85_; 
v_reuseFailAlloc_85_ = lean_alloc_ctor(0, 7, 1);
lean_ctor_set(v_reuseFailAlloc_85_, 0, v___x_71_);
lean_ctor_set(v_reuseFailAlloc_85_, 1, v___x_72_);
lean_ctor_set(v_reuseFailAlloc_85_, 2, v___x_73_);
lean_ctor_set(v_reuseFailAlloc_85_, 3, v___x_74_);
lean_ctor_set(v_reuseFailAlloc_85_, 4, v___x_75_);
lean_ctor_set(v_reuseFailAlloc_85_, 5, v___y_77_);
lean_ctor_set(v_reuseFailAlloc_85_, 6, v___y_78_);
v___x_84_ = v_reuseFailAlloc_85_;
goto v_reusejp_83_;
}
v_reusejp_83_:
{
lean_ctor_set_uint8(v___x_84_, sizeof(void*)*7, v___x_82_);
return v___x_84_;
}
}
}
v___jp_86_:
{
uint8_t v___x_89_; 
v___x_89_ = lean_int_dec_le(v_M2_63_, v___y_88_);
if (v___x_89_ == 0)
{
lean_dec(v___y_88_);
v___y_77_ = v___y_87_;
v___y_78_ = v_M2_63_;
goto v___jp_76_;
}
else
{
lean_dec(v_M2_63_);
v___y_77_ = v___y_87_;
v___y_78_ = v___y_88_;
goto v___jp_76_;
}
}
v___jp_100_:
{
lean_object* v___x_102_; lean_object* v___x_103_; lean_object* v___x_104_; lean_object* v___x_105_; lean_object* v___x_106_; lean_object* v___x_107_; lean_object* v___x_108_; lean_object* v___x_109_; lean_object* v___x_110_; lean_object* v___x_111_; lean_object* v___x_112_; uint8_t v___x_113_; 
v___x_102_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_step___closed__2, &lp_Zeta23_Zeta23_PairCeiling_step___closed__2_once, _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__2);
v___x_103_ = lean_int_mul(v___x_102_, v___x_92_);
lean_dec(v___x_92_);
v___x_104_ = lean_int_mul(v___x_103_, v___x_74_);
v___x_105_ = lean_unsigned_to_nat(3u);
v___x_106_ = l_Int_pow(v___x_97_, v___x_105_);
lean_dec(v___x_97_);
v___x_107_ = lean_int_mul(v___x_106_, v___x_99_);
lean_dec(v___x_99_);
lean_dec(v___x_106_);
v___x_108_ = lean_int_sub(v___x_104_, v___x_107_);
lean_dec(v___x_104_);
v___x_109_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_108_);
lean_dec(v___x_108_);
v___x_110_ = lean_int_mul(v___x_103_, v___x_75_);
lean_dec(v___x_103_);
v___x_111_ = lean_int_sub(v___x_110_, v___x_107_);
lean_dec(v___x_107_);
lean_dec(v___x_110_);
v___x_112_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_111_);
lean_dec(v___x_111_);
v___x_113_ = lean_int_dec_le(v___x_109_, v___x_112_);
if (v___x_113_ == 0)
{
lean_dec(v___x_112_);
v___y_87_ = v___y_101_;
v___y_88_ = v___x_109_;
goto v___jp_86_;
}
else
{
lean_dec(v___x_109_);
v___y_87_ = v___y_101_;
v___y_88_ = v___x_112_;
goto v___jp_86_;
}
}
v___jp_114_:
{
uint8_t v___x_116_; 
v___x_116_ = lean_int_dec_le(v_M1_62_, v___y_115_);
if (v___x_116_ == 0)
{
lean_dec(v___y_115_);
v___y_101_ = v_M1_62_;
goto v___jp_100_;
}
else
{
lean_dec(v_M1_62_);
v___y_101_ = v___y_115_;
goto v___jp_100_;
}
}
v___jp_117_:
{
uint8_t v___x_120_; 
v___x_120_ = lean_int_dec_le(v___y_118_, v___y_119_);
if (v___x_120_ == 0)
{
lean_dec(v___y_119_);
v___y_115_ = v___y_118_;
goto v___jp_114_;
}
else
{
lean_dec(v___y_118_);
v___y_115_ = v___y_119_;
goto v___jp_114_;
}
}
v___jp_122_:
{
lean_object* v___x_124_; lean_object* v___x_125_; lean_object* v___x_126_; lean_object* v___x_127_; lean_object* v___x_128_; lean_object* v___x_129_; uint8_t v___x_130_; 
v___x_124_ = lean_int_mul(v___x_93_, v___x_72_);
v___x_125_ = lean_int_sub(v___x_124_, v___x_121_);
lean_dec(v___x_124_);
v___x_126_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_125_);
lean_dec(v___x_125_);
v___x_127_ = lean_int_mul(v___x_93_, v___x_73_);
lean_dec(v___x_93_);
v___x_128_ = lean_int_sub(v___x_127_, v___x_121_);
lean_dec(v___x_121_);
lean_dec(v___x_127_);
v___x_129_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_128_);
lean_dec(v___x_128_);
v___x_130_ = lean_int_dec_le(v___x_126_, v___x_129_);
if (v___x_130_ == 0)
{
lean_dec(v___x_129_);
v___y_118_ = v___y_123_;
v___y_119_ = v___x_126_;
goto v___jp_117_;
}
else
{
lean_dec(v___x_126_);
v___y_118_ = v___y_123_;
v___y_119_ = v___x_129_;
goto v___jp_117_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_step___boxed(lean_object* v_N_138_, lean_object* v_K_139_, lean_object* v_s_140_, lean_object* v_e_141_){
_start:
{
lean_object* v_res_142_; 
v_res_142_ = lp_Zeta23_Zeta23_PairCeiling_step(v_N_138_, v_K_139_, v_s_140_, v_e_141_);
lean_dec_ref(v_e_141_);
return v_res_142_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0(lean_object* v_N_143_, lean_object* v_K_144_, lean_object* v_x_145_, lean_object* v_x_146_){
_start:
{
if (lean_obj_tag(v_x_146_) == 0)
{
lean_dec(v_K_144_);
lean_dec(v_N_143_);
return v_x_145_;
}
else
{
lean_object* v_head_147_; lean_object* v_tail_148_; lean_object* v___x_149_; 
v_head_147_ = lean_ctor_get(v_x_146_, 0);
v_tail_148_ = lean_ctor_get(v_x_146_, 1);
lean_inc(v_K_144_);
lean_inc(v_N_143_);
v___x_149_ = lp_Zeta23_Zeta23_PairCeiling_step(v_N_143_, v_K_144_, v_x_145_, v_head_147_);
v_x_145_ = v___x_149_;
v_x_146_ = v_tail_148_;
goto _start;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0___boxed(lean_object* v_N_151_, lean_object* v_K_152_, lean_object* v_x_153_, lean_object* v_x_154_){
_start:
{
lean_object* v_res_155_; 
v_res_155_ = lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0(v_N_151_, v_K_152_, v_x_153_, v_x_154_);
lean_dec(v_x_154_);
return v_res_155_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_run(lean_object* v_N_156_, lean_object* v_K_157_, lean_object* v_l_158_, lean_object* v_s_159_){
_start:
{
lean_object* v___x_160_; 
v___x_160_ = lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0(v_N_156_, v_K_157_, v_s_159_, v_l_158_);
return v___x_160_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_run___boxed(lean_object* v_N_161_, lean_object* v_K_162_, lean_object* v_l_163_, lean_object* v_s_164_){
_start:
{
lean_object* v_res_165_; 
v_res_165_ = lp_Zeta23_Zeta23_PairCeiling_run(v_N_161_, v_K_162_, v_l_163_, v_s_164_);
lean_dec(v_l_163_);
return v_res_165_;
}
}
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_check(lean_object* v_d_166_){
_start:
{
lean_object* v_N_167_; lean_object* v_K_168_; lean_object* v_encl_169_; lean_object* v_bD1n_170_; lean_object* v_bD1d_171_; lean_object* v_bE1n_172_; lean_object* v_bE1d_173_; lean_object* v_b1n_174_; lean_object* v_b1d_175_; lean_object* v_b2n_176_; lean_object* v_b2d_177_; lean_object* v___x_178_; lean_object* v_s_179_; lean_object* v_j_180_; lean_object* v_Tlo_181_; lean_object* v_Thi_182_; lean_object* v_Ulo_183_; lean_object* v_Uhi_184_; lean_object* v_M1_185_; lean_object* v_M2_186_; uint8_t v_ok_187_; lean_object* v___x_188_; lean_object* v___x_189_; lean_object* v___x_190_; lean_object* v___x_191_; lean_object* v___x_192_; lean_object* v___x_193_; lean_object* v___x_194_; lean_object* v___y_196_; lean_object* v___y_197_; lean_object* v___y_198_; lean_object* v___y_199_; lean_object* v___y_200_; lean_object* v___y_237_; lean_object* v___x_250_; lean_object* v___x_251_; lean_object* v___x_252_; lean_object* v___x_253_; lean_object* v___x_254_; lean_object* v___x_255_; uint8_t v___x_256_; 
v_N_167_ = lean_ctor_get(v_d_166_, 0);
lean_inc_n(v_N_167_, 3);
v_K_168_ = lean_ctor_get(v_d_166_, 1);
lean_inc_n(v_K_168_, 3);
v_encl_169_ = lean_ctor_get(v_d_166_, 2);
lean_inc(v_encl_169_);
v_bD1n_170_ = lean_ctor_get(v_d_166_, 3);
lean_inc(v_bD1n_170_);
v_bD1d_171_ = lean_ctor_get(v_d_166_, 4);
lean_inc(v_bD1d_171_);
v_bE1n_172_ = lean_ctor_get(v_d_166_, 5);
lean_inc(v_bE1n_172_);
v_bE1d_173_ = lean_ctor_get(v_d_166_, 6);
lean_inc(v_bE1d_173_);
v_b1n_174_ = lean_ctor_get(v_d_166_, 7);
lean_inc(v_b1n_174_);
v_b1d_175_ = lean_ctor_get(v_d_166_, 8);
lean_inc(v_b1d_175_);
v_b2n_176_ = lean_ctor_get(v_d_166_, 9);
lean_inc(v_b2n_176_);
v_b2d_177_ = lean_ctor_get(v_d_166_, 10);
lean_inc(v_b2d_177_);
lean_dec_ref(v_d_166_);
v___x_178_ = lp_Zeta23_Zeta23_PairCeiling_St_init;
v_s_179_ = lp_Zeta23_List_foldl___at___00Zeta23_PairCeiling_run_spec__0(v_N_167_, v_K_168_, v___x_178_, v_encl_169_);
lean_dec(v_encl_169_);
v_j_180_ = lean_ctor_get(v_s_179_, 0);
lean_inc(v_j_180_);
v_Tlo_181_ = lean_ctor_get(v_s_179_, 1);
lean_inc(v_Tlo_181_);
v_Thi_182_ = lean_ctor_get(v_s_179_, 2);
lean_inc(v_Thi_182_);
v_Ulo_183_ = lean_ctor_get(v_s_179_, 3);
lean_inc(v_Ulo_183_);
v_Uhi_184_ = lean_ctor_get(v_s_179_, 4);
lean_inc(v_Uhi_184_);
v_M1_185_ = lean_ctor_get(v_s_179_, 5);
lean_inc(v_M1_185_);
v_M2_186_ = lean_ctor_get(v_s_179_, 6);
lean_inc(v_M2_186_);
v_ok_187_ = lean_ctor_get_uint8(v_s_179_, sizeof(void*)*7);
lean_dec_ref(v_s_179_);
v___x_188_ = lean_unsigned_to_nat(2u);
v___x_189_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_step___closed__0, &lp_Zeta23_Zeta23_PairCeiling_step___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__0);
v___x_190_ = lean_nat_to_int(v_N_167_);
v___x_191_ = lean_int_mul(v___x_189_, v___x_190_);
v___x_192_ = lean_int_mul(v___x_191_, v_Tlo_181_);
lean_dec(v_Tlo_181_);
v___x_193_ = l_Int_pow(v___x_190_, v___x_188_);
v___x_194_ = lean_nat_to_int(v_K_168_);
v___x_250_ = lean_int_mul(v___x_193_, v___x_194_);
v___x_251_ = lean_int_sub(v___x_192_, v___x_250_);
lean_dec(v___x_192_);
v___x_252_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_251_);
lean_dec(v___x_251_);
v___x_253_ = lean_int_mul(v___x_191_, v_Thi_182_);
lean_dec(v_Thi_182_);
lean_dec(v___x_191_);
v___x_254_ = lean_int_sub(v___x_253_, v___x_250_);
lean_dec(v___x_250_);
lean_dec(v___x_253_);
v___x_255_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_254_);
lean_dec(v___x_254_);
v___x_256_ = lean_int_dec_le(v___x_252_, v___x_255_);
if (v___x_256_ == 0)
{
lean_dec(v___x_255_);
v___y_237_ = v___x_252_;
goto v___jp_236_;
}
else
{
lean_dec(v___x_252_);
v___y_237_ = v___x_255_;
goto v___jp_236_;
}
v___jp_195_:
{
if (v_ok_187_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_j_180_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
lean_dec(v_K_168_);
lean_dec(v_N_167_);
return v_ok_187_;
}
else
{
uint8_t v___x_201_; 
v___x_201_ = lean_nat_dec_eq(v_j_180_, v_N_167_);
lean_dec(v_j_180_);
if (v___x_201_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
lean_dec(v_K_168_);
lean_dec(v_N_167_);
return v___x_201_;
}
else
{
lean_object* v___x_202_; uint8_t v___x_203_; 
v___x_202_ = lean_unsigned_to_nat(0u);
v___x_203_ = lean_nat_dec_lt(v___x_202_, v_N_167_);
lean_dec(v_N_167_);
if (v___x_203_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
lean_dec(v_K_168_);
return v___x_203_;
}
else
{
uint8_t v___x_204_; 
v___x_204_ = lean_nat_dec_lt(v___x_202_, v_K_168_);
lean_dec(v_K_168_);
if (v___x_204_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
return v___x_204_;
}
else
{
uint8_t v___x_205_; 
v___x_205_ = lean_nat_dec_lt(v___x_202_, v_bD1d_171_);
if (v___x_205_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
return v___x_205_;
}
else
{
uint8_t v___x_206_; 
v___x_206_ = lean_nat_dec_lt(v___x_202_, v_bE1d_173_);
if (v___x_206_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
return v___x_206_;
}
else
{
uint8_t v___x_207_; 
v___x_207_ = lean_nat_dec_lt(v___x_202_, v_b1d_175_);
if (v___x_207_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
return v___x_207_;
}
else
{
uint8_t v___x_208_; 
v___x_208_ = lean_nat_dec_lt(v___x_202_, v_b2d_177_);
if (v___x_208_ == 0)
{
lean_dec(v___y_200_);
lean_dec(v___y_199_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v___x_193_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
lean_dec(v_bD1d_171_);
lean_dec(v_bD1n_170_);
return v___x_208_;
}
else
{
lean_object* v___x_209_; lean_object* v___x_210_; lean_object* v___x_211_; lean_object* v___x_212_; lean_object* v___x_213_; lean_object* v___x_214_; uint8_t v___x_215_; 
v___x_209_ = lean_nat_to_int(v_bD1d_171_);
v___x_210_ = lean_int_mul(v___y_199_, v___x_209_);
lean_dec(v___x_209_);
lean_dec(v___y_199_);
v___x_211_ = lean_nat_to_int(v_bD1n_170_);
v___x_212_ = lean_int_mul(v___x_189_, v___x_193_);
lean_dec(v___x_193_);
v___x_213_ = lean_int_mul(v___x_212_, v___x_194_);
lean_dec(v___x_212_);
v___x_214_ = lean_int_mul(v___x_211_, v___x_213_);
lean_dec(v___x_211_);
v___x_215_ = lean_int_dec_le(v___x_210_, v___x_214_);
lean_dec(v___x_214_);
lean_dec(v___x_210_);
if (v___x_215_ == 0)
{
lean_dec(v___x_213_);
lean_dec(v___y_200_);
lean_dec(v___y_198_);
lean_dec(v___y_197_);
lean_dec(v___x_194_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
lean_dec(v_bE1d_173_);
lean_dec(v_bE1n_172_);
return v___x_215_;
}
else
{
lean_object* v___x_216_; lean_object* v___x_217_; lean_object* v___x_218_; lean_object* v___x_219_; lean_object* v___x_220_; lean_object* v___x_221_; uint8_t v___x_222_; 
v___x_216_ = lean_nat_to_int(v_bE1d_173_);
v___x_217_ = lean_int_mul(v___y_200_, v___x_216_);
lean_dec(v___x_216_);
lean_dec(v___y_200_);
v___x_218_ = lean_nat_to_int(v_bE1n_172_);
v___x_219_ = lean_int_mul(v___y_196_, v___y_197_);
lean_dec(v___y_197_);
v___x_220_ = lean_int_mul(v___x_219_, v___x_194_);
lean_dec(v___x_194_);
lean_dec(v___x_219_);
v___x_221_ = lean_int_mul(v___x_218_, v___x_220_);
lean_dec(v___x_218_);
v___x_222_ = lean_int_dec_le(v___x_217_, v___x_221_);
lean_dec(v___x_221_);
lean_dec(v___x_217_);
if (v___x_222_ == 0)
{
lean_dec(v___x_220_);
lean_dec(v___x_213_);
lean_dec(v___y_198_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
lean_dec(v_b1d_175_);
lean_dec(v_b1n_174_);
return v___x_222_;
}
else
{
lean_object* v___x_223_; lean_object* v___x_224_; lean_object* v___x_225_; lean_object* v___x_226_; uint8_t v___x_227_; 
v___x_223_ = lean_nat_to_int(v_b1d_175_);
v___x_224_ = lean_int_mul(v_M1_185_, v___x_223_);
lean_dec(v___x_223_);
v___x_225_ = lean_nat_to_int(v_b1n_174_);
v___x_226_ = lean_int_mul(v___x_225_, v___x_213_);
lean_dec(v___x_213_);
lean_dec(v___x_225_);
v___x_227_ = lean_int_dec_le(v___x_224_, v___x_226_);
lean_dec(v___x_226_);
lean_dec(v___x_224_);
if (v___x_227_ == 0)
{
lean_dec(v___x_220_);
lean_dec(v___y_198_);
lean_dec(v_M2_186_);
lean_dec(v_M1_185_);
lean_dec(v_b2d_177_);
lean_dec(v_b2n_176_);
return v___x_227_;
}
else
{
lean_object* v___x_228_; lean_object* v___x_229_; lean_object* v___x_230_; lean_object* v___x_231_; lean_object* v___x_232_; lean_object* v___x_233_; lean_object* v___x_234_; uint8_t v___x_235_; 
v___x_228_ = lean_nat_to_int(v___y_198_);
v___x_229_ = lean_int_mul(v___x_228_, v_M1_185_);
lean_dec(v_M1_185_);
lean_dec(v___x_228_);
v___x_230_ = lean_int_add(v_M2_186_, v___x_229_);
lean_dec(v___x_229_);
lean_dec(v_M2_186_);
v___x_231_ = lean_nat_to_int(v_b2d_177_);
v___x_232_ = lean_int_mul(v___x_230_, v___x_231_);
lean_dec(v___x_231_);
lean_dec(v___x_230_);
v___x_233_ = lean_nat_to_int(v_b2n_176_);
v___x_234_ = lean_int_mul(v___x_233_, v___x_220_);
lean_dec(v___x_220_);
lean_dec(v___x_233_);
v___x_235_ = lean_int_dec_le(v___x_232_, v___x_234_);
lean_dec(v___x_234_);
lean_dec(v___x_232_);
return v___x_235_;
}
}
}
}
}
}
}
}
}
}
}
}
v___jp_236_:
{
lean_object* v___x_238_; lean_object* v___x_239_; lean_object* v___x_240_; lean_object* v___x_241_; lean_object* v___x_242_; lean_object* v___x_243_; lean_object* v___x_244_; lean_object* v___x_245_; lean_object* v___x_246_; lean_object* v___x_247_; lean_object* v___x_248_; uint8_t v___x_249_; 
v___x_238_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_step___closed__2, &lp_Zeta23_Zeta23_PairCeiling_step___closed__2_once, _init_lp_Zeta23_Zeta23_PairCeiling_step___closed__2);
v___x_239_ = lean_int_mul(v___x_238_, v___x_190_);
v___x_240_ = lean_int_mul(v___x_239_, v_Ulo_183_);
lean_dec(v_Ulo_183_);
v___x_241_ = lean_unsigned_to_nat(3u);
v___x_242_ = l_Int_pow(v___x_190_, v___x_241_);
lean_dec(v___x_190_);
v___x_243_ = lean_int_mul(v___x_242_, v___x_194_);
v___x_244_ = lean_int_sub(v___x_240_, v___x_243_);
lean_dec(v___x_240_);
v___x_245_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_244_);
lean_dec(v___x_244_);
v___x_246_ = lean_int_mul(v___x_239_, v_Uhi_184_);
lean_dec(v_Uhi_184_);
lean_dec(v___x_239_);
v___x_247_ = lean_int_sub(v___x_246_, v___x_243_);
lean_dec(v___x_243_);
lean_dec(v___x_246_);
v___x_248_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_247_);
lean_dec(v___x_247_);
v___x_249_ = lean_int_dec_le(v___x_245_, v___x_248_);
if (v___x_249_ == 0)
{
lean_dec(v___x_248_);
v___y_196_ = v___x_238_;
v___y_197_ = v___x_242_;
v___y_198_ = v___x_241_;
v___y_199_ = v___y_237_;
v___y_200_ = v___x_245_;
goto v___jp_195_;
}
else
{
lean_dec(v___x_245_);
v___y_196_ = v___x_238_;
v___y_197_ = v___x_242_;
v___y_198_ = v___x_241_;
v___y_199_ = v___y_237_;
v___y_200_ = v___x_248_;
goto v___jp_195_;
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_check___boxed(lean_object* v_d_257_){
_start:
{
uint8_t v_res_258_; lean_object* v_r_259_; 
v_res_258_ = lp_Zeta23_Zeta23_PairCeiling_check(v_d_257_);
v_r_259_ = lean_box(v_res_258_);
return v_r_259_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Pow_Real(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_Order_Floor_Defs(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_BigOperators_Intervals(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PairCeiling_NumericCert(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Analysis_SpecialFunctions_Pow_Real(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_Order_Floor_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_BigOperators_Intervals(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_Zeta23_Zeta23_PairCeiling_St_init = _init_lp_Zeta23_Zeta23_PairCeiling_St_init();
lean_mark_persistent(lp_Zeta23_Zeta23_PairCeiling_St_init);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
