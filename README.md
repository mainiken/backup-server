Server Backup System
Простая система резервного копирования с отправкой в Telegram.

Особенности
Создание архивов с выбранных директорий
Отправка бэкапов в Telegram
Автоматическое удаление старых копий
Работа по расписанию
Поддержка Docker
Установка
Клонируйте репозиторий:
bash
git clone https://github.com/yourusername/backup-server.git
cd backup-server
Создайте виртуальное окружение и установите зависимости:
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
Создайте файл .env на основе примера:
bash
cp .env.example .env
Настройте .env файл:
bash
TELEGRAM_TOKEN=your_bot_token
CHAT_ID=your_chat_id
BACKUP_SOURCE=/path/to/backup
BACKUP_DIR=/path/to/store/backups
KEEP_BACKUPS=3
BACKUP_TIME=00:00
BACKUP_INTERVAL=24
Использование
Через Python
bash
# Запуск меню
python main.py

# Быстрый бэкап
python main.py --a 1

# Запуск по расписанию
python main.py --a 2
Через Docker
bash
# Сборка и запуск
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down
Telegram канал
Подпишитесь на @mainecrypto для:

Обновлений проекта
Новостей криптовалют
Обучающих материалов
Технических обзоров
Общения с сообществом
Поддержка
По всем вопросам обращайтесь:

Telegram: @mainecrypto
Issues на GitHub
Лицензия
MIT License
