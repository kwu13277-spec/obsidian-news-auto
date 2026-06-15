# UK Biobank 中肺炎、结核与泌尿系感染的表型定义：数据来源与 ICD-10 编码

> 适用场景：在 UK Biobank（UKB）中构建感染性疾病暴露、结局或协变量，例如肺炎、结核、泌尿系感染（urinary tract infection, UTI）的病例定义、基线患病排除、随访事件识别与敏感性分析。  
> 检索日期：2026-05-12  
> 说明：本文档按 UKB 可复现研究口径整理。实际分析时，应以本人 UKB 项目下载的数据版本、数据截止日期和访问权限为准。

---

## 1. 总体结论

### 1.1 推荐主定义

| 疾病/表型 | 推荐主定义 | 推荐 UKB 数据来源 | 事件日期 |
|---|---|---|---|
| 肺炎 | ICD-10 `J12–J18` | 住院 ICD-10 汇总 `Field 41270`，必要时合并死亡登记 `Field 40001/40002` | 住院日期用 `Field 41280`；若使用 First occurrences，则用对应 3 位 ICD-10 首次发生日期字段 |
| 结核 | ICD-10 `A15–A19` | 住院 ICD-10 汇总 `Field 41270`，必要时合并死亡登记 `Field 40001/40002` | 同上 |
| 泌尿系感染 / UTI，严格定义 | ICD-10 `N39.0` | 优先使用原始 4 位 ICD-10：`Field 41270` 或 record-level `HESIN_DIAG.DIAG_ICD10`；必要时合并死亡登记 | `Field 41280` 或 record-level episode date |
| 泌尿系感染 / UTI，宽定义 | `N39.0` + `N10–N12` + `N30` + `N34`；可选加入 `N13.6`、`N15.1`、`N15.9` | 同上 | 同上 |
| 整个泌尿系统疾病，而非感染 | ICD-10 `N00–N99` | 不建议作为“感染”定义；这是整个 genitourinary system diseases 范围 | 取决于具体研究问题 |

核心建议：  
1. 如果研究目的是定义“感染性疾病”，不要把 `N00–N99` 直接称为“泌尿系感染”。`N00–N99` 是整个泌尿生殖系统疾病章节，包含肾炎、肾衰、结石、前列腺疾病、生殖系统疾病等大量非感染性疾病。  
2. 如果研究目的是定义 UTI，最保守定义是 `N39.0`。  
3. 如果希望覆盖上尿路、膀胱、尿道等感染相关诊断，可使用宽定义：`N39.0`、`N10–N12`、`N30`、`N34`；对于复杂尿路感染，可在敏感性分析中加入 `N13.6`、`N15.1`、`N15.9`。  
4. UKB 的 First occurrences 字段只映射到 3 位 ICD-10，因此 `N39` 不能等价于 `N39.0`。如果要严格定义 UTI，应使用原始 4 位 ICD-10 数据。

---

## 2. UKB 可用数据来源

### 2.1 住院 ICD-10 汇总数据：首选数据源

| UKB 字段 | 含义 | 用途 |
|---|---|---|
| `Field 41270` | Diagnoses - ICD10 | 每位参与者住院记录中出现过的 ICD-10 诊断汇总，包含主诊断或次诊断位置 |
| `Field 41280` | Date of first in-patient diagnosis - ICD10 | 与 `Field 41270` 对应，给出该 ICD-10 诊断首次出现在住院记录中的日期 |
| `Field 41202` | Diagnoses - main ICD10 | 仅主诊断 ICD-10；更严格，但敏感性较低 |
| `Field 41204` | Diagnoses - secondary ICD10 | 次诊断 ICD-10；可用于区分主诊断与伴随诊断 |

推荐用法：

```text
病例 = Field 41270 中任意 ICD-10 代码匹配目标 code list
事件日期 = 与该 ICD-10 代码数组位置对应的 Field 41280 日期
```

如果研究需要更高特异性，可做敏感性分析：

```text
严格病例 = Field 41202 主诊断中匹配目标 code list
宽病例 = Field 41270 主诊断或次诊断中匹配目标 code list
```

