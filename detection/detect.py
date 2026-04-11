import pandas as pd
from sklearn.ensemble import IsolationForest
def detect_anomalies():
    data = pd.read_csv("data/logs.csv")

    model = IsolationForest(contamination=0.3)
    model.fit(data[['failed_logins', 'port_scan']])

    data['attack'] = model.predict(data[['failed_logins', 'port_scan']])

    attackers = data[data['attack'] == -1]

    return attackers['ip'].tolist()

if __name__ == "__main__":
    print(detect_anomalies())
