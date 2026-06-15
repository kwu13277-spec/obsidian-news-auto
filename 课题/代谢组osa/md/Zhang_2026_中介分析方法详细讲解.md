# Zhang 2026 空气污染-OA 论文的中介分析方法详细讲解

## 一句话概括

- 这篇文章的中介分析要回答的问题是：空气污染增加骨关节炎（OA）风险，其中有多少比例可以由空气污染相关的循环代谢特征解释。
- 作者把研究链条设定为：空气污染暴露 → 空气污染相关代谢特征 → incident OA。
- 主要中介变量不是单个代谢物，而是用 elastic net 从 251 个 NMR 代谢物中筛出的 50 个代谢物构成的 metabolic signature score。

## 中介分析中的三个核心变量

- 暴露变量 X
  - 主要暴露是 composite air pollution score，即综合空气污染评分。
  - 单一污染物也分别做了中介分析，包括 PM2.5、PM10、PM2.5-10、NO2、NOx。
  - 暴露数据来自基于居住地址的土地利用回归模型。

- 中介变量 M
  - 主中介变量是 air pollution-related metabolic signature。
  - 这个代谢特征不是直接测得的单一指标，而是通过 elastic net regularized regression 构建。
  - 公式思想是：metabolic signature score = Σ(βi × metabolitei)。
  - 也就是说，每个被保留的代谢物根据 elastic net 系数加权，最后合成为一个代谢特征评分。

- 结局变量 Y
  - 主要结局是 incident OA。
  - OA 通过 ICD-9/ICD-10 诊断编码，从国家健康登记系统中识别。
  - 随访从 UK Biobank 基线开始，到首次 OA 诊断、死亡、失访或 2022-12-31 为止。

## 为什么先构建 metabolic signature，再做中介分析

- 代谢组数据有 251 个指标，很多代谢物之间高度相关。
- 如果逐个代谢物做中介，容易出现多重比较、共线性和解释碎片化。
- Elastic net 同时具有 LASSO 的变量筛选能力和 Ridge 的共线性处理能力。
- 作者先用 elastic net 找到与空气污染评分相关的 50 个代谢物，再把它们合成为一个代谢特征。
- 这个 metabolic signature 可以理解为“空气污染在血液代谢层面的综合指纹”。
- 因此，中介分析不是问“某一个代谢物是否中介”，而是先问“整体代谢重塑是否中介空气污染与 OA 的关联”。

## 统计模型的大致结构

- 第一步：估计总效应
  - 模型评估空气污染暴露 X 与 incident OA Y 的关联。
  - 主要使用 Cox proportional hazards model。
  - 得到空气污染对 OA 的总效应，即不考虑中介变量时的效应。

- 第二步：估计 X 对 M 的影响
  - 作者先用 elastic net 证明空气污染暴露与一组代谢物相关。
  - 这些代谢物构成 metabolic signature score。
  - 逻辑上，这一步对应中介分析中的 a 路径：X → M。

- 第三步：估计 M 对 Y 的影响，并控制 X
  - 作者评估 metabolic signature 与 incident OA 的关联。
  - 在 Cox 模型中，metabolic signature 每增加 1 个 IQR，OA 风险升高。
  - 这一步对应 b 路径：M → Y，同时控制 X 和协变量。

- 第四步：用反事实框架分解效应
  - 作者使用 R 包 CMAverse。
  - 方法描述为 counterfactual-based causal mediation analysis。
  - 通过 bootstrap 重抽样 n=200 估计中介比例和 95% CI。
  - 目标是把总效应拆成直接效应和间接效应。

## 效应分解怎么理解

- Total effect
  - 空气污染对 OA 的总体影响。
  - 包括所有路径，不区分是否经过代谢特征。

- Natural indirect effect
  - 空气污染通过 metabolic signature 传递到 OA 的那部分效应。
  - 也就是“空气污染改变代谢特征，代谢特征再影响 OA”的路径。

- Natural direct effect
  - 空气污染不经过 metabolic signature，而通过其他机制影响 OA 的效应。
  - 例如直接炎症、氧化应激、其他未测量生物通路或残余混杂。

- Proportion mediated
  - 中介比例 = 间接效应 / 总效应。
  - 论文最核心的中介结果是：metabolic signature 介导了 composite air pollution score 与 OA 关联的 21.04%。

