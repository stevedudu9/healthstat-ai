import json
from io import BytesIO

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


st.set_page_config(
    page_title="HealthStat AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    .disclaimer {
        border: 1px solid #f0c66b;
        border-left: 6px solid #a96f00;
        background: #fff9ea;
        border-radius: 8px;
        padding: 1rem;
        color: #3c2d0d;
        margin: 0.75rem 0 1.25rem;
    }
    .metric-note {
        color: #667085;
        font-size: 0.9rem;
    }
    @media (max-width: 720px) {
        .block-container { padding-left: 0.8rem; padding-right: 0.8rem; }
        h1 { font-size: 1.8rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


DISEASE_PROFILES = [
    {
        "id": "heart",
        "name": "Heart Disease Prediction",
        "target_hints": ["target", "heartdisease", "heart_disease", "disease", "condition", "num"],
        "keywords": ["cholesterol", "chol", "chest", "cp", "thalach", "oldpeak", "angina", "exang", "slope", "ca", "thal", "trestbps", "restecg"],
        "message": "Cardiometabolic and exercise-response variables are prioritized.",
    },
    {
        "id": "diabetes",
        "name": "Diabetes Risk Prediction",
        "target_hints": ["outcome", "diabetes", "diabetic", "class", "target"],
        "keywords": ["glucose", "insulin", "pregnancies", "diabetespedigreefunction", "pedigree", "skinthickness", "bmi", "bloodpressure"],
        "message": "Glucose, BMI, insulin, and metabolic-history variables are emphasized.",
    },
    {
        "id": "breast",
        "name": "Breast Cancer Classification",
        "target_hints": ["diagnosis", "malignant", "benign", "class", "target"],
        "keywords": ["radius", "texture", "perimeter", "area", "smoothness", "compactness", "concavity", "concave", "symmetry", "fractal"],
        "message": "Tumor morphology fields are treated as the main diagnostic signals.",
    },
    {
        "id": "stroke",
        "name": "Stroke Risk Prediction",
        "target_hints": ["stroke", "target", "outcome"],
        "keywords": ["hypertension", "heart_disease", "ever_married", "work_type", "residence_type", "avg_glucose_level", "smoking_status", "bmi"],
        "message": "Vascular, demographic, glucose, and smoking variables are prioritized.",
    },
]


DEMO_DATA = {
    "Heart Disease": pd.DataFrame(
        [
            [63, "M", "typical angina", 145, 233, 1, "normal", 150, "no", 2.3, 1],
            [37, "M", "non-anginal", 130, 250, 0, "st-t abnormality", 187, "no", 3.5, 1],
            [41, "F", "atypical angina", 130, 204, 0, "normal", 172, "no", 1.4, 1],
            [57, "M", "asymptomatic", 140, 192, 0, "normal", 148, "no", 0.4, 0],
            [54, "M", "asymptomatic", 140, 239, 0, "normal", 160, "no", 1.2, 0],
            [64, "M", "asymptomatic", 110, 211, 0, "lv hypertrophy", 144, "yes", 1.8, 0],
            [52, "M", "non-anginal", 172, 199, 1, "normal", 162, "no", 0.5, 1],
            [48, "F", "non-anginal", 130, 275, 0, "normal", 139, "no", 0.2, 1],
            [49, "M", "atypical angina", 130, 266, 0, "normal", 171, "no", 0.6, 1],
            [58, "F", "asymptomatic", 150, 283, 1, "lv hypertrophy", 162, "no", 1.0, 1],
        ],
        columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "target"],
    ),
    "Diabetes": pd.DataFrame(
        [
            [6, 148, 72, 35, 0, 33.6, 0.627, 50, 1],
            [1, 85, 66, 29, 0, 26.6, 0.351, 31, 0],
            [8, 183, 64, 0, 0, 23.3, 0.672, 32, 1],
            [1, 89, 66, 23, 94, 28.1, 0.167, 21, 0],
            [0, 137, 40, 35, 168, 43.1, 2.288, 33, 1],
            [5, 116, 74, 0, 0, 25.6, 0.201, 30, 0],
            [2, 197, 70, 45, 543, 30.5, 0.158, 53, 1],
            [10, 139, 80, 0, 0, 27.1, 1.441, 57, 0],
            [1, 189, 60, 23, 846, 30.1, 0.398, 59, 1],
            [5, 166, 72, 19, 175, 25.8, 0.587, 51, 1],
        ],
        columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"],
    ),
    "Breast Cancer": pd.DataFrame(
        [
            [17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, "M"],
            [20.57, 17.77, 132.9, 1326, 0.0847, 0.0786, 0.0869, "M"],
            [19.69, 21.25, 130, 1203, 0.1096, 0.1599, 0.1974, "M"],
            [12.45, 15.7, 82.57, 477.1, 0.1278, 0.17, 0.1578, "B"],
            [13.71, 20.83, 90.2, 577.9, 0.1189, 0.1645, 0.0937, "B"],
            [13.0, 21.82, 87.5, 519.8, 0.1273, 0.1932, 0.1859, "B"],
            [16.02, 23.24, 102.7, 797.8, 0.0821, 0.0667, 0.0330, "M"],
            [15.78, 17.89, 103.6, 781, 0.0971, 0.1292, 0.0995, "M"],
            [15.85, 23.95, 103.7, 782.7, 0.0840, 0.1002, 0.0994, "M"],
            [13.73, 22.61, 93.6, 578.3, 0.1131, 0.2293, 0.2128, "B"],
        ],
        columns=["mean_radius", "mean_texture", "mean_perimeter", "mean_area", "mean_smoothness", "mean_compactness", "mean_concavity", "diagnosis"],
    ),
    "Stroke": pd.DataFrame(
        [
            ["Male", 67, 0, 1, "Yes", "Private", "Urban", 228.69, 36.6, "formerly smoked", 1],
            ["Female", 61, 0, 0, "Yes", "Self-employed", "Rural", 202.21, 28.1, "never smoked", 1],
            ["Male", 80, 0, 1, "Yes", "Private", "Rural", 105.92, 32.5, "never smoked", 1],
            ["Female", 49, 0, 0, "Yes", "Private", "Urban", 171.23, 34.4, "smokes", 1],
            ["Female", 69, 0, 0, "No", "Private", "Urban", 94.39, 22.8, "never smoked", 0],
            ["Female", 59, 0, 0, "Yes", "Private", "Rural", 76.15, 28.0, "Unknown", 0],
            ["Male", 54, 0, 0, "Yes", "Govt_job", "Urban", 104.51, 27.3, "smokes", 0],
            ["Female", 64, 0, 0, "Yes", "Self-employed", "Urban", 84.45, 30.9, "never smoked", 0],
            ["Male", 43, 0, 0, "Yes", "Private", "Rural", 96.77, 33.8, "never smoked", 0],
            ["Female", 52, 1, 0, "Yes", "Private", "Urban", 233.29, 48.9, "never smoked", 1],
        ],
        columns=["gender", "age", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"],
    ),
}


def normalize_name(value: str) -> str:
    return "".join(ch for ch in str(value).lower() if ch.isalnum())


def detect_disease(columns):
    normalized = [normalize_name(col) for col in columns]
    scored = []
    for profile in DISEASE_PROFILES:
        keyword_hits = sum(any(normalize_name(keyword) in col or col in normalize_name(keyword) for col in normalized) for keyword in profile["keywords"])
        target_hits = sum(any(normalize_name(hint) in col for col in normalized) for hint in profile["target_hints"])
        scored.append((keyword_hits * 2 + target_hits * 1.5, keyword_hits, target_hits, profile))
    score, keyword_hits, target_hits, profile = sorted(scored, key=lambda item: item[0], reverse=True)[0]
    confidence = min(98, round(45 + score * 7))
    return profile, confidence, keyword_hits, target_hits


def detect_target(df: pd.DataFrame, profile):
    candidates = []
    for col in df.columns:
        name = normalize_name(col)
        unique_count = df[col].dropna().astype(str).nunique()
        hint = 10 if any(name == normalize_name(hint) or normalize_name(hint) in name for hint in profile["target_hints"]) else 0
        binary = 4 if unique_count == 2 else 2 if unique_count <= 4 else 0
        end_bonus = 1 if col == df.columns[-1] else 0
        avoid = -5 if name in {"age", "sex", "gender", "bmi"} else 0
        candidates.append((hint + binary + end_bonus + avoid, col))
    return sorted(candidates, reverse=True)[0][1]


def encode_target(series: pd.Series):
    positive = {"1", "yes", "true", "positive", "m", "malignant", "disease", "stroke", "diabetic"}
    negative = {"0", "no", "false", "negative", "b", "benign", "normal", "healthy"}

    def encode(value):
        if pd.isna(value):
            return np.nan
        text = str(value).strip().lower()
        if text in positive:
            return 1
        if text in negative:
            return 0
        number = pd.to_numeric(value, errors="coerce")
        if pd.isna(number):
            return np.nan
        return 1 if number > 0 else 0

    return series.map(encode)


def load_uploaded_file(uploaded_file):
    suffix = uploaded_file.name.lower().split(".")[-1]
    if suffix == "csv":
        return pd.read_csv(uploaded_file)
    if suffix in {"xlsx", "xls"}:
        return pd.read_excel(uploaded_file)
    if suffix == "json":
        data = json.load(uploaded_file)
        if isinstance(data, dict) and "data" in data:
            data = data["data"]
        return pd.DataFrame(data)
    raise ValueError("Unsupported file type. Please upload CSV, Excel, or JSON.")


def train_model(df: pd.DataFrame, target_col: str):
    y = encode_target(df[target_col])
    model_df = df.loc[y.notna()].copy()
    y = y.loc[y.notna()].astype(int)
    X = model_df.drop(columns=[target_col])
    if len(y) < 6 or y.nunique() < 2:
        return None, None, None, "Need at least 6 rows and both outcome classes to train a validation model."

    numeric_cols = X.select_dtypes(include=["number", "bool"]).columns.tolist()
    categorical_cols = [col for col in X.columns if col not in numeric_cols]
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), numeric_cols),
            ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("encoder", OneHotEncoder(handle_unknown="ignore"))]), categorical_cols),
        ]
    )
    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    stratify = y if y.value_counts().min() >= 2 else None
    test_size = 0.3 if len(y) >= 12 else 0.4
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=stratify)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    metrics = {
        "Training rows": len(X_train),
        "Validation rows": len(X_test),
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions, zero_division=0),
        "Recall": recall_score(y_test, predictions, zero_division=0),
        "F1": f1_score(y_test, predictions, zero_division=0),
        "ROC-AUC": roc_auc_score(y_test, probabilities) if y_test.nunique() == 2 else np.nan,
    }
    return model, X, metrics, None


