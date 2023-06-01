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
SESSION = "BQARxYAgmY86OW1ibSiSsBow9RgLwCxdHpM9CX8drOEswIg-VL9P26OdMtGPNgcWOOMddFFjk-F54vPBHnNRexuYz2u6PH5K8P_NxVP99ZrdtNJ0hbZ_OVfMOCRZVm0lqsSR4Vsw3BoLMwRkzkX7uJeas9dU2TCRK4ARzATgEzG-LEfgkBCSA9HfilZfK4PUP5FnA-EjU-PDJEq96aCERjnbZuCDNJOEKuweZVfy4gKU4vjRMH_6B5Hb_pIjuY6u6SqJ0fvefHddM1FLs2e3EuO99geuP5e6VXjigQMvXlttOcQgfY8jR16a9plxH6trvn-y1AUNCcM9uCikMdtXzsyMAAAAAWmshDEA"
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
