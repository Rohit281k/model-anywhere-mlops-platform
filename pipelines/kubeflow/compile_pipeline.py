from kfp import compiler
from pipeline import pipeline
compiler.Compiler().compile(pipeline_func=pipeline, package_path='pipelines/kubeflow/model_anywhere_pipeline.yaml')
print('compiled pipeline')
