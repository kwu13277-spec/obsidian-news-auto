# Schoenfeld 残差：检验比例风险假设的原理、模拟与解读

内容类型：主题知识介绍

## 摘要

本文介绍 Schoenfeld 残差（Schoenfeld residuals）的原理、为什么它能检验 Cox 模型的比例风险假设、如何通过模拟数据验证其表现，以及实际分析中如何解读结果。面向初学者，配有完整 R 代码演示。

## 关键词

Schoenfeld 残差；比例风险假设；Cox 比例风险模型；scaled Schoenfeld residuals；时间-交互作用；PH 假设检验

## 大纲

1. 为什么需要检验比例风险假设
2. Schoenfeld 残差的核心思想
3. 从残差到正式检验：scaled Schoenfeld residuals
4. 模拟数据设计：构建符合 / 违反 PH 假设的场景
5. R 代码完整演示
6. 结果解读指南
7. 常见误区与处理建议

---

## 正文

### 1. 为什么需要检验比例风险假设

本节概要：本节说明 Cox 模型的核心假设是什么，以及违反它会带来什么问题。

- **Cox 模型的核心公式**：
  $$
  h(t|X) = h_0(t) \exp(\beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_p X_p)
  $$

  - $h(t|X)$：在协变量 X 下的风险函数（hazard function）
  - $h_0(t)$：基准风险函数，完全不加任何假设（Cox 把它留在外面不估计）
  - $\exp(\beta_1 X_1 + \cdots)$：协变量对风险的**倍数效应**

- **比例风险（Proportional Hazards, PH）假设**：$\exp(\beta X)$ 这一项**不随时间变化**。
  - 意思是：某个因素（如服药 vs 不服药）在整个随访期间对风险的**倍数关系是固定的**。
  - 例如：服药组的死亡风险始终是未服药组的 0.5 倍（HR = 0.5），不管是在随访第 1 个月还是第 5 年。

- **违反 PH 假设的典型情况**：
  - 某种治疗的效果随时间衰减（早期有效，后期无效）。
  - 某种生物标志物只在疾病早期有预测价值。
  - 手术风险在术后早期极高，但长期存活者风险回归正常。

- **违反 PH 假设的后果**：
  - Cox 模型估计的 HR 是"平均效应"，如果效应随时间变化，这个平均值没有实际意义。
  - 检验效能下降，可能漏掉真正有作用的变量。
  - 可能导致完全相反的错误结论。

> 所以，做 Cox 回归后，检验 PH 假设是标准流程中的必要步骤。

---

### 2. Schoenfeld 残差的核心思想

本节概要：本节用最直观的方式解释 Schoenfeld 残差是什么、它为什么能检测 PH 假设是否成立。

#### 2.1 残差直觉

- 对于每个**事件发生的时间点** $t_i$，Schoenfeld 残差计算的是：**在那一刻发生事件的那个人的协变量值，减去"如果 PH 假设成立，我们预期这个人协变量值应该是多少"**。
  
  公式形式（对于协变量 $k$）：
  $$
  r_{ik} = X_{ik} - \frac{\sum_{j \in R(t_i)} X_{jk} \exp(\beta X_j)}{\sum_{j \in R(t_i)} \exp(\beta X_j)}
  $$

  其中 $R(t_i)$ 是在 $t_i$ 时刻仍然处于风险中的个体集合（risk set）。

- **白话解释**：
  - 在时间 $t_i$，一个人去世了。他的某个特征（比如年龄 = 65）是多少。
  - 在那一刻，所有还活着的人的平均年龄是多少（比如 60）。
  - 残差 = 65 − 60 = 5。
  - 如果 PH 假设成立，这个残差**随时间没有趋势**——既不会越来越大，也不会越来越小。

#### 2.2 为什么残差的趋势能检验 PH 假设

- 如果 PH 假设成立（HR 不随时间变化），那么 Cox 模型估计的 $\beta$ 在整个时间轴上都是正确的。
  - 每个时间点的 Schoenfeld 残差围绕 0 随机波动，没有系统性趋势。

