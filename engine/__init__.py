from flask import Flask, render_template
from engine.monitor import logs_cache
from engine.detector import detect_attack

app = Flask(__name__)

@app.route("/")
def home():
    formatted = []

    for log in logs_cache[::-1]:
        formatted.append({
            "log": log,
            "alert": detect_attack(log)
        })

    return render_template("index.html", logs=formatted)

if __name__ == "__main__":
    app.run(debug=True)
