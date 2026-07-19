# HealthStat AI Project Summary

## What This Project Is

HealthStat AI is a healthcare risk prediction and statistical analytics portfolio project.

The project is designed as a general healthcare analytics platform instead of a single-purpose prediction app. It can work with multiple healthcare datasets, automatically detect the dataset structure, identify the likely target column, run exploratory analysis, train a lightweight prediction model, and generate a report with validation metrics.

Supported healthcare workflows include:

- Heart Disease Prediction
- Diabetes Risk Prediction
- Breast Cancer Classification
- Stroke Risk Prediction

The project is intended for educational, analytical, and portfolio use only. It is not a medical device and should not be used for diagnosis or treatment decisions.

## Main Features

- Multi-dataset healthcare workflow detection
- Automatic target-column detection
- CSV upload support in the static app
- CSV, Excel, and JSON upload support in the Streamlit app
- Demo healthcare datasets
- Exploratory data analysis
- Logistic regression model training
- Validation metrics including accuracy, precision, recall, F1 score, and ROC-AUC where available
- Explainable feature/risk-factor ranking
- Patient risk simulator
- Generated report output
- Downloadable Markdown report
- Downloadable dataset CSV
- Downloadable JSON analysis summary
- Visible research and educational-use disclaimer
- Mobile-friendly Streamlit layout

## Published Links

GitHub repository:

https://github.com/stevedudu9/healthstat-ai

Streamlit live app:

https://healthstat-ai.streamlit.app/

GitHub Pages static version:

https://stevedudu9.github.io/healthstat-ai/

## What Was Done In This Chat

During this chat, the project was expanded from a basic healthcare prediction idea into a more complete portfolio-ready analytics platform.

The main work completed was:

- Built the multi-dataset HealthStat AI web app.
- Added support for heart disease, diabetes, breast cancer, and stroke workflows.
- Added automatic dataset and target-column detection.
- Added model validation outputs.
- Added risk simulation and explainable feature ranking.
- Added generated reports and downloadable outputs.
- Added the visible healthcare disclaimer on the app page.
- Created the README and validation/limitations documentation.
- Created deployment documentation.
- Created a demo video script.
- Created a technical blog post draft.
- Created an interview practice guide.
- Created a Streamlit Community Cloud version of the app.
- Added support for CSV, Excel, and JSON uploads in Streamlit.
- Added sample upload test files:
  - `outputs/sample-heart-upload.csv`
  - `outputs/sample-heart-upload.json`
- Created and published the GitHub repository.
- Deployed the static version to GitHub Pages.
- Deployed the Streamlit version to Streamlit Community Cloud.
- Verified that the Streamlit app loads, wakes from sleep, shows the disclaimer, detects the demo dataset, generates validation metrics, opens the report tab, downloads the Markdown report, and remains readable on a mobile viewport.

## Validation Notes

The app includes a lightweight logistic regression model and reports validation metrics such as accuracy, precision, recall, F1 score, and ROC-AUC where available.

The demo datasets are intentionally small, so high validation scores should not be interpreted as proof of real-world medical performance. A production-grade healthcare model would require larger public datasets, cross-validation, calibration analysis, external validation, bias checks, and clinical expert review.

## Latest Published State

The latest pushed GitHub commit mentioned in this chat was:

`d916c91 Add Streamlit upload test files`

That commit added sample upload files and updated the Streamlit deployment checklist.
