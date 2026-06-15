# 《Plasma proteomic biomarkers and poor cardiovascular health with incident dementia》PPT汇报

- 题目：Plasma proteomic biomarkers and the association between poor cardiovascular health and incident dementia: The UK Biobank study
- 期刊：Brain, Behavior, and Immunity
- 研究对象：UK Biobank 50-74岁参与者
- 汇报主线：poor CVH -> incident dementia -> plasma proteome mediation

---

## 1. 为什么研究心血管健康与痴呆？

- 痴呆负担随人口老龄化持续上升
- 心血管危险因素是痴呆的重要可干预来源
- Life's Essential 8 (LE8) 可综合评估心血管健康
- 关键问题不只是“有没有关联”，还包括“通过什么生物学路径发生”

---

## 2. 研究假设

- 较差心血管健康 poor CVH 会增加 incident all-cause dementia 风险
- 血浆蛋白组可能位于 CVH 与痴呆之间
- 中介蛋白可能反映炎症、血管功能、代谢和细胞外基质重塑
- 目标：找出能解释 LE8z_rev-dementia 关系的关键蛋白

---

## 3. 研究总体设计

- 数据来源：UK Biobank
- 基线时间：2006-2010年
- 随访终点：2021年10月31日
- 分析样本：28,974人
- 事件数：786例 incident all-cause dementia
- 蛋白组：Olink Explore 1536平台，1,463种血浆蛋白

---

## 4. 核心变量定义

- 暴露：LE8 total score 反向标准化为 LE8z_rev
- LE8z_rev 越高，表示 CVH 越差
- 结局：incident all-cause dementia
- 主要中介：plasma proteomic biomarkers
- 调整因素：年龄、性别、种族/族裔、家庭规模、SES z-score
- 额外分层：性别、AD PRS tertile

---

## 5. 统计分析框架

- Cox模型：检验 LE8z_rev 与 incident dementia 的总关联
- 蛋白筛选：1,463个蛋白分别与 LE8z_rev 建模
- 四路分解：区分 CDE、PIE、INTREF、INTMED
- PCA：整合多个核心中介蛋白为共同因子
- 通路分析：OLINK Insight + STRING 聚类解释机制

---

## 6. Figure 1：不同CVH水平的无痴呆生存曲线

![Figure 1](./蛋白中介血管与痴呆_PPT_assets/figure1_km_curve.png)

- T1：ideal CVH；T2：intermediate CVH；T3：poor CVH
- 总体样本中，不同 LE8z_rev tertile 的 dementia-free survival 有差异
- 男性分层中差异仍明显
- 女性分层中 log-rank 检验不显著

---

## 7. Table 1：样本基线特征（1）

![Table 1 part 1](./蛋白中介血管与痴呆_PPT_assets/table1_sample_characteristics_part1.png)

- 总样本 N=28,974
- 男性 N=13,759，女性 N=15,215
- 平均基线年龄约60.7岁
- 女性占52.5%
- LE8总分：女性高于男性，提示女性整体 CVH 更好

---

## 8. Table 1：样本基线特征（2）

![Table 1 part 2](./蛋白中介血管与痴呆_PPT_assets/table1_sample_characteristics_part2.png)

- all-cause dementia 累积发生率：2.7%
- 男性发生率高于女性：3.2% vs 2.3%
- AD dementia 累积发生率：1.2%
- AD PRS 三分位分布基本均衡
- 后续分析需要同时考虑性别和遗传风险分层

---

## 9. Table 2：poor CVH 与痴呆风险的主效应

![Table 2](./蛋白中介血管与痴呆_PPT_assets/table2_le8_dementia_cox.png)

- LE8z_rev 每升高1 SD，all-cause dementia 风险增加11%
- 总体：HR=1.11，95% CI 1.03-1.20，P=0.005
- 男性：HR=1.12，95% CI 1.01-1.24，P=0.026
- 女性：HR=1.10，95% CI 0.99-1.23，P=0.088
- 低 AD PRS tertile 中关联最强：HR=1.42

---

## 10. Figure 2：LE8z_rev关联蛋白的火山图（1）

![Figure 2 part 1](./蛋白中介血管与痴呆_PPT_assets/figure2_volcano_part1.png)

- 横轴：LE8z_rev 对蛋白表达的回归系数
- 纵轴：关联显著性，-log10(P)
- 每个点代表一种血浆蛋白
- 目的是从1,463个蛋白中筛选与 poor CVH 强相关的候选蛋白

---

## 11. Figure 2：LE8z_rev关联蛋白的火山图（2）

