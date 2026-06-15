# 糖尿病/高血糖与白血病关联：event 处理与生存模型整理

整理日期：2026-06-02

目的：重整 `糖尿病高血糖与白血病关联_Cox变量整理.md`。本文件把重点从“协变量”调整为：

1. 生存分析起点是什么
2. event 如何定义
3. censor 如何处理
4. 是否存在 competing event
5. 具体使用哪一种生存模型

协变量只作为次要信息保留。

## 关键判断

同样写作 Cox regression，含义可能完全不同：

- `incident leukemia`：event 是首次白血病诊断。
- `overall survival`：event 是全因死亡。
- `cancer-specific survival`：event 是白血病相关死亡，其他死因如何处理非常关键。
- `time to first treatment`：event 是第一次治疗，不是死亡。
- `Fine-Gray`：通常说明作者把死亡或其他结局作为 competing event 处理。
- `Poisson regression`、`SIR`、`Kaplan-Meier/log-rank` 不是 Cox。

## 一、糖尿病/高血糖与白血病发病风险

| 序号 | 文献                                                                                                                                                | 起始时间                                                                        | event 定义                                                                | censor / competing event 处理                                                                                                                                                       | 生存模型类型                                                                                                           | 协变量，次要                                                                                                                            | DOI                                  |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| 1    | Prospective associations of diabetes with 15 cancers in 2.2 million UK and Chinese adults                                                           | cohort baseline / recruitment                                                   | 首次发生目标癌症；分析 15 类癌症，其中包括 leukemia                       | person-years 从 baseline 到以下最早者：任意恶性癌症、死亡、移民/失访、癌症随访结束。也就是说，非目标癌症会终止随访；死亡作为 censor，不是 competing risk 模型                       | Cox regression；按出生队列、性别、地区分层                                                                             | Model 1：教育、族裔、Townsend deprivation。Model 2：再加吸烟、饮酒、体力活动、BMI、腰围、早年体型、高血压、血压、女性生殖因素           | `10.1093/jnci/djaf154`             |
| 2    | Associations of Type 2 Diabetes with Risk of Overall and Site-Specific Cancers in a Cohort of Predominantly Low-Income Racially Diverse Populations | Southern Community Cohort Study enrollment / baseline survey                    | incident overall cancer 和 21 个 site-specific cancers；其中包括 leukemia | incident cancer 通过 state cancer registries linkage 获得。可访问摘要未明确逐项列出 leukemia 分析中的 censor 规则；按 cohort cancer incidence 常规应为事件发生、死亡/失访、随访结束 | Cox proportional hazards model                                                                                         | 年龄、性别、种族、教育、收入、入组来源、吸烟状态、吸烟包年、BMI                                                                         | `10.1158/1055-9965.EPI-23-1079`    |
| 3    | The risk of myelodysplastic syndrome and acute myeloid leukemia by metformin use and type 2 diabetes status                                         | 2000-01-01 或进入相应暴露状态后随访；全国 Danish registers                      | 新发 MDS、AML，及 MDS/AML 合并结局                                        | 使用丹麦全国登记随访到 2017-12-31；死亡/迁出/随访结束通常为 censor。文章建模描述未提示 Fine-Gray，主要不是 competing risk                                                           | Stratified Cox regression；age as underlying timescale；birth year 和 sex 作为 strata                                  | 多变量模型调整 Nordic Multimorbidity Index；T2D/metformin 暴露按状态比较                                                                | `10.2340/1651-226X.2025.42422`     |
| 4    | Metformin Use and Leukemia Risk in Patients With Type 2 Diabetes Mellitus                                                                           | T2D 患者首次抗糖尿病药物处方后开始；排除随访 <12 个月、既往癌症或 12 个月内癌症 | new-onset leukemia                                                        | 随访到 leukemia、死亡/退出保险或 2011-12-31。敏感性分析包括排除短随访、排除 incretin use、按纳入时期分层、在未规律续方后 4 或 6 个月 censor                                         | Cox regression with inverse probability of treatment weighting based on propensity score；ITT 和 per-protocol 两套分析 | PS 包含开始随访日期、年龄、糖尿病病程、性别、职业、地区、共病、糖尿病并发症、感染/肝炎/烟酒相关诊断、常用药物等                         | `10.3389/fendo.2020.541090`        |
| 5    | Incidence of hematologic malignancies and mortality associated with GLP-1RA and SGLT2i use in T2D                                                   | T2D diagnosis / EHR cohort entry；药物使用作为时间变化暴露                      | AML、CML、MDS、multiple myeloma 发病；另做这些肿瘤患者死亡                | 文章表注说明：药物诊断前已有 malignancy 的人计入 control events。可访问文本未完整给出每个个体 censor 节点；主要分析为 EHR 中从 T2D 诊断起的 cumulative incidence                    | Time-dependent Cox proportional hazards model + IPTW。药物为 time-varying covariate                                    | 固定调整 race、ethnicity；IPTW 用年龄、性别、nicotine dependence、脑梗死、慢性缺血性心脏病、CKD、高血压；死亡模型额外控制 heart failure | `10.1016/j.eclinm.2025.103749`     |
| 6    | Risk of cancer in a large cohort of U.S. veterans with diabetes                                                                                     | VA hospitalization cohort entry                                                 | 多癌种，包括 leukemia                                                     | 非 Cox。比较糖尿病 vs 非糖尿病男性 veterans 的癌症发生率                                                                                                                            | Poisson regression；不是 Cox 生存模型                                                                                  | 摘要报告 adjusted RR；协变量需查全文，当前重点为非 Cox                                                                                  | `10.1002/ijc.25362`                |
| 7    | Cancer risk among patients hospitalized for Type 1 diabetes mellitus                                                                                | T1D hospitalization 后                                                          | subsequent cancers，包括 leukemia 和 acute lymphatic leukemia             | 非 Cox。将 T1D 住院患者的癌症发生与一般人群预期发生比较                                                                                                                             | Standardized incidence ratio，SIR；不是 Cox                                                                            | 标准化比较，不是个体级 Cox 调整                                                                                                         | `10.1111/j.1464-5491.2010.03011.x` |
| 8    | Increased incidence of non-Hodgkin lymphoma, leukemia, and myeloma in T2D                                                                           | 不适用                                                                          | leukemia 等血液肿瘤                                                       | 不适用                                                                                                                                                                              | Meta-analysis；不是自身生存模型                                                                                        | 汇总纳入研究的 OR/RR，不能作为 Cox event 处理模板                                                                                       | `10.1182/blood-2011-06-362830`     |
| 9    | The association between type 1 and 2 diabetes mellitus and the risk of leukemia                                                                     | 不适用                                                                          | leukemia                                                                  | 不适用                                                                                                                                                                              | Meta-analysis of cohort studies；不是自身生存模型                                                                      | 汇总 RR，不能作为 Cox event 处理模板                                                                                                    | `10.1507/endocrj.EJ20-0138`        |

