#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23788442
API_HASH = "72dd69766639a884b8985937d7fb3e43"
BOT_TOKEN = "6178286330:AAGyOx8tGlxbtD-_PCElEJNajtmmmZz_ehA"
SESSION = "BQFq-5oAxJ-sGxPMtuNV8q9dyGVNFjrl4fLdp9aPozjGlKrs2c6zETGCfbO2PdnBcF1vEaWQem_Part7tt2ps9UIPI8OvCnmNEaOBvgHDCse9x3vqe8obSmZzRLfNdUj4WSS43vvsB-DwIxnlakURXQ4S4NWHwUqLo5o9ZFN3uXwO5fLAcT5WpLXSnFvSqK8us5GyN4GVIju1xZ9JmsF_3Yb-X72WpouWi471cft7-nm8uhXs78EvqkViM6wfsvKWapMqLMKnOHJeyKzQ2V_0E41B2l6OunQ6Rh5rOb8SlV_xzjrTI5pPvFWf6nMDTGkAgCaDI94HcmBfcIk9QLe7cXqvBQcTwAAAABNCkZ9AA"
FORCESUB = "SK_MoviesOffl"
AUTH = 1292519037

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
