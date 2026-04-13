import subprocess
import re
import time

blocked_ips = set()

def extract_ip(line):
    match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    return match.group() if match else None

def detect_attack(line):
    return "Failed password" in line or "authentication failure" in line.lower()

def block_ip(ip):
    if ip not in blocked_ips:
        blocked_ips.add(ip)
        print(f"🛡️ BLOCKED IP: {ip}")

def monitor_logs():
    print("🚀 SOC SYSTEM RUNNING...\n")

    process = subprocess.Popen(
        ["journalctl", "-f"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    while True:
        line = process.stdout.readline()

        if not line:
            time.sleep(0.1)
            continue

        line = line.strip()
        print("LOG:", line)

        if detect_attack(line):
            ip = extract_ip(line)
            if ip:
                print(f"🚨 ATTACK DETECTED: {ip}")
                block_ip(ip)

if __name__ == "__main__":
    monitor_logs()
def simulate_attack(line):
    test_keywords = [
        "Failed password",
        "authentication failure",
        "Invalid user",
        "Failed login"
    ]

    return any(word in line for word in test_keywords)
