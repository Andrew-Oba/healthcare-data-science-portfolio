# Data Dictionary — Heart Disease Cleveland UCI

**Source:** [Kaggle — cherngs/heart-disease-cleveland-uci](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)
**Original source:** UCI Machine Learning Repository — Cleveland Clinic Foundation
**Records:** 297 patients
**Missing values:** None (confirmed via `df.isnull().sum()`)

## Columns

| Column | Description | Values |
|---|---|---|
| `age` | Age in years | Continuous |
| `sex` | Sex | 0 = female, 1 = male |
| `cp` | Chest pain type | 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic |
| `trestbps` | Resting blood pressure (mm Hg) on admission to hospital | Continuous |
| `chol` | Serum cholesterol (mg/dl) | Continuous |
| `fbs` | Fasting blood sugar > 120 mg/dl | 0 = false, 1 = true |
| `restecg` | Resting electrocardiographic results | 0 = normal, 1 = ST-T wave abnormality, 2 = probable/definite left ventricular hypertrophy (Estes' criteria) |
| `thalach` | Maximum heart rate achieved | Continuous |
| `exang` | Exercise-induced angina | 0 = no, 1 = yes |
| `oldpeak` | ST depression induced by exercise relative to rest | Continuous |
| `slope` | Slope of the peak exercise ST segment | 0 = upsloping, 1 = flat, 2 = downsloping |
| `ca` | Number of major vessels colored by fluoroscopy | 0–3 |
| `thal` | Thalassemia (blood flow) result | 0 = normal, 1 = fixed defect, 2 = reversible defect |
| `condition` | Target variable — presence of heart disease | 0 = no disease, 1 = disease present |

## Notes

- This version of the dataset uses 0-indexed categorical codes (e.g. `cp` ranges 0–3, `slope` ranges 0–2), which differs slightly from some other published mirrors of the original UCI dataset that use 1-indexed codes. Always confirm indexing against `df.describe()` min/max before mapping labels.
- `condition` is already collapsed to binary (0/1) in this version, unlike the original UCI `num` field which ranges 0–4 (severity levels).
