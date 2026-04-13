import subprocess
import re

blocked_ips = set()

def detect_attack(line):
    if "Failed password" in line:
        return True
    return False

def extract_ip(line):
    match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    if match:
        return match.group()
    return None

def block_ip(ip):
    if ip not in blocked_ips:
        blocked_ips.add(ip)
        print(f"🛡️ BLOCKING IP: {ip}")

def monitor_logs():
    process = subprocess.Popen(
        ["journalctl", "-f"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        print("Log:", line.strip())

        if detect_attack(line):
            ip = extract_ip(line)
            if ip:
                print(f"🚨 ATTACK DETECTED from IP: {ip}")
                block_ip(ip)

if __name__ == "__main__":
    monitor_logs()