## 协变量调整

- Fig 4 图注说明，中介模型调整了以下变量：
  - age
  - sex
  - race
  - education
  - income
  - physical activity
  - smoke
  - alcohol
  - DASH diet
  - BMI
  - history of diabetes mellitus
  - hypertension
  - CVD
  - cancer
- 这些变量覆盖人口学、社会经济状态、生活方式、饮食、体型和基础慢病。
- 目的在于减少暴露-结局、暴露-中介、中介-结局之间的混杂。

## 主要中介结果

- 综合空气污染评分 → metabolic signature → OA
  - 中介比例：21.04%。
  - 95% CI：16.52% 到 41.95%。
  - P < 0.001。
  - 含义：约五分之一的空气污染-OA 关联可以由空气污染相关代谢改变解释。

- 单一污染物的中介比例
  - PM2.5：21.52%，95% CI 16.73% 到 48.43%。
  - NOx：16.63%，95% CI 15.28% 到 32.26%。
  - NO2：18.97%，95% CI 18.91% 到 39.07%。
  - PM2.5-10：8.41%，95% CI 5.78% 到 10.83%。
  - 原文在排序表述上略有不一致，因为 NO2 的 18.97% 大于 NOx 的 16.63%，写作时建议只报告数值，不强调原文的“followed by”顺序。

- 单个代谢物中介结果
  - Albumin：7.43%。
  - HDL size：10.12%。
  - Glycoprotein acetyls：6.28%。
  - 这些结果来自 sTable 7，说明除了整体 metabolic signature，部分关键代谢物也有单独中介贡献。

## 这套中介分析的逻辑强点

- 先证明空气污染与 OA 有关联。
- 再证明空气污染对应一组代谢改变。
- 再证明这组代谢改变本身预测 OA。
- 最后用中介分析量化“代谢改变解释了多少污染-OA 关联”。
- 这种顺序比直接做中介更完整，因为它先建立了 X-Y、X-M、M-Y 三个基础关系。

## 需要注意的局限

- 这是观察性队列研究，中介分析不能等同于真正随机试验中的因果证明。
- 反事实中介分析依赖较强假设，包括没有未测量的暴露-结局混杂、暴露-中介混杂和中介-结局混杂。
- 代谢组只在基线测量一次，不能反映随访期间代谢特征的动态变化。
- 空气污染暴露来自居住地模型估计，不是个人实时暴露监测，可能存在暴露错分。
- Bootstrap 次数为 200，较常见的 500 或 1000 次少，部分置信区间较宽。
- 论文没有在正文中详细说明 CMAverse 的具体函数、是否包含暴露-中介交互项、以及 survival outcome 下的具体效应尺度，这些若要复现需要查看补充材料或代码。

## 如果仿照这篇文章写自己的中介分析

- 可以采用类似结构：
  - 先构建暴露相关代谢评分。
  - 再验证代谢评分与疾病风险关联。
  - 最后做中介分析，报告中介比例。

- 方法部分可写成：
  - We performed causal mediation analysis under the counterfactual framework to evaluate whether the exposure-related metabolic signature mediated the association between exposure and incident disease.
  - The mediation models were adjusted for demographic, lifestyle, socioeconomic, and clinical covariates.
  - Bootstrap resampling was used to estimate 95% confidence intervals for the mediation proportion.

- 结果部分可写成：
  - The exposure-related metabolic signature mediated XX% of the association between exposure and incident disease, suggesting that systemic metabolic alterations accounted for part of the observed exposure-disease relationship.

## 对你当前 OSA-MET-OA 课题的启发

- 你的研究可以借鉴它的三步框架：
  - OSA → OA：先确认 OSA 与 OA 风险相关。
  - OSA → MET_SCORE：构建或验证 OSA 相关代谢评分。
  - OSA → MET_SCORE → OA：用中介分析估计 MET_SCORE 解释了多少 OSA-OA 关联。

- 需要注意的是：
  - 如果你的结局是生存结局，最好明确中介分析使用的结局模型类型。
  - 如果用 R mediation 包和 survival::survreg，要说明是 AFT outcome model。
  - 如果想更贴近 Zhang 2026，可以考虑用 CMAverse 的反事实中介框架，但需要先确认它对你的生存结局、二分类暴露和连续中介变量的支持方式。

---