---

### 2.2 Record-level 住院数据：用于精细分析

UKB 住院 record-level 数据包括多个表：

| 表 | 用途 |
|---|---|
| `HESIN` | 住院 episode/spell 层面的基本信息，如入院日期、episode start date 等 |
| `HESIN_DIAG` | 住院诊断代码表，包含 `DIAG_ICD10` |
| `HESIN_OPER` | 手术/操作代码 |
| `HESIN_CRITICAL` | 重症监护相关记录 |
| `HESIN_PSYCH` | 精神科住院记录 |
| `HESIN_MATERNITY` / `HESIN_DELIVERY` | 产科相关记录 |

如果只需要“是否发生某疾病”和“首次发生时间”，`Field 41270 + Field 41280` 通常足够。  
如果需要处理同一次住院、重复住院、诊断位置、episode/spell 层级、不同地区数据差异，建议使用 record-level `HESIN_DIAG` 与 `HESIN`。

---

### 2.3 死亡登记数据：用于补充致死病例

| UKB 字段 | 含义 | 用途 |
|---|---|---|
| `Field 40001` | Underlying primary cause of death: ICD10 | 根本死因 ICD-10 |
| `Field 40002` | Contributory secondary causes of death: ICD10 | 继发/贡献死因 ICD-10，可有 0 个、1 个或多个 |
| `Field 40000` | Date of death | 死亡日期 |
| `Field 40007` | Age at death | 死亡年龄 |

推荐用法：

```text
死亡补充病例 = Field 40001 或 Field 40002 中 ICD-10 代码匹配目标 code list
事件日期 = Field 40000
```

对于肺炎、结核等可能作为死亡原因出现的感染性疾病，建议至少在敏感性分析中合并死亡登记数据。

---

### 2.4 First occurrences：用于快速获取跨来源首次发生日期

UKB 的 First occurrences 类别将多种来源映射到 3 位 ICD-10，包括：

1. Primary care 的 Read code 信息；
2. Hospital inpatient 的 ICD-9/ICD-10；
3. Death register 的 ICD-10；
4. 基线或后续评估中心自报疾病 `Field 20002`。

该类别为每个 3 位 ICD-10 代码提供两个字段：

```text
Date field   = 首次记录日期
Source field = 首次记录来源，以及是否后续在其他来源中也出现
```

优点：  
- 快速获得跨来源首次发生日期；
- 适合构建某些常见疾病的首次发生时间；
- 可用于基线排除或随访结局识别。

局限：  
- 只到 3 位 ICD-10，不能区分 `N39.0` 与其他 `N39.*`；
- 对肺炎 `J12–J18`、结核 `A15–A19`可用；
- 对 UTI 严格定义 `N39.0` 不推荐直接使用 First occurrence 的 `N39` 作为唯一依据。

---

### 2.5 Primary care / GP 数据

UKB 的 primary care 数据来源于 GP 系统，包含诊断、处方、转诊等编码信息，但覆盖并非全队列。UKB 数据说明中提到 GP 数据约覆盖 UKB 队列的 45%，并且不同供应商和地区的覆盖时间不同。

适用场景：

| 场景 | 是否建议使用 GP 数据 |
|---|---|
| 需要提高感染事件敏感性 | 建议 |
| 仅使用全队列住院结局 | 可不使用 |
| 分析轻症 UTI 或社区获得性感染 | 强烈建议考虑 |
| 需要与全队列保持一致可比性 | 谨慎使用，因为 GP 数据覆盖不完整 |

若使用 GP 数据，建议在论文中明确：

```text
Primary care data were available for a subset of UK Biobank participants; therefore, analyses incorporating GP records were performed as supplementary or sensitivity analyses.
```

---

### 2.6 自报疾病 `Field 20002`

`Field 20002` 是 Non-cancer illness code, self-reported，主要来自基线或后续评估中心访谈/问卷。

对于肺炎、结核、UTI 这类感染性疾病：

| 用法 | 建议 |
|---|---|
| 基线既往史补充 | 可考虑 |
| 主结局定义 | 不建议单独使用 |
| 与 First occurrences 合并 | 可用，但需要说明可能存在回忆偏倚 |
| 轻症感染识别 | 自报可靠性有限，优先 GP 或住院数据 |

