def detect_anomaly(amount, frequency):
    if amount > 5000 and frequency > 8:
        return True
    return False
