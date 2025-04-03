import os
import discord
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command  
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DUYURU_KANAL_ID = int(os.getenv("DUYURU_KANAL_ID", 0))

# Hata kontrolü
if not DISCORD_TOKEN or not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID or not DUYURU_KANAL_ID:
    raise ValueError("Gerekli çevre değişkenleri eksik!")

# Telegram botu
tg_bot = Bot(
    token=TELEGRAM_BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode="HTML")
)

# Telegram Router
router = Router()

@router.message(Command("start"))  
async def start_command(message: types.Message):
    await message.answer("Telegram bot is running!")

async def start_telegram_bot():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(tg_bot)

# Discord Bot
class DiscordBot(discord.Client):
    async def on_ready(self):
        print(f"Discord bot logged in as: {self.user}")

    async def on_message(self, message):
        if message.channel.id == DUYURU_KANAL_ID and message.author != self.user:
            telegram_message = message.content

            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(
                        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                        json={"chat_id": TELEGRAM_CHAT_ID, "text": telegram_message, "parse_mode": "HTML"}
                    ) as resp:
                        print(f"Telegram mesaj durumu: {await resp.text()}")
                except Exception as e:
                    print(f"Telegram mesaj gönderme hatası: {e}")

intents = discord.Intents.default()
intents.message_content = True
discord_bot = DiscordBot(intents=intents)

async def main():
    await asyncio.gather(
        discord_bot.start(DISCORD_TOKEN),
        start_telegram_bot()
    )

if __name__ == "__main__":
    asyncio.run(main())
