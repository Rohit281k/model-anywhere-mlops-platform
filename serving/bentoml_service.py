import bentoml
from pydantic import BaseModel
from typing import Dict, Any
import pandas as pd
import joblib

class PredictRequest(BaseModel):
    features: Dict[str, Any]

svc = bentoml.Service('model_anywhere_service')
artifact = joblib.load('models/model.joblib')
model = artifact['model']
features = artifact['features']

@svc.api(input=bentoml.io.JSON(pydantic_model=PredictRequest), output=bentoml.io.JSON())
def predict(request: PredictRequest):
    df = pd.DataFrame([request.features])[features]
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0].max()
    return {'prediction': int(pred), 'confidence': float(round(proba, 4))}

@svc.api(input=bentoml.io.JSON(), output=bentoml.io.JSON())
def health(_: dict):
    return {'status': 'ok'}
