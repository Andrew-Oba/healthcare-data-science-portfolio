# Healthcare Data Science Portfolio — Progress Tracker

Last updated: 2026-07-12

**How to use this file:** Update the status and notes after every session, right before you stop. When resuming a project — with me or on your own — read this file first; it's the source of truth, not chat history.

Status key: ⬜ Not started · 🟡 In progress · ✅ Complete

---

## Project 1 — Heart Disease Risk Factor Analysis (Weeks 1–2)
**Domain:** Clinical Medicine | **Dataset:** `heart_cleveland_upload.csv` (297 patients, 14 features)

### Sunday 1 (ADS/Python track)
| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Data audit: `df.info()`, `df.describe()`, `df.isnull().sum()` + markdown audit summary | ✅ | Flagged chol outlier (564 mg/dl), BP range 94–200 |
| 2 | Map numeric codes → clinical labels; median-impute missing rows | ✅ | 0 nulls found (dataset pre-cleaned to 297 rows vs. plan's 303) — imputation correctly skipped, documented in notebook |
| 3 | 2×2 histograms (age, chol, trestbps, thalach) with clinical reference lines | ✅ | Saved: `figures/01_univariate_histograms.png` |
| 4 | Grouped box plots, disease vs. no-disease | ✅ | 5 variables, saved: `figures/02_bivariate_boxplots.png` |

### Sunday 2 (ADS/Python track)
| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Pearson correlation heatmap + cholesterol treatment-effect write-up | ✅ | Saved: `figures/03_correlation_heatmap.png`. Top correlates: `ca` (0.46), `oldpeak` (0.42), `thalach` (-0.42) |
| 2 | Prevalence by age decade × sex — summary table | ✅ | Overall prevalence 46.1%; male > female at every decade 40s+ |
| 3 | 200-word clinical narrative (top 3 risk factors + 1 counter-intuitive finding, research-abstract style) | ✅ | Material ready: ca/oldpeak/thalach as top 3; chol/BP weak correlation as counter-intuitive finding |
| 4 | GitHub push with clean README | ✅ | Should reference both Python analysis and Power BI dashboard |

### Power BI stretch goal
| Task | Status | Notes |
|---|---|---|
| Card visual: overall disease prevalence | ✅ | Use cleaned CSV; prevalence = 46.1% |
| Bar chart: risk factor prevalence | ✅ | |

**⚠️ Open note:** Project 1's tools list includes seaborn, but the plan document states seaborn isn't introduced in the ADS track until Weeks 5–6. Notebook already uses `sns.boxplot`/`sns.heatmap` in Step 4 (Weeks 1–2). Decide whether to mention as "used ahead of schedule" in README, or leave as-is.

**Next action:** Power BI Card + bar chart → then Task 3 (narrative) → then Task 4 (GitHub push).

---

## Project 2 — Retail Store Sales Performance Dashboard (Weeks 3–4)
**Status:** ⬜ Not started

## Project 3 — US Chronic Disease Burden Explorer (Weeks 5–6)
**Status:** ⬜ Not started

## Project 4 — Hospital Readmission Risk Analysis with SQL (Weeks 7–8)
**Status:** ⬜ Not started

## Project 5 — Opioid Prescribing and Overdose Mortality Analysis (Weeks 9–10)
**Status:** ⬜ Not started

## Weeks 11–16 — Open Project Sundays
**Status:** ⬜ Not started (bonus DataCamp projects / BI polish / Project 6–9 prep)

## Project 6 — Customer LTV Regression & RFM Segmentation (Weeks 17–18)
**Status:** ⬜ Not started

## Project 7 — Diabetes 30-Day Readmission Prediction Model (Weeks 19–20)
**Status:** ⬜ Not started

## Project 8 — NHANES Population Diabetes Screening Classifier (Weeks 21–22)
**Status:** ⬜ Not started

## Project 9 — CAPSTONE: ICU Length-of-Stay Prediction on MIMIC-IV (Weeks 23–24)
**Status:** ⬜ Not started
**Reminder:** Register at physionet.org + complete CITI training by Saturday of Week 20.

---

## Final Portfolio Step
⬜ Root `README.md` (300 words): background, skills table (Python/pandas/SQL Server/scikit-learn/PySpark/Power BI/Tableau), target roles, links to DataCamp profile + LinkedIn. Pin repo on GitHub profile.
