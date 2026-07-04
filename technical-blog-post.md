# Building HealthStat AI: A Multi-Dataset Healthcare Analytics Prototype

## Introduction

HealthStat AI is a healthcare analytics portfolio project designed to solve a common limitation in student and portfolio machine learning projects: many projects work on only one dataset.

Instead of building a single heart disease predictor or a single diabetes classifier, HealthStat AI is designed as an adaptive analytics platform. It can work with multiple healthcare datasets, detect the likely disease context, identify the target variable, train a lightweight model, and generate explainable outputs.

The current prototype supports four demo workflows:

- Heart Disease Prediction
- Diabetes Risk Prediction
- Breast Cancer Classification
- Stroke Risk Prediction

The goal is not to create a clinical diagnostic tool. The goal is to demonstrate statistical thinking, reusable machine learning design, responsible validation, and healthcare-focused analytics.

## Dataset Structure Detection

Different healthcare datasets use different column names. For example:

- A heart disease dataset may include `chol`, `cp`, `thalach`, and `target`.
- A diabetes dataset may include `Glucose`, `BMI`, `Insulin`, and `Outcome`.
- A breast cancer dataset may include `mean_radius`, `mean_texture`, and `diagnosis`.
- A stroke dataset may include `hypertension`, `avg_glucose_level`, `smoking_status`, and `stroke`.

HealthStat AI detects the dataset type by comparing uploaded column names with known clinical keyword patterns. This makes the application more flexible than a single-purpose model.

## Target Variable Detection

The target variable is the outcome the model tries to predict. The app looks for likely target names such as:

- `target`
- `Outcome`
- `diagnosis`
- `stroke`
- `class`

It also considers whether a column has a small number of unique values, because classification targets are often binary or categorical.

## Exploratory Data Analysis

Before modeling, HealthStat AI performs basic exploratory analysis:

- Row and column count
- Missing-value detection
- Duplicate-row detection
- Numeric and categorical variable identification
- Outcome distribution
- Feature association with the target

This step is important because model performance can be misleading if the dataset has missing values, duplicated rows, class imbalance, or poorly understood variables.

## Logistic Regression Model

The prototype uses a lightweight logistic regression model implemented in browser-side JavaScript.

Logistic regression is useful for binary classification problems such as:

- Disease vs. no disease
- Diabetes vs. no diabetes
- Malignant vs. benign
- Stroke vs. no stroke

The model estimates a probability between 0 and 1. A higher probability means the patient profile looks more similar to records with a positive outcome in the dataset.

## Model Validation Metrics

HealthStat AI reports several validation metrics:

### Accuracy

Accuracy measures the percentage of correct predictions.

Accuracy is easy to understand, but it can be misleading when classes are imbalanced.

### Precision

Precision answers:

"When the model predicts a positive case, how often is it correct?"

Precision is important when false positives are costly.

### Recall

Recall answers:

"Of all true positive cases, how many did the model detect?"

Recall is important when missing a positive case is costly.

### F1 Score

F1 score combines precision and recall into one metric. It is useful when both false positives and false negatives matter.

### ROC-AUC

ROC-AUC measures how well the model ranks positive cases above negative cases across classification thresholds.

In small datasets, ROC-AUC can be unstable, so it should be interpreted carefully.

## Explainable AI

Healthcare analytics should not behave like a black box. HealthStat AI ranks top risk factors based on observed relationships with the outcome and model contributions.

The risk simulator also explains which variables raise or lower the model score. This helps make predictions easier to discuss and critique.

## Responsible Healthcare Disclaimer

Because this is healthcare-related software, the app includes a visible disclaimer:

HealthStat AI is for research and educational use only. It is not a medical device, should not be used for diagnosis or treatment decisions, and has not undergone clinical validation.

This disclaimer is important because small demo datasets cannot prove real-world medical accuracy.

## Limitations

The current version has important limitations:

- Demo datasets are small.
- Validation metrics are unstable on small samples.
- The model is not externally validated.
- The app does not perform clinical calibration.
- The tool has not been reviewed by medical experts.
- It should not be used for real patient decisions.

## Future Improvements

Future versions should add:

- Larger public healthcare datasets
- K-fold cross-validation
- Calibration plots
- External validation
- Model comparison with random forests and gradient boosting
- Bias and fairness checks
- Clinician-reviewed interpretation templates

## Conclusion

HealthStat AI demonstrates how a healthcare machine learning project can move beyond a single dataset. By adapting to multiple dataset structures, automatically detecting targets, training a validation-aware model, and explaining risk factors, the project becomes a stronger portfolio example of statistical analytics and responsible AI design.
