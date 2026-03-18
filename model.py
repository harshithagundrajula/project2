import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = pd.DataFrame({
    'amount': [100, 5000, 200, 7000, 150, 8000, 300, 9000],
    'frequency': [1, 10, 2, 12, 1, 15, 2, 18],
    'fraud': [0, 1, 0, 1, 0, 1, 0, 1]
})

X = data[['amount', 'frequency']]
y = data['fraud']

model = RandomForestClassifier()
model.fit(X, y)

def predict_fraud(amount, frequency):
    features = [[amount, frequency]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return prediction, probability
