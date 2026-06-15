import os, json
import pandas as pd

path = 'data/processed/train.csv'
df = pd.read_csv(path)
required = ['feature_1','feature_2','feature_3','feature_4','label']
checks = {
    'required_columns_present': all(c in df.columns for c in required),
    'no_nulls': not df[required].isna().any().any(),
    'label_exists': 'label' in df.columns,
    'row_count_positive': len(df) > 0
}
report = {'success': all(checks.values()), 'checks': checks, 'rows': int(len(df))}
os.makedirs('reports', exist_ok=True)
with open('reports/data_validation.json','w') as f: json.dump(report,f,indent=2)
if not report['success']: raise ValueError(report)
print(json.dumps(report, indent=2))
