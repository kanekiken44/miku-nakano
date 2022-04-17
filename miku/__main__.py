#### file where bot starts
from miku import miku, tele
from pyrogram import idle
from vars import Config

miku.start()
tele.start(bot_token=Config.BOT_TOKEN)
idle()
