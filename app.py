from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response("Fitness Tracker API - Secure Connection")
    # Исправляем то, на что ругался ZAP:
    response.headers['X-Frame-Options'] = 'DENY'  # Защита от кликджекинга
    response.headers['X-Content-Type-Options'] = 'nosniff' # Защита от подмены типов
    response.headers['Content-Security-Policy'] = "default-src 'self'" # CSP заголовок
    response.headers['Server'] = 'SecureServer' # Скрываем версию сервера
    return response

if __name__ == "__main__":
    # Возвращаем host для Docker, но пока без SSL, чтобы ZAP не спотыкался
    app.run(host='0.0.0.0', port=5000)
