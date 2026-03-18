# Intelligent Real-Time Fraud Detection System

## 🚀 Overview
AI-powered system to detect fraudulent transactions using machine learning and anomaly detection.

## 🔥 Features
- Fraud prediction using Random Forest
- Anomaly detection logic
- Real-time API using Flask
- High-risk transaction alerts

## 🛠 Tech Stack
Python, Flask, Scikit-learn, Pandas

## ▶️ Run
pip install -r requirements.txt
python app.py

## 📩 API
POST /predict

## Sample Input
{
  "amount": 7000,
  "location": "Chennai",
  "frequency": 12
}

## Sample Output
{
  "fraud": 1,
  "fraud_probability": 0.91,
  "anomaly_detected": true
}