![Figure 2](./蛋白中介血管与痴呆_PPT_assets/figure2_volcano_part1.png)

- 进入后续中介分析的筛选标准：
- Bonferroni校正 P<0.05
- 效应量绝对值 >0.20
- 最终筛选出144个蛋白进入四路分解分析
- 这一步解决“哪些蛋白最能反映 poor CVH”

---

## 12. Figure 3：四路分解筛出一致性中介蛋白

![Figure 3](./蛋白中介血管与痴呆_PPT_assets/figure3_four_way_heatmap.png)

- 144个候选蛋白分成3类
- 77个：无显著 pure mediation
- 56个：inconsistent mediation
- 11个：consistent mediation
- 一致性中介蛋白是后续机制解释的重点

---

## 13. 四路分解怎么理解？

- TE：total effect，总效应
- CDE：controlled direct effect，不经中介/交互解释的直接部分
- PIE：pure indirect effect，纯中介效应
- INTREF：interaction only，单纯交互部分
- INTMED：mediated interaction，中介与交互重叠部分
- 本文重点看 PIE 和 INTMED 对总效应的解释比例

---

## 14. Table 3：GDF15 是最强中介蛋白

![Table 3 part 1](./蛋白中介血管与痴呆_PPT_assets/table3_mediation_part1.png)

- 11个一致性中介蛋白中，GDF15 最突出
- GDF15 与痴呆风险关联最强：HR=1.24，95% CI 1.16-1.33，P<0.001
- GDF15 的 PIE 占总效应约48%
- PIE+INTMED 合计解释约62.6%
- 说明 GDF15 很可能承载 poor CVH 到痴呆风险的一条重要炎症/应激路径

---

## 15. Table 3：ADM 及其他中介蛋白

![Table 3 part 2](./蛋白中介血管与痴呆_PPT_assets/table3_mediation_part2.png)

- ADM 是仅次于 GDF15 的关键中介
- ADM 的 PIE 占总效应约41%
- PIE+INTMED 合计解释约56%
- COL6A3、PLAUR、GFRA1 等也有显著中介贡献
- 这些蛋白共同指向血管调节、炎症和细胞外基质重塑

---

## 16. Table 3：其余一致性中介蛋白

![Table 3 part 3](./蛋白中介血管与痴呆_PPT_assets/table3_mediation_part3.png)

- TGFA、TNFRSF6B、ACVRL1 等继续支持一致性中介模式
- 多数蛋白的 PIE 显著，但单个蛋白解释比例低于 GDF15/ADM
- 说明机制不是单蛋白路径，而是多蛋白网络共同作用
- Table 3 是全文机制证据的核心结果表

---

## 17. PCA：10个核心中介蛋白的共同因子

- 作者将10个核心中介蛋白提取第一主成分
- 蛋白包括：TNFRSF1A、GDF15、FSTL3、COL6A3、PLAUR、ADM、GFRAL、ACVRL1、TNFRSF6B、TGFA
- 该主成分中介 LE8z_rev-dementia 总效应的53.6%
- 这提示 poor CVH 对痴呆风险的影响，较大部分可由蛋白组通路解释
- PCA 的意义：把多个相关蛋白压缩成一个更稳定的机制因子

---

## 18. 通路分析：中介蛋白指向哪些机制？

- OLINK Insight 分析纳入所有显著 PIE 蛋白：k=526
- 主要通路：immune system
- 主要通路：signal transduction
- 主要通路：metabolism / protein metabolism
- 其他通路：hemostasis、membrane trafficking、extracellular matrix organization
- STRING 聚类强调 cytokine-mediated signaling 和 peptidyl-tyrosine phosphorylation

---

## 19. 机制整合

- poor CVH 不是单一危险因素，而是生活方式和生物学负担的综合表型
- LE8z_rev 升高可能伴随慢性炎症、血管内皮功能异常、代谢紊乱
- GDF15 代表应激和炎症反应增强
- ADM 代表血管调节和内皮相关路径
- 多蛋白网络最终可能增加神经炎症、血管脑损伤和痴呆风险

---

## 20. 文献评价与一句话总结

- 优势：大样本、事件性痴呆结局、Olink高通量蛋白组、四路分解和PCA验证
- 局限：观察性研究仍可能有残余混杂
- 局限：痴呆发病时间和类型可能存在误分类或低估
- 局限：UK Biobank 样本选择偏倚和族群代表性有限
- 一句话总结：poor CVH 与更高痴呆风险相关，其中 GDF15、ADM 等血浆蛋白构成的炎症-血管-代谢网络解释了相当比例的风险路径。

---
