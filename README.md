# Seasonal Agriculture Performance Analysis

## Project
A data analytics project that studies how agricultural performance changes across Kharif, Rabi and Zaid seasons.

## Deliverables
- `Seasonal_Agriculture_Performance_Analysis.ipynb` — complete analysis notebook
- `app.py` — optional Streamlit interactive dashboard
- `seasonal_agriculture_performance_dataset.csv` — project dataset
- `requirements.txt` — Python dependencies
- `PROJECT_REPORT.md` — project report
- `VOIS_Major_Project_Submission.pptx` — presentation based on the supplied VOIS template

## How to run
```bash
pip install -r requirements.txt
jupyter notebook Seasonal_Agriculture_Performance_Analysis.ipynb
```

Optional dashboard:
```bash
streamlit run app.py
```

## Workflow
Data understanding → quality check → cleaning → descriptive analysis → seasonal comparison → crop-season analysis → correlation analysis → ANOVA → recommendations.

## Important
The dataset contains missing values in Rainfall, Soil Moisture and Yield. The notebook uses median imputation for these numeric fields and reports the data-quality check before analysis.
