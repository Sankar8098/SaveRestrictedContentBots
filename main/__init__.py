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
BOT_TOKEN = "6120739837:AAFftL-5-qOMbJo6YnLWqcQYUiWz-KKJKMc"
SESSION = "BQFjJnYAeTnEkcpa1bVkuU5jOOz45xO-Mxb0GyZ_iAHBMEi2xHt6oBHb7nEShG-IQRx5CWzq63fF-nYw2Tbec2SVqvhxsodn7nQPFC38jvIhiOD6bu46CVxwzLL_v-_qiizdBNrrU0O6pubbiknF2LVVu_Cl-vn1_H2W5rfRsQo9o2KPJJOcfXRl9DcfJhkneWMYOjXS8qvG4XoJ9h9K7HzUDhSojr3vNdiSnWg2BoshNVqms0ZVYQeos4Ud3rSAaBIyLmPwiQgAruXp9jmjrWRLArt9MSpP9YEE5fIaFUPXwKKsIjfyVXI6DJ_e8bfqWDO7MdWvnxzcystbzNI8KfXp5c-qQAAAAAF2sa3TAQ"
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
