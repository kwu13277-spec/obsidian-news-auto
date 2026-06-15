# Omega-6、CHIP 与类风湿关节炎风险课题解读

## 文献与数据基础

- 课题名称
  - Omega-6 脂肪酸与克隆性造血 CHIP 的交互作用对类风湿关节炎 RA 发病风险的影响。[总结]
- 研究主线
  - 在基线具有 Omega-6、CHIP、RA 结局和随访时间信息的人群中，先评估 Omega-6 与 RA 风险的关系，再检验 CHIP 是否修饰这一关系。[出处: statistical_analysis_plan.md; result_structure_recommendation.md]
- 当前最稳妥的论文叙事
  - `Omega-6 -> RA` 是主效应问题。
  - `Omega-6 × CHIP -> RA` 是核心效应修饰问题。
  - `CHIP -> RA` 是支持性结果，用于说明 CHIP 本身具有临床相关性。
  - 基因层面、small/large CHIP、M05/M06、排除前 2 年发病等结果更适合放在补充材料或敏感性分析中。[出处: result_structure_recommendation.md]
- 当前分析材料的版本差异
  - `3analysis_results` 中最新基线表显示总体样本量为 `255,546`，其中 no CHIP 为 `234,967`，any CHIP 为 `20,579`。[出处: baseline/baseline_table_final_output.docx]
  - RCS 分析中清洗后样本量为 `255,237`，RA 事件数为 `3,468`。[出处: cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx; 0scripts_code/Omega6_RA_RCS_Analysis.R]
  - logistic 交互分析中纳入 `254,619` 名受试者，RA 事件 `3,446` 例。[出处: interaction/总效应分析/Interaction_Analysis.docx]
  - 早期汇报文档中曾出现 `178,871` 的样本量，因此正式写作前需要确认最终数据版本。[待复核][出处: 1cohort_core_files/数据分析与研究结果汇报.docx]

## 课题背景

- RA 是研究结局
  - 类风湿关节炎是一类慢性自身免疫性疾病，核心病理过程包括滑膜炎、系统性炎症和关节破坏。[总结]
  - 该课题使用 ICD-10 诊断记录构建 RA 结局，且部分材料区分 M05 与 M06 两类 RA 亚型。[出处: 1cohort_core_files/数据分析与研究结果汇报.docx]
- Omega-6 是主要暴露
  - Omega-6 脂肪酸在传统炎症生物学中常被视为花生四烯酸和类二十烷酸等炎症介质的前体。
  - 但当前项目结果显示，循环 Omega-6 水平在总体人群中与 RA 风险降低相关，提示它在真实人群中的作用并非简单“促炎”。[总结][出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx]
- CHIP 是效应修饰因素
  - CHIP 指造血干/祖细胞获得体细胞突变后发生克隆性扩增，但尚未达到血液肿瘤诊断标准的状态。[总结]
  - 课题中 CHIP 被作为免疫系统背景状态，用于检验同样的 Omega-6 水平在 CHIP 携带者和非携带者中的 RA 风险是否不同。[出处: statistical_analysis_plan.md]
- 核心科学问题
  - Omega-6 与后续 RA 风险是否相关。
  - 这种相关是否呈非线性或剂量-反应关系。
  - CHIP 是否改变 Omega-6 与 RA 之间的风险关系。
  - 如果存在修饰作用，风险差异主要来自 any CHIP、small CHIP、large CHIP，还是特定驱动基因。[总结]
- 核心假说
  - 在无 CHIP 人群中，较高 Omega-6 可能与较低 RA 风险相关。
  - 在 CHIP 携带者中，克隆性造血相关的炎症背景可能削弱或改变 Omega-6 的保护性关联。[推断][出处: 1cohort_core_files/数据分析与研究结果汇报.docx; interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]

## 整体研究框架

- Step 1：构建研究队列
  - 目标是获得同时具备 Omega-6、CHIP、RA 状态、随访时间和主要协变量的分析人群。
  - 主要数据来源包括 UK Biobank 相关的全外显子测序、NMR 代谢组学、诊断记录和基线协变量。[总结][出处: 1cohort_core_files/数据分析与研究结果汇报.docx]
  - 最新基线表纳入 `255,546` 人，其中 any CHIP 携带者 `20,579` 人，占约 `8.1%`。[出处: baseline/baseline_table_final_output.docx]
