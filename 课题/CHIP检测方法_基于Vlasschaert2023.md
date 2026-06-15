建议文件名：CHIP检测方法_基于Vlasschaert2023.md

# CHIP 检测方法：基于 Vlasschaert 等 2023 年 Blood 文献

内容类型：基于指定文献的主题介绍

## 摘要

本文整理 Vlasschaert 等文献中 CHIP 的检测流程，重点说明变异调用、注释、质量过滤、假阳性剔除、胚系变异识别和等位基因深度阈值优化。

## 关键词

克隆性造血（Clonal Hematopoiesis）；意义未明的克隆性造血（Clonal Hematopoiesis of Indeterminate Potential, CHIP）；变异等位基因频率（Variant Allele Fraction, VAF）；Mutect2；最小等位基因深度（minimum allele depth, minAD）；测序伪影（sequencing artifact）；胚系变异（germline variant）

## 大纲

1. [研究场景与 CHIP 判定对象](#section-1)
2. [总体检测流程](#section-2)
3. [候选体细胞变异识别](#section-3)
4. [基础测序质量过滤](#section-4)
5. [测序伪影过滤](#section-5)
6. [胚系变异过滤](#section-6)
7. [样本质量与基因列表再筛选](#section-7)
8. [minAD 阈值优化与最终 CHIP call set](#section-8)
9. [方法特点与适用边界](#section-9)

## 正文

<a id="section-1"></a>

### 1. 研究场景与 CHIP 判定对象：在大规模 WES/WGS 数据中识别真实 CHIP

本节概要：本节说明该文献检测 CHIP 的数据场景和基本判定对象，重点是从大规模外周血测序数据中区分真实 CHIP、测序伪影和胚系变异。

该文献关注的问题是：在没有配对非血液组织样本的情况下，如何利用大规模人群遗传数据集识别可信的 CHIP 变异。研究对象包括 UK Biobank 的全外显子组测序（Whole-Exome Sequencing, WES）数据和 All of Us 的全基因组测序（Whole-Genome Sequencing, WGS）数据。两者均为外周血来源 DNA，因此检测到的变异可能来自造血细胞克隆，也可能是测序伪影、胚系变异或非驱动性体细胞变异。

文献采用的 CHIP 基本定义是：个体存在髓系肿瘤驱动基因中的体细胞突变，并且变异等位基因频率（Variant Allele Fraction, VAF）达到或超过 2%；若存在未解释的持续性血细胞减少，则更接近克隆性血细胞减少（Clonal Cytopenia of Undetermined Significance, CCUS）而不是单纯 CHIP。

<a id="section-2"></a>

### 2. 总体检测流程：先宽松识别候选变异，再逐层剔除假阳性

本节概要：本节概括文献中的 CHIP 检测框架，重点是“候选变异识别 + 多层过滤 + 人群尺度验证”的组合策略。

该文献的 CHIP 检测不是只设定一个 VAF 阈值，而是采用分步式变异整理流程。流程可以概括为：

1. 使用体细胞变异检测工具从 CRAM/BAM 等比对文件中识别候选体细胞变异。
2. 使用预设 CHIP driver gene / driver variant 清单限制分析范围。
3. 对候选变异进行基因和蛋白水平注释。
4. 先用较宽松的测序质量阈值过滤低可信变异。
5. 利用人群规模数据识别反复出现的测序伪影。
6. 通过统计检验识别可能的胚系变异。
7. 检查异常样本和异常高变异数个体。
8. 根据年龄、TERT promoter 变异、结局关联等信号优化最小等位基因深度（minimum allele depth, minAD）阈值。
9. 得到最终 CHIP mutation call set。

该流程的核心逻辑是：真实 CHIP 应该表现出与年龄升高、CHIP 相关遗传背景和髓系肿瘤风险等已知生物学特征相一致的模式；不符合这些模式、且在人群中反复出现的候选变异，更可能是伪影或非 CHIP 变异。

<a id="section-3"></a>

### 3. 候选体细胞变异识别：Mutect2 调用 73 个 canonical CHIP driver genes，U2AF1 单独处理

本节概要：本节说明候选变异如何被初步找出，重点是 Mutect2、U2AF1 特殊处理和 ANNOVAR 注释。

文献将初始扫描范围限制在既往 CHIP 流行病学研究提出的 74 个 canonical CHIP driver genes 及其候选变异规则中。不同基因的纳入规则并不完全相同：有些基因中所有功能缺失变异（loss-of-function mutation）可作为候选 CHIP 变异，有些基因则只纳入特定错义突变（missense mutation）或热点变异（hotspot mutation）。

候选体细胞变异识别主要使用 Mutect2。Mutect2 是 Genome Analysis Toolkit（GATK）中的体细胞变异调用工具，基于局部单倍型组装和贝叶斯建模识别单核苷酸变异与小插入缺失。文献使用 Mutect2 在 UK Biobank 和 All of Us 的比对测序文件中扫描 73 个 canonical CHIP driver genes。

U2AF1 是例外。由于 GRCh38 / hg38 参考基因组中 U2AF1 位点存在错误重复，常规 Mutect2 流程不能可靠识别该基因的变异。文献因此使用自定义 pileup region 脚本，对映射到 U2AF1 两个基因组位置之一的 reads 进行突变等位基因计数，并只把预先指定热点位置对应的变异作为候选 CHIP 变异。对于同时映射到两个位点的样本，等位基因深度取两个位点的平均值。

候选变异被识别后，文献使用 ANNOVAR 对变异进行基因和蛋白水平注释，为后续过滤提供依据。

<a id="section-4"></a>

### 4. 基础测序质量过滤：DP、minAD、双向 reads 支持和 VAF 阈值

本节概要：本节说明第一层过滤参数，重点是用测序深度和 VAF 去除低质量候选变异。

文献首先应用基础测序质量过滤，去除测序支持不足的变异。初始过滤条件包括：

| 过滤指标                                    |                     文献中的初始阈值 | 含义                     |
| --------------------------------------- | ---------------------------: | ---------------------- |
| 总测序深度（Depth, DP）                        |                      DP ≥ 20 | 变异位点总 reads 数不能过低      |
| 最小替代等位基因深度（minimum allele depth, minAD） |                    minAD ≥ 3 | 支持突变等位基因的 reads 数至少为 3 |
| 双向 reads 支持                             | forward 和 reverse reads 均需支持 | 避免只由单方向 reads 支持的假阳性   |
| 变异等位基因频率（VAF）                           |                     VAF ≥ 2% | 符合 CHIP 常用定义阈值         |

经过基础过滤后，仍然会保留真实 CHIP、胚系变异、非致病 passenger 变异和测序伪影。因此，这一步只是低质量变异清理，不足以直接定义最终 CHIP。

文献还特别提醒，多等位基因变异（multiallelic variants）在大规模 Mutect2 输出中较常见，常被认为难以解释或可能是伪影。但一些真实双等位基因变异可能被误归入 multiallelic 结果，因此不应机械地全部删除，而应单独检查。

<a id="section-5"></a>

### 5. 测序伪影过滤：用年龄和 TERT promoter rs7705526 关联验证反复出现的变异

本节概要：本节说明文献如何识别 recurrent sequencing artifacts，重点是利用大人群数据中 CHIP 与年龄、TERT promoter 位点的已知关联。

基础过滤之后，文献利用人群尺度数据识别反复出现的假阳性变异。具体做法是：对在人群中多次出现的变异组进行统计验证。文献设定的复发性变异检查门槛为：

| 数据集 | 进入 recurrent artifact 检查的门槛 |
|---|---:|
| UK Biobank | 同一变异出现在 ≥20 个个体中 |
| All of Us | 同一变异出现在 ≥15 个个体中 |

这些变异组随后被检验是否与两个 CHIP 强相关指标相关：

- 年龄（age）：CHIP 随年龄增长而更常见。
- TERT promoter 常见遗传变异 rs7705526：该位点与 CHIP 易感性相关。

如果某个反复出现的变异既不与年龄相关，也不与 rs7705526 相关，即使只按较宽松标准 P < 0.10 判断也没有信号，文献将其视为疑似测序伪影并剔除。

ASXL1 是该策略的重要例子。ASXL1 的 G645/G646 同聚物区域容易产生体外插入缺失伪影，尤其与 PCR 相关流程有关。文献对 ASXL1 p.G646Wfs*12 和 p.G645Vfs*58 进行了更细化处理：G646Wfs*12 在 VAF ≥10% 时表现出与年龄和临床结局一致的真实 CHIP 信号，因此保留较大克隆；G645Vfs*58 缺乏相应年龄关联，更符合外显子测序伪影，因此剔除。

文献还对部分被过滤的变异进行热点复核。若某些变异虽然未通过年龄/TERT 关联，但已在 COSMIC v96 中至少 3 例髓系肿瘤中出现，则保留为真实热点候选；文献提到的例外包括 TP53 R175H 和 DNMT3A V716I。

<a id="section-6"></a>

### 6. 胚系变异过滤：用二项检验识别接近杂合胚系状态的候选变异

本节概要：本节说明文献如何从 CHIP 候选变异中剔除 germline variants，重点是 TET2、CBL 和其他反复出现变异的二项检验策略。

在无配对非血液组织样本的 biobank 数据中，胚系变异是 CHIP 检测中的重要假阳性来源。文献采用二项检验（binomial test）判断某些候选变异是否接近杂合胚系变异预期。

逻辑是：若某变异为杂合胚系变异，突变等位基因 reads 通常接近总 reads 的一半，即 VAF 接近 50%。因此可检验某候选变异的突变 reads 深度是否显著不同于总深度的一半。若未能与 50% 杂合状态区分，则提示可能是胚系变异。

文献首先将该策略用于 TET2 和 CBL 催化结构域中的 missense variants，并将 P < 0.01 作为二项检验筛选依据。由于高 VAF CHIP 大克隆也可能接近 50%，文献没有简单删除所有接近 50% 的候选变异，而是进一步检查这些变异加入后是否增强或削弱与年龄的关联。

在 TET2 中，文献认为 H1904R、I1873T 和 T1884A 这 3 个位点加入后增强了年龄关联，因此更可能是真实 CHIP 大克隆，免于按二项检验删除。

随后，文献把二项检验扩展到其他基因中反复出现超过 3 次的变异组。若某一变异组的所有变异均未通过二项检验，则被视为 recurrent germline variants 并删除。文献列出的被删除例子包括 DNMT3A G298R、TP53 R110C、RUNX1 R223C 和 SUZ12 D725Vfs*18。

<a id="section-7"></a>

### 7. 样本质量与基因列表再筛选：检查异常高突变数样本，并移除低支持基因

本节概要：本节说明候选变异之外的两个补充质控环节，重点是样本级异常和 driver gene list 的再评估。

除单个变异过滤外，文献还建议检查每个样本的变异数量。若某个样本携带异常多的候选 CHIP 变异，可能提示样本质量问题或系统性伪影。文献以 All of Us 为例，发现 10 个个体携带 4 个或更多突变，其中 5 个样本的所有变异表现为低质量、可能为伪影，另 5 个看起来较可信。

文献还重新评估了原始 74 个 CHIP driver genes 列表。随着样本量扩大，可以判断某些基因中的候选变异是否真的表现出 CHIP 特征。文献发现 16 个基因中的候选变异既不与年龄呈正相关，也未在两个队列的髓系肿瘤病例中观察到，并且缺乏作为髓系 CHIP driver 的文献支持，因此将这些基因从最终 CHIP call set 中移除。

被移除的 16 个基因为：

SF3A1；GATA1；GATA3；PTEN；SF1；STAG1；IKZF2；IKZF3；PDSS2；LUC7L2；JAK1；JAK3；GNA13；KMT2A；KMT2D；CSF1R。

<a id="section-8"></a>

### 8. minAD 阈值优化与最终 CHIP call set：UKB 用 minAD ≥5，All of Us 用 minAD ≥3

本节概要：本节说明最终阈值如何确定，重点是不同测序数据类型需要不同 minAD 标准。

初始过滤时，文献使用较宽松的 minAD ≥3，以提高 CHIP 候选变异检测敏感性。但为了优化最终 call set，文献进一步比较 minAD 3、4、5、6 不同分层下的可信度。评估依据包括候选 CHIP 与年龄的关联、与 TERT promoter rs7705526 的关联，以及在 UK Biobank 中对死亡和新发髓系肿瘤风险的预测能力。

在 UK Biobank WES 数据中，minAD ≥5 比更低阈值更合适。文献的模拟分析提示，minAD 3 层中的假阳性污染较高，估计约 50%；即使在 VAF ≥10% 的大克隆中，minAD 3 层的污染仍约 40%。因此，UK Biobank 最终 CHIP call set 只纳入 minAD ≥5 的变异。

在 All of Us WGS 数据中，minAD 3 层的污染估计较低，约为 5%–25%。All of Us 使用 PCR-free WGS、读长和数据特征不同，每个 minAD 分层捕获的 VAF 范围也不同。因此，文献最终在 All of Us 中保留 minAD ≥3 的变异。

最终结果方面，排除入组前或入组后 6 个月内发生血液恶性肿瘤的个体后，文献报告：

| 数据集 | 最终 CHIP 变异数 | 携带 CHIP 个体数 | CHIP 患病率 |
|---|---:|---:|---:|
| UK Biobank | 16,239 | 15,304 | 3.6% |
| All of Us | 5,125 | 4,617 | 4.8% |

<a id="section-9"></a>

### 9. 方法特点与适用边界：适合大队列 CHIP 研究，但依赖队列规模和可用表型

本节概要：本节总结该检测方法的关键特点和限制，重点是其适合 biobank 规模数据，但不等同于临床诊断中的配对样本验证。

该方法的优势在于把传统序列质量过滤与大规模人群关联信号结合起来。由于 CHIP 本身与年龄、特定遗传背景和髓系肿瘤风险存在已知关系，文献利用这些外部生物学信号来区分真实 CHIP 与反复出现的伪影。这使得方法特别适合 UK Biobank、All of Us 这类样本量大、具有测序数据和表型数据的队列。

该方法也强调不同测序平台需要不同过滤策略。UK Biobank 的 WES 与 All of Us 的 PCR-free WGS 在伪影类型、读长、捕获方式和等位基因深度表现上不同，因此不能机械复用同一 minAD 或基因特异性规则。ASXL1 同聚物区域和 U2AF1 在 hg38 参考基因组中的问题，说明 CHIP 检测需要对特定基因和特定位点进行专门处理。

该方法的边界是：它主要用于大规模研究数据集中的 CHIP ascertainment，而不是替代临床诊断。没有配对非血液组织样本时，胚系变异不能被完全排除；缺乏纵向血常规时，也难以严格区分 CHIP 与 CCUS。文献因此把方法定位为提高 CHIP call fidelity 和研究可重复性的实用框架，而不是单一固定阈值规则。

## 方法流程简表

| 步骤 | 输入 | 方法 | 输出 |
|---|---|---|---|
| 1. 候选变异调用 | WES/WGS aligned CRAM 文件 | Mutect2；U2AF1 用自定义 pileup 脚本 | putative somatic variants |
| 2. 注释 | 候选变异 | ANNOVAR | 基因、蛋白、功能注释 |
| 3. 基础过滤 | 候选变异 | DP ≥20；minAD ≥3；双向 reads 支持；VAF ≥2% | 初筛 CHIP 候选变异 |
| 4. CHIP 规则过滤 | 注释后变异 | canonical driver gene / hotspot / LoF / splice-site 规则 | 符合 CHIP driver 规则的候选变异 |
| 5. 测序伪影过滤 | 反复出现变异 | 年龄和 TERT rs7705526 关联；ASXL1 特殊规则；COSMIC 热点复核 | 去除 recurrent sequencing artifacts |
| 6. 胚系变异过滤 | VAF 接近 50% 或反复出现变异 | 二项检验；年龄关联复核 | 去除 likely germline variants |
| 7. 样本级质控 | 个体变异计数 | 检查异常高突变数样本 | 去除低质量样本或异常结果 |
| 8. 基因列表修订 | 74 个 canonical genes | 年龄关联、髓系肿瘤出现情况、文献支持 | 移除 16 个低支持基因 |
| 9. minAD 优化 | 不同 minAD 分层 | 年龄、TERT、结局关联和模拟污染估计 | UKB minAD ≥5；All of Us minAD ≥3 |
| 10. 最终定义 | 过滤后变异 | VAF ≥2%，并排除血液恶性肿瘤相关个体 | final CHIP call set |

## 参考来源

1. Vlasschaert C, Mack T, Heimlich JB, et al. *A practical approach to curate clonal hematopoiesis of indeterminate potential in human genetic data sets*. Blood. 2023;141(18):2214–2223. DOI: 10.1182/blood.2022018825.
2. PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10273159/
3. ScienceDirect article page: https://www.sciencedirect.com/science/article/pii/S000649712300143X