---

## 3. 数据可用性与截止日期注意事项

UKB 对不同数据源有不同的数据供应商、覆盖时间和推荐 censoring date。需要在研究方案中写明所用数据版本和截止日期。

### 3.1 住院数据来源

| 地区 | 数据源 | ICD-10 可用时间 | UKB 页面给出的参考 censoring date |
|---|---|---:|---:|
| England | Hospital Episode Statistics, HES / NHS England | 1997 onwards | 2023-03-31 |
| Scotland | Scottish Morbidity Record, SMR / ISD Scotland | 1996 onwards | 2022-08-31 |
| Wales | Patient Episode Database for Wales, PEDW / SAIL | 1999 onwards | 2022-05-31 |

### 3.2 死亡登记

| 地区 | 数据源 | ICD-10 可用时间 | UKB 页面给出的参考 censoring date |
|---|---|---:|---:|
| England & Wales | NHS England | 2006 onwards / ICD-10 from April 2006 onwards | 2024-08-31 |
| Scotland | NHS Central Register / National Records of Scotland | 2006 onwards / ICD-10 from April 2006 onwards | 2024-11-30 |

### 3.3 Primary care / GP

| 地区或供应商 | 大致覆盖人数 | 参考覆盖终点 |
|---|---:|---:|
| England TPP | 约 165,000 | 2016-05-31 |
| England Vision | 约 18,000 | 2017-05-31 |
| Scotland Vision/EMIS | 约 27,000 | 2017-03-31 |
| Wales Vision/EMIS | 约 21,000 | 2017-08-31 |

注意：  
上述日期是 UKB 页面给出的参考信息。实际研究必须以项目下载数据的 release、字段版本和数据截止日期为准。

---

## 4. 疾病定义与 ICD-10 code list

## 4.1 肺炎 Pneumonia

### 推荐定义

```text
Pneumonia = ICD-10 J12–J18
```

### 代码表

| ICD-10 | 英文名称 | 中文解释 | 是否纳入主定义 |
|---|---|---|---|
| `J12` | Viral pneumonia, not elsewhere classified | 病毒性肺炎，未另分类 | 是 |
| `J13` | Pneumonia due to Streptococcus pneumoniae | 肺炎链球菌性肺炎 | 是 |
| `J14` | Pneumonia due to Haemophilus influenzae | 流感嗜血杆菌性肺炎 | 是 |
| `J15` | Bacterial pneumonia, not elsewhere classified | 细菌性肺炎，未另分类 | 是 |
| `J16` | Pneumonia due to other infectious organisms, not elsewhere classified | 其他感染性病原体所致肺炎 | 是 |
| `J17` | Pneumonia in diseases classified elsewhere | 其他疾病分类中的肺炎 | 是，可做敏感性分析排除 |
| `J18` | Pneumonia, organism unspecified | 病原体未特指的肺炎 | 是 |
| `J69.0` | Pneumonitis due to food and vomit | 吸入性肺炎/吸入性肺炎样病变 | 不纳入主定义；可作为敏感性分析 |
| `J09–J11` | Influenza | 流感及流感相关疾病 | 不纳入主定义；若研究“流感和肺炎”可另行纳入 |

### UKB First occurrence 字段

| ICD-10 | Date field | Source field |
|---|---:|---:|
| `J12` | `131444` | `131445` |
| `J13` | `131446` | `131447` |
| `J14` | `131448` | `131449` |
| `J15` | `131450` | `131451` |
| `J16` | `131452` | `131453` |
| `J17` | `131454` | `131455` |
| `J18` | `131456` | `131457` |

### 推荐论文写法

```text
Pneumonia was defined using ICD-10 codes J12–J18 recorded in linked hospital inpatient records. The primary ascertainment source was UK Biobank Field 41270, which summarises ICD-10 diagnoses recorded in either primary or secondary positions across hospital inpatient records. The first inpatient diagnosis date was obtained from Field 41280. Death register ICD-10 codes in Fields 40001 and 40002 were additionally considered in sensitivity analyses.
```

