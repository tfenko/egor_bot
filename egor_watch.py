import os
from telethon import TelegramClient, events
import requests

# 🔑 Секрети з Environment Variables
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

# Юзернейм або ID чату, де буде відслідковуватися Егор
chat_username = os.environ["CHAT_USERNAME"]  # username без @ або ID (починається з -100)
egor_id = int(os.environ["EGOR_ID"])        # Telegram ID Егора

# Telegram Bot для пересилки
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = [int(i) for i in os.environ["CHAT_IDS"].split(",")]  # список чатів, куди надсилати

# Функція для надсилання повідомлень через Telegram Bot API
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in CHAT_IDS:
        requests.post(url, data={"chat_id": chat_id, "text": text})

# Ініціалізація клієнта Telethon
client = TelegramClient("session", api_id, api_hash)

# Старт клієнта
client.start()

# Надсилаємо повідомлення після старту
send_telegram_message("✅ Поиск Егора...")
print("✅ Поиск Егора...")

# Подія: нове вхідне повідомлення в чаті
@client.on(events.NewMessage(chats=chat_username, incoming=True))
async def handler(event):
    sender_id = event.sender_id
    text = event.text

    # Друк у лог для перевірки sender_id
    print(f"Message from {sender_id}: {text}")

    # Якщо повідомлення від Егора
    if sender_id == egor_id:
        msg = f"Егор написал!!!!!!❤️: {text}"
    else:
        msg = f"Новое сообщение в чате: {text}"

    send_telegram_message(msg)

# Відключення лише коли зупиниш
client.run_until_disconnected()