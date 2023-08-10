#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24329924
API_HASH = "395fe20d8f4439e2f5bb1371533a25d3"
BOT_TOKEN = "6107891601:AAGXMd98Uoye5zNtsPmf4OWUqT6XXvSM0rY"
SESSION = "AQFzPsQAscat2Geg067hEBZdAMrrrB8_j-1EWIqCrd_VZK7Pl3bFWtejlQWuQsH-3ob0YO_sK3EzCdmrmEw_Wvnw27nkCNBaZZclG6VxltgvgybWjWJfSNaFd1eqfl94tZkXcCc4EzEc8C_5IVF9GwF0ZwftI39bIuJQcakYx166HvJxm2k2-DGtPCUoGMr-XC4Aot_QuZDywlniMApUUiLVpwetxW03NrFcVWLbRGHP7bk5kXPZchOm2ydfqLqSWJt0JajpCCmKNo0pvfnYdu5Qb6i7_B_f_4JIavILaYWlTBWujBvVc2BPABmcC6NYL_F9HpxF1uiajtoiUCbeI7YEP-_-QgAAAAFm4TwjAA"
FORCESUB = "SK_MoviesOffl"
AUTH = 6021004323

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