def feature_associations(df: pd.DataFrame, target_col: str):
    y = encode_target(df[target_col])
    rows = []
    for col in df.drop(columns=[target_col]).columns:
        encoded = pd.to_numeric(df[col], errors="coerce")
        if encoded.notna().sum() < 3:
            encoded = df[col].astype(str).astype("category").cat.codes.replace(-1, np.nan)
        valid = encoded.notna() & y.notna()
        if valid.sum() < 3:
            score = 0
        else:
            score = abs(np.corrcoef(encoded[valid], y[valid])[0, 1])
            if np.isnan(score):
                score = 0
        rows.append({"Feature": col, "Association": score})
    return pd.DataFrame(rows).sort_values("Association", ascending=False)


def build_report(profile, confidence, df, target_col, metrics, associations):
    metric_lines = []
    if metrics:
        for key, value in metrics.items():
            if isinstance(value, float):
                metric_lines.append(f"- {key}: {value:.3f}")
            else:
                metric_lines.append(f"- {key}: {value}")
    else:
        metric_lines.append("- Model validation was not available for this dataset.")

    top_features = associations.head(5)["Feature"].tolist() if not associations.empty else []
    return f"""# HealthStat AI Report

## Dataset Detection

- Detected workflow: {profile["name"]}
- Detection confidence: {confidence}%
- Target column: {target_col}
- Rows analyzed: {len(df)}
- Columns analyzed: {len(df.columns)}

## Data Quality

- Missing values: {int(df.isna().sum().sum())}
- Duplicate rows: {int(df.duplicated().sum())}

## Model Validation

{chr(10).join(metric_lines)}

## Top Risk Factors

{chr(10).join(f"- {feature}" for feature in top_features)}

## Interpretation

{profile["message"]}

## Disclaimer

This application is intended for educational and analytical purposes. It is not a medical device, should not be used for diagnosis or treatment decisions, and has not undergone clinical validation.
"""