中文版本：

```text
肺炎定义为 UK Biobank 住院记录中 ICD-10 代码 J12–J18。主要数据来源为 Field 41270，该字段汇总了参与者住院记录中主诊断或次诊断位置出现过的 ICD-10 诊断；首次住院诊断日期由 Field 41280 获得。敏感性分析中进一步合并死亡登记中的 Field 40001 和 Field 40002。
```

---

## 4.2 结核 Tuberculosis

### 推荐定义

```text
Tuberculosis = ICD-10 A15–A19
```

该定义更接近“活动性结核病”。如果研究对象是 latent tuberculosis infection，应另行考虑相关代码，例如 `Z22.7` 或 primary care/实验室/用药记录，但这不等同于活动性结核。

### 代码表

| ICD-10 | 英文名称 | 中文解释 | 是否纳入主定义 |
|---|---|---|---|
| `A15` | Respiratory tuberculosis, bacteriologically and histologically confirmed | 经细菌学或组织学确认的呼吸系统结核 | 是 |
| `A16` | Respiratory tuberculosis, not confirmed bacteriologically or histologically | 未经细菌学或组织学确认的呼吸系统结核 | 是 |
| `A17` | Tuberculosis of nervous system | 神经系统结核 | 是 |
| `A18` | Tuberculosis of other organs | 其他器官结核 | 是 |
| `A19` | Miliary tuberculosis | 粟粒性结核 | 是 |
| `A31` | Infection due to other mycobacteria | 其他分枝杆菌感染 | 不纳入结核主定义 |
| `Z22.7` | Carrier of tuberculosis / latent TB-related coding in some systems | 潜伏结核/携带状态相关编码 | 不纳入活动性结核主定义 |

### UKB First occurrence 字段

| ICD-10 | Date field | Source field |
|---|---:|---:|
| `A15` | `130020` | `130021` |
| `A16` | `130022` | `130023` |
| `A17` | `130024` | `130025` |
| `A18` | `130026` | `130027` |
| `A19` | `130028` | `130029` |

### 推荐论文写法

```text
Tuberculosis was defined using ICD-10 codes A15–A19 in linked hospital inpatient records and, where applicable, death register records. A15–A19 capture respiratory tuberculosis, tuberculosis of the nervous system, tuberculosis of other organs, and miliary tuberculosis. Non-tuberculous mycobacterial infections were not included in the primary definition.
```

中文版本：

```text
结核定义为 ICD-10 代码 A15–A19，数据来源为 UK Biobank 住院 ICD-10 诊断记录，并在敏感性分析中合并死亡登记记录。A15–A19 覆盖呼吸系统结核、神经系统结核、其他器官结核和粟粒性结核。非结核分枝杆菌感染不纳入主定义。
```

---

## 4.3 泌尿系感染 Urinary tract infection / UTI

### 重要区分

“泌尿系”有三种可能含义：

| 中文表述 | 英文/统计含义 | 推荐 ICD-10 |
|---|---|---|
| 泌尿系统疾病 | Diseases of genitourinary system | `N00–N99`，但这不是感染定义 |
| 泌尿系统感染 / UTI | Urinary tract infection | 严格：`N39.0`；宽：`N39.0 + N10–N12 + N30 + N34` |
| 复杂泌尿系感染 | Complicated UTI / upper UTI-related | 在宽定义基础上可考虑 `N13.6`、`N15.1`、`N15.9` |

### 严格定义

```text
UTI_strict = ICD-10 N39.0
```

| ICD-10 | 英文名称 | 中文解释 | 说明 |
|---|---|---|---|
| `N39.0` | Urinary tract infection, site not specified | 尿路感染，部位未特指 | 最保守、最常用的 UTI ICD-10 定义 |

### 宽定义

```text
UTI_broad = N39.0 OR N10–N12 OR N30 OR N34
```

