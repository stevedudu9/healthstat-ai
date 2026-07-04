# HealthStat AI

HealthStat AI is a healthcare analytics portfolio prototype that adapts to multiple healthcare datasets instead of being limited to one disease prediction task.

The app can inspect an uploaded or demo dataset, detect the likely healthcare context, identify the target column, generate exploratory analytics, train a lightweight prediction model, display explainable risk factors, and produce a simple clinical-style report.

## Supported Demo Workflows

- Heart Disease Prediction
- Diabetes Risk Prediction
- Breast Cancer Classification
- Stroke Risk Prediction

## Features

- CSV upload and pasted CSV analysis
- Streamlit upload support for CSV, Excel, and JSON files
- Automatic healthcare dataset detection
- Automatic target-column detection
- Dataset preview and data quality summary
- Exploratory data analysis charts
- In-browser logistic regression model
- Validation metrics including accuracy, precision, recall, F1 score, and ROC-AUC where available
- Patient risk simulator
- Explainable risk-factor ranking
- Downloadable report output

## How to Run

Open the app directly in a browser:

```text
outputs/healthstat-ai-multidataset.html
```

No backend server or installation is required for the prototype.

For deployment, the project also includes:

- `streamlit_app.py`
- `requirements.txt`
- `outputs/index.html`
- `netlify.toml`
- `vercel.json`
- `outputs/deployment-guide.md`

## Streamlit Community Cloud Deployment

Use these settings in Streamlit Community Cloud:

```text
Repository: stevedudu9/healthstat-ai
Branch: main
Main file path: streamlit_app.py
```

The Streamlit version supports CSV, Excel, and JSON uploads, report generation, report downloads, dataset downloads, and analysis summary JSON downloads.

After deployment, use `outputs/streamlit-deployment-checklist.md` to verify the live app.

## Portfolio Materials

The following materials are included to help present, deploy, and discuss the project:

- `outputs/deployment-guide.md`
- `outputs/streamlit-deployment-checklist.md`
- `outputs/demo-video-script.md`
- `outputs/technical-blog-post.md`
- `outputs/interview-practice-guide.md`

## Validation and Limitations

HealthStat AI includes a lightweight in-browser logistic regression model that trains on the selected dataset and reports validation accuracy, precision, recall, F1 score, and ROC-AUC where available.

The app was tested across four healthcare demo datasets:

- Heart Disease Prediction
- Diabetes Risk Prediction
- Breast Cancer Classification
- Stroke Risk Prediction

Across these datasets, target columns were detected correctly, the risk simulator executed successfully, and generated reports included model validation outputs without broken, missing, or undefined results.

HealthStat AI is intended as a healthcare analytics portfolio prototype, not a clinical diagnostic tool. The built-in demo datasets are small, so high validation scores should not be interpreted as proof of real-world medical accuracy. Future versions should use larger public datasets, cross-validation, calibration analysis, external validation, and clinical expert review.

## Future Improvements

- Add larger public healthcare datasets
- Add k-fold cross-validation
- Add calibration plots and threshold tuning
- Add external validation datasets
- Add model comparison across logistic regression, random forest, and gradient boosting
- Add clinical expert review notes and bias checks