- 如果 PH 假设被违反（HR 随时间变化），那么用一个"固定 $\beta$"去预测每个时间点的"预期协变量"就会产生系统性偏差。
  - 如果某变量的效应随时间减弱：早期残差偏正，晚期残差偏负（或反过来），形成一条**有斜率的趋势线**。

- **关键直觉**：Schoenfeld 残差 vs 时间 的散点图→如果趋势线接近水平（斜率为 0），PH 假设成立；如果趋势线有明显斜率，PH 假设被违反。

---

### 3. 从残差到正式检验：scaled Schoenfeld residuals

本节概要：说明实际软件中使用的标准化版本和对应的假设检验方法。

#### 3.1 为什么要 scaling（缩放）

- 原始 Schoenfeld 残差的方差在不同时间点不一样（早期风险集大，方差小；晚期风险集小，方差大）。
- 直接对原始残差做回归检验，会因为方差不齐而产生偏倚。

#### 3.2 Scaled Schoenfeld residuals

- 公式：
  $$
  r_{ik}^* = m \times \text{Var}(r_k)^{-1} \times r_{ik}
  $$
  其中 $m$ 是事件总数，$\text{Var}(r_k)$ 是协变量 $k$ 的残差协方差矩阵。

- 缩放后，**每个残差的方差被标准化为 1**，可以像普通回归一样做检验。

#### 3.3 Grambsch & Therneau 检验（PH 假设的正式检验）

- 对 scaled Schoenfeld residuals 和时间做回归：
  $$
  r_k^*(t) = \beta_k + \gamma_k \times f(t) + \epsilon
  $$
  其中 $f(t)$ 是时间的某种函数（可以是线性、秩变换、KM 变换等，默认使用 KM 变换）。

- **零假设**：$\gamma_k = 0$，即残差与时间无关 → PH 假设成立。

- **输出指标**：
  - $\chi^2$ 统计量
  - $p$ 值：$p < 0.05$ 提示 PH 假设被违反。

- **全局检验**：对所有协变量联合检验，看模型整体是否满足 PH 假设。

#### 3.4 R 中的实现：`cox.zph()`

```r
library(survival)
fit <- coxph(Surv(time, status) ~ age + trt, data = dat)
test <- cox.zph(fit)
print(test)
plot(test)  # 绘制残差趋势图
```

- `cox.zph()` 默认使用 Kaplan-Meier 变换后的时间尺度。
- `plot()` 会显示每个协变量的 scaled Schoenfeld residuals 散点图 + 平滑拟合曲线。

---

### 4. 模拟数据设计

本节概要：本节设计两组模拟数据——一组符合 PH 假设，一组违反 PH 假设——为后续演示做准备。

#### 4.1 场景 A：PH 假设成立

- 一个治疗分组变量 `trt`（0 = 对照组，1 = 治疗组）
- 真实 HR 固定为 0.5（治疗组风险始终是对照组的一半）
- 生存时间用 Weibull 分布生成，两组共享相同的 shape 参数

#### 4.2 场景 B：PH 假设被违反

- 治疗分组变量相同，但**治疗效果随时间衰减**
- 模拟方法：让 log(HR) 随时间线性变化
- 设定：在 $t=0$ 时 HR = 0.3（强保护），在 $t=10$ 时 HR = 1.0（完全失效）

#### 4.3 数据规模

- 每组样本量 N = 200
- 删失率控制在 20%-30%
- 随访时间范围 0-10 年

---

### 5. R 代码完整演示

本节概要：完整的 R 模拟、拟合、检验和可视化代码，可直接复制运行。

#### 5.1 加载包与设定随机种子

```r
library(survival)
library(ggplot2)
library(dplyr)
set.seed(2024)
```

#### 5.2 生成符合 PH 假设的数据（场景 A）

```r
# 场景 A：PH 假设成立
n <- 200
trt <- rbinom(n, 1, 0.5)

# Weibull 基础生存：shape=1.5, scale(对照)=5
# 治疗组 HR=0.5（恒定）
shape <- 1.5
scale_ctrl <- 5
scale_trt <- scale_ctrl / 0.5^(1/shape)  # 使 HR 约为 0.5

Tlat <- ifelse(
  trt == 0,
  rweibull(n, shape = shape, scale = scale_ctrl),
  rweibull(n, shape = shape, scale = scale_trt)
)

# 生成删失时间（独立删失）
C <- rexp(n, rate = 1/15)
time <- pmin(Tlat, C)
status <- as.numeric(Tlat <= C)

datA <- data.frame(time = time, status = status, trt = trt)
```