| ICD-10 | 英文名称 | 中文解释 | 是否纳入宽定义 |
|---|---|---|---|
| `N10` | Acute tubulo-interstitial nephritis | 急性肾小管间质性肾炎；临床上常覆盖急性肾盂肾炎编码 | 是 |
| `N11` | Chronic tubulo-interstitial nephritis | 慢性肾小管间质性肾炎；可包含慢性肾盂肾炎相关编码 | 是，视研究目的 |
| `N12` | Tubulo-interstitial nephritis, not specified as acute or chronic | 未特指急慢性的肾小管间质性肾炎；可包含未特指肾盂肾炎 | 是 |
| `N30` | Cystitis | 膀胱炎 | 是 |
| `N34` | Urethritis and urethral syndrome | 尿道炎和尿道综合征 | 是 |
| `N39.0` | Urinary tract infection, site not specified | 尿路感染，部位未特指 | 是 |

### 可选扩展：复杂尿路感染敏感性分析

| ICD-10 | 英文名称 | 中文解释 | 建议 |
|---|---|---|---|
| `N13.6` | Pyonephrosis | 脓肾/积脓性肾积水 | 不纳入主定义；可用于复杂 UTI 敏感性分析 |
| `N15.1` | Renal and perinephric abscess | 肾及肾周脓肿 | 不纳入主定义；可用于复杂 UTI 敏感性分析 |
| `N15.9` | Renal tubulo-interstitial disease, unspecified / infection of kidney NOS in some classifications | 未特指肾小管间质疾病 / 肾感染 NOS | 谨慎使用，仅敏感性分析 |

### UKB First occurrence 字段

| ICD-10 3 位码 | Date field | Source field | 备注 |
|---|---:|---:|---|
| `N10` | `132016` | `132017` | 急性肾小管间质性肾炎 |
| `N11` | `132018` | `132019` | 慢性肾小管间质性肾炎 |
| `N12` | `132020` | `132021` | 未特指急慢性的肾小管间质性肾炎 |
| `N30` | `132054` | `132055` | 膀胱炎 |
| `N34` | `132062` | `132063` | 尿道炎和尿道综合征 |
| `N39` | `132070` | `132071` | 其他泌尿系统疾病；注意不等同于 `N39.0` |

### 为什么不建议用 First occurrence 的 `N39` 直接定义 UTI？

因为 UKB First occurrences 映射到 3 位 ICD-10。`N39` 是 “Other disorders of urinary system”，其中可包含：

```text
N39.0 = Urinary tract infection, site not specified
N39.3 = Stress incontinence
N39.4 = Other specified urinary incontinence
N39.8 = Other specified disorders of urinary system
N39.9 = Disorder of urinary system, unspecified
```

因此：

```text
N39 First occurrence ≠ N39.0 UTI
```

推荐处理：

```text
主分析：使用 Field 41270 或 HESIN_DIAG.DIAG_ICD10 中的 4 位代码 N39.0
敏感性分析：加入 N10–N12、N30、N34
若需要跨来源首次日期：可使用 First occurrences 的 N10、N11、N12、N30、N34，但 N39 要谨慎
```

### 推荐论文写法

英文：

```text
Urinary tract infection was primarily defined using ICD-10 code N39.0 in linked hospital inpatient records. To capture site-specific urinary tract infections, a broader definition additionally included N10–N12, N30 and N34. Because UK Biobank first-occurrence fields are mapped to 3-character ICD-10 codes, the N39 first-occurrence field was not used as a strict proxy for N39.0.
```

中文：

```text
泌尿系感染的主定义采用住院记录中的 ICD-10 代码 N39.0。为提高敏感性，宽定义进一步纳入 N10–N12、N30 和 N34。由于 UK Biobank 的 First occurrences 字段仅映射至 3 位 ICD-10，N39 首次发生字段不能严格等同于 N39.0，因此不建议将其作为严格 UTI 定义的唯一依据。
```

---

## 5. 可直接用于分析的 code list

### 5.1 R 代码

```r
# Pneumonia
codes_pneumonia <- c("J12", "J13", "J14", "J15", "J16", "J17", "J18")

# Tuberculosis
codes_tb <- c("A15", "A16", "A17", "A18", "A19")

# UTI strict
codes_uti_strict <- c("N39.0")

# UTI broad
codes_uti_broad_3char <- c("N10", "N11", "N12", "N30", "N34")
codes_uti_broad_4char <- c("N39.0")

# Optional complicated UTI sensitivity
codes_uti_complicated_optional <- c("N13.6", "N15.1", "N15.9")
```