st.title("HealthStat AI")
st.caption("Adaptive Healthcare Risk Prediction & Statistical Analytics Platform")
st.markdown(
    """
    <div class="disclaimer">
      <strong>Research & Educational Use Only</strong><br>
      This application is intended for educational and analytical purposes. It is not a medical device,
      should not be used for diagnosis or treatment decisions, and has not undergone clinical validation.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Data Source")
    uploaded = st.file_uploader("Upload CSV, Excel, or JSON", type=["csv", "xlsx", "xls", "json"])
    demo_choice = st.selectbox("Or choose a demo dataset", list(DEMO_DATA.keys()))

try:
    if uploaded is not None:
        data = load_uploaded_file(uploaded)
        source = uploaded.name
    else:
        data = DEMO_DATA[demo_choice].copy()
        source = f"{demo_choice} demo"
except Exception as exc:
    st.error(f"Could not load file: {exc}")
    st.stop()

if data.empty:
    st.warning("The dataset is empty.")
    st.stop()

profile, confidence, keyword_hits, target_hits = detect_disease(data.columns)
target_col = detect_target(data, profile)
model, X, metrics, model_error = train_model(data, target_col)
associations = feature_associations(data, target_col)
report = build_report(profile, confidence, data, target_col, metrics, associations)

top = st.container()
with top:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Detected Workflow", profile["name"])
    c2.metric("Confidence", f"{confidence}%")
    c3.metric("Rows", f"{len(data):,}")
    c4.metric("Target", target_col)

tab_overview, tab_data, tab_model, tab_report = st.tabs(["Overview", "Data & EDA", "Model & Risk", "Report & Downloads"])

with tab_overview:
    st.subheader("Adaptive Detection")
    st.write(profile["message"])
    st.write(f"Detected from {keyword_hits} clinical keyword matches and {target_hits} target-name matches.")
    st.plotly_chart(px.bar(associations.head(10), x="Association", y="Feature", orientation="h", title="Top Feature Associations"), use_container_width=True)

with tab_data:
    st.subheader("Dataset Preview")
    st.dataframe(data.head(50), use_container_width=True)
    q1, q2, q3 = st.columns(3)
    q1.metric("Columns", len(data.columns))
    q2.metric("Missing Values", int(data.isna().sum().sum()))
    q3.metric("Duplicate Rows", int(data.duplicated().sum()))
    st.subheader("Outcome Distribution")
    st.plotly_chart(px.histogram(data, x=target_col, title=f"Distribution of {target_col}"), use_container_width=True)
    st.subheader("Variable Summary")
    summary = pd.DataFrame(
        {
            "column": data.columns,
            "dtype": [str(data[col].dtype) for col in data.columns],
            "missing": [int(data[col].isna().sum()) for col in data.columns],
            "unique": [int(data[col].nunique(dropna=True)) for col in data.columns],
        }
    )
    st.dataframe(summary, use_container_width=True)

with tab_model:
    st.subheader("Validation Metrics")
    if model_error:
        st.warning(model_error)
    else:
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Accuracy", f"{metrics['Accuracy']:.2f}")
        m2.metric("Precision", f"{metrics['Precision']:.2f}")
        m3.metric("Recall", f"{metrics['Recall']:.2f}")
        m4.metric("F1", f"{metrics['F1']:.2f}")
        auc_value = metrics["ROC-AUC"]
        m5.metric("ROC-AUC", "N/A" if pd.isna(auc_value) else f"{auc_value:.2f}")

        st.subheader("Patient Risk Simulator")
        values = {}
        cols = st.columns(2)
        selected_features = associations.head(8)["Feature"].tolist()
        for index, feature in enumerate(selected_features):
            with cols[index % 2]:
                if pd.api.types.is_numeric_dtype(data[feature]):
                    series = pd.to_numeric(data[feature], errors="coerce")
                    values[feature] = st.number_input(
                        feature,
                        value=float(series.median()),
                        min_value=float(series.min()),
                        max_value=float(series.max()),
                    )
                else:
                    options = data[feature].dropna().astype(str).unique().tolist()
                    values[feature] = st.selectbox(feature, options or [""])

        if st.button("Calculate Risk"):
            input_row = X.iloc[[0]].copy()
            for feature, value in values.items():
                input_row.loc[input_row.index[0], feature] = value
            probability = model.predict_proba(input_row)[0, 1]
            st.metric("Predicted Probability", f"{probability:.1%}")
            st.caption("This is an educational model output and must not be used for diagnosis or treatment decisions.")

with tab_report:
    st.subheader("Generated Report")
    st.markdown(report)
    st.download_button("Download Markdown Report", report, file_name="healthstat-ai-report.md", mime="text/markdown")
    st.download_button("Download Dataset as CSV", data.to_csv(index=False), file_name="healthstat-ai-data.csv", mime="text/csv")
    summary_json = {
        "source": source,
        "detected_workflow": profile["name"],
        "confidence": confidence,
        "target": target_col,
        "rows": len(data),
        "columns": len(data.columns),
        "metrics": metrics,
        "top_features": associations.head(8).to_dict(orient="records"),
    }
    st.download_button(
        "Download Analysis Summary JSON",
        json.dumps(summary_json, indent=2, default=str),
        file_name="healthstat-ai-summary.json",
        mime="application/json",
    )
