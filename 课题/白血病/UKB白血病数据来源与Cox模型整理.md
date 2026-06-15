# UK Biobank 白血病相关文献：数据来源与 Cox 模型整理

整理日期：2026-06-02

范围：基于前一份 `UKB白血病定义文献整理.md` 中列出的 8 篇文献。

说明：并非所有文献都把 Cox 回归作为主要分析模型。有些是 GWAS、机器学习、MR 或风险评分研究；这类文献在表中标为“未作为主要 Cox 分析”。

## 汇总表

| 序号 | 文献 | 主要数据来源 | Cox 回归/生存模型使用情况 | 主要模型或调整变量 | DOI |
|---|---|---|---|---|---|
| 1 | Early-life exposures and risk of hematological malignancies in adulthood | UK Biobank 基线问卷、体测和 linked health records；血液肿瘤结局来自 UKB 连接的健康记录/登记资料；另做 meta-analysis 和 MR | 使用 Cox proportional hazards model 估计 early-life exposures 与成人血液肿瘤风险 | 主要为多变量 Cox。暴露包括出生体重、儿童期体型/身高、早年吸烟等；结局包括 overall hematological malignancies 及亚型。模型报告 HR 和 95% CI，并做中介分析、meta-analysis、MR 作为补充 | `10.1186/s12885-025-14780-y` |
| 2 | Lymphocyte count and risk of chronic lymphocytic leukemia | UKB 基线血常规绝对淋巴细胞计数；CLL/SLL 来自 linked national cancer registries | 主要使用 flexible parametric survival modelling；文中也报告 HR | 模型核心变量为年龄、性别、基线绝对淋巴细胞计数；目标是建立 CLL 绝对风险模型，而不是传统分层 Cox 模型 | `10.1093/jnci/djaf338` |
| 3 | Mitochondrial heteroplasmy is a risk factor for the development of chronic lymphocytic leukemia | UKB 遗传数据、线粒体 heteroplasmy、CHIP/L-CHIP、基线血常规；CLL 来自 cancer registry；All of Us 为验证队列 | 使用 Cox proportional hazards models 分析 heteroplasmy 与 incident CLL | 主要模型评估 mtDNA heteroplasmy 数量/特征与 CLL 风险；常见调整包括年龄、性别、吸烟、既往癌症史等；敏感性模型进一步纳入 mtDNA copy number、血细胞计数、L-CHIP/CHIP 等相关变量 | `10.1038/s41467-026-69861-8` |
| 4 | Integration of Germline and Somatic Variation Improves Chronic Lymphocytic Leukemia Risk Stratification | UKB germline variants、somatic variation/CHIP 相关信息；incident CLL 用 ICD-10 `C91.1`；PLCO 作为验证/比较队列 | 使用 Cox proportional hazards / time-to-event risk model 评估 CLL 风险分层 | 主要比较 germline PRS、somatic/CHIP 信息及联合模型对 incident CLL 的预测；模型通常纳入年龄、性别、遗传祖源/PCs 等基础协变量，并比较单独模型与联合模型 | `10.1158/0008-5472.CAN-24-4251` |
| 5 | AI-informed retinal biomarkers predict 10-year risk of onset of multiple hematological malignancies | UKB 眼底照相、视网膜血管 AI 特征、临床变量；血液肿瘤结局来自 ICD-10 诊断 | 使用 Cox survival/risk analysis 报告 RetHemo 风险组与血液肿瘤发病风险的 HR | 模型比较 RetHemo 高风险 vs 低风险与 10 年内白血病、骨髓瘤、淋巴瘤等发病；同时比较传统临床预测变量和 retinal biomarker/AI 模型的预测性能 | `10.1016/j.ejca.2025.115752` |
| 6 | Multiparameter prediction of myeloid neoplasia risk | UKB whole-exome sequencing、CH driver mutations、血常规、血生化、人口学变量；结局来自 EHR ICD-9/ICD-10；Leeds/Pavia CCUS 队列做外部验证 | 使用 Cox/time-to-event 框架建立 myeloid neoplasia 风险预测；同时使用机器学习/风险评分方法 | 主要模型整合年龄、血液学指标、CH 突变特征、遗传和临床变量预测 MN。分析重点是多参数风险预测，而不是单一暴露 Cox；外部 CCUS 队列用于验证风险模型表现 | `10.1038/s41588-023-01472-1` |
| 7 | Plasma Proteomic Signature Predicts Myeloid Neoplasm Risk | UKB Olink plasma proteomics、WES/CH、mCA、血常规、遗传 PCs；MN 结局来自 UKB cancer registries ICD-10 和 ICD-O-3 histology | 明确使用多类 Cox 模型，包括常规 Cox 和 LASSO Cox | 1. 单蛋白 Cox：每个蛋白与 incident MN 风险；2. 亚型 Cox：MPN、MDS/AML；3. 调整 CH 后 Cox；4. LASSO Cox 用于特征选择和风险预测。主要协变量包括年龄、性别、吸烟状态、采样年份、血细胞计数、遗传祖源前 10 个 PCs；CH SNV/indel 用最大 VAF 连续建模，mCA 用二分类变量 | `10.1158/1078-0432.CCR-23-3468` |
| 8 | Patterns and drivers of 43,617 mosaic chromosomal alterations in blood | UKB blood-derived whole-genome sequencing、mCA calling、SNP-array/TOPMed-imputed genotypes；CLL 结局合并 cancer registry、HES、death registry | 不是以 Cox 回归作为主要分析；主要是 mCA 发现、GWAS、风险关联和 CLL 相关分析 | CLL GWAS 中为增加病例数合并 ICD-10 `C91.1` 记录；文章重点是 mCA 模式、驱动因素、遗传关联和 CLL 风险/生存相关分析，而不是传统暴露-结局 Cox 模型 | `10.1038/s41588-026-02592-0` |

