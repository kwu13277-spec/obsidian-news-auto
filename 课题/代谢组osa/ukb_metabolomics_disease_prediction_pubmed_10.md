# PubMed 检索：UKB 代谢组学通过机器学习预测疾病的近五年论文（10 篇）

检索日期：2026-05-24  
时间范围：2021-05-24 至 2026-05-24  
数据库：PubMed / NCBI E-utilities  

## 检索策略

核心检索式：

```text
((UK Biobank[Title/Abstract] OR UKB[Title/Abstract])
 AND (metabolomic[Title/Abstract] OR metabolomics[Title/Abstract] OR metabolome[Title/Abstract]
      OR metabolic profiling[Title/Abstract] OR NMR[Title/Abstract])
 AND (machine learning[Title/Abstract] OR deep learning[Title/Abstract]
      OR artificial intelligence[Title/Abstract] OR neural network[Title/Abstract]
      OR transformer[Title/Abstract] OR random forest[Title/Abstract]
      OR XGBoost[Title/Abstract] OR CatBoost[Title/Abstract]
      OR LASSO[Title/Abstract] OR elastic net[Title/Abstract])
 AND (predict[Title/Abstract] OR prediction[Title/Abstract]
      OR risk stratification[Title/Abstract] OR incident[Title/Abstract])
 AND (disease[Title/Abstract] OR cardiovascular[Title/Abstract] OR diabetes[Title/Abstract]
      OR kidney[Title/Abstract] OR dementia[Title/Abstract] OR cancer[Title/Abstract]
      OR atrial fibrillation[Title/Abstract] OR gout[Title/Abstract]
      OR eye disease[Title/Abstract] OR MASLD[Title/Abstract]))
 AND 2021/05/24:2026/05/24[Date - Publication]
```

PubMed 返回 65 条候选。下面 10 篇按三个标准筛选：

- 数据：使用 UK Biobank/UKB，且有 NMR 代谢组学或血浆/血清代谢组学特征。
- 方法：明确使用机器学习、深度学习、神经网络、Transformer、XGBoost、CatBoost、随机森林、SVM、SHAP、elastic net/LASSO 等建模方法。
- 任务：用于疾病预测、风险分层、疾病进展预测或多疾病结局预测。

## 推荐清单

