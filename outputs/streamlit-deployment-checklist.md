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

You can test uploads with the included sample files:

- `outputs/sample-heart-upload.csv`
- `outputs/sample-heart-upload.json`

For Excel, open `outputs/sample-heart-upload.csv` in Excel or Google Sheets and save it as `.xlsx`, then upload that file.

The app accepts:

- `.csv`
- `.xlsx`
- `.xls`
- `.json`

## Important Note

The application is for research and educational use only. It is not a medical device and must not be used for diagnosis or treatment decisions.
