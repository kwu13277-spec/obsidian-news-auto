# 糖尿病/高血糖与白血病关联文献及 Cox 变量整理

检索日期：2026-06-02

检索范围：PubMed 为主，补充 PMC 全文、期刊页和 DOI 元数据。关键词包括 diabetes、type 2 diabetes、type 1 diabetes、hyperglycemia、blood glucose、leukemia、leukaemia、acute myeloid leukemia、chronic lymphocytic leukemia、Cox、hazard ratio、cohort。

整理原则：

- 优先纳入队列研究、真实世界电子健康记录研究、白血病患者预后研究。
- 纯 meta-analysis 单独标注，因为没有自己的 Cox 协变量。
- 使用 SIR、Poisson、logistic、Kaplan-Meier 而非 Cox 的研究，不强行写成 Cox。

## 一、糖尿病/高血糖与白血病发病风险

| 序号  | 文献                                                                                                                                                  | 暴露                                                          | 白血病/血液肿瘤结局                               | 统计模型                                                 | Cox 或相关模型变量                                                                                                                                                        | 主要结果                                                                                      | DOI                                |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ---------------------------------- |
| 1   | Prospective associations of diabetes with 15 cancers in 2.2 million UK and Chinese adults                                                           | 基线糖尿病；UK Biobank、Million Women Study、China Kadoorie Biobank | 15 类癌症，包括 leukemia                       | Cox regression                                       | 分层：出生队列、性别、地区。Model 1：教育、族裔、Townsend deprivation index 等社会经济因素。Model 2：Model 1 + 吸烟、饮酒、体力活动、BMI、腰围、早年体型/早年肥胖指标、高血压史、收缩压、舒张压、女性生殖因素                                 | 糖尿病与 leukemia 风险有较弱正相关；作者认为胃癌、结直肠癌、白血病等可能有较小效应，需注意混杂                                      | `10.1093/jnci/djaf154`             |
| 2   | Associations of Type 2 Diabetes with Risk of Overall and Site-Specific Cancers in a Cohort of Predominantly Low-Income Racially Diverse Populations | 基线 T2D                                                      | overall cancer 和 21 个部位癌症，包括 leukemia    | Cox proportional hazards model                       | 调整：年龄、性别、种族、教育、收入、入组来源、吸烟状态、吸烟包年、BMI                                                                                                                               | T2D 与总体癌症及多个部位癌症风险升高相关；包括 leukemia，但摘要未给出 leukemia 单项 HR                                  | `10.1158/1055-9965.EPI-23-1079`    |
| 3   | The risk of myelodysplastic syndrome and acute myeloid leukemia by metformin use and type 2 diabetes status: a Danish nation-wide cohort study      | T2D 状态、metformin 使用                                         | MDS、AML、MDS/AML 合并                       | Stratified Cox regression                            | 分层：出生年份、性别；时间尺度：年龄。多变量模型额外调整 Nordic Multimorbidity Index，作为共病/生活方式代理变量                                                                                             | T2D 与 MDS/AML 合并风险无显著关联；T2D 与 MDS 风险升高相关，AML 未见关联；metformin 与 MDS/AML 或 AML 风险无显著关联       | `10.2340/1651-226X.2025.42422`     |
| 4   | Metformin Use and Leukemia Risk in Patients With Type 2 Diabetes Mellitus                                                                           | T2D 患者中 metformin initiator vs non-initiator                | new-onset leukemia                       | Cox regression with IPTW based on propensity score   | PS 变量：开始随访日期、年龄、糖尿病诊断至用药时间、性别、职业、居住地区、高血压、血脂异常、肥胖、肾病、眼病、卒中、缺血性心脏病、外周动脉病、COPD、烟草滥用、酒精相关诊断、胆石症、幽门螺杆菌、EBV、HBV、HCV、肌肉骨骼/结缔组织疾病、HIV、ACEI/ARB、CCB、statin、fibrate、aspirin | 主分析显示 metformin 对 leukemia 风险总体中性；ITT HR 0.943，per-protocol HR 0.852，均未显著                 | `10.3389/fendo.2020.541090`        |
| 5   | Incidence of hematologic malignancies and mortality associated with GLP-1 receptor agonist and SGLT2 inhibitor use in type 2 diabetes mellitus      | T2D 患者中 GLP-1RA 或 SGLT2 inhibitor 使用                        | AML、CML、MDS、multiple myeloma；另分析死亡       | Time-dependent Cox proportional hazards model + IPTW | 药物作为 time-varying covariate；固定协变量：race、ethnicity。IPTW 加权变量：年龄、性别、nicotine dependence、脑梗死史、慢性缺血性心脏病、CKD、高血压。死亡模型额外包含 heart failure                                  | GLP-1RA/SGLT2i 对 AML、CML、MDS 发病风险未见显著改变；GLP-1RA 与 MM 风险降低相关。SGLT2i 在 AML/MM 患者死亡分析中提示风险升高 | `10.1016/j.eclinm.2025.103749`     |
| 6   | Risk of cancer in a large cohort of U.S. veterans with diabetes                                                                                     | 糖尿病住院/诊断状态                                                  | 多癌种，包括 leukemia                          | Poisson regression，不是 Cox                            | 该研究报告 adjusted RR；摘要未给出 Cox 协变量。属于非 Cox 风险研究                                                                                                                       | 男性糖尿病患者 leukemia 风险升高，RR 1.14，95% CI 1.08-1.21                                            | `10.1002/ijc.25362`                |
| 7   | Cancer risk among patients hospitalized for Type 1 diabetes mellitus: a population-based cohort study in Sweden                                     | 住院 T1D                                                      | 多癌种，包括 leukemia、acute lymphatic leukemia | SIR，不是 Cox                                           | 与一般人群比较的 standardized incidence ratio；不是 Cox 模型                                                                                                                    | T1D 患者 leukemia 风险升高；急性淋巴细胞白血病 SIR 5.31，95% CI 3.32-8.05                                  | `10.1111/j.1464-5491.2010.03011.x` |
| 8   | Increased incidence of non-Hodgkin lymphoma, leukemia, and myeloma in patients with diabetes mellitus type 2: a meta-analysis                       | T2D                                                         | NHL、leukemia、myeloma                     | Meta-analysis，不是自身 Cox                               | 汇总纳入研究的 OR/RR；没有统一 Cox 协变量                                                                                                                                         | T2D 与 leukemia 风险升高相关，pooled OR 1.22，95% CI 1.03-1.44                                     | `10.1182/blood-2011-06-362830`     |
| 9   | The association between type 1 and 2 diabetes mellitus and the risk of leukemia: a systematic review and meta-analysis of 18 cohort studies         | T1D、T2D                                                     | leukemia                                 | Meta-analysis，不是自身 Cox                               | 汇总 cohort studies 的 RR；没有统一 Cox 协变量                                                                                                                                | T2D 与 leukemia 风险升高相关，summary RR 1.33，95% CI 1.21-1.47；T1D 汇总结果不显著                        | `10.1507/endocrj.EJ20-0138`        |

