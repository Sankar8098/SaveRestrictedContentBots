#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 8802706
API_HASH = "97546900397a98f481bfb8252b1ac4f4"
BOT_TOKEN = "6073401662:AAHdR7d95gVt-3u-p4XBMueyajWO3cgq-vc"
SESSION = "BQCQ_WDDLVIlIdITV_t0j1TvcP4ZZPYvUqq89CoDI09SWLyUXOq1XxCwfYIs7OH2n_aCYlPVjOuqineu_ucHDa09gb_RTczHJ2YPW9XyTp5T0fwXC8R4wG-snt6-7qw_IuD7zTTpw9TVQuCDMWsCeW7OX-10n29CwbAMYARvgU97xs83ZtVJgXq1Ud_m0EFlhReffWXhYYwhEypYdIIXIh2AW_YuUPRKtf8RHFdUxLIPgvRMN2BluLEmbwFVH_AtxUAOSh5itMT4DrksFLlfDE77fW9WVEGqDA3rhxJ4S8APdr78aj7YUFmkGBsr0VWqXW-ekyjPtQuIsNWZw-l-Eh2MAAAAAExl8tUA"
FORCESUB = "xxx_xmdisk"
AUTH = 5564974530

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
