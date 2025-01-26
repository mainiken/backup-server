FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаем директории для бэкапов и логов
RUN mkdir -p /data/source /data/backups /app/logs

# Используем переменные окружения из .env
ENV $(cat .env | xargs)

VOLUME ["/data/source", "/data/backups", "/app/logs"]

CMD ["python", "main.py", "--a", "2"]