如果 `Field 41270` 中代码有小数点，例如 `N39.0`，可用：

```r
is_uti_strict <- function(x) {
  x %in% c("N39.0")
}

is_pneumonia <- function(x) {
  substr(x, 1, 3) %in% c("J12", "J13", "J14", "J15", "J16", "J17", "J18")
}

is_tb <- function(x) {
  substr(x, 1, 3) %in% c("A15", "A16", "A17", "A18", "A19")
}

is_uti_broad <- function(x) {
  substr(x, 1, 3) %in% c("N10", "N11", "N12", "N30", "N34") | x == "N39.0"
}
```

如果 UKB 导出的代码去掉了小数点，例如 `N390`，应先标准化：

```r
normalize_icd10 <- function(x) {
  x <- toupper(trimws(x))
  x <- gsub("\\.", "", x)
  x
}

is_uti_strict_norm <- function(x) {
  x <- normalize_icd10(x)
  x %in% c("N390")
}
```

---

### 5.2 Python 代码

```python
PNEUMONIA_3 = {"J12", "J13", "J14", "J15", "J16", "J17", "J18"}
TB_3 = {"A15", "A16", "A17", "A18", "A19"}

UTI_STRICT_4 = {"N390", "N39.0"}
UTI_BROAD_3 = {"N10", "N11", "N12", "N30", "N34"}
UTI_COMPLICATED_OPTIONAL_4 = {"N136", "N13.6", "N151", "N15.1", "N159", "N15.9"}

def clean_icd10(code):
    if code is None:
        return None
    return str(code).strip().upper()

def clean_icd10_no_dot(code):
    code = clean_icd10(code)
    if code is None:
        return None
    return code.replace(".", "")

def is_pneumonia(code):
    code = clean_icd10_no_dot(code)
    return code[:3] in PNEUMONIA_3 if code else False

def is_tb(code):
    code = clean_icd10_no_dot(code)
    return code[:3] in TB_3 if code else False

def is_uti_strict(code):
    code_raw = clean_icd10(code)
    code_nodot = clean_icd10_no_dot(code)
    return code_raw == "N39.0" or code_nodot == "N390"

def is_uti_broad(code):
    code_raw = clean_icd10(code)
    code_nodot = clean_icd10_no_dot(code)
    if not code_nodot:
        return False
    return code_nodot[:3] in UTI_BROAD_3 or code_raw == "N39.0" or code_nodot == "N390"
```

---

## 6. 建议的研究表型构建流程

```text
Step 1. 明确疾病定义
        肺炎 = J12–J18
        结核 = A15–A19
        UTI strict = N39.0
        UTI broad = N39.0 + N10–N12 + N30 + N34

Step 2. 选择主数据源
        主分析：Field 41270 + Field 41280
        需要精细 episode 信息：HESIN_DIAG + HESIN
        死亡补充：Field 40001/40002 + Field 40000

Step 3. 构建病例
        若任意 ICD-10 匹配 code list，则定义为 case
        若多个日期，取首次日期

Step 4. 区分 prevalent 与 incident
        prevalent = 首次日期 < baseline date
        incident = 首次日期 >= baseline date

Step 5. 设置随访终点
        event date = 首次诊断日期
        censor date = 死亡、失访、地区数据截止日期或研究预设终点中的最早者

Step 6. 做敏感性分析
        仅主诊断 Field 41202
        主诊断或次诊断 Field 41270
        合并死亡登记
        对 UTI 比较 strict 与 broad 定义
        排除 baseline 前既往感染者
```

---

## 7. 推荐 Methods 写法模板

### 7.1 英文模板

