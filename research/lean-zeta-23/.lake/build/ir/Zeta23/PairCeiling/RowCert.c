// Lean compiler output
// Module: Zeta23.PairCeiling.RowCert
// Imports: public import Init public meta import Init public import Zeta23.PairCeiling.NearCUE public import Zeta23.PairCeiling.NumericCert
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
lean_object* lean_nat_to_int(lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
lean_object* lean_int_mul(lean_object*, lean_object*);
lean_object* lean_int_add(lean_object*, lean_object*);
lean_object* lean_int_sub(lean_object*, lean_object*);
lean_object* lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(lean_object*);
uint8_t lean_int_dec_le(lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0;
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_rowsOK(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_rowsOK___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0;
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumHi(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumHi___boxed(lean_object*);
static lean_once_cell_t lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0;
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_checkRows(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_checkRows___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_rowsOK_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_rowsOK_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_sumLo_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_sumLo_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*);
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lean_unsigned_to_nat(1u);
v___x_2_ = lean_nat_to_int(v___x_1_);
return v___x_2_;
}
}
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_rowsOK(lean_object* v_N_3_, lean_object* v_K_4_, lean_object* v_tn_5_, lean_object* v_td_6_, lean_object* v_x_7_, lean_object* v_x_8_){
_start:
{
if (lean_obj_tag(v_x_8_) == 0)
{
uint8_t v___x_9_; 
lean_dec(v_x_7_);
lean_dec(v_td_6_);
lean_dec(v_tn_5_);
lean_dec(v_K_4_);
lean_dec(v_N_3_);
v___x_9_ = 1;
return v___x_9_;
}
else
{
lean_object* v_head_10_; lean_object* v_tail_11_; uint8_t v___y_13_; lean_object* v___x_17_; lean_object* v___x_18_; uint8_t v___x_19_; 
v_head_10_ = lean_ctor_get(v_x_8_, 0);
v_tail_11_ = lean_ctor_get(v_x_8_, 1);
v___x_17_ = lean_unsigned_to_nat(1u);
v___x_18_ = lean_nat_add(v_x_7_, v___x_17_);
v___x_19_ = lean_nat_dec_le(v_N_3_, v___x_18_);
lean_dec(v___x_18_);
if (v___x_19_ == 0)
{
lean_object* v_fst_20_; lean_object* v_snd_21_; lean_object* v___x_22_; lean_object* v___x_23_; lean_object* v___x_24_; lean_object* v___x_25_; lean_object* v___x_26_; lean_object* v___x_27_; lean_object* v___x_28_; lean_object* v___x_29_; lean_object* v___x_30_; lean_object* v___x_31_; lean_object* v___x_32_; lean_object* v___x_33_; lean_object* v___x_34_; uint8_t v___x_35_; 
v_fst_20_ = lean_ctor_get(v_head_10_, 0);
v_snd_21_ = lean_ctor_get(v_head_10_, 1);
lean_inc(v_N_3_);
v___x_22_ = lean_nat_to_int(v_N_3_);
v___x_23_ = lean_int_mul(v___x_22_, v_fst_20_);
lean_inc(v_x_7_);
v___x_24_ = lean_nat_to_int(v_x_7_);
v___x_25_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0, &lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_rowsOK___closed__0);
v___x_26_ = lean_int_add(v___x_24_, v___x_25_);
lean_dec(v___x_24_);
lean_inc(v_K_4_);
v___x_27_ = lean_nat_to_int(v_K_4_);
v___x_28_ = lean_int_mul(v___x_26_, v___x_27_);
lean_dec(v___x_26_);
v___x_29_ = lean_int_sub(v___x_23_, v___x_28_);
lean_dec(v___x_23_);
v___x_30_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_29_);
lean_dec(v___x_29_);
lean_inc(v_td_6_);
v___x_31_ = lean_nat_to_int(v_td_6_);
v___x_32_ = lean_int_mul(v___x_30_, v___x_31_);
lean_dec(v___x_30_);
lean_inc(v_tn_5_);
v___x_33_ = lean_nat_to_int(v_tn_5_);
v___x_34_ = lean_int_mul(v___x_33_, v___x_27_);
lean_dec(v___x_27_);
lean_dec(v___x_33_);
v___x_35_ = lean_int_dec_le(v___x_32_, v___x_34_);
lean_dec(v___x_32_);
if (v___x_35_ == 0)
{
lean_dec(v___x_34_);
lean_dec(v___x_31_);
lean_dec(v___x_28_);
lean_dec(v___x_22_);
v___y_13_ = v___x_35_;
goto v___jp_12_;
}
else
{
lean_object* v___x_36_; lean_object* v___x_37_; lean_object* v___x_38_; lean_object* v___x_39_; uint8_t v___x_40_; 
v___x_36_ = lean_int_mul(v___x_22_, v_snd_21_);
lean_dec(v___x_22_);
v___x_37_ = lean_int_sub(v___x_36_, v___x_28_);
lean_dec(v___x_28_);
lean_dec(v___x_36_);
v___x_38_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_37_);
lean_dec(v___x_37_);
v___x_39_ = lean_int_mul(v___x_38_, v___x_31_);
lean_dec(v___x_31_);
lean_dec(v___x_38_);
v___x_40_ = lean_int_dec_le(v___x_39_, v___x_34_);
lean_dec(v___x_34_);
lean_dec(v___x_39_);
v___y_13_ = v___x_40_;
goto v___jp_12_;
}
}
else
{
v___y_13_ = v___x_19_;
goto v___jp_12_;
}
v___jp_12_:
{
if (v___y_13_ == 0)
{
lean_dec(v_x_7_);
lean_dec(v_td_6_);
lean_dec(v_tn_5_);
lean_dec(v_K_4_);
lean_dec(v_N_3_);
return v___y_13_;
}
else
{
lean_object* v___x_14_; lean_object* v___x_15_; 
v___x_14_ = lean_unsigned_to_nat(1u);
v___x_15_ = lean_nat_add(v_x_7_, v___x_14_);
lean_dec(v_x_7_);
v_x_7_ = v___x_15_;
v_x_8_ = v_tail_11_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_rowsOK___boxed(lean_object* v_N_41_, lean_object* v_K_42_, lean_object* v_tn_43_, lean_object* v_td_44_, lean_object* v_x_45_, lean_object* v_x_46_){
_start:
{
uint8_t v_res_47_; lean_object* v_r_48_; 
v_res_47_ = lp_Zeta23_Zeta23_PairCeiling_rowsOK(v_N_41_, v_K_42_, v_tn_43_, v_td_44_, v_x_45_, v_x_46_);
lean_dec(v_x_46_);
v_r_48_ = lean_box(v_res_47_);
return v_r_48_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0(void){
_start:
{
lean_object* v___x_49_; lean_object* v___x_50_; 
v___x_49_ = lean_unsigned_to_nat(0u);
v___x_50_ = lean_nat_to_int(v___x_49_);
return v___x_50_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo(lean_object* v_x_51_){
_start:
{
if (lean_obj_tag(v_x_51_) == 0)
{
lean_object* v___x_52_; 
v___x_52_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0, &lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0);
return v___x_52_;
}
else
{
lean_object* v_head_53_; lean_object* v_tail_54_; lean_object* v_fst_55_; lean_object* v___x_56_; lean_object* v___x_57_; 
v_head_53_ = lean_ctor_get(v_x_51_, 0);
v_tail_54_ = lean_ctor_get(v_x_51_, 1);
v_fst_55_ = lean_ctor_get(v_head_53_, 0);
v___x_56_ = lp_Zeta23_Zeta23_PairCeiling_sumLo(v_tail_54_);
v___x_57_ = lean_int_add(v_fst_55_, v___x_56_);
lean_dec(v___x_56_);
return v___x_57_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumLo___boxed(lean_object* v_x_58_){
_start:
{
lean_object* v_res_59_; 
v_res_59_ = lp_Zeta23_Zeta23_PairCeiling_sumLo(v_x_58_);
lean_dec(v_x_58_);
return v_res_59_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumHi(lean_object* v_x_60_){
_start:
{
if (lean_obj_tag(v_x_60_) == 0)
{
lean_object* v___x_61_; 
v___x_61_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0, &lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_sumLo___closed__0);
return v___x_61_;
}
else
{
lean_object* v_head_62_; lean_object* v_tail_63_; lean_object* v_snd_64_; lean_object* v___x_65_; lean_object* v___x_66_; 
v_head_62_ = lean_ctor_get(v_x_60_, 0);
v_tail_63_ = lean_ctor_get(v_x_60_, 1);
v_snd_64_ = lean_ctor_get(v_head_62_, 1);
v___x_65_ = lp_Zeta23_Zeta23_PairCeiling_sumHi(v_tail_63_);
v___x_66_ = lean_int_add(v_snd_64_, v___x_65_);
lean_dec(v___x_65_);
return v___x_66_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_sumHi___boxed(lean_object* v_x_67_){
_start:
{
lean_object* v_res_68_; 
v_res_68_ = lp_Zeta23_Zeta23_PairCeiling_sumHi(v_x_67_);
lean_dec(v_x_67_);
return v_res_68_;
}
}
static lean_object* _init_lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0(void){
_start:
{
lean_object* v___x_69_; lean_object* v___x_70_; 
v___x_69_ = lean_unsigned_to_nat(2u);
v___x_70_ = lean_nat_to_int(v___x_69_);
return v___x_70_;
}
}
LEAN_EXPORT uint8_t lp_Zeta23_Zeta23_PairCeiling_checkRows(lean_object* v_d_71_){
_start:
{
lean_object* v_N_72_; lean_object* v_K_73_; lean_object* v_encl_74_; lean_object* v_tn_75_; lean_object* v_td_76_; lean_object* v_dn_77_; lean_object* v_dd_78_; uint8_t v___y_80_; lean_object* v___x_108_; uint8_t v___x_109_; 
v_N_72_ = lean_ctor_get(v_d_71_, 0);
lean_inc(v_N_72_);
v_K_73_ = lean_ctor_get(v_d_71_, 1);
lean_inc(v_K_73_);
v_encl_74_ = lean_ctor_get(v_d_71_, 2);
lean_inc(v_encl_74_);
v_tn_75_ = lean_ctor_get(v_d_71_, 3);
lean_inc(v_tn_75_);
v_td_76_ = lean_ctor_get(v_d_71_, 4);
lean_inc(v_td_76_);
v_dn_77_ = lean_ctor_get(v_d_71_, 5);
lean_inc(v_dn_77_);
v_dd_78_ = lean_ctor_get(v_d_71_, 6);
lean_inc(v_dd_78_);
lean_dec_ref(v_d_71_);
v___x_108_ = lean_unsigned_to_nat(0u);
v___x_109_ = lean_nat_dec_lt(v___x_108_, v_N_72_);
if (v___x_109_ == 0)
{
v___y_80_ = v___x_109_;
goto v___jp_79_;
}
else
{
uint8_t v___x_110_; 
v___x_110_ = lean_nat_dec_lt(v___x_108_, v_K_73_);
v___y_80_ = v___x_110_;
goto v___jp_79_;
}
v___jp_79_:
{
if (v___y_80_ == 0)
{
lean_dec(v_dd_78_);
lean_dec(v_dn_77_);
lean_dec(v_td_76_);
lean_dec(v_tn_75_);
lean_dec(v_encl_74_);
lean_dec(v_K_73_);
lean_dec(v_N_72_);
return v___y_80_;
}
else
{
lean_object* v___x_81_; uint8_t v___x_82_; 
v___x_81_ = lean_unsigned_to_nat(0u);
v___x_82_ = lean_nat_dec_lt(v___x_81_, v_td_76_);
if (v___x_82_ == 0)
{
lean_dec(v_dd_78_);
lean_dec(v_dn_77_);
lean_dec(v_td_76_);
lean_dec(v_tn_75_);
lean_dec(v_encl_74_);
lean_dec(v_K_73_);
lean_dec(v_N_72_);
return v___x_82_;
}
else
{
uint8_t v___x_83_; 
v___x_83_ = lean_nat_dec_lt(v___x_81_, v_dd_78_);
if (v___x_83_ == 0)
{
lean_dec(v_dd_78_);
lean_dec(v_dn_77_);
lean_dec(v_td_76_);
lean_dec(v_tn_75_);
lean_dec(v_encl_74_);
lean_dec(v_K_73_);
lean_dec(v_N_72_);
return v___x_83_;
}
else
{
lean_object* v___x_84_; uint8_t v___x_85_; 
v___x_84_ = l_List_lengthTR___redArg(v_encl_74_);
v___x_85_ = lean_nat_dec_eq(v___x_84_, v_N_72_);
lean_dec(v___x_84_);
if (v___x_85_ == 0)
{
lean_dec(v_dd_78_);
lean_dec(v_dn_77_);
lean_dec(v_td_76_);
lean_dec(v_tn_75_);
lean_dec(v_encl_74_);
lean_dec(v_K_73_);
lean_dec(v_N_72_);
return v___x_85_;
}
else
{
uint8_t v___x_86_; 
lean_inc(v_K_73_);
lean_inc(v_N_72_);
v___x_86_ = lp_Zeta23_Zeta23_PairCeiling_rowsOK(v_N_72_, v_K_73_, v_tn_75_, v_td_76_, v___x_81_, v_encl_74_);
if (v___x_86_ == 0)
{
lean_dec(v_dd_78_);
lean_dec(v_dn_77_);
lean_dec(v_encl_74_);
lean_dec(v_K_73_);
lean_dec(v_N_72_);
return v___x_86_;
}
else
{
lean_object* v___x_87_; lean_object* v___x_88_; lean_object* v___x_89_; lean_object* v___x_90_; lean_object* v___x_91_; lean_object* v___x_92_; lean_object* v___x_93_; lean_object* v___x_94_; lean_object* v___x_95_; lean_object* v___x_96_; lean_object* v___x_97_; lean_object* v___x_98_; lean_object* v___x_99_; lean_object* v___x_100_; uint8_t v___x_101_; 
v___x_87_ = lean_obj_once(&lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0, &lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0_once, _init_lp_Zeta23_Zeta23_PairCeiling_checkRows___closed__0);
v___x_88_ = lp_Zeta23_Zeta23_PairCeiling_sumLo(v_encl_74_);
v___x_89_ = lean_int_mul(v___x_87_, v___x_88_);
lean_dec(v___x_88_);
v___x_90_ = lean_nat_to_int(v_K_73_);
v___x_91_ = lean_nat_to_int(v_N_72_);
v___x_92_ = lean_int_mul(v___x_90_, v___x_91_);
v___x_93_ = lean_int_sub(v___x_89_, v___x_92_);
lean_dec(v___x_89_);
v___x_94_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_93_);
lean_dec(v___x_93_);
v___x_95_ = lean_nat_to_int(v_dd_78_);
v___x_96_ = lean_int_mul(v___x_94_, v___x_95_);
lean_dec(v___x_94_);
v___x_97_ = lean_nat_to_int(v_dn_77_);
v___x_98_ = lean_int_mul(v___x_87_, v___x_90_);
lean_dec(v___x_90_);
v___x_99_ = lean_int_mul(v___x_98_, v___x_91_);
lean_dec(v___x_91_);
lean_dec(v___x_98_);
v___x_100_ = lean_int_mul(v___x_97_, v___x_99_);
lean_dec(v___x_99_);
lean_dec(v___x_97_);
v___x_101_ = lean_int_dec_le(v___x_96_, v___x_100_);
lean_dec(v___x_96_);
if (v___x_101_ == 0)
{
lean_dec(v___x_100_);
lean_dec(v___x_95_);
lean_dec(v___x_92_);
lean_dec(v_encl_74_);
return v___x_101_;
}
else
{
lean_object* v___x_102_; lean_object* v___x_103_; lean_object* v___x_104_; lean_object* v___x_105_; lean_object* v___x_106_; uint8_t v___x_107_; 
v___x_102_ = lp_Zeta23_Zeta23_PairCeiling_sumHi(v_encl_74_);
lean_dec(v_encl_74_);
v___x_103_ = lean_int_mul(v___x_87_, v___x_102_);
lean_dec(v___x_102_);
v___x_104_ = lean_int_sub(v___x_103_, v___x_92_);
lean_dec(v___x_92_);
lean_dec(v___x_103_);
v___x_105_ = lp_Zeta23_abs___at___00Zeta23_PairCeiling_step_spec__0(v___x_104_);
lean_dec(v___x_104_);
v___x_106_ = lean_int_mul(v___x_105_, v___x_95_);
lean_dec(v___x_95_);
lean_dec(v___x_105_);
v___x_107_ = lean_int_dec_le(v___x_106_, v___x_100_);
lean_dec(v___x_100_);
lean_dec(v___x_106_);
return v___x_107_;
}
}
}
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23_Zeta23_PairCeiling_checkRows___boxed(lean_object* v_d_111_){
_start:
{
uint8_t v_res_112_; lean_object* v_r_113_; 
v_res_112_ = lp_Zeta23_Zeta23_PairCeiling_checkRows(v_d_111_);
v_r_113_ = lean_box(v_res_112_);
return v_r_113_;
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_rowsOK_match__1_splitter___redArg(lean_object* v_x_114_, lean_object* v_x_115_, lean_object* v_h__1_116_, lean_object* v_h__2_117_){
_start:
{
if (lean_obj_tag(v_x_115_) == 0)
{
lean_object* v___x_118_; 
lean_dec(v_h__2_117_);
v___x_118_ = lean_apply_1(v_h__1_116_, v_x_114_);
return v___x_118_;
}
else
{
lean_object* v_head_119_; lean_object* v_tail_120_; lean_object* v___x_121_; 
lean_dec(v_h__1_116_);
v_head_119_ = lean_ctor_get(v_x_115_, 0);
lean_inc(v_head_119_);
v_tail_120_ = lean_ctor_get(v_x_115_, 1);
lean_inc(v_tail_120_);
lean_dec_ref_known(v_x_115_, 2);
v___x_121_ = lean_apply_3(v_h__2_117_, v_x_114_, v_head_119_, v_tail_120_);
return v___x_121_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_rowsOK_match__1_splitter(lean_object* v_motive_122_, lean_object* v_x_123_, lean_object* v_x_124_, lean_object* v_h__1_125_, lean_object* v_h__2_126_){
_start:
{
if (lean_obj_tag(v_x_124_) == 0)
{
lean_object* v___x_127_; 
lean_dec(v_h__2_126_);
v___x_127_ = lean_apply_1(v_h__1_125_, v_x_123_);
return v___x_127_;
}
else
{
lean_object* v_head_128_; lean_object* v_tail_129_; lean_object* v___x_130_; 
lean_dec(v_h__1_125_);
v_head_128_ = lean_ctor_get(v_x_124_, 0);
lean_inc(v_head_128_);
v_tail_129_ = lean_ctor_get(v_x_124_, 1);
lean_inc(v_tail_129_);
lean_dec_ref_known(v_x_124_, 2);
v___x_130_ = lean_apply_3(v_h__2_126_, v_x_123_, v_head_128_, v_tail_129_);
return v___x_130_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_sumLo_match__1_splitter___redArg(lean_object* v_x_131_, lean_object* v_h__1_132_, lean_object* v_h__2_133_){
_start:
{
if (lean_obj_tag(v_x_131_) == 0)
{
lean_object* v___x_134_; lean_object* v___x_135_; 
lean_dec(v_h__2_133_);
v___x_134_ = lean_box(0);
v___x_135_ = lean_apply_1(v_h__1_132_, v___x_134_);
return v___x_135_;
}
else
{
lean_object* v_head_136_; lean_object* v_tail_137_; lean_object* v___x_138_; 
lean_dec(v_h__1_132_);
v_head_136_ = lean_ctor_get(v_x_131_, 0);
lean_inc(v_head_136_);
v_tail_137_ = lean_ctor_get(v_x_131_, 1);
lean_inc(v_tail_137_);
lean_dec_ref_known(v_x_131_, 2);
v___x_138_ = lean_apply_2(v_h__2_133_, v_head_136_, v_tail_137_);
return v___x_138_;
}
}
}
LEAN_EXPORT lean_object* lp_Zeta23___private_Zeta23_PairCeiling_RowCert_0__Zeta23_PairCeiling_sumLo_match__1_splitter(lean_object* v_motive_139_, lean_object* v_x_140_, lean_object* v_h__1_141_, lean_object* v_h__2_142_){
_start:
{
if (lean_obj_tag(v_x_140_) == 0)
{
lean_object* v___x_143_; lean_object* v___x_144_; 
lean_dec(v_h__2_142_);
v___x_143_ = lean_box(0);
v___x_144_ = lean_apply_1(v_h__1_141_, v___x_143_);
return v___x_144_;
}
else
{
lean_object* v_head_145_; lean_object* v_tail_146_; lean_object* v___x_147_; 
lean_dec(v_h__1_141_);
v_head_145_ = lean_ctor_get(v_x_140_, 0);
lean_inc(v_head_145_);
v_tail_146_ = lean_ctor_get(v_x_140_, 1);
lean_inc(v_tail_146_);
lean_dec_ref_known(v_x_140_, 2);
v___x_147_ = lean_apply_2(v_h__2_142_, v_head_145_, v_tail_146_);
return v___x_147_;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PairCeiling_NearCUE(uint8_t builtin);
lean_object* initialize_Zeta23_Zeta23_PairCeiling_NumericCert(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Zeta23_Zeta23_PairCeiling_RowCert(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PairCeiling_NearCUE(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Zeta23_Zeta23_PairCeiling_NumericCert(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
