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
BOT_TOKEN = "6073401662:AAHdR7d95gVt-3u-p4XBMueyajWO3cgq-vc"
SESSION = "BQB8a3KQ1HsM1YfNU-1AIk9meM2P1ZQo_nCK3Mk1xmbiy3mtnNNuGOE7i77AGOBjhpkfr5aCAUYsUXCDOotd9eXHW-bDfSWF_cZRFS7YDCuzExHLnxMIb8aLjJMdnTqQS7iXynb-ciNP0I5_PDBzvWDilBzH857Xz4LeT1Gdt2hya671KPq4RrEy01dUsGpEWVNw6oC8_R_juseA1sS0Qump9KaPHHdgqtd0wC8iTFD4Lx6nFA8WG61CSUCcJXWSSf4ql9gipDetAxNKo0t8VPzYokNszt-13Ulkin3C-GjP6Orqu2c7qvkL0ronvBlIITRJKWkItEkKnhZTxLTtwLjTAAAAAUuyxcIA"
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
