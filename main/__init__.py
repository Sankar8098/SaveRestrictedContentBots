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
SESSION = "1BVtsOGYBu6pniE4TPu3i8R1dbzsZUn0TpeHWxTVdFRo7y0cIhB6PTc8z-imEe5AMOdypDbSJSB4nm_OiBKjLMHcUZvorgbIxMnWZsGIjRMRjueBXOKY4dG5Tg6Y4C0e1uTd65ozVWr2xZrgEqE1ZaIHP0h1wNhwocnrcNGVPmSiOT2O71NPlXp0A_tkRT9hvSmMRylt5_RlA5APZLpYHcpZRn88_OBY6hU95NXQ1B0Vexm5soMsfEYttiap8Y3eshsesbiy1P-EqoOGUN5jrZMnCyc4i-XIGStM5FPSb1--gsmkneq-AzX5pbxLp_Yp78zQeaCNUeFNX8oi__jjM4iMvZTrCxOU="
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
