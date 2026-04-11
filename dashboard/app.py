from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    data = pd.read_csv("../data/logs.csv")
    return render_template("index.html", tables=[data.to_html()])

if __name__ == "__main__":
    print("Dashboard running on http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
