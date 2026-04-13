from flask import Flask, render_template
import subprocess
import re

app = Flask(__name__)

def get_logs():
    logs = []
    
    process = subprocess.Popen(
        ["journalctl", "-n", "20"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        logs.append(line.strip())

    return logs

def detect(line):
    keywords = ["failed password", "authentication failure", "invalid user"]
    return any(k in line.lower() for k in keywords)

@app.route("/")
def home():
    logs = get_logs()

    formatted = []
    for l in logs:
        formatted.append({
            "log": l,
            "alert": detect(l)
        })

    return render_template("index.html", logs=formatted)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