## 二、糖尿病/高血糖与白血病患者预后

| 序号 | 文献                                                                                                         | 起始时间                                                | event 定义                                                                                                                 | censor / competing event 处理                                                                                                                                                   | 生存模型类型                                                                                                                | 协变量，次要                                                                                                                        | DOI                               |
| ---- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| 1    | Diabetes Mellitus Is Associated with Inferior Prognosis in Patients with Chronic Lymphocytic Leukemia        | CLL diagnosis                                           | TTFT：第一次 CLL 治疗；CSS：CLL-specific death，包括 CLL-related pneumonia；OS：全因死亡                                   | TTFT：诊断后立即治疗者排除；未发生治疗者随访结束 censor。CSS：其他原因死亡从 CSS 分析中排除；这更接近 cause-specific survival 思路，但文章使用 Cox 而非 Fine-Gray               | Kaplan-Meier + log-rank；univariate/multivariate Cox regression；PSM 后重复分析                                             | PSM 匹配性别、年龄、Binet stage、ECOG PS、Hb、PLT、LDH、β2-MG、TP53、ATM、IGHV、CD38、ZAP-70                                       | `10.4143/crt.2019.122`          |
| 2    | Impact of type 2 diabetes on mortality, cause of death, and treatment in chronic lymphocytic leukemia        | CLL diagnosis；另有 first-line treatment 起点           | OS from diagnosis：全因死亡；OS from treatment：一线治疗后全因死亡；TTFT：第一次治疗；cause-specific death：感染等特定死因 | 使用 Fine-Gray 说明作者考虑 competing risks。OS 中 event 为死亡，无 competing event。TTFT 中死亡可作为 competing event。cause-specific death 中其他死因通常作为 competing event | Cox proportional hazards regression + Fine-Gray regression                                                                  | 可访问摘要未完整列出全部协变量；研究使用 Danish national registers 和 Mayo CLL Resource 并行分析                                    | `10.1002/ajh.26964`             |
| 3    | Association between glycemic control, age, and outcomes among intensively treated AML patients               | AML induction chemotherapy initiation / hospitalization | OS：全因死亡；CR/CRi：缓解结局，不是 survival event                                                                        | OS 中未死亡者随访结束 censor。CR/CRi 用 logistic regression，不是 Cox。未提示 competing risk                                                                                    | Cox proportional hazards models for OS；logistic regression for CR/CRi 和 30-day mortality；按年龄 `<60` 与 `>=60` 分层 | 多变量纳入双变量 P <= 0.1 变量；候选变量包括 BMI、CCI、Hb、bilirubin、WBC、creatinine、LDH、cytogenetic risk、steroids、diabetes 等 | `10.1007/s00520-018-4582-6`     |
| 4    | Hyperglycemia increases complicated infection and mortality during induction therapy in adult acute leukemia | induction therapy 开始，观察前后 30 天                  | complicated infection；30-day mortality；complete remission                                                                | 固定 30 天窗口；不是 time-to-event Cox。死亡是二分类 30 天结局                                                                                                                  | Chi-square / Fisher exact tests；不是 Cox                                                                                   | 不适合作为 Cox 模板                                                                                                                 | `10.5581/1516-8484.20130013`    |
| 5    | Impact of chemotherapy-related hyperglycemia on prognosis of child ALL                                       | induction treatment / diagnosis 后                      | 5-year OS：死亡；RFS：复发或死亡，具体复合 event 需看全文；CR：完全缓解                                                    | Kaplan-Meier 曲线和 log-rank 比较；未见 Cox                                                                                                                                     | Kaplan-Meier + log-rank；不是 Cox                                                                                           | 不适合作为多变量 Cox 模板，除非另查全文确认有 Cox                                                                                   | `10.7314/apjcp.2014.15.20.8855` |

