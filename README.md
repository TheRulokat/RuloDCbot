# 🚀 Discord-Telegram Duyuru Botu
![Untitled](https://github.com/user-attachments/assets/235b3e26-000a-4b72-919d-5d30d4a75c9a)

Bu proje, belirlenen bir Discord kanalındaki mesajları otomatik olarak bir Telegram grubuna veya kanalına ileten bir bottur. Hem Discord hem de Telegram botlarını entegre eden bu sistem, duyuruların farklı platformlarda eş zamanlı paylaşılmasını sağlar. 📢

## ⭐ Özellikler
- 🔍 Belirlenen bir Discord kanalındaki mesajları izler.
- 🔄 Bu mesajları otomatik olarak belirtilen Telegram kanalına veya grubuna iletir.
- 📝 `/start` gibi temel Telegram bot komutlarını destekler.
- 🔒 API anahtarlarını ve yapılandırmayı güvenli bir şekilde yönetmek için çevre değişkenlerini kullanır.

## 📌 Gereksinimler
Bu botu çalıştırmak için aşağıdaki bağımlılıkların kurulu olması gerekmektedir:

- 🐍 Python 3.8+
- 🤖 `discord.py`
- 🤖 `aiogram`
- 🌐 `aiohttp`
- 🛠️ `python-dotenv`

Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
```bash
pip install -r requirements.txt
```

## 🛠️ Kurulum
1. 📂 Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/discord-telegram-bot.git
   cd discord-telegram-bot
   ```
2. 📄 Proje dizininde bir `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:
   ```ini
   DISCORD_TOKEN=discord_bot_tokeniniz
   TELEGRAM_BOT_TOKEN=telegram_bot_tokeniniz
   TELEGRAM_CHAT_ID=telegram_chat_id
   DUYURU_KANAL_ID=discord_kanal_id
   ```
3. ▶️ Botu başlatın:
   ```bash
   python RuloDCbot.py
   ```

## 🔄 Çalışma Mantığı
- 🏗️ Discord botu, belirlenen kanalın mesajlarını dinler.
- 📩 Bir mesaj algılandığında, içeriği alınır ve Telegram API aracılığıyla belirtilen Telegram grubuna veya kanalına iletilir.
- ✅ Telegram botu, çalıştığını doğrulamak için `/start` komutuna yanıt verebilir.

## 🛠️ Hata Ayıklama
Eğer bot düzgün çalışmıyorsa, aşağıdaki adımları kontrol edin:
- 📌 `.env` dosyanızın doğru API anahtarlarını ve kanal/grup kimliklerini içerdiğinden emin olun.
- 🔑 Discord botunun belirtilen kanaldan mesajları okuyabilmesi için gerekli izinlere sahip olduğundan emin olun.
- 📲 Telegram botunun hedef gruba veya kanala mesaj gönderebildiğini kontrol edin.

## 🤝 Katkıda Bulunma
Sorularınız veya geri bildirimleriniz için bana Discord üzerinden ulaşabilirsiniz: ## the.rulokat

## 📜 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. 📝

---

# 🚀 Discord-Telegram Announcement Bot
![Untitled](https://github.com/user-attachments/assets/46bc6d0a-3524-4694-97f4-bc6ee6477bfc)

This project is a bot that automatically forwards messages from a specified Discord channel to a Telegram group or channel. By integrating both Discord and Telegram bots, this system ensures seamless, real-time announcement synchronization across platforms. 📢

## ⭐ Features
- 🔍 Monitors messages in a designated Discord channel.
- 🔄 Automatically forwards messages to a specified Telegram channel or group.
- 📝 Supports basic Telegram bot commands, such as `/start`.
- 🔒 Securely manages API tokens and configuration using environment variables.

## 📌 Requirements
To run this bot, ensure you have the following dependencies installed:

- 🐍 Python 3.8+
- 🤖 `discord.py`
- 🤖 `aiogram`
- 🌐 `aiohttp`
- 🛠️ `python-dotenv`

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## 🛠️ Installation
1. 📂 Clone this repository:
   ```bash
   git clone https://github.com/username/discord-telegram-bot.git
   cd discord-telegram-bot
   ```
2. 📄 Create a `.env` file in the project directory and add the following information:
   ```ini
   DISCORD_TOKEN=your_discord_bot_token
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   DUYURU_KANAL_ID=your_discord_channel_id
   ```
3. ▶️ Start the bot:
   ```bash
   python RuloDCbot.py
   ```

## 🔄 How It Works
- 🏗️ The Discord bot listens for new messages in a specified channel.
- 📩 When a message is detected, its content is retrieved and forwarded to the designated Telegram group or channel via the Telegram API.
- ✅ The Telegram bot provides basic functionality, such as responding to the `/start` command to confirm it is operational.

## 🛠️ Troubleshooting
If the bot is not functioning correctly, try the following steps:
- 📌 Verify that your `.env` file contains the correct API tokens and chat/channel IDs.
- 🔑 Ensure that the Discord bot has the necessary permissions to read messages from the designated channel.
- 📲 Check whether the Telegram bot has permission to send messages in the target group or channel.

## 🤝 Contributing
For any questions or feedback, feel free to contact me on Discord: the.rulokat 🎯

## 📜 License
This project is licensed under the MIT License. 📝