#### 5.3 生成违反 PH 假设的数据（场景 B）

```r
# 场景 B：PH 假设被违反 —— 治疗效果随时间衰减
n <- 200
trt <- rbinom(n, 1, 0.5)

# 用分段方法模拟时间变化效应
# 基础风险来自指数分布（rate=0.15）
# log(HR) 随时间线性变化：从 log(0.3) 到 log(1.0)
# 即早期 HR≈0.3（强保护），随时间逐渐衰减到 HR=1.0（无效）

hazard_rate <- function(t, trt) {
  base_rate <- 0.15
  if (trt == 0) return(base_rate)
  # 随时间衰减的效应：log(HR) 从 log(0.3) 线性增加到 log(1.0)
  log_hr <- log(0.3) + (log(1.0) - log(0.3)) * min(t / 10, 1)
  return(base_rate * exp(log_hr))
}

# 用逆变换法生成生存时间
generate_surv_time <- function(trt) {
  u <- runif(1)
  # 数值积分求解
  f <- function(t) {
    integrate(function(s) hazard_rate(s, trt), 0, t)$value + log(u)
  }
  uniroot(f, c(0, 50))$root
}

Tlat <- sapply(trt, generate_surv_time)
C <- rexp(n, rate = 1/15)
time <- pmin(Tlat, C)
status <- as.numeric(Tlat <= C)

datB <- data.frame(time = time, status = status, trt = trt)
```

#### 5.4 拟合 Cox 模型并进行 PH 假设检验

```r
# 场景 A：PH 成立
fitA <- coxph(Surv(time, status) ~ trt, data = datA)
testA <- cox.zph(fitA)
print("=== 场景 A：PH 假设成立 ===")
print(summary(fitA))
print(testA)

# 场景 B：PH 被违反
fitB <- coxph(Surv(time, status) ~ trt, data = datB)
testB <- cox.zph(fitB)
print("=== 场景 B：PH 假设被违反 ===")
print(summary(fitB))
print(testB)
```

#### 5.5 绘制 Schoenfeld 残差图

```r
par(mfrow = c(1, 2))
plot(testA, main = "场景 A：PH 假设成立")
abline(h = 0, lty = 2, col = "gray")
plot(testB, main = "场景 B：PH 假设被违反")
abline(h = 0, lty = 2, col = "gray")
```

---

### 6. 结果解读指南

本节概要：教初学者如何看 `cox.zph()` 的输出表和残差图。

#### 6.1 解读 `cox.zph()` 的输出表

输出示例：

```
        chisq df    p
trt      0.34  1  0.56   ← PH 成立时 p 值很大
GLOBAL   0.34  1  0.56
```

```
        chisq df    p
trt      7.82  1 0.005   ← PH 被违反时 p 值很小
GLOBAL   7.82  1 0.005
```

解读步骤：

1. **先看 p 值**：
   - $p > 0.05$ → 没有充分证据拒绝 PH 假设，可以接受 Cox 模型的结果。
   - $p < 0.05$ → PH 假设可能被违反，需要进一步处理。

2. **再看具体协变量**：
   - 多变量模型中，有的变量 $p > 0.05$、有的 $p < 0.05$。
   - 只有 $p < 0.05$ 的变量需要处理，其他变量保持原状即可。

3. **查看全局检验（GLOBAL）**：
   - 对所有协变量联合检验。
   - 如果全局显著，说明模型中至少有一个变量违反了 PH 假设。

#### 6.2 解读 Schoenfeld 残差图

- **X 轴**：时间（或时间变换后的尺度）
- **Y 轴**：scaled Schoenfeld residuals + Beta(t) 值
- **实线**：平滑拟合曲线（残差随时间的趋势）
- **虚线**：$\pm 2$ 标准误
- **水平虚线**：$\beta$（模型估计的固定效应）

**三种典型图形模式**：