- Step 2：描述队列基线特征
  - 目标是说明 CHIP 携带者与非携带者在人口学、BMI、社会经济状态、活动水平和 RA 事件上的差异。
  - 这一步为后续模型调整提供依据，尤其是年龄、性别、BMI、Townsend 等混杂因素。[总结][出处: baseline/baseline_table_final_output.docx; statistical_analysis_plan.md]
- Step 3：检验 Omega-6 与 RA 的主效应
  - 目标是判断 Omega-6 本身是否与 RA 风险相关。
  - 使用 Cox 比例风险模型，把 Omega-6 按五分位分组，以 Q1 为参照，逐步调整协变量。[出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx; 0scripts_code/Omega6_CHIP_COX_quintile.R]
- Step 4：检验 Omega-6 与 RA 的非线性关系
  - 目标是判断 Omega-6 的作用是否可以用线性关系概括。
  - 使用 restricted cubic spline，设置 5 个节点，并以第 25 百分位数作为参考值。[出处: cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx; 0scripts_code/Omega6_RA_RCS_Analysis.R]
- Step 5：检验 CHIP 与 RA 的关联
  - 目标是确认 CHIP 本身是否与 RA 风险相关。
  - 先做无协变量 Cox，再做调整年龄和性别后的 Cox，分析 any CHIP、small CHIP、large CHIP 以及主要突变基因。[出处: cox/CHIP_AND_RA/cox_univariate_results.docx; cox/CHIP_AND_RA/cox_multivariate_results.docx]