## 三、最需要从文献中抄清楚的字段

以后整理类似文献，优先写这些字段：

```text
time origin:
  baseline / diagnosis / treatment start / medication initiation

event:
  incident leukemia / AML / CLL / MDS
  all-cause death
  leukemia-specific death
  first treatment
  relapse-free survival event

censor:
  end of follow-up
  loss to follow-up
  emigration
  death before event
  other cancer diagnosis
  medication discontinuation / irregular refill

competing event:
  death before treatment
  death from non-leukemia causes
  other cancers

model:
  Cox proportional hazards
  stratified Cox
  time-dependent Cox
  cause-specific Cox
  Fine-Gray subdistribution hazards
  flexible parametric survival
  Kaplan-Meier/log-rank only
  Poisson/SIR, not survival Cox
```

## 四、对你当前课题的直接建议

如果你的问题是“糖尿病/高血糖是否增加白血病发病风险”，首选模板是：

```text
time origin: UKB baseline assessment
event: first leukemia diagnosis, preferably ICD-10 C91-C95; 或按 AML/CLL/MDS 亚型
censor: first of death, loss to follow-up, end of cancer registry follow-up
other cancer: 需要明确是 censor at any first cancer，还是只 censor 对应 leukemia event
model: Cox proportional hazards; 可以按 sex/region/birth cohort stratify
```

如果你的问题是“糖尿病/高血糖对白血病患者预后是否有影响”，首选模板是：

```text
time origin: leukemia diagnosis 或 treatment start
event 1: all-cause death -> Cox PH
event 2: leukemia-specific death -> Fine-Gray 或 cause-specific Cox，需要说明其他死因怎么处理
event 3: time to first treatment -> Fine-Gray 更稳妥，因为死亡会阻止治疗发生
event 4: relapse/progression -> 需要明确复合 event 定义
```

## 五、当前证据中最可借鉴的模型

| 用途                   | 最可借鉴文献                                         | 原因                                                                      |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------- |
| UKB 风格发病风险       | Prospective associations of diabetes with 15 cancers | event/censor 规则写得清楚，明确把任意癌症、死亡、失访、随访结束作为终止点 |
| 全国登记发病风险       | Danish metformin/T2D-MDS/AML cohort                  | 使用 age as timescale、birth year/sex stratified Cox，适合 registry 数据  |
| 药物暴露随时间变化     | GLP-1RA/SGLT2i-T2D hematologic malignancy study      | time-dependent Cox，适合药物使用不是 baseline 固定暴露的场景              |
| CLL 预后               | Diabetes prognosis in CLL                            | 清楚区分 TTFT、CSS、OS 三类 event                                         |
| CLL 死因和治疗竞争风险 | T2D mortality in CLL                                 | 同时使用 Cox 和 Fine-Gray，适合处理 TTFT 和 cause-specific death          |
| AML 治疗期血糖         | Glycemic control and AML outcomes                    | OS 用 Cox，CR/CRi 用 logistic，避免把非时间结局硬塞进 Cox                 |

---
