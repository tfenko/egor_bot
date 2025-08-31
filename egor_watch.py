import os
from telethon import TelegramClient, events
import requests

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

chat_username = os.environ["CHAT_USERNAME"]
egor_id = int(os.environ["EGOR_ID"])

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = [int(i) for i in os.environ["CHAT_IDS"].split(",")]