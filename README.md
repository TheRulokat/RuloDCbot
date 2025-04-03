# Discord-Telegram Duyuru Botu

Bu proje, belirlenen bir Discord kanalındaki mesajları otomatik olarak bir Telegram grubuna veya kanalına ileten bir bottur. Hem Discord hem de Telegram botlarını entegre eden bu sistem, duyuruların farklı platformlara eş zamanlı aktarılmasını sağlar.

## Özellikler
- Belirlenen bir Discord kanalındaki mesajları algılar.
- Bu mesajları Telegram kanalına veya grubuna gönderir.
- Telegram botu temel komutları destekler (örn. `/start`).
- Çevre değişkenleri ile güvenli yapılandırma sağlar.

## Gereksinimler
Bu botu çalıştırmak için aşağıdaki paketlerin sisteminizde yüklü olması gerekmektedir:

- Python 3.8+
- `discord.py`
- `aiogram`
- `aiohttp`
- `python-dotenv`

Gerekli bağımlılıkları yüklemek için:
```bash
pip install -r requirements.txt
```

## Kurulum
1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/discord-telegram-bot.git
   cd discord-telegram-bot
   ```
2. Bir `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:
   ```ini
   DISCORD_TOKEN=discord_bot_token
   TELEGRAM_BOT_TOKEN=telegram_bot_token
   TELEGRAM_CHAT_ID=telegram_chat_id
   DUYURU_KANAL_ID=discord_kanal_id
   ```
3. Botu başlatın:
   ```bash
   python bot.py
   ```

## Çalışma Mantığı
- Discord botu, belirlenen kanalın mesajlarını dinler.
- Eğer mesaj, botun çalıştığı kanal üzerinden gelirse, içerik alınır ve Telegram API kullanılarak belirlenen Telegram kanalına/grubuna gönderilir.
- Telegram botu, `/start` komutu ile çalıştığını doğrulayabilir.

## Hata Ayıklama
Eğer bot düzgün çalışmıyorsa:
- `.env` dosyanızın doğru bilgiler içerdiğinden emin olun.
- Discord botunun doğru izinlere sahip olduğundan emin olun.
- Telegram botunun ilgili gruba veya kanala mesaj gönderebildiğini kontrol edin.

## Katkıda Bulunma
Bu projeye katkıda bulunmak için pull request gönderebilir veya yeni özellikler önerebilirsiniz.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır.

# Discord-Telegram Announcement Bot

This project is a bot that automatically forwards messages from a specified Discord channel to a Telegram group or channel. By integrating both Discord and Telegram bots, this system ensures real-time announcement synchronization across platforms.

## Features
- Listens to messages in a specified Discord channel.
- Sends these messages to a Telegram channel or group.
- Supports basic Telegram bot commands (e.g., `/start`).
- Uses environment variables for secure configuration.

## Requirements
To run this bot, you need the following dependencies installed:

- Python 3.8+
- `discord.py`
- `aiogram`
- `aiohttp`
- `python-dotenv`

To install the required dependencies:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/discord-telegram-bot.git
   cd discord-telegram-bot
   ```
2. Create a `.env` file and add the following information:
   ```ini
   DISCORD_TOKEN=discord_bot_token
   TELEGRAM_BOT_TOKEN=telegram_bot_token
   TELEGRAM_CHAT_ID=telegram_chat_id
   DUYURU_KANAL_ID=discord_channel_id
   ```
3. Start the bot:
   ```bash
   python bot.py
   ```

## How It Works
- The Discord bot listens for messages in a specified channel.
- If a message is detected in that channel, its content is retrieved and sent to the designated Telegram group/channel using the Telegram API.
- The Telegram bot can respond to the `/start` command to confirm it is running.

## Debugging
If the bot is not working properly:
- Ensure your `.env` file contains the correct information.
- Make sure the Discord bot has the necessary permissions.
- Check if the Telegram bot has permission to send messages in the designated group or channel.

## Contributing
You can contribute to this project by submitting pull requests or suggesting new features.

## License
This project is licensed under the MIT License.

