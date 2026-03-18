from flask import Flask, request, jsonify
from model import predict_fraud
from anomaly import detect_anomaly

app = Flask(__name__)

@app.route('/')
def home():
    return "Fraud Detection System Running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    amount = data['amount']
    location = data['location']
    frequency = data['frequency']

    fraud, probability = predict_fraud(amount, frequency)
    anomaly = detect_anomaly(amount, frequency)

    return jsonify({
        "fraud": int(fraud),
        "fraud_probability": round(probability, 2),
        "anomaly_detected": anomaly
    })

if __name__ == '__main__':
    app.run(debug=True)
