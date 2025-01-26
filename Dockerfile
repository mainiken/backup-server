FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TELEGRAM_TOKEN=""
ENV CHAT_ID=""
ENV BACKUP_SOURCE="/data/source"
ENV BACKUP_DIR="/data/backups"
ENV KEEP_BACKUPS="3"
ENV BACKUP_TIME="00:00"
ENV BACKUP_INTERVAL="24"

VOLUME ["/data/source", "/data/backups"]

CMD ["python", "main.py", "--a", "2"]
