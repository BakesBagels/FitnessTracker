from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Fitness Tracker API - Secure Connection"

if __name__ == "__main__":
    # Исправление CWE-319: Включаем SSL-контекст для шифрования трафика
    app.run(ssl_context='adhoc')
