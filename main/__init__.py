#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23275126
API_HASH = "532c54bbe1c3f2296981f02469455915"
BOT_TOKEN = "5922614273:AAE8igC0tlCB7AqiNHjuFTbLMQ-spDF9lxY"
SESSION = "BQFjJnYAk7WJemeEW8hSLCITV10DIMy2UaVVlQ1iJI0NrnyZN5Ki5_hL8LoSwuZL_XDTpSi8D12LmXtU-mMe18dgm3I2Cs9fY4E3wEoZyxxRYeGG8RbDcGSvsMwYhlYbJco4v15z6bhMlRU3veOptgHcKAY02Tm3XBYacvbfsTETsY1IUA02GFVR44PdIccMcB4OxCUmFqikSTXN2Xin9qySZ545WwraSYQJOUYRhOWz-pFSXNokS7E-WKU1VO_l48uDGEdzPZAHvN9pHoG9pWQJS5mTOdiMevjwdJ2ESkNQ3I1uyu20gzCOX76aj7hSMUv43UkNeFJIDs0Kf-6zvY0e4dD_GQAAAAFprIQxAA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5677824892

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
