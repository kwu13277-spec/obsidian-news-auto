# PubMed 中 UK Biobank 白血病定义相关文献整理

检索主题：PubMed 中使用 UK Biobank 数据、并涉及白血病或血液肿瘤定义的研究。

整理重点：这些研究如何用 UK Biobank 数据定义白血病、白血病亚型或相关血液肿瘤结局，并记录 DOI。

检索/整理日期：2026-06-02

## 总体规律

多数 UK Biobank 研究不是主要依赖问卷自报来定义白血病，而是使用 linked health records，尤其是 cancer registry、hospital inpatient records 和 death registry。

常用 UKB 字段包括：

- cancer registry ICD-10 cancer code：Data-Field `40006`
- cancer registry ICD-9 cancer code：Data-Field `40013`
- cancer registry ICD-O-3 histology code：Data-Field `40011`

常见白血病定义：

- 白血病大类：ICD-10 `C91-C95`；ICD-9 `204-208`
- AML：ICD-10 `C92.0` 或 `C920`；ICD-9 `2050`
- CLL：ICD-10 `C91.1` 或 `C911`；ICD-9 `204.1` 或 `2041`
- CLL/SLL 合并表型：ICD-10 `C91.1` + `C83.0`

## 文献表

| 序号  |                                                                                                                                           文献 |     PMID | 白血病/血液肿瘤定义方式                                                                                                                                                                                                | DOI                             |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------: | -------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 1   | Early-life exposures and risk of hematological malignancies in adulthood: a cohort study, meta-analysis and Mendelian randomization analysis | 41063022 | 补充表定义：Leukemia = ICD-9 `204, 205, 206, 207, 208`；ICD-10 `C91, C92, C93, C94, C95`。AML = ICD-9 `2050`，ICD-10 `C920`。CLL = ICD-9 `2041`，ICD-10 `C911`。                                                        | `10.1186/s12885-025-14780-y`    |
| 2   |                                                                                    Lymphocyte count and risk of chronic lymphocytic leukemia | 41324573 | CLL 病例来自 UK Biobank linked national cancer registries。定义为 ICD-10 `C911` 和 `C830`，即 CLL 与 SLL 合并表型。                                                                                                          | `10.1093/jnci/djaf338`          |
| 3   |                                              Mitochondrial heteroplasmy is a risk factor for the development of chronic lymphocytic leukemia | 41708630 | CLL 使用 cancer registry 的 ICD-9 `204.1` 和 ICD-10 `C91.1` 定义；排除既往 CLL，以及基线淋巴细胞计数 > 5000/µL 的参与者。                                                                                                              | `10.1038/s41467-026-69861-8`    |
| 4   |                                      Integration of Germline and Somatic Variation Improves Chronic Lymphocytic Leukemia Risk Stratification | 40305105 | Incident CLL 定义为入组后出现任意 ICD-10 `C91.1` 诊断；UK Biobank 与 PLCO 队列使用同一 ICD-10 定义。                                                                                                                               | `10.1158/0008-5472.CAN-24-4251` |
| 5   |                                          AI-informed retinal biomarkers predict 10-year risk of onset of multiple hematological malignancies | 40925094 | UKB 血液肿瘤按 ICD-10 定义。Leukemia 包括 lymphoid leukemia `C91` 与 myeloid leukemia `C92`；细分编码包括 `C910-C919`、`C920-C929`。                                                                                            | `10.1016/j.ejca.2025.115752`    |
| 6   |                                                                                          Multiparameter prediction of myeloid neoplasia risk | 37620601 | 通过电子健康记录中的 ICD-9/ICD-10 定义 myeloid neoplasia。AML 包括 ICD-9 `205.0/205.2/205.3/205.8/205.9/206.0/206.2/207.0/207.2/238.4/238.5/238.7`，ICD-10 `C92.0-C92.9`、`C93.0`、`C93.2`、`C94.0`、`C94.2`。同时定义 MDS、MPN、CMML。 | `10.1038/s41588-023-01472-1`    |
| 7   |                                                                                    Plasma Proteomic Signature Predicts Myeloid Neoplasm Risk | 38446993 | Myeloid neoplasm 由 UKB cancer registry 的 ICD-10 `40006` 和 ICD-O-3 histology `40011` 定义。AML 包括 ICD-10 `C92`，但排除 `C92.3`，并包括 `C93`、`C94`。                                                                     | `10.1158/1078-0432.CCR-23-3468` |
| 8   |                                                                       Patterns and drivers of 43,617 mosaic chromosomal alterations in blood | 42156563 | 为 CLL GWAS 增加病例数，将 cancer registry、hospital episode statistics 和 death registry 中所有 ICD-10 `C91.1` 记录合并；得到 1,502 个 CLL 病例。                                                                                  | `10.1038/s41588-026-02592-0`    |

## 可复用定义建议

如果研究目标是“白血病大类”，可以参考文献 1 的定义：

```text
ICD-10: C91-C95
ICD-9: 204-208
```

如果研究目标是 CLL，建议根据研究问题选择：

```text
严格 CLL:
ICD-10 C91.1 / C911
ICD-9 204.1 / 2041

CLL/SLL 合并:
ICD-10 C91.1 + C83.0
```

如果希望提高病例捕获率，可以参考文献 8，将以下来源合并：

```text
cancer registry
hospital inpatient records / HES
death registry
```

如果研究目标是 AML 或 myeloid neoplasia，建议优先参考文献 6 和文献 7，因为它们对髓系肿瘤亚型定义更细。

## 注意事项

- UKB 中同一个 ICD-10 编码有时写成带点格式，例如 `C91.1`，有时写成无点格式，例如 `C911`；二者含义相同，需要按具体数据字段格式处理。
- CLL 与 SLL 在流行病学研究中常被合并，因为二者属于同一疾病谱；如果只研究 CLL，需要说明是否排除 `C83.0`。
- 白血病大类 `C91-C95` 会包含淋巴细胞白血病、髓系白血病、单核细胞白血病、其他指定白血病和未明示白血病；若研究机制或遗传风险，最好按亚型拆分。
- 使用 cancer registry 可提高诊断特异性；合并住院和死亡登记可提高敏感性，但需要在方法中说明数据来源优先级和去重规则。

---
