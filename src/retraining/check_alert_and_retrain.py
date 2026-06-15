import json, subprocess
with open('reports/nannyml_alert.json') as f: alert = json.load(f)
if alert.get('alert_triggered') and alert.get('recommended_action') == 'trigger_retraining':
    print('Alert triggered. Starting retraining through DVC pipeline.')
    subprocess.run(['dvc','repro'], check=True)
else:
    print('No retraining required.')
