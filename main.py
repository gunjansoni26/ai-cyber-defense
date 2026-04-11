from detection.detect import detect_anomalies
from response.respond import block_ip

def run_system():
    attackers = detect_anomalies()

    print("Detected attackers:", attackers)  # ✅ ADD THIS

    for ip in attackers:
        print(f"Detected attacker: {ip}")
        block_ip(ip)

if __name__ == "__main__":
    run_system()