| 图形特征 | 含义 | 严重程度 |
|---------|------|---------|
| 拟合线接近水平，围绕固定 $\beta$ 波动 | PH 假设成立 | ✅ |
| 拟合线有明显上升或下降趋势 | PH 假设被违反 | ⚠️ |
| 拟合线弯曲（先上升后下降等） | 效应随时间复杂变化 | 🚨 |

**重要提示**：不要只看 p 值，一定要结合残差图判断趋势的大小和临床意义。大样本中，即使微小的偏离也会产生显著的 p 值，但如果趋势线偏离不大，Cox 模型仍可接受。

#### 6.3 模拟结果预期

| 场景 | HR 估计 | cox.zph() p 值 | 残差图趋势 |
|------|---------|---------------|-----------|
| A：PH 成立 | HR ≈ 0.5（正确估计） | p > 0.05 | 水平趋势线 |
| B：PH 被违反 | HR ≈ 0.6（平均效应，不反映真实时间变化） | p < 0.05 | 明显上升趋势（残差从负到正） |

场景 B 中，Cox 模型报告的 HR 约 0.6，是 0.3 到 1.0 的"平均"值，这个数字不能准确描述"早期有效、后期无效"的真实情况。

---

### 7. 常见误区与处理建议

本节概要：初学者最容易踩的坑，以及在 PH 违反后的可操作策略。

#### 7.1 常见误区

- **❌ 误区 1：cox.zph() p > 0.05 就万事大吉**
  - 大样本中即使微小的偏离也会显著，要结合残差图判断效应大小。

- **❌ 误区 2：p < 0.05 直接放弃 Cox 模型**
  - PH 违反不意味着 Cox 模型完全不能用，有多种处理策略。

- **❌ 误区 3：把所有变量一起做 cox.zph() 就完事了**
  - 对于连续变量（年龄、BMI 等），分层检验和图形检查同样重要。

- **❌ 误区 4：把 Schoenfeld 残差图错当成"残差越大数据越差"**
  - Schoenfeld 残差的**趋势**（而非大小）是诊断依据。单个残差点的大小没有诊断意义。

#### 7.2 PH 假设违反后的处理策略

| 策略 | 适用场景 | R 实现 |
|------|---------|--------|
| **分层 Cox 模型** (strata) | 分类变量（如中心、性别）违反 PH | `coxph(Surv(time, status) ~ strata(trt) + age)` |
| **时间交互项** (tt) | 连续或分类变量的效应线性变化 | `coxph(Surv(time, status) ~ trt + tt(trt), tt = function(x, t, ...) x * t)` |
| **限制平均生存时间** (RMST) | 不需要 HR，直接比较平均生存时间 | `survRM2::rmst2()` |
| **分段模型** | 效应有明确的转折点 | 分时间段分别拟合 |
| **加速失效时间模型** (AFT) | 完全不依赖 PH 假设 | `survreg(Surv(time, status) ~ trt, dist = "weibull")` |

- **推荐的决策流程**：
  1. 运行 `cox.zph()`，看 p 值和残差图。
  2. 如果 p < 0.05 且趋势明显 → 加入时间交互项。
  3. 检查时间交互项的显著性。
  4. 如果交互项也显著 → 使用分层模型或 RMST。

#### 7.3 给初学者的建议

- **先跑完整流程**：Cox 模型 → `cox.zph()` → 看 p 值 → 画残差图 → 判断趋势。
- **残差图比 p 值更可靠**：图形可以告诉你偏离的方向和程度，这是单一 p 值无法提供的。
- **不要把 PH 假设当作"过不过"的考试**：它是一个诊断工具，告诉你模型是否足够好地描述了数据。
- **如果 PH 违反不严重**（趋势线偏离不大、p 值在 0.01-0.05 之间），很多人会选择忽略，在论文中报告"轻微违反 PH 假设"即可。

---

### 参考

- Grambsch, P. M., & Therneau, T. M. (1994). Proportional hazards tests and diagnostics based on weighted residuals. *Biometrika*, 81(3), 515-526.
- Therneau, T. M., & Grambsch, P. M. (2000). *Modeling Survival Data: Extending the Cox Model*. Springer.
- R Documentation: `?cox.zph`

---
