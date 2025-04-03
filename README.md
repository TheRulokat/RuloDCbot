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

