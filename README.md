# 📦 Maine Server Backup  
**Простая система резервного копирования фермы с отправкой в Telegram.**

[🇷🇺 Русский](README.md) | [🇬🇧 English](README_en.md)

[<img src="https://res.cloudinary.com/dkgz59pmw/image/upload/v1736756459/knpk224-28px-market_ksivis.svg" alt="Market Link" width="200">](https://t.me/MaineMarketBot?start=8HVF7S9K)
[<img src="https://res.cloudinary.com/dkgz59pmw/image/upload/v1736756459/knpk224-28px-channel_psjoqn.svg" alt="Channel Link" width="200">](https://t.me/+vpXdTJ_S3mo0ZjIy)
[<img src="https://res.cloudinary.com/dkgz59pmw/image/upload/v1736756459/knpk224-28px-chat_ixoikd.svg" alt="Chat Link" width="200">](https://t.me/+wWQuct9bljQ0ZDA6)

---

## ✨ Особенности  
- 📂 Создание архивов с выбранных директорий  
- 📤 Отправка бэкапов в Telegram  
- 🗑️ Автоматическое удаление старых копий  
- ⏰ Работа по расписанию  
- 🛣️ Поддержка Docker  

---

## 🛠️ Установка  

1. **Клонируйте репозиторий:**  
   ```bash
   git clone https://github.com/yourusername/backup-server.git
   cd backup-server
   ```

2. **Создайте виртуальное окружение и установите зависимости:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или
   .\venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Создайте файл `.env` на основе примера:**  
   ```bash
   cp .env.example .env
   ```

4. **Настройте `.env` файл:**  
   ```env
   TELEGRAM_TOKEN=your_bot_token
   CHAT_ID=your_chat_id
   BACKUP_SOURCE=/path/to/backup
   BACKUP_DIR=/path/to/store/backups
   KEEP_BACKUPS=3
   BACKUP_TIME=00:00
   BACKUP_INTERVAL=24
   ```

---

## 🚀 Использование  

### 💻 Через Python  
- **Запуск меню:**  
   ```bash
   python main.py
   ```

- **Быстрый бэкап:**  
   ```bash
   python main.py --a 1
   ```

- **Запуск по расписанию:**  
   ```bash
   python main.py --a 2
   ```

### 🛣️ Через Docker  
- **Сборка и запуск:**  
   ```bash
   docker-compose up -d
   ```

- **Просмотр логов:**  
   ```bash
   docker-compose logs -f
   ```

- **Остановка:**  
   ```bash
   docker-compose down
   ```

---

## 📢 Telegram канал  

Подпишитесь на [@mainecrypto](https://t.me/mainecrypto) для:  
- 🔄 Обновлений проекта  
- 🗰 Новостей криптовалют  
- 📓 Обучающих материалов  
- 🔍 Технических обзоров  
- 🗨️ Общения с сообществом  

---

## 📮 Поддержка  

- Telegram: [@mainecrypto](https://t.me/mainecrypto)  

---

## 📜 Лицензия  

Проект распространяется под лицензией [MIT License](https://opensource.org/licenses/MIT).  
