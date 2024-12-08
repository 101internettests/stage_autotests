import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))
daily = int(os.getenv("CHAT_ID_DAILY", "0"))
host_stage = os.getenv("URL_STAGE")