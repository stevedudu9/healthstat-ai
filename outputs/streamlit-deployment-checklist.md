# Streamlit Community Cloud Deployment Checklist

## App Settings

- Repository: `stevedudu9/healthstat-ai`
- Branch: `main`
- Main file path: `streamlit_app.py`
- Python dependencies: `requirements.txt`

## Verification Checklist

After deployment, verify:

- Live URL loads.
- CSV upload works.
- Excel upload works.
- JSON upload works.
- Demo datasets load.
- Model metrics render.
- Patient risk simulator runs.
- Markdown report generates.
- Report download works.
- Dataset CSV download works.
- Analysis summary JSON download works.
- Mobile layout is readable.

## Test File Formats

You can test uploads by exporting one demo dataset to CSV, Excel, or JSON from any spreadsheet/data tool. The app accepts:

- `.csv`
- `.xlsx`
- `.xls`
- `.json`

## Important Note

The application is for research and educational use only. It is not a medical device and must not be used for diagnosis or treatment decisions.
