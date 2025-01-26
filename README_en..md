# 📦 Server Backup System  
**A simple backup system with Telegram integration.**

---

## ✨ Features  
- 📂 Create archives from selected directories  
- 📤 Send backups to Telegram  
- 🗑️ Automatically delete old backups  
- ⏰ Schedule backups  
- 🛣️ Docker support  

---

## 🛠️ Installation  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/backup-server.git
   cd backup-server
   ```

2. **Create a virtual environment and install dependencies:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Create a `.env` file based on the example:**  
   ```bash
   cp .env.example .env
   ```

4. **Configure the `.env` file:**  
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

## 🚀 Usage  

### 💻 Via Python  
- **Launch menu:**  
   ```bash
   python main.py
   ```

- **Quick backup:**  
   ```bash
   python main.py --a 1
   ```

- **Scheduled backup:**  
   ```bash
   python main.py --a 2
   ```

### 🛣️ Via Docker  
- **Build and run:**  
   ```bash
   docker-compose up -d
   ```

- **View logs:**  
   ```bash
   docker-compose logs -f
   ```

- **Stop:**  
   ```bash
   docker-compose down
   ```

---

## 📢 Telegram Channel  

Subscribe to [@mainecrypto](https://t.me/mainecrypto) for:  
- 🔄 Project updates  
- 🗰 Cryptocurrency news  
- 📓 Educational materials  
- 🔍 Technical reviews  
- 🗨️ Community discussions  

---

## 📮 Support  

- Telegram: [@mainecrypto](https://t.me/mainecrypto)  
- Issues on [GitHub](https://github.com/yourusername/backup-server/issues)  

---

## 📜 License  

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
