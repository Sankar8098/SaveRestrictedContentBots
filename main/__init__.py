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
SESSION = "hTFkP7c_QIHdprTieXE13zQq1wWDGwLLgFpwjoTBGAx0ir8T_XDgvZBmR0vnU_9Z5qN5dzXcyXi1AUc6IFE3aq85dUTYahm96RcD3jjwL4xs6RHz71fOrrjXrl2s1hzS93LbqsAWYaXVtkhoHyrryc7WBfz059bONdNY0JnNtWaioAJ4JLM9J7175TKhSIes2sMl--cmeufuzdU-VzLiGAK6T38Bv0PP3uI82jOccgAAAAFerw5dAA"
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
