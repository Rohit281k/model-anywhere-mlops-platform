import os
import pandas as pd
try:
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset
except Exception:
    Report = None
os.makedirs('reports', exist_ok=True)
ref = pd.read_csv('data/processed/train.csv')
cur = pd.read_csv('data/processed/test.csv')
if Report:
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html('reports/evidently_report.html')
else:
    open('reports/evidently_report.html','w').write('<h1>Evidently placeholder</h1>')
print('saved reports/evidently_report.html')
