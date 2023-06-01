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
BOT_TOKEN = "6047195823:AAEuJCqHWWeOz4k76P3sU00RLcNiZTvjYzU"
SESSION = "BQFjJnYAxF4fOj1Z2PYw29hlBAZDMzFkUwC0IvF8i5GK3t8sAwDSYCCL-WYAjYXGuXh4SFVRAWKvupuhlQSYAGiTsmdlZQEJZrG5-FGSaQvyRYQKTlObibpbr909lDqCvCuvi7cgIBbo367Z21fPr7ABmNfrYmJYlUC0MyRDWjGNJg-btf7Vi4vph-pIboA-mAWhKjElQj1FlCWZe3GKkYNfiR4H9t5vUol8pYMFaWGb7glX3xu1tpuF4GnD_lH1Bf3KJQwl4b0kxb-Wr9EaYj0mzZHpe13IBOGW6MH5CWkwwyHPW4fspfkBQJK_hWu_D4man3S_ZwCbeSWS7f6e4wYvKiYSgQAAAAFSbLt8AA"
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
