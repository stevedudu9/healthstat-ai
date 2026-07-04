# HealthStat AI Interview Practice Guide

Use this guide to practice explaining the project in interviews, portfolio reviews, or presentations.

## 30-Second Pitch

HealthStat AI is a healthcare analytics platform that adapts to multiple healthcare datasets. Instead of building one model for one disease, it detects the dataset structure, identifies the target column, performs exploratory analysis, trains an in-browser logistic regression model, reports validation metrics, ranks risk factors, and generates an analytical report. The project demonstrates healthcare analytics, statistical modeling, explainable AI, and responsible communication of limitations.

## 2-Minute Explanation

HealthStat AI was built to show how healthcare prediction software can be designed more flexibly. Many portfolio projects use only one dataset, such as heart disease or diabetes. I designed HealthStat AI to support several dataset types, including heart disease, diabetes, breast cancer, and stroke.

The app reads the dataset columns and compares them with clinical keyword patterns. Based on those patterns, it detects the likely healthcare context. It then identifies the target column, separates numeric and categorical features, performs basic data quality checks, and creates exploratory charts.

For modeling, the app trains a lightweight logistic regression model in the browser. It reports validation accuracy, precision, recall, F1 score, and ROC-AUC where available. It also includes a risk simulator and explainability section that shows which variables influence the model score.

Because this is healthcare-related, I added a visible disclaimer explaining that it is for research and educational use only, not diagnosis or treatment. The demo datasets are small, so the results are useful for demonstrating the system but not for clinical decision-making.

## Questions and Strong Answers

### Why did you make the app support multiple datasets?

Single-dataset projects are useful, but they can look narrow. I wanted to show reusable software design. By supporting multiple healthcare datasets, the app becomes a general healthcare analytics platform rather than just one disease classifier.

### How does the app detect the dataset type?

It looks at column names and matches them against clinical keyword patterns. For example, glucose and insulin suggest diabetes, cholesterol and chest pain suggest heart disease, tumor radius and texture suggest breast cancer, and hypertension or smoking status suggest stroke.

### How does the app detect the target column?

It looks for common outcome names such as target, Outcome, diagnosis, stroke, or class. It also checks whether the column has a small number of unique values, because classification targets are often binary or categorical.

### Why did you use logistic regression?

Logistic regression is interpretable, lightweight, and appropriate for binary classification. It produces probabilities and makes it easier to explain how features contribute to the prediction compared with more complex black-box models.

### What validation metrics did you include?

The app reports accuracy, precision, recall, F1 score, and ROC-AUC where available. These metrics help evaluate different aspects of model performance, especially when false positives and false negatives have different meanings.

### Why is accuracy not enough?

Accuracy can be misleading when classes are imbalanced. For example, if only 10% of patients have a disease, a model could predict "no disease" for everyone and still be 90% accurate. That is why precision, recall, F1 score, and ROC-AUC are also important.

### What does ROC-AUC mean?

ROC-AUC measures how well the model ranks positive cases above negative cases across different thresholds. A higher ROC-AUC means the model is better at separating the two classes.

### How did you handle explainability?

The app ranks risk factors based on their observed relationship with the outcome and model contribution. The simulator also explains which variables raise or lower the model score.

### Is this clinically accurate?

No. It is a portfolio prototype for educational and analytical purposes. The built-in demo datasets are small, and the model has not undergone clinical validation. Real deployment would require larger datasets, cross-validation, calibration, external validation, privacy review, and clinical expert review.

### What would you improve next?

I would add larger public datasets, k-fold cross-validation, calibration plots, model comparison, fairness checks, and external validation. I would also add a more formal preprocessing pipeline and clinician-reviewed report templates.

## Technical Talking Points

- Static browser application
- No backend required
- CSV upload and pasted CSV support
- Automatic schema detection
- Target-column inference
- Exploratory data analysis
- Logistic regression
- Stratified holdout validation
- Accuracy, precision, recall, F1, and ROC-AUC
- Explainable feature ranking
- Report generation
- Responsible healthcare disclaimer

## Interview Questions to Practice

1. What problem does this project solve?
2. Why is multi-dataset support more impressive than one dataset?
3. How does target detection work?
4. Why did you choose logistic regression?
5. What do precision and recall mean in a healthcare context?
6. What are the limitations of your model?
7. How would you make this production-ready?
8. How would you validate this externally?
9. How would you handle missing values in a larger version?
10. How would you explain the model to a non-technical healthcare stakeholder?

## Resume Bullet Ideas

- Built a multi-dataset healthcare analytics dashboard supporting heart disease, diabetes, breast cancer, and stroke workflows.
- Implemented automatic schema detection, target inference, exploratory analysis, in-browser logistic regression, and explainable risk-factor ranking.
- Added validation metrics including accuracy, precision, recall, F1 score, and ROC-AUC, with clear healthcare-use limitations and disclaimer.