## 按 Cox 模型类型归类

### 1. 暴露-结局 Cox

代表文献：

- Early-life exposures and risk of hematological malignancies in adulthood
- Mitochondrial heteroplasmy is a risk factor for the development of chronic lymphocytic leukemia
- Plasma Proteomic Signature Predicts Myeloid Neoplasm Risk

用途：估计某个暴露或生物标志物与 incident leukemia / CLL / MN 的 HR。

### 2. 风险预测 Cox / 生存风险模型

代表文献：

- Lymphocyte count and risk of chronic lymphocytic leukemia
- Multiparameter prediction of myeloid neoplasia risk
- Integration of Germline and Somatic Variation Improves Chronic Lymphocytic Leukemia Risk Stratification
- AI-informed retinal biomarkers predict 10-year risk of onset of multiple hematological malignancies

用途：建立绝对风险模型、10 年风险模型或多参数预测模型，而不只是检验单一暴露。

### 3. LASSO Cox

代表文献：

- Plasma Proteomic Signature Predicts Myeloid Neoplasm Risk

用途：在蛋白组、CH 和临床变量中筛选最有预测价值的特征。该文使用 5-fold nested cross-validation，并重复 100 次训练/测试拆分。

### 4. 未以 Cox 为主要模型

代表文献：

- Patterns and drivers of 43,617 mosaic chromosomal alterations in blood

用途：主要做 WGS mCA calling、遗传关联、GWAS 和 CLL 病例扩充；Cox 不是核心统计模型。

## 建模时可借鉴的协变量

如果你要在 UKB 中复现类似 Cox 分析，最常见的一组基础协变量是：

```text
age
sex
smoking status
assessment center / sample collection year
genetic ancestry principal components
blood count measurements
BMI 或其他暴露相关混杂因素
```

如果研究与遗传或克隆造血相关，建议额外考虑：

```text
CHIP / CH status
maximum VAF
mCA status
mtDNA copy number
baseline lymphocyte count
baseline cancer history
```

如果研究对象是 incident CLL 或 MN，建议在 Cox 中排除：

```text
baseline 前已有相应白血病/血液肿瘤诊断者
基线后极短时间内诊断者，例如 3 个月或 1 年内诊断者，用于降低反向因果风险
```

---
