import os, json, yaml, joblib
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score, f1_score
from src.model_plugin.custom_model import CustomModel

with open('params.yaml') as f: params = yaml.safe_load(f)
train = pd.read_csv('data/processed/train.csv')
test = pd.read_csv('data/processed/test.csv')
features = [c for c in train.columns if c != 'label']
X_train, y_train = train[features], train['label']
X_test, y_test = test[features], test['label']

model = CustomModel(random_state=params['model']['random_state'])
mlflow.set_experiment(params['project']['name'])
with mlflow.start_run():
    model.train(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average='weighted')
    mlflow.log_param('model_type', params['model']['type'])
    mlflow.log_metric('accuracy', acc)
    mlflow.log_metric('weighted_f1', f1)
    mlflow.sklearn.log_model(model.model, 'model', registered_model_name=params['model']['registered_name'])

os.makedirs('models', exist_ok=True)
os.makedirs('reports', exist_ok=True)
joblib.dump({'model': model, 'features': features}, 'models/model.joblib')
with open('reports/metrics.json','w') as f: json.dump({'accuracy':acc,'weighted_f1':f1}, f, indent=2)
print(json.dumps({'accuracy':acc,'weighted_f1':f1}, indent=2))
