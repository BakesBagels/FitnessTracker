from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    return "Fitness Tracker API - Secure Connection"

# Этот декоратор применит заголовки ко ВСЕМ ответам (включая 404 и 500)
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Более строгая политика CSP, чтобы убрать WARN [10055]
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none';"
    response.headers['Permissions-Policy'] = 'geolocation=(), camera=(), microphone=()'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    # Убираем инфо о сервере
    response.headers['Server'] = 'Hidden' 
    # Управление кэшем (уберет WARN [10049])
    response.headers['Cache-Control'] = 'no-store, max-age=0'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
