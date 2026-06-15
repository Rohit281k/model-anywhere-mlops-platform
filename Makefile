.PHONY: data validate train monitor retrain serve docker helm

data:
	python src/data/make_dataset.py

validate:
	python src/validation/validate_data.py

train:
	python src/training/train.py

monitor:
	python src/monitoring/evidently_monitor.py
	python src/monitoring/nannyml_alert.py

retrain:
	python src/retraining/check_alert_and_retrain.py

monitor-and-retrain:
	python src/monitoring/evidently_monitor.py
	python src/monitoring/nannyml_alert.py
	python src/retraining/check_alert_and_retrain.py

serve:
	bentoml serve serving/bentoml_service.py:svc --reload --port 3000

docker:
	docker build -t rohit1k/model-anywhere-mlops:latest .

helm:
	helm upgrade --install model-anywhere charts/model-anywhere -n mlops --create-namespace