## 二、糖尿病/高血糖与白血病患者预后

| 序号 | 文献 | 研究对象 | 暴露 | 结局 | Cox 模型变量 | 主要结果 | DOI |
|---|---|---|---|---|---|---|---|
| 1 | Diabetes Mellitus Is Associated with Inferior Prognosis in Patients with Chronic Lymphocytic Leukemia | 新诊断 CLL 患者 | 既往 DM、pre-diabetes、DM duration | TTFT、CSS、OS | 单变量和多变量 Cox；另做 1:1 propensity score matching。PSM 匹配变量：性别、年龄、Binet stage、ECOG PS、Hb、PLT、LDH、β2-microglobulin、TP53 disruption、ATM deletion、IGHV mutation status、CD38、ZAP-70。Cox 预测变量包括 DM 及 CLL 临床/分子预后指标 | DM 是 TTFT 和 CSS 的独立不良预后因素；DM 加入 CLL-IPI 可提高 CSS 预测能力 | `10.4143/crt.2019.122` |
| 2 | Impact of type 2 diabetes on mortality, cause of death, and treatment in chronic lymphocytic leukemia | Danish CLL registers 与 Mayo Clinic CLL Resource | T2D | OS from CLL diagnosis、OS from treatment、TTFT；另做 cause-specific death | Cox proportional hazard regression 和 Fine-Gray regression。摘要确认使用 Cox/Fine-Gray，但可访问摘要未完整列出所有 Cox 协变量；按 CLL register 研究通常纳入年龄、性别、诊断/治疗时间、治疗状态和 CLL 相关风险因素/共病 | CLL 合并 T2D 患者诊断后和一线治疗后 OS 较差，死亡增加主要由感染相关死亡驱动 | `10.1002/ajh.26964` |
| 3 | Association between glycemic control, age, and outcomes among intensively treated patients with acute myeloid leukemia | 接受强化诱导治疗的新诊断 AML 患者 | 住院期间 mean blood glucose、glycemic variability；另看 diabetes 和 steroid use | OS；CR/CRi 用 logistic regression | Cox proportional hazards models，按年龄分层 `<60` vs `>=60`。多变量模型纳入双变量分析 P <= 0.1 的变量；候选协变量包括年龄层、性别、种族/族裔、保险类型、BMI、Charlson Comorbidity Index、Hb、bilirubin、WBC、creatinine、LDH、cytogenetic risk、steroid use、insulin/oral antidiabetic medication；探索性模型额外调整 diabetes 和 steroid medication | 老年 AML 患者中，mean glucose 和 glycemic variability 每升高 10 mg/dL 与 OS 更差相关 | `10.1007/s00520-018-4582-6` |
| 4 | Hyperglycemia increases the complicated infection and mortality rates during induction therapy in adult acute leukemia patients | 成人急性白血病诱导治疗患者 | 诱导治疗期间 hyperglycemia，定义为至少一次 fasting glucose >100 mg/dL | complicated infection、30-day mortality、complete remission | 主要使用 chi-square/Fisher 检验，不是 Cox | 高血糖与复杂感染和 30 天死亡率升高相关 | `10.5581/1516-8484.20130013` |
| 5 | Impact of chemotherapy-related hyperglycemia on prognosis of child acute lymphocytic leukemia | 儿童 ALL | 诱导治疗期间 hyperglycemia，fasting glucose >=126 mg/dL 或 random glucose >=200 mg/dL | 5-year OS、RFS、CR | Kaplan-Meier 和 log-rank；不是 Cox | 高血糖组 5 年 OS 和 RFS 更差 | `10.7314/apjcp.2014.15.20.8855` |

