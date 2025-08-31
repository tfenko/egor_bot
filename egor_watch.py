import os
from telethon import TelegramClient, events
import requests

# Секрети
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

chat_username = os.environ["CHAT_USERNAME"]
egor_id = int(os.environ["EGOR_ID"])

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = [int(i) for i in os.environ["CHAT_IDS"].split(",")]

# Функція надсилання повідомлень через Telegram Bot API
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in CHAT_IDS:
        requests.post(url, data={"chat_id": chat_id, "text": text})

# Ініціалізація клієнта Telethon
client = TelegramClient("session", api_id, api_hash)

# Подія: нове повідомлення
@client.on(events.NewMessage(chats=chat_username))
async def handler(event):
    if event.sender_id == egor_id:
        msg = f"Егор написал!!!!!!❤️: {event.text}"
        print(msg)
        send_telegram_message(msg)

# Старт клієнта
client.start()

# Надсилаємо повідомлення після старту
send_telegram_message("✅ Поиск Егора...")
print("✅ Поиск Егора...")

# Відключення лише коли зупиниш
client.run_until_disconnected()