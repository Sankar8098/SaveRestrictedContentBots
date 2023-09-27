#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29409646
API_HASH = "a69d0340a520c1913c517bea143a3de7"
BOT_TOKEN = "5682083705:AAHHEc78t-XJUKPMba4CIRc4C1by-GH9lxE"
SESSION = "SKAQHAwW4AJEIroiVAUfNgtjly7dSFT9qqWA8nO7FtBe2YH90Aa8dx3bUX_eNrBGKLvGbglkS2ah23gAjJZZfJUvgd9JObnkJr7f3C8txjt9etqswU6qjjS8Bzy75wEhX5xUcN4uOnhY1ppru8Wn6NV-DjqoriwHKRE4WcegtjVwCFW7TprTn_E1l47IllG39NDGh9jdsfUqwdlVDYCbco4mqSyXmH_K-IYKrGPGaMvmxavf8WCRo20FHGzHxgvD0JX906vHqq1CTjzJsHG6TBfqEPcoUm2HhnMe-ZjK-66RECHwDSEPBK3H2YS1JzoQYEDOtRClezrAQSGJpmD2Rxi1gt8W9mwwAAAAFerw5dAA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5883498077

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
