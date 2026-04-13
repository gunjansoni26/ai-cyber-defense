import subprocess
from engine.detector import detect_attack, extract_ip
from engine.response import block_ip

logs_cache = []

def stream_logs():
    process = subprocess.Popen(
        ["journalctl", "-f"],
        stdout=subprocess.PIPE,
        text=True
    )

    while True:
        line = process.stdout.readline().strip()

        if not line:
            continue

        logs_cache.append(line)
        if len(logs_cache) > 50:
            logs_cache.pop(0)

        print("LOG:", line)

        if detect_attack(line):
            ip = extract_ip(line)
            if ip:
                print(f"🚨 ATTACK DETECTED: {ip}")
                block_ip(ip)