| 序号 | 年份 | 疾病/结局 | 题名 | 期刊 | 机器学习/建模方法 | PMID / DOI |
|---:|---:|---|---|---|---|---|
| 1 | 2026 | 6 类常见心血管疾病 | AI-based multiomics profiling reveals complementary omics contributions to personalized prediction of cardiovascular disease | Nature Communications | multitask deep learning；代谢组 MetScore；蛋白组 ProScore | [41629312](https://pubmed.ncbi.nlm.nih.gov/41629312/) / [10.1038/s41467-026-68956-6](https://doi.org/10.1038/s41467-026-68956-6) |
| 2 | 2025 | 16 种慢性病 | MetaboLM: a metabolomic language model for multi-disease early prediction and risk stratification | Nature Communications | Transformer 代谢组语言模型；MetaboRS 风险评分 | [41339308](https://pubmed.ncbi.nlm.nih.gov/41339308/) / [10.1038/s41467-025-66163-3](https://doi.org/10.1038/s41467-025-66163-3) |
| 3 | 2022 | 24 种常见疾病 | Metabolomic profiles predict individual multidisease outcomes | Nature Medicine | neural network 学习 disease-specific metabolomic states | [36138150](https://pubmed.ncbi.nlm.nih.gov/36138150/) / [10.1038/s41591-022-01980-3](https://doi.org/10.1038/s41591-022-01980-3) |
| 4 | 2026 | 慢性肾病 | Explainable machine learning integrating biochemical and metabolomic biomarkers with conventional clinical factors improves chronic kidney disease prediction and risk stratification | BMC Nephrology | CatBoost；SHAP；可解释 biomarker risk score | [41612264](https://pubmed.ncbi.nlm.nih.gov/41612264/) / [10.1186/s12882-026-04781-9](https://doi.org/10.1186/s12882-026-04781-9) |
| 5 | 2025 | 主要不良心血管事件 | Improved prediction and risk stratification of major adverse cardiovascular events using an explainable machine learning approach combining plasma biomarkers and traditional risk factors | Cardiovascular Diabetology | JMIM 特征筛选；CatBoost；SHAP；biomarker risk score | [40176039](https://pubmed.ncbi.nlm.nih.gov/40176039/) / [10.1186/s12933-025-02711-x](https://doi.org/10.1186/s12933-025-02711-x) |
| 6 | 2024 | 糖尿病前期进展为糖尿病 | Nuclear magnetic resonance-based metabolomics with machine learning for predicting progression from prediabetes to diabetes | eLife | SVM；random forest；XGBoost；random survival forest | [39302270](https://pubmed.ncbi.nlm.nih.gov/39302270/) / [10.7554/eLife.98709](https://doi.org/10.7554/eLife.98709) |
| 7 | 2026 | 良性前列腺增生 | Plasma metabolomics identifies key metabolites and improves the prediction of benign prostatic hyperplasia | International Journal of Surgery | Elastic Net；XGBoost；SHAP | [41677327](https://pubmed.ncbi.nlm.nih.gov/41677327/) / [10.1097/JS9.0000000000004929](https://doi.org/10.1097/JS9.0000000000004929) |
| 8 | 2026 | MASLD 及共病风险 | Delineating Metabolic Dysfunction-Associated Steatotic Liver Disease and Comorbid Risk With Clinical, Blood and Metabolomic Parameters-A UK Biobank Analysis | Journal of Clinical and Experimental Hepatology | supervised learning；PLS-DA；random forest；SVM；K-means | [42078579](https://pubmed.ncbi.nlm.nih.gov/42078579/) / [10.1016/j.jceh.2026.103537](https://doi.org/10.1016/j.jceh.2026.103537) |
| 9 | 2024 | 阿尔茨海默病 | Assessing polyomic risk to predict Alzheimer's disease using a machine learning model | Alzheimer's & Dementia | tree-based methods；deep learning；SHAP；多组学模型含 metabolomics | [39511865](https://pubmed.ncbi.nlm.nih.gov/39511865/) / [10.1002/alz.14319](https://doi.org/10.1002/alz.14319) |
| 10 | 2025 | 肝硬化风险分层 | Machine learning-based plasma metabolomics for improved cirrhosis risk stratification | BMC Gastroenterology | elastic net-regularized Cox；代谢组 + APRI/FIB-4 预测模型 | [39915740](https://pubmed.ncbi.nlm.nih.gov/39915740/) / [10.1186/s12876-025-03655-y](https://doi.org/10.1186/s12876-025-03655-y) |

## 每篇重点

### 1. PMID 41629312

这篇是最符合“AI/机器学习 + 多组学 + 疾病预测”的论文之一。作者基于 UK Biobank 的 2,920 个蛋白和 168 个代谢物，提出 CardiOmicScore 多任务深度学习框架，为 6 类常见 CVD 学习蛋白组风险评分和代谢组风险评分。摘要报告 MetScore 的 C-index 为 0.64-0.74，并可与临床数据结合提升发病前最长 15 年的个体化风险预测。

### 2. PMID 41339308

MetaboLM 是 transformer-based metabolomic language model，使用 83,744 名 UKB 相对健康参与者的血浆代谢组数据预训练，再针对 16 种慢性病微调。文章核心贡献是把代谢组学数据作为序列/语言建模对象，生成 MetaboRS，用于 10 年以上提前预测疾病风险。

### 3. PMID 36138150

这是该方向的基础性论文。作者使用 UKB 中 117,981 名参与者的 168 个循环代谢标志物，训练神经网络学习疾病特异性代谢状态，预测 24 种常见疾病，并在 4 个独立队列验证。适合作为“代谢组机器学习预测多疾病”的经典起点。

### 4. PMID 41612264

这篇聚焦 CKD。研究使用 233,589 名基线无 CKD 的 UKB 参与者，整合生化与代谢组标志物、传统临床因素，使用 CatBoost 和 SHAP 构建可解释风险分层工具，并在英格兰开发队列与苏格兰/威尔士验证队列评估判别和校准。

### 5. PMID 40176039

这篇研究 MACE 新发风险。作者结合传统风险因素、生化和代谢组 biomarker，使用 JMIM 进行特征选择，并通过 CatBoost 与 SHAP 确定二元阈值，构建 Biomarker Risk Score。适合用于比较“传统风险模型 vs 可解释机器学习 + 代谢组标志物”的增益。

### 6. PMID 39302270

这篇非常直接地符合题目。研究对象为 13,489 名 UKB 糖尿病前期参与者，使用 NMR 代谢组学，采用 SVM、随机森林、XGBoost 选择代谢物面板，并用 Cox 与 random survival forest 验证糖尿病进展预测能力。

### 7. PMID 41677327

这篇研究良性前列腺增生。作者使用 78,724 名 UKB 参与者的 NMR 血浆代谢组数据，先用 Elastic Net 和逐步回归筛选关键代谢物，再用 XGBoost 做风险预测，并用 SHAP 解释特征重要性。

### 8. PMID 42078579

这篇研究 MASLD 风险和共病风险分层。摘要明确使用 multivariate supervised learning，模型包括 PLS-DA、random forest、support vector machine、logistic regression，并用 K-means 聚类识别 MASLD 亚型。代谢组特征作为临床、遗传、血液、生化特征的一部分进入预测框架。

### 9. PMID 39511865

这篇针对阿尔茨海默病，使用 UK Biobank 的基因组、蛋白组、代谢组和用药数据训练多组学预测模型。方法包括 tree-based 和 deep learning，并用 SHAP 解释特征重要性。虽然最强预测特征来自 APOE/蛋白组，但 metabolomics 是模型输入模态之一。

### 10. PMID 39915740

这篇标题直接为 machine learning-based plasma metabolomics，使用 UKB 的 1H-NMR 血清代谢组数据，通过 elastic net-regularized Cox 模型做慢性肝病患者肝硬化风险分层，并评估代谢组与 FIB-4/APRI 联合后的预测提升。

## 优先阅读顺序

如果只读 5 篇，建议：

1. PMID 36138150：神经网络 + 多疾病预测的基础论文。
2. PMID 41339308：Transformer/语言模型范式。
3. PMID 41629312：深度学习多组学 CVD 个体化预测。
4. PMID 39302270：机器学习代谢组预测糖尿病进展，方法最直接。
5. PMID 41612264：CatBoost/SHAP 可解释机器学习预测 CKD。

---
