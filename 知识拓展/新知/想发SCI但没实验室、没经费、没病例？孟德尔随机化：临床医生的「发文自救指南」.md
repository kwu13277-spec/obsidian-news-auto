[[ReadItLater]] [[Article]]

# [想发SCI但没实验室、没经费、没病例？孟德尔随机化：临床医生的「发文自救指南」](https://mp.weixin.qq.com/s/O4GrCOznY-N72kGJ_eS1dw)

### 

#PyCharm#转录组分析#蛋白组分析#单细胞分析#R

孟德尔随机化分析实操课程见如下文章：

[【孟德尔随机化分析代码实操录播课：全流程精讲+真实数据复现+附代码】](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247487821&idx=1&sn=9a1cbb883baaf5faf2c1a6d1bd5b24b7&scene=21#wechat_redirect)

     这篇题为《A causal relationship between childhood obesity and risk of osteoarthritis: results from a two-sample Mendelian randomization analysis.》的研究于2022发表在《Annals of medicine》，该研究采用**两样本孟德尔随机化（Two-sample MR）**方法，利用与儿童期肥胖强相关的遗传变异作为工具变量，系统评估了儿童期肥胖与总体OA及其亚型（膝OA、髋OA）之间的因果关系。  

![](https://mmbiz.qpic.cn/mmbiz_png/BUOP6FQoibXXCibTSO1VEKnjYtUqAYBliciaaUzfDmHiaRTGXKA3QJ5fVExAvLBv3vPweUsvLpeEtjsAOiacJ5qibztcjKYK6GXJjuppG3IiccFPCMA/640?wx_fmt=png&from=appmsg)

https://pubmed.ncbi.nlm.nih.gov/35703935/

## 一、研究背景及意义

    骨关节炎（Osteoarthritis, OA）是全球最常见的慢性退行性关节疾病，影响超过2.5亿人口，可导致关节疼痛、功能障碍，并造成巨大的健康和社会经济负担。OA的病理特征包括关节软骨退变、骨赘形成、滑膜炎症以及软骨下骨改变，临床表现为进行性关节疼痛、僵硬、肿胀、活动受限和畸形。已知的风险因素包括高龄、女性、肥胖、遗传因素及重大关节损伤等。  
    肥胖作为OA最重要的可调控风险因素之一，已有大量观察性研究证实其与膝、髋等外周关节OA的密切关联。体重减轻干预措施也被证明能显著改善OA患者的疼痛和功能障碍。然而，现有研究主要聚焦于成年期肥胖与OA的关系，对于儿童期肥胖（Childhood Obesity, CO）与OA风险的关联知之甚少。  
    观察性研究虽提示儿童期肥胖与成年后膝关节疼痛、僵硬和功能障碍相关，但这类研究易受混杂因素（如健康状况、营养状态）影响，且可能存在反向因果偏倚。因此，明确儿童期肥胖与OA之间是否存在真正的因果关系，对于制定早期预防策略、识别高危人群具有重要临床意义。  
    该文献采用孟德尔随机化（Mendelian Randomization, MR）方法，利用遗传变异作为工具变量，能够有效规避传统观察性研究中的混杂偏倚和反向因果问题，为揭示儿童期肥胖与OA的因果关系提供了更为可靠的证据。

## 二、研究创新点

1. 首次系统评估儿童期肥胖与OA的因果关联   该研究是首个采用孟德尔随机化方法全面评估儿童期肥胖与骨关节炎（包括总体OA、膝OA和髋OA）因果关系的临床研究，填补了该领域因果推断证据的空白。2. 多模型、多结局的稳健性验证   研究同时应用了五种不同的MR分析方法（IVW、WME、WM、MR-Egger、MRAPS），并对总体OA、膝OA和髋OA三个结局进行分析，通过多模型一致性验证增强了结论的可靠性。3. 严格的工具变量筛选与质量控制   面对全基因组显著性阈值下SNP数量不足的挑战，研究在放宽阈值（p<5×10⁻⁶）的同时，通过F统计量评估弱工具变量偏倚、利用pheWAS数据库排除混杂相关SNP、采用MR-PRESSO检测并剔除异常值，确保了工具变量的有效性。4. 大样本公共数据库的充分利用   研究整合了来自EGG联盟（13,848例欧洲儿童）和UK Biobank（462,933例欧洲人）等多个大规模GWAS数据，样本量大、统计效能高。5. 聚焦儿童期这一关键时间窗口   区别于以往关注成年期肥胖的研究，该研究聚焦儿童期肥胖这一早期暴露，为"生命历程"视角下的OA预防提供了新证据，提示早期干预的重要性。

## 三、研究思路与技术路线

该研究采用两样本孟德尔随机化（Two-sample MR）设计，整体研究思路如下：  
  
【第一阶段：暴露数据获取与工具变量筛选】• 暴露因素：儿童期肥胖（Childhood Obesity）• 数据来源：EGG联盟GWAS荟萃分析（ieu-a-1096），包含13,848例欧洲儿童• 初始SNP筛选：由于严格阈值（p<5×10⁻⁸）仅获得6个SNP，不满足MR分析最低要求（≥10个IV），故采用放宽阈值p<5×10⁻⁶，最终获得15个SNP  
• 连锁不平衡控制：严格参数（r²=0.001，kb=10,000）进行clumping  
• 排除回文SNP：剔除rs1040070（中等频率回文SNP）• 混杂因素排查：在pheWAS数据库中检索各SNP与结局混杂因素的关联（阈值p<5×10⁻⁶）• 弱工具变量评估：计算F统计量，F<10视为存在弱工具变量偏倚风险• 最终纳入：14个合格的工具变量（IVs）  
  
【第二阶段：结局数据获取】• 主要结局：骨关节炎（OA）——MRC-IEU联盟基于UK Biobank构建（ukb-b-14486），462,933例欧洲人• 次要结局1：膝骨关节炎（Knee OA）——Tachmazidou等研究（GCST007090），403,124例欧洲人• 次要结局2：髋骨关节炎（Hip OA）——Tachmazidou等研究（GCST007091），393,873例欧洲人  
  
【第三阶段：MR统计分析】• 数据协调：统一暴露与结局数据的效应等位基因方向• 主要分析方法：逆方差加权模型（IVW）作为核心方法• 补充分析方法：加权中位数估计（WME）、加权模型法（WM）、MR-Egger回归、MRAPS  
• 异质性检验：Cochran's Q检验，p<0.05采用随机效应模型• 多效性检验：MR-Egger截距检验、MR-PRESSO全局检验• 敏感性分析：逐一剔除法（Leave-one-out）、异常值检测与剔除  
  
【第四阶段：结果解释与结论提炼】• 综合五种模型结果，重点关注IVW结果• 结合异质性、多效性、敏感性分析评估结果稳健性• 讨论生物学机制及临床意义• 阐明研究局限性

## 四、核心使用方法详解

1. 两样本孟德尔随机化（Two-sample MR）   原理：利用与暴露强相关的遗传变异（SNP）作为工具变量（IV），在两组独立样本中分别估计SNP-暴露和SNP-结局的关联，进而推断暴露对结局的因果效应。   三大核心假设：   (1) 相关性假设：IV与暴露强相关；   (2) 独立性假设：IV与暴露\-结局间的混杂因素无关联；   (3) 排他性限制：IV仅通过暴露影响结局，不存在水平多效性。  
  
2. 逆方差加权模型（Inverse Variance Weighted, IVW）   作为MR分析的金标准方法，IVW通过meta分析框架合并各SNP的Wald比值估计值，在不存在定向多效性时能提供最稳定、准确的因果估计。该研究将其作为主要分析模型。  
  
3\. MR-Egger回归   通过回归截距检验定向多效性（intercept≠0提示存在定向多效性），同时通过回归斜率提供对多效性校正后的因果估计。该方法不要求所有IV均有效，但统计效能较低。  
  
4. 加权中位数估计（Weighted Median Estimator, WME）   当超过50%的权重来自有效IV时，WME能提供稳健估计。该方法允许部分IV存在多效性，在存在水平多效性时降低I类错误。5. 加权模型法（Weighted Mode, WM）   当大多数相似个体估计值来自有效IV时，WM可获得稳健的总体因果估计。  
  
6\. MR-Robust Adjusted Profile Score（MRAPS）   在IV独立性假设完美成立时，MRAPS能提供更准确的因果评估，作为补充方法使用。  
  
7\. MR-PRESSO检验   MR Pleiotropy RESidual Sum and Outlier test通过检测SNP效应值的异常离群值来识别水平多效性，并进行异常值剔除和因果效应重新估计。该研究利用该方法剔除了膝OA分析中的rs6752378和rs9941349，以及髋OA分析中的rs9941349。  
  
8. 异质性检验（Cochran's Q检验）   评估各IV间效应估计的异质性，p<0.05提示显著异质性，需采用随机效应模型；否则采用固定效应模型。9. 逐一剔除法敏感性分析（Leave-one-out）   系统性地每次剔除一个IV后重新估计因果效应，评估单个IV对总体结果的驱动作用，验证结果的稳定性。  
  
10\. F统计量    评估弱工具变量偏倚，F<10提示可能存在弱工具变量问题。该研究中除rs9568856（F=9.14）和rs17697518（F=8.98）外，其余IV的F值均\>10。  
  

## 五、主要研究结果

1. 主要结局：儿童期肥胖与总体骨关节炎   • IVW模型：OR=1.0075，95%CI \[1.0054, 1.0095\]，p=8.12×10⁻¹³  
   • WME模型：OR=1.0079，95%CI \[1.0050, 1.0107\]，p=5.53×10⁻⁸  
   • WM模型：OR=1.0081，95%CI \[1.0037, 1.0125\]，p=2.98×10⁻³  
   • MRAPS模型：OR=1.0078，95%CI \[1.0056, 1.0101\]，p=6.88×10⁻¹²  
   • 异质性：Cochran's Q检验p=0.8628，采用固定效应模型   • 多效性：MR-Egger截距p=0.8995，MR-PRESSO全局检验p=0.908，无异常值   • 结论：儿童期肥胖与总体OA存在显著因果关联2. 次要结局：儿童期肥胖与膝骨关节炎   • 初始分析存在显著异质性（Q=30.05，p=0.0046），采用随机效应模型   • MR-PRESSO识别两个异常值（rs6752378、rs9941349），剔除后：   • IVW模型：OR=1.1067，95%CI \[1.0769, 1.1373\]，p=3.30×10⁻¹³  
   • WME模型：OR=1.0952，95%CI \[1.0394, 1.1541\]，p=6.58×10⁻⁴  
   • MRAPS模型：OR=1.1103，95%CI \[1.0686, 1.1536\]，p=8.46×10⁻⁸  
   • 结论：儿童期肥胖与膝OA存在显著因果关联3. 次要结局：儿童期肥胖与髋骨关节炎   • 存在显著异质性（Q=26.75，p=0.0135），采用随机效应模型   • MR-PRESSO识别异常值rs9941349，剔除后：   • IVW模型：OR=1.1272，95%CI \[1.0610, 1.1976\]，p=1.07×10⁻⁴  
   • WME模型：OR=1.0944，95%CI \[1.0216, 1.1723\]，p=1.02×10⁻²  
   • MRAPS模型：OR=1.1238，95%CI \[1.0536, 1.1987\]，p=3.89×10⁻⁴  
   • 结论：儿童期肥胖与髋OA存在显著因果关联4. 敏感性分析   • 逐一剔除法显示：去除任一IV后，总体结果方向保持一致，无明显单个IV驱动效应   • 无定向多效性证据，结果稳健可靠

## 六、对其他研究领域的启发

1. 慢性病早期预防与"生命历程"流行病学    本研究证实儿童期肥胖对中年及老年期OA风险具有因果影响，支持了"生命历程"理论在慢性病研究中的应用。这提示其他慢性退行性疾病（如心血管疾病、2型糖尿病、某些癌症）的研究也应关注儿童期暴露的长期健康效应，推动从"治疗已病"向"预防未病"转变。2. 孟德尔随机化方法的拓展应用   研究展示了MR在揭示早期暴露与远期结局因果关系中的独特优势。该方法可推广至：   • 儿童期营养/运动与成年期代谢综合征   • 青少年期BMI轨迹与老年期认知功能障碍   • 早期生活环境与自身免疫性疾病   • 生命早期微生物暴露与过敏性疾病3. 公共数据库整合利用策略   研究充分利用了EGG、UK Biobank、GWAS catalog等公共数据库，为资源有限的研究团队提供了"数据驱动型"研究的范例。未来研究可借鉴此模式，通过跨数据库整合实现大样本、多结局的因果推断。4. 方法学启示：阈值放宽与质量控制平衡   面对严格全基因组显著性阈值下工具变量不足的问题，本研究采用放宽阈值（p<5×10⁻⁶）并通过F统计量、多效性检验、异常值剔除等多重质控手段确保结果可靠性。这一策略可为其他面临类似方法学挑战的MR研究提供参考。

## 总结

该研究通过严谨的两样本孟德尔随机化分析，首次从遗传学角度证实了儿童期肥胖与骨关节炎（尤其是膝OA和髋OA）之间存在因果关联。主要发现包括：• 遗传预测的儿童期肥胖使总体OA风险增加（OR=1.0075）• 膝OA风险显著增加（OR=1.1067）• 髋OA风险显著增加（OR=1.1272）  

该研究的重要价值在于：  

【理论层面】为"儿童期肥胖\-成年期OA"的因果链条提供了遗传学证据，支持生命早期暴露对远期健康结局的持久影响，丰富了OA病因学的"发育起源"理论。【方法层面】展示了在严格全基因组阈值下工具变量不足时，通过合理放宽阈值并配合多重质量控制（F统计量、pheWAS排查、MR-PRESSO异常值剔除、多模型验证）仍可获得可靠因果推断的策略。  

【临床层面】明确提示有儿童期肥胖史的个体需要针对性的临床关注以预防膝、髋OA的发生。这为儿科、骨科、公共卫生等多学科协作制定早期干预策略提供了循证依据。  

孟德尔随机化分析实操课程见如下文章：

[【孟德尔随机化分析代码实操录播课：全流程精讲+真实数据复现+附代码】](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247487821&idx=1&sn=9a1cbb883baaf5faf2c1a6d1bd5b24b7&scene=21#wechat_redirect)

详细分析流程内容见如下文章：

[(三)孟德尔随机化分析（MR）完整流程及可视化解读（保姆级实操详解）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247487518&idx=1&sn=0b66006d5ae47132a5bd68b32e95d229&scene=21#wechat_redirect)

关注即成长👆👆，优质内容助你更上一层！

\---------------end-----------------

往期精彩内容：

1. [RNA-seq（完整）：转录组测序分析（论文级数据分析及可视化全套）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247483871&idx=1&sn=592cbee7528fd412587af3be5561fd7e&scene=21#wechat_redirect)

2. [Label-Free 全蛋白质组学分析（论文级数据分析及可视化全套）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247483994&idx=1&sn=447a0cefbecbd71847c97e31ee82475b&scene=21#wechat_redirect)

3. [医学综述训练营，限时开放](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247483894&idx=1&sn=ad07d19d98b6402f29357c63a43b67c8&scene=21#wechat_redirect)

4.[（零基础）Deep Seek大模型医学创新+影像组学顶刊论文复现实操培训班](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247483983&idx=1&sn=8974a4beb4157272063ffde83d703adf&scene=21#wechat_redirect)

5. [Python及PyCharm保姆级下载安装配置详细教程](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247484122&idx=1&sn=4821fd81a74afecef4bb5d961db5bb07&scene=21#wechat_redirect)

6.[PyCharm保姆级详细使用手册（Python新手快速上手篇）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247484069&idx=1&sn=3e62641b7a341f39ddec81ff48b0b11d&scene=21#wechat_redirect)

7.[（一）推荐一款绘图神器Origin，助你高效数据分析绘图（保姆级安装使用实操快速上手篇）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247484295&idx=1&sn=48c3091b4af265394adec47bce90d907&scene=21#wechat_redirect)

8.[(二)网络毒理学分析完整流程（保姆级实操详解）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247484643&idx=1&sn=bca73f937b2574adb67b430975c60f39&scene=21#wechat_redirect)

9.[(二)孟德尔随机化分析（MR）完整流程（保姆级实操详解）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247485238&idx=1&sn=5169d98d879e002e67f010310c4f8ed4&scene=21#wechat_redirect)

10.[(二)中药网络药理学分析完整流程（保姆级实操详解）](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247485254&idx=1&sn=1d175b74ccb4a4a0e69184f8a31318dc&scene=21#wechat_redirect)

11.[【无实验数据发表文章，文献计量分析代码实操录播课】](https://mp.weixin.qq.com/s?__biz=MzkyNjY2OTYxNw==&mid=2247487196&idx=1&sn=581d98837e0ddc9b5e4cf0b4bcb72445&scene=21#wechat_redirect)

私人定制：

若有个性化生信分析需求、转录组分析、蛋白组分析、单细胞转录组、孟德尔随机化、网络毒理学、网络药理学、文献计量分析等分析需求或者科研辅导、实验指导、写作辅导、壁报辅导等可联系 文文老师 ，助你更上一层

![](https://mmbiz.qpic.cn/mmbiz_jpg/usN6WhNLgsRCfibD0RY6epLH7FV3FUcmjsVDyS3mkunvEAzsDibicckHp3MfR9EtlaWtCXoqqGC0Rx3tGL9ggrf3w/640?wx_fmt=jpeg)