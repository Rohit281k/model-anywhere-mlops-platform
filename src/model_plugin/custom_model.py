from sklearn.ensemble import RandomForestClassifier

class CustomModel:
    """Replace this class with any model. Keep train/predict/predict_proba methods."""
    def __init__(self, random_state=42):
        self.model = RandomForestClassifier(n_estimators=100, random_state=random_state)

    def train(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
