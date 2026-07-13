# Heart Disease Risk Factor Analysis

Clinical EDA on the UCI/Cleveland Clinic heart disease dataset, examining which clinical and diagnostic variables most strongly associate with coronary artery disease (CAD) presence, and whether patterns differ by age and sex.

## Dataset

**Source:** UCI Heart Disease Dataset (Cleveland) — [kaggle.com/datasets/cherngs/heart-disease-cleveland-uci](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

Consists of 297 anonymized patients referred for cardiac catheterization, 14 clinical attributes including age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting ECG findings, maximum heart rate achieved, exercise-induced angina, ST-segment depression (`oldpeak`), number of major vessels visualized by fluoroscopy (`ca`), and thallium stress test result (`thal`). Target variable: disease presence/absence (`condition`).

**Note:** this is a clinical referral cohort, not a general-population sample — patients were already undergoing catheterization workup. Findings describe prevalence and correlation *within this cohort*, not population-level epidemiology.

## Methods

- Data audit (`df.info()`, `.describe()`, `.isnull()`), numeric-to-clinical-label mapping
- Univariate EDA: histograms with clinical reference thresholds (age > 50, cholesterol > 240 mg/dl, resting BP > 130 mmHg)
- Bivariate EDA: grouped box plots (disease vs. no-disease) and a Pearson/point-biserial correlation matrix
- Prevalence table by age decade × sex
- Power BI dashboard (`dashboards/heart_disease_dashboard.pbix`): overall disease prevalence (Card visual) and a clustered column chart comparing prevalence of age >50, male sex, elevated cholesterol, and elevated fasting blood sugar across the cohort

## Key Findings

- **Overall disease prevalence: 46.1%** across the cohort, rising from near 0% in patients under 40 to 74.5% (male) and 41.2% (female) in the 60s age decade.
- **Top 3 correlates of disease presence:** number of major vessels visualized by fluoroscopy (`ca`, r=0.46), ST-segment depression on exercise testing (`oldpeak`, r=0.42), and maximum heart rate achieved (`thalach`, r=-0.42). All three are direct or near-direct measurements of existing disease burden rather than upstream, modifiable risk factors.
- **Counter-intuitive finding:** serum cholesterol — elevated in 51% of the cohort and heavily emphasized in general cardiac risk counseling — showed negligible correlation with disease presence (r=0.08), likely reflecting a treatment effect in cross-sectional data (values reflect already-managed levels, not untreated levels at disease onset).
- Male sex (67%) and age >50 (69%) were the most prevalent characteristics in the cohort; of the two, only age showed a meaningful (if modest) correlation with disease presence.

Full clinical narrative: `notebooks/01_load_and_inspect.ipynb`, Step 5.

## Limitation

This dataset reflects a clinical referral population undergoing catheterization, not a random population sample — prevalence and correlation estimates here should not be generalized to broader population-level cardiac risk without adjustment for referral bias. Additionally, cholesterol and blood pressure values are cross-sectional single measurements, likely taken after treatment had already begun for many patients, which may understate their true association with disease onset.

## Contents

```
01-heart-disease-eda/
├── data/raw/heart_cleveland_upload.csv
├── figures/
│   ├── 01_univariate_histograms.png
│   ├── 02_bivariate_boxplots.png
│   └── 03_correlation_heatmap.png
├── dashboards/heart_disease_dashboard.pbix
└── notebooks/01_load_and_inspect.ipynb
```
