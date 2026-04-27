# Используем легкий образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта
COPY . .

# Указываем переменную окружения для Flask
ENV FLASK_APP=app.py

# Открываем порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