## 三、建模变量可借鉴框架

如果做“糖尿病/高血糖 -> 白血病发病风险”的 Cox 分析，建议至少考虑：

```text
年龄或出生队列
性别
地区/中心
种族/族裔
社会经济状态：教育、收入、Townsend deprivation index
吸烟状态和吸烟强度
饮酒
体力活动
BMI、腰围、早年体型
高血压和血压
共病指数：例如 Nordic Multimorbidity Index、Charlson Comorbidity Index
糖尿病药物：metformin、insulin、GLP-1RA、SGLT2i 等
```

如果做“白血病患者合并糖尿病/高血糖 -> 预后”的 Cox 分析，建议至少考虑：

```text
年龄
性别
白血病亚型和诊断年份
治疗方案或治疗强度
ECOG performance status
Charlson Comorbidity Index 或具体共病
血常规和生化指标：Hb、PLT、WBC、LDH、creatinine、bilirubin
白血病风险分层：Binet/Rai stage、CLL-IPI、cytogenetic risk
分子指标：TP53、ATM deletion、IGHV、CD38、ZAP-70 等，按白血病类型选择
糖皮质激素使用
糖尿病病程、HbA1c、住院平均血糖、血糖变异度
```

## 四、结论

现有证据大致指向：

- T2D 与 leukemia 发病风险可能有轻到中度正相关，但不同队列的混杂控制差异较大。
- 与 AML/MDS 相关的最新丹麦全国队列显示：T2D 对 AML 无明显关联，但对 MDS 有一定风险升高；metformin 未显示保护作用。
- 在已患白血病人群中，糖尿病或治疗期高血糖更常表现为预后不良因素，尤其在 CLL 和老年 AML 中。
- Cox 协变量选择需要区分“发病风险模型”和“白血病预后模型”；前者重点控制生活方式和社会经济因素，后者重点控制白血病本身的预后分层、治疗和共病。

---