- Step 6：检验 Omega-6 与 CHIP 的交互作用
  - 目标是回答 CHIP 是否修饰 Omega-6 与 RA 的关系。
  - 交互项分析使用 logistic 回归报告 OR。
  - 分层和联合暴露分析使用 Cox 模型报告 HR。
  - 这种混合分析框架能从“统计交互”和“风险格局”两个角度解释结果，但正式论文中需要清楚区分 OR 与 HR。[总结][出处: interaction/总效应分析/Interaction_Analysis.docx; interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- Step 7：扩展到 CHIP 负荷和基因层面
  - 目标是判断交互信号是否主要由 small CHIP、large CHIP 或特定突变基因驱动。
  - 当前结果提示 small CHIP 的交互更明显，而 large CHIP 的交互不明显。[出处: interaction/交互作用/HR/RA/small_CHIP_HR_RA/joint_analyse.docx; interaction/交互作用/HR/RA/large_CHIP_HR_RA/joint_analyse.docx]
- Step 8：进行敏感性和探索性分析
  - 目标是评估结果是否受早期发病、RA 亚型定义、CHIP 负荷、基因多重比较或替代模型影响。
  - 当前目录包含 HR_2years、M05RA、M06RA、单基因交互和 GO 富集等结果，建议作为补充材料组织。[出处: result_structure_recommendation.md]

## 研究对象与变量定义

- 研究对象
  - 最新基线描述中总体样本为 `255,546` 人。[出处: baseline/baseline_table_final_output.docx]
  - RCS 分析在剔除 Townsend 缺失和关键变量缺失后保留 `255,237` 人。[出处: cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx; 0scripts_code/Omega6_RA_RCS_Analysis.R]
  - 交互 logistic 分析纳入 `254,619` 人。[出处: interaction/总效应分析/Interaction_Analysis.docx]
- 主要暴露变量
  - `Omega.6.Fatty.Acids` 是主要暴露变量。
  - 分析中使用了连续变量、五分位分组、三分位分组和 RCS 曲线几种编码方式。[出处: statistical_analysis_plan.md; cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx; interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- 效应修饰变量
  - `CHIP` 是主要效应修饰变量。
  - 扩展变量包括 `small_CHIP`、`large_CHIP` 和具体驱动基因，如 DNMT3A、TET2、ATM、TP53、ASXL1、PPM1D、JAK2、SRSF2 等。[出处: cox/CHIP_AND_RA/cox_multivariate_results.docx]
  - 早期汇报中将 small CHIP 定义为 VAF `< 10%`，large CHIP 定义为 VAF `>= 10%`。[出处: 1cohort_core_files/数据分析与研究结果汇报.docx]
- 结局变量
  - 主要结局为 RA 状态，脚本中使用 `RA.status` 表示事件变量。
  - Cox 模型使用 `followup_years` 作为随访时间变量。[出处: 0scripts_code/Omega6_RA_RCS_Analysis.R; 0scripts_code/CHIP_AND_RA_AGE_SEX_BMI_TOMSEND_COX.R]
  - 是否已经严格排除基线既往 RA，需要以最终清洗脚本和分析数据版本复核。[待复核]
- 协变量
  - 主要协变量包括年龄、性别、BMI 和 Townsend 剥夺指数。
  - 部分方案文件还建议扩展纳入吸烟、饮酒、种族、教育、糖尿病、高血压、心血管病和药物/补充剂使用情况，但当前核心结果主要集中在 age、sex、BMI、Townsend。[出处: statistical_analysis_plan.md; 0scripts_code/Omega6_RA_RCS_Analysis.R; 0scripts_code/Omega6_CHIP_COX_quintile.R]

## 研究方法

- 描述性统计
  - 目的
    - 描述总体人群、no CHIP 人群和 any CHIP 人群的基线差异。
  - 方法
    - 分类变量用人数和百分比表示。
    - 连续变量用均值和标准差表示。
    - 组间差异报告 P 值。[出处: baseline/baseline_table_final_output.docx]
  - 关键作用
    - 判断 CHIP 携带者是否更年长、代谢状态是否不同、RA 事件比例是否更高。
- Omega-6 五分位 Cox 分析
  - 目的
    - 检验不同 Omega-6 水平组与 RA 风险的关系。
  - 暴露编码
    - 将 Omega-6 按五分位分为 Q1 到 Q5。
    - Q1 作为参考组。
  - 模型设置
    - Model 1 调整 Age 和 Sex。
    - Model 2 在 Model 1 基础上加入 Townsend。
    - Model 3 在 Model 2 基础上加入 BMI。[出处: 0scripts_code/Omega6_CHIP_COX_quintile.R]
  - 结果报告
    - 报告 HR、95% CI 和 P 值。
- RCS 非线性分析
  - 目的
    - 检验 Omega-6 与 RA 风险是否存在非线性剂量-反应关系。
  - 模型设置
    - 使用 Cox 模型。
    - 使用 `rcs(Omega.6.Fatty.Acids, 5)` 设置 5 个样条节点。
    - 参考值为 Omega-6 第 25 百分位数 `4.04290`。
    - 调整 Age、Sex、BMI、Townsend。[出处: 0scripts_code/Omega6_RA_RCS_Analysis.R]
  - 结果报告
    - 报告不同百分位点的 HR。
    - 报告总体关联 P 值和非线性 P 值。[出处: cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx]
- CHIP 与 RA 的 Cox 分析
  - 目的
    - 检验 CHIP 是否独立关联 RA 风险。
  - 分析层次
    - any CHIP。
    - small CHIP 与 large CHIP。
    - 单基因突变。
  - 模型设置
    - 单变量 Cox 不调整协变量。
    - 多变量 Cox 至少调整 Age 和 Sex。[出处: cox/CHIP_AND_RA/cox_univariate_results.docx; cox/CHIP_AND_RA/cox_multivariate_results.docx]
- Omega-6 与 CHIP 的乘法交互分析
  - 目的
    - 检验 `Omega-6 × CHIP` 是否显著影响 RA 风险。
  - logistic 模型
    - 因变量为 RA 状态。
    - 自变量包括 Omega-6、CHIP、二者交互项、年龄、性别和 BMI。[出处: interaction/总效应分析/Interaction_Analysis.docx; 0scripts_code/omega6_CHIP_RA_INTERACTION.R]
  - 结果报告
    - 交互项报告 OR、95% CI 和 P 值。
    - 该结果反映 odds 层面的乘法交互，不等同于时间到事件模型中的 HR 交互。[总结]
- Omega-6 三分位分层 Cox 分析
  - 目的
    - 在低、中、高 Omega-6 水平内分别估计 CHIP 对 RA 的 HR。
  - 分组方式
    - Low、Medium、High 三组，每组 `84,873` 人。
    - Low 范围为 `1.0053 - 4.1962`。
    - Medium 范围为 `4.1962 - 4.7642`。
    - High 范围为 `4.7642 - 16.4110`。[出处: interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
  - 结果解释
    - 如果 CHIP 在高 Omega-6 组中的 HR 更高，说明高 Omega-6 的保护性关联可能在 CHIP 携带者中被削弱。
- 联合暴露分析
  - 目的
    - 把 Omega-6 三分位和 CHIP 状态组合起来，构建 6 个风险组。
  - 参考组
    - Low Omega-6 + Non-Carrier 作为参照。
  - 解释重点
    - 比较 High Omega-6 + Non-Carrier 与 High Omega-6 + Carrier 的风险差异。
    - 该比较最直观地展示“同样高 Omega-6 状态下，CHIP 是否改变风险格局”。[总结][出处: interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]

## 主要研究结果

- 基线特征
  - 总体样本为 `255,546` 人。
  - no CHIP 为 `234,967` 人。
  - any CHIP 为 `20,579` 人。
  - RA 事件总数为 `3,471`，总体比例约 `1.4%`。
  - no CHIP 组 RA 为 `3,113` 例，比例约 `1.3%`。
  - any CHIP 组 RA 为 `358` 例，比例约 `1.7%`。
  - 平均随访时间为 `15.41` 年。
  - any CHIP 组平均随访时间略短，为 `15.17` 年；no CHIP 组为 `15.43` 年。[出处: baseline/baseline_table_final_output.docx]
- 基线差异的含义
  - any CHIP 人群中 RA 比例更高，提示 CHIP 与 RA 风险存在初步相关。
  - BMI 分组在 CHIP 状态间有统计学差异，肥胖比例在 any CHIP 组为 `24.8%`，no CHIP 组为 `24.2%`。
  - 体力活动、学历和种族分布也存在差异，因此后续模型调整是必要的。[总结][出处: baseline/baseline_table_final_output.docx]

## Omega-6 与 RA 的主效应结果

- 五分位 Cox 结果
  - 在 Model 3 中，Q2 相对 Q1 的 HR 为 `0.966 (0.870-1.072)`，P = `0.5142`。
  - 在 Model 3 中，Q3 相对 Q1 的 HR 为 `0.886 (0.797-0.986)`，P = `0.0265`。
  - 在 Model 3 中，Q4 相对 Q1 的 HR 为 `0.784 (0.703-0.874)`，P `< 0.001`。
  - 在 Model 3 中，Q5 相对 Q1 的 HR 为 `0.846 (0.761-0.941)`，P = `0.0020`。[出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx]
- 主效应解读
  - 中高 Omega-6 分位组的 RA 风险低于最低分位组。
  - Q4 的风险最低，Q5 仍显著低于 Q1，但低于 Q4 的保护幅度。
  - 这提示 Omega-6 与 RA 之间可能不是简单线性关系，而是存在平台期、阈值或 U/J 型趋势。[总结][出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx]
- RCS 结果
  - 以第 25 百分位数 `4.04290` 为参考。
  - 第 5 百分位数 `3.45960` 的 HR 为 `1.43 (1.27, 1.61)`。
  - 第 50 百分位数 `4.47200` 的 HR 为 `1.26 (1.14, 1.39)`。
  - 第 75 百分位数 `4.93750` 的 HR 为 `1.12 (1.02, 1.23)`。
  - 第 95 百分位数 `5.70622` 的 HR 为 `1.18 (1.06, 1.30)`。
  - 总体关联 P 值为 `0.0000`。
  - 非线性 P 值为 `0.0042`。[出处: cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx]
- RCS 解读
  - Omega-6 与 RA 风险存在显著总体关联。
  - 非线性 P 值显著，说明不能只用“每增加 1 单位 Omega-6 风险线性降低”概括全部结果。
  - 五分位 Cox 与 RCS 的共同信息是，Omega-6 的风险关系有明显形状特征，需要在结果中用图展示，而不是只报告单个 HR。[总结]

## CHIP 与 RA 的结果

- 单变量 Cox 结果
  - any CHIP 与 RA 风险升高相关，HR = `1.334 (1.196-1.488)`，P `< 0.001`。
  - small CHIP 与 RA 风险升高相关，HR = `1.363 (1.197-1.551)`，P `< 0.001`。
  - large CHIP 与 RA 风险升高相关，HR = `1.230 (1.018-1.486)`，P = `0.0316`。
  - DNMT3A 在单变量模型中显著，HR = `1.311 (1.122-1.532)`，P `< 0.001`。
  - ATM 在单变量模型中显著，HR = `1.449 (1.080-1.945)`，P = `0.0134`。
  - SRSF2 在单变量模型中显著，HR = `2.158 (1.160-4.015)`，P = `0.0151`。[出处: cox/CHIP_AND_RA/cox_univariate_results.docx]
- 多变量 Cox 结果
  - any CHIP 调整后仍显著，HR = `1.209 (1.084-1.350)`，P `< 0.001`。
  - small CHIP 调整后仍显著，HR = `1.249 (1.097-1.422)`，P `< 0.001`。
  - large CHIP 调整后不显著，HR = `1.104 (0.913-1.334)`，P = `0.3070`。
  - ATM 调整后仍显著，HR = `1.450 (1.081-1.946)`，P = `0.0132`。
  - SRSF2 调整后仍显著，HR = `2.004 (1.077-3.729)`，P = `0.0282`。
  - DNMT3A 调整后不显著，HR = `1.123 (0.960-1.313)`，P = `0.1459`。[出处: cox/CHIP_AND_RA/cox_multivariate_results.docx]
- CHIP 结果解读
  - any CHIP 与 RA 风险升高具有较稳定的关联。
  - small CHIP 的信号比 large CHIP 更稳健，这与后续交互分析中 small CHIP 更明显的结果一致。
  - 单基因结果中 ATM 和 SRSF2 的信号值得注意，但由于基因层面分析涉及多重比较和较少事件数，正式结论应谨慎。[总结]

## Omega-6 与 CHIP 的交互结果

- logistic 交互结果
  - Omega-6 主效应 OR = `0.90 (0.86, 0.95)`，P `< 0.001`。
  - CHIP 主效应 OR = `0.58 (0.28, 1.20)`，P = `0.14`。
  - `Omega.6.Fatty.Acids * CHIP` 交互项 OR = `1.17 (1.00, 1.37)`，P = `0.045`。[出处: interaction/总效应分析/Interaction_Analysis.docx]
- logistic 交互解读
  - Omega-6 的 OR 小于 1，说明在总体 logistic 模型中较高 Omega-6 与较低 RA odds 相关。
  - 交互项 OR 大于 1，说明 CHIP 存在时，Omega-6 的保护性关联被削弱。
  - P = `0.045` 属于边界显著，不能过度表述为强交互，应表述为“提示存在效应修饰”。[总结]
- 三分位分层 Cox 结果
  - Low Omega-6 组中，CHIP 调整后 HR = `1.12 (0.93-1.36)`，P = `0.245`。
  - Medium Omega-6 组中，CHIP 调整后 HR = `1.11 (0.91-1.36)`，P = `0.298`。
  - High Omega-6 组中，CHIP 调整后 HR = `1.41 (1.18-1.69)`，P `< 0.001`。[出处: interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- 分层 Cox 解读
  - 在高 Omega-6 人群中，CHIP 携带者的 RA 风险明显高于非携带者。
  - 该结果支持“CHIP 改变高 Omega-6 背景下的风险格局”这一叙事。
  - 但分层 Cox 结果检验的是 Omega-6 分层内 CHIP 的 HR，不等同于 Cox 模型中的正式交互项检验。[总结]
- 联合暴露 Cox 结果
  - 参照组为 Low Omega-6 + Non-Carrier。
  - Medium Omega-6 + Non-Carrier 调整后 HR = `0.89 (0.82-0.97)`，P = `0.009`。
  - High Omega-6 + Non-Carrier 调整后 HR = `0.80 (0.74-0.88)`，P `< 0.001`。
  - Low Omega-6 + Carrier 调整后 HR = `1.13 (0.94-1.37)`，P = `0.199`。
  - Medium Omega-6 + Carrier 调整后 HR = `0.98 (0.80-1.19)`，P = `0.821`。
  - High Omega-6 + Carrier 调整后 HR = `1.13 (0.94-1.36)`，P = `0.182`。[出处: interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- 联合暴露解读
  - 在非携带者中，高 Omega-6 组风险明显降低。
  - 在 CHIP 携带者中，高 Omega-6 组并未显示相同的风险降低。
  - 最适合正文呈现的对比是 High Omega-6 + Non-Carrier 的 HR `0.80` 与 High Omega-6 + Carrier 的 HR `1.13`。
  - 这说明高 Omega-6 的低风险格局主要出现在非 CHIP 人群中。[总结]

## small CHIP 与 large CHIP 交互结果

- small CHIP logistic 交互
  - 调整后 `small_CHIP1:Omega.6.Fatty.Acids` OR = `1.22 (1.01-1.47)`，P = `0.035`。[出处: interaction/交互作用/HR/RA/small_CHIP_HR_RA/joint_analyse.docx]
- small CHIP 分层 Cox
  - High Omega-6 组中 small CHIP 调整后 HR = `1.53 (1.24-1.88)`，P `< 0.001`。
  - Low Omega-6 组中 small CHIP 调整后 HR = `1.12 (0.89-1.41)`，P = `0.346`。
  - Medium Omega-6 组中 small CHIP 调整后 HR = `1.11 (0.87-1.41)`，P = `0.406`。[出处: interaction/交互作用/HR/RA/small_CHIP_HR_RA/joint_analyse.docx]
- small CHIP 联合暴露
  - High Omega-6 + Non-Carrier 调整后 HR = `0.80 (0.74-0.88)`，P `< 0.001`。
  - High Omega-6 + Carrier 调整后 HR = `1.23 (1.00-1.51)`，P = `0.054`。[出处: interaction/交互作用/HR/RA/small_CHIP_HR_RA/joint_analyse.docx]
- small CHIP 解读
  - small CHIP 是当前交互结果中最值得作为补充重点的部分。
  - 它既有显著 logistic 交互项，也在高 Omega-6 分层中显示较强的 Cox HR。
  - 这提示早期或较小克隆负荷状态下，代谢暴露与克隆性造血背景的关系可能更容易被观察到。[推断]
- large CHIP logistic 交互
  - 调整后 `large_CHIP1:Omega.6.Fatty.Acids` OR = `1.06 (0.81-1.38)`，P = `0.683`。[出处: interaction/交互作用/HR/RA/large_CHIP_HR_RA/joint_analyse.docx]
- large CHIP 分层 Cox
  - High Omega-6 组中 large CHIP 调整后 HR = `1.12 (0.80-1.56)`，P = `0.516`。[出处: interaction/交互作用/HR/RA/large_CHIP_HR_RA/joint_analyse.docx]
- large CHIP 解读
  - large CHIP 当前没有提供明确交互证据。
  - 如果写作空间有限，large CHIP 更适合放补充材料，而不是正文重点。[总结]

## 单基因交互结果

- DNMT3A
  - 调整后 logistic 交互项 OR = `1.22 (0.97-1.51)`，P = `0.083`。
  - High Omega-6 组中 DNMT3A 调整后 HR = `1.39 (1.09-1.78)`，P = `0.009`。
  - High Omega-6 + DNMT3A carrier 调整后联合暴露 HR = `1.13 (0.88-1.45)`，P = `0.334`。[出处: interaction/交互作用/HR/RA/DNMT3A_HR_RA/joint_analyse.docx]
  - 解读
    - DNMT3A 有边界交互信号和高 Omega-6 分层信号，但联合暴露调整后不显著。
    - 适合作为探索性机制线索，而不是主结论。[总结]
- TET2
  - 调整后 logistic 交互项 OR = `1.31 (0.94-1.81)`，P = `0.101`。
  - High Omega-6 组中 TET2 调整后 HR = `1.25 (0.85-1.85)`，P = `0.254`。[出处: interaction/交互作用/HR/RA/TET2_HR_RA/joint_analyse.docx]
  - 解读
    - TET2 方向上与假说一致，但统计证据不足。[总结]
- ATM
  - 调整后 logistic 交互项 OR = `0.79 (0.51-1.22)`，P = `0.302`。
  - Low Omega-6 组中 ATM 调整后 HR = `2.03 (1.33-3.10)`，P `< 0.001`。
  - Low Omega-6 + ATM carrier 调整后联合暴露 HR = `2.03 (1.33-3.10)`，P `< 0.001`。
  - High Omega-6 + ATM carrier 调整后联合暴露 HR = `1.15 (0.68-1.95)`，P = `0.602`。[出处: interaction/交互作用/HR/RA/ATM_HR_RA/joint_analyse.docx]
  - 解读
    - ATM 的信号不是典型“高 Omega-6 下风险更高”，而是“低 Omega-6 + ATM carrier”风险更高。
    - 这提示不同 CHIP 驱动基因可能具有不同的脂质代谢-免疫交互模式。[推断]
- TP53
  - 调整后 logistic 交互项 OR = `0.91 (0.44-1.81)`，P = `0.795`。
  - High Omega-6 组中 TP53 调整后 HR = `0.77 (0.32-1.86)`，P = `0.568`。[出处: interaction/交互作用/HR/RA/TP53_HR_RA/joint_analyse.docx]
  - 解读
    - 当前结果不支持 TP53 作为主要交互来源。[总结]
- ASXL1
  - 调整后 logistic 交互项 OR = `0.80 (0.44-1.45)`，P = `0.478`。
  - High Omega-6 组中 ASXL1 调整后 HR = `1.14 (0.54-2.40)`，P = `0.730`。[出处: interaction/交互作用/HR/RA/ASXL1_HR_RA/joint_analyse.docx]
  - 解读
    - 当前结果不支持 ASXL1 作为主要交互来源。[总结]
- PPM1D
  - 调整后 logistic 交互项 OR = `1.20 (0.56-2.44)`，P = `0.624`。
  - Low Omega-6 组中 PPM1D 调整后 HR = `1.65 (0.74-3.67)`，P = `0.223`。
  - High Omega-6 组中 PPM1D 调整后 HR = `1.42 (0.59-3.43)`，P = `0.431`。[出处: interaction/交互作用/HR/RA/PPM1D_HR_RA/joint_analyse.docx]
  - 解读
    - 当前结果方向不稳定且置信区间宽，提示统计效能不足。[总结]

## Omega-6 与 CHIP 发生风险的补充结果

- any CHIP
  - Omega-6 五分位与 CHIP 风险呈负相关趋势。
  - Model 3 中，Q5 相对 Q1 的 HR = `0.857 (0.820-0.895)`，P `< 0.001`。[出处: cox/OMEGA6_AND_CHIP/cox_omega6_chip_results.docx]
- small CHIP
  - Model 3 中，Q5 相对 Q1 的 HR = `0.878 (0.832-0.927)`，P `< 0.001`。[出处: cox/OMEGA6_AND_CHIP/cox_omega6_small_chip_results.docx]
- large CHIP
  - Model 3 中，Q5 相对 Q1 的 HR = `0.815 (0.755-0.879)`，P `< 0.001`。[出处: cox/OMEGA6_AND_CHIP/cox_omega6_large_chip_results.docx]
- 结果定位
  - 这部分回答的是 Omega-6 是否与 CHIP 状态相关。
  - 它不直接回答 Omega-6 与 CHIP 是否共同影响 RA。
  - 建议放在补充材料或机制探索部分，不作为正文主线。[总结][出处: result_structure_recommendation.md]

## 机制解释框架

- 总体机制假说
  - Omega-6 在普通人群中可能与较低 RA 风险相关。
  - CHIP 携带者的髓系免疫细胞可能处于促炎或预激活状态，从而改变 Omega-6 相关脂质介质的免疫效应。[推断]
- 为什么 CHIP 可能削弱 Omega-6 的保护性关联
  - CHIP 相关突变可能改变单核细胞和巨噬细胞的炎症阈值。
  - 当免疫细胞已经由克隆性造血驱动进入促炎状态时，同样的脂质底物可能不再产生普通人群中的低风险关联。[推断]
- 为什么 small CHIP 信号更值得关注
  - small CHIP 调整后交互项显著，而 large CHIP 不显著。
  - 一种合理解释是，早期克隆扩增阶段仍更容易受到代谢环境影响。
  - 另一种可能是 large CHIP 样本或事件数不足，导致估计不稳定。[推断]
- 为什么 ATM 结果需要单独解释
  - ATM 结果显示低 Omega-6 + ATM carrier 风险较高。
  - 这不同于 any CHIP 和 small CHIP 中更关注高 Omega-6 组的模式。
  - 因此单基因结果不宜被简单合并为“所有 CHIP 基因都削弱 Omega-6 保护作用”。[总结]

## 推荐正文结果结构

- 第一部分：队列构建与基线特征
  - 写清总样本量、CHIP 携带比例、RA 事件数和平均随访时间。
  - 用 Table 1 展示 baseline characteristics。[出处: baseline/baseline_table_final_output.docx]
- 第二部分：Omega-6 与 RA 的主效应
  - 用五分位 Cox 结果作为主表。
  - 强调 Q3、Q4、Q5 相对 Q1 的风险降低。
  - 避免只报告连续变量结果，因为 RCS 显示非线性显著。[出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx; cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx]
- 第三部分：Omega-6 与 RA 的非线性关系
  - 用 RCS 曲线作为 Figure 1。
  - 报告总体 P 值和非线性 P 值。
  - 解释为剂量-反应关系不是单调直线。[总结]
- 第四部分：Omega-6 × CHIP 的交互和联合暴露
  - 用 logistic 交互项作为统计交互证据。
  - 用分层 Cox 和联合暴露 Cox 展示风险格局。
  - 重点展示 high Omega-6 非携带者 HR `0.80` 与 high Omega-6 携带者 HR `1.13` 的差异。[出处: interaction/总效应分析/Interaction_Analysis.docx; interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- 第五部分：CHIP 与 RA 的支持性结果
  - 简短说明 any CHIP 和 small CHIP 与 RA 风险升高相关。
  - 作为为什么研究 CHIP 效应修饰的合理性支撑。[出处: cox/CHIP_AND_RA/cox_multivariate_results.docx]
- 第六部分：补充材料
  - small/large CHIP。
  - 单基因交互。
  - M05/M06。
  - HR_2years。
  - Omega-6 与 CHIP 的关系。
  - GO 富集分析。[出处: result_structure_recommendation.md]

## 核心结论

- 结论 1
  - 在总体队列中，较高 Omega-6 分位与较低 RA 风险相关，且这种关系具有非线性特征。[出处: cox/OMEGA6_AND_RA/cox_omega6_quintile_results.docx; cox/OMEGA6_AND_RA/Omega6_RA_RCS_Results.docx]
- 结论 2
  - any CHIP 与 RA 风险升高相关，调整年龄和性别后仍显著。[出处: cox/CHIP_AND_RA/cox_multivariate_results.docx]
- 结论 3
  - Omega-6 与 CHIP 的乘法交互项达到边界显著，提示 CHIP 可能修饰 Omega-6 与 RA 的关系。[出处: interaction/总效应分析/Interaction_Analysis.docx]
- 结论 4
  - 在非 CHIP 人群中，高 Omega-6 对应较低 RA 风险；在 CHIP 携带者中，这种低风险格局不明显。[出处: interaction/交互作用/HR/RA/ALL_HR_RA/joint_analyse.docx]
- 结论 5
  - small CHIP 的交互信号强于 large CHIP，是当前补充分析中最值得强调的结果。[出处: interaction/交互作用/HR/RA/small_CHIP_HR_RA/joint_analyse.docx; interaction/交互作用/HR/RA/large_CHIP_HR_RA/joint_analyse.docx]
- 结论 6
  - 单基因分析存在方向差异和统计效能限制，适合用于提出机制假说，不适合作为主结论。[总结]

## 局限性与待复核点

- 样本量版本需要统一
  - `178,871`、`254,619`、`255,237` 和 `255,546` 同时出现在不同材料中。
  - 正式论文必须明确最终分析集，并在方法部分解释不同模型样本量差异。[待复核]
- RA 结局定义需要最终锁定
  - 当前分析使用 `RA.status` 和 `followup_years` 进行 Cox。
  - 需要确认 `RA.status` 是否严格表示 incident RA，是否排除基线 RA，以及删失规则如何定义。[待复核]
- 交互模型体系需要统一
  - logistic 模型报告 OR，Cox 模型报告 HR。
  - 如果正文主问题是随访发病风险，建议正文优先使用 Cox 结果，logistic 作为补充或敏感性结果。[总结][出处: result_structure_recommendation.md]
- 协变量调整仍可加强
  - 当前核心模型主要调整 age、sex、BMI、Townsend。
  - 方案文件建议进一步考虑吸烟、饮酒、种族、教育、慢病和药物因素。
  - 是否纳入更多协变量取决于缺失率、因果图和模型稳定性。[出处: statistical_analysis_plan.md]
- 多重比较问题
  - 单基因、M05/M06、small/large CHIP、HR_2years 等分析数量较多。
  - 正文不宜把所有显著或边界显著结果并列为主发现。
  - 建议明确主分析与探索性分析，并对探索性分析考虑 FDR 或至少进行谨慎解释。[总结]

## 一句话带走

- 这个课题最有价值的发现不是简单地说 Omega-6 保护或 CHIP 有害，而是提示 Omega-6 与 RA 的低风险关联可能依赖个体的克隆性造血背景；在 CHIP 尤其 small CHIP 携带者中，这种低风险格局被削弱或消失。[总结]

---
