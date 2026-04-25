from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Fitness Tracker API"

if __name__ == "__main__":
    # CWE-319: Специально без SSL, чтобы сканер нашел ошибку
    app.run(host="0.0.0.0", port=5000)
