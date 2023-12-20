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
SESSION = "AQHAwW4AHS9JD_BWFLUr4cyAHIGuh711y9WBJmKg8sMsYKf3tm-D0vHX8GCAoG71VWiH3L_g-XJwg6bLPKOY-NGfq7RFivvrqKpTbf3TpRwyoAmbQVyNW2xTVYiBUqFpVLV05Mp8i_ais9Uf35tMRzWdTxGO5-g2wZA6-D1fz94dqWzVcsh5qjr4_6BvbgORcgUWdTIFQxrZHvH4erhZNchQTEG-14_1r6KIH3CrvBMlREDj9CUut7wiqAKVFozTHT91sGa_KqMPgr5uqwQWLZ_XMc3wDr0X8Phxfh66eKBSqDsMBpZ_c7wW2FnSlptidc6ShHDeWaTDhmRGDkgSK71kJYGMsQAAAAFerw5dAA"
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
