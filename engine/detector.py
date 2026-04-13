import re

def extract_ip(line):
    match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
    return match.group() if match else None

def detect_attack(line):
    keywords = ["failed password", "invalid user", "authentication failure"]
    return any(k in line.lower() for k in keywords)
