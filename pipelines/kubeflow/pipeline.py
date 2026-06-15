from kfp import dsl

@dsl.component(base_image='python:3.11')
def validate():
    import subprocess
    subprocess.run(['python','src/validation/validate_data.py'], check=True)

@dsl.component(base_image='python:3.11')
def train():
    import subprocess
    subprocess.run(['python','src/training/train.py'], check=True)

@dsl.component(base_image='python:3.11')
def monitor():
    import subprocess
    subprocess.run(['python','src/monitoring/evidently_monitor.py'], check=True)
    subprocess.run(['python','src/monitoring/nannyml_alert.py'], check=True)

@dsl.pipeline(name='model-anywhere-mlops-pipeline')
def pipeline():
    v = validate()
    t = train().after(v)
    monitor().after(t)
