from telethon import TelegramClient, events
import requests

api_id = 28636534
api_hash = "3b222decd980eef83f2201b912d51c80"


chat_username = "minetnya"
egor_id = 137750972

BOT_TOKEN = "8413510086:AAHTzx0kj7s_1uMwoNR07HD1ufU_JKSQm9M"
CHAT_IDS = [1669383404, 7030296301] 

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in CHAT_IDS:
        payload = {"chat_id": chat_id, "text": text}
        requests.post(url, data=payload)

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=chat_username))
async def handler(event):
    if event.sender_id == egor_id:
        msg = f"Егор написал!!!!!!❤️: {event.text}"
        print(msg)                
        send_telegram_message(msg) 


async def on_startup():
    send_telegram_message("✅ Поиск Егора...")
    print("✅ Поиск Егора...")

print("✅ Поиск Егора...")
client.start()
client.loop.run_until_complete(on_startup())
client.run_until_disconnected()