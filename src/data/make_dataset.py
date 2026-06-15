import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

data = load_iris(as_frame=True)
df = data.frame.rename(columns={
    'sepal length (cm)': 'feature_1',
    'sepal width (cm)': 'feature_2',
    'petal length (cm)': 'feature_3',
    'petal width (cm)': 'feature_4',
    'target': 'label'
})
df.to_csv('data/raw/dataset.csv', index=False)
train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])
train.to_csv('data/processed/train.csv', index=False)
test.to_csv('data/processed/test.csv', index=False)
print('dataset generated')