```text
Disease outcomes were ascertained using linked electronic health records in UK Biobank. Hospital inpatient diagnoses were primarily obtained from Field 41270, which summarises ICD-10 diagnosis codes recorded in either primary or secondary diagnostic positions across inpatient records. The corresponding first inpatient diagnosis dates were obtained from Field 41280. Death register records were used as supplementary sources, including underlying cause of death (Field 40001) and contributory causes of death (Field 40002).

Pneumonia was defined using ICD-10 codes J12–J18, and tuberculosis was defined using ICD-10 codes A15–A19. Urinary tract infection was primarily defined using ICD-10 code N39.0; a broader sensitivity definition additionally included N10–N12, N30 and N34. For analyses using UK Biobank first-occurrence fields, we considered the corresponding 3-character ICD-10 first occurrence fields, but did not use the N39 first-occurrence field as a strict proxy for N39.0 because first-occurrence fields are mapped to 3-character ICD-10 codes.
```

### 7.2 中文模板

```text
本研究基于 UK Biobank 链接电子健康记录识别疾病结局。住院诊断主要来自 Field 41270，该字段汇总了参与者住院记录中主诊断或次诊断位置出现过的 ICD-10 诊断代码；首次住院诊断日期由 Field 41280 获得。死亡登记作为补充数据源，包括根本死因 Field 40001 和继发/贡献死因 Field 40002。

肺炎定义为 ICD-10 代码 J12–J18，结核定义为 ICD-10 代码 A15–A19。泌尿系感染的主定义采用 ICD-10 代码 N39.0；宽定义敏感性分析进一步纳入 N10–N12、N30 和 N34。对于使用 UK Biobank First occurrences 字段的分析，本研究采用相应 3 位 ICD-10 首次发生字段；但由于 First occurrences 仅映射到 3 位 ICD-10，N39 字段不能严格等同于 N39.0，因此不将其作为严格 UTI 定义的唯一依据。
```

---

## 8. 参考数据来源

1. UK Biobank Showcase. `Field 41270: Diagnoses - ICD10`.  
   https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=41270

2. UK Biobank Showcase. `Field 41280: Date of first in-patient diagnosis - ICD10`.  
   https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=41280

3. UK Biobank Showcase. `Field 41202: Diagnoses - main ICD10`.  
   https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=41202

4. UK Biobank Showcase. `Field 40001: Underlying primary cause of death: ICD10`.  
   https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=40001

5. UK Biobank Showcase. `Field 40002: Contributory secondary causes of death: ICD10`.  
   https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=40002

6. UK Biobank Showcase. `Category 1712: First occurrences`.  
   https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=1712

7. UK Biobank Showcase. `Category 2000: Hospital inpatient`.  
   https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=2000

8. UK Biobank Showcase. `Category 2006: Record-level access`.  
   https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=2006

9. UK Biobank. `Data providers and dates of data availability`.  
   https://biobank.ndph.ox.ac.uk/ukb/exinfo.cgi?src=Data_providers_and_dates

10. UK Biobank Community. `What is the difference between ICD 9 and ICD 10 data?`  
    https://community.ukbiobank.ac.uk/hc/en-gb/articles/15957344064797-What-is-the-difference-between-ICD-9-and-ICD-10-data

11. UK Biobank Community. `Why are there several fields for one disease?`  
    https://community.ukbiobank.ac.uk/hc/en-gb/articles/15957770621469-Why-are-there-several-fields-for-one-disease

12. WHO ICD-10 Browser, Version 2019.  
    https://icd.who.int/browse10/2019/en

13. Statistics Canada ICD-10 classification page for `N39`.  
    https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=3&CPV=8.14.6.7&CST=01012014&CVD=152297&Function=getVD&MLV=5&TVD=152294&adm=0&dis=0

---

## 9. 最终推荐

若论文中只需要一个清晰、可复现、审稿人容易接受的定义，建议使用：

```text
肺炎：J12–J18
结核：A15–A19
泌尿系感染主定义：N39.0
泌尿系感染宽定义敏感性分析：N39.0 + N10–N12 + N30 + N34
主数据源：UKB Field 41270
日期来源：UKB Field 41280
死亡补充：Field 40001 + Field 40002
必要时：使用 First occurrences，但注意其为 3 位 ICD-10 映射，不能将 N39 直接等同于 N39.0
```

---
