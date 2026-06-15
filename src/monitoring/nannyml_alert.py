import os, json, yaml
import pandas as pd
from datetime import datetime

with open('params.yaml') as f: params = yaml.safe_load(f)
th = params['monitoring']['drift_threshold']
ref = pd.read_csv('data/processed/train.csv')
cur = pd.read_csv('data/processed/test.csv')
ref_dist = ref['label'].value_counts(normalize=True).to_dict()
cur_dist = cur['label'].value_counts(normalize=True).to_dict()
labels = sorted(set(ref_dist) | set(cur_dist))
drift_score = sum(abs(ref_dist.get(x,0)-cur_dist.get(x,0)) for x in labels)
alert = {
    'timestamp': datetime.utcnow().isoformat(),
    'tool': 'nannyml-style-monitor',
    'model_name': params['model']['registered_name'],
    'drift_score': round(float(drift_score),4),
    'drift_threshold': th,
    'alert_triggered': bool(drift_score > th),
    'recommended_action': 'trigger_retraining' if drift_score > th else 'no_action',
    'reference_distribution': ref_dist,
    'current_distribution': cur_dist
}
os.makedirs('reports', exist_ok=True)
with open('reports/nannyml_alert.json','w') as f: json.dump(alert,f,indent=2)
print(json.dumps(alert, indent=2))
