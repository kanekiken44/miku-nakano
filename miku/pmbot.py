#### module
import os
import time
import shutil
import psutil
import pyrogram
import subprocess

from sys import version as pyver
from pyrogram import Client, filters, idle
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from vars import Config
from miku import LOGGER
from miku import miku

##### TEXTS ########
START_TEXT = """Hey, {}-kun it's me Miku-Nakano
Personal Assistant of [Dazai](t.me/dazai_xxx)
You can contact him through me
Send your msg here, he'll reply wen he is online."""

INFO_TEXT = """Heya

Itz me Dazai
about me - just a 15y/o kid who likes programming n Linux.
Languages i know - None, im not expert at any programing langs.
Moi github id - github.com/kanekiken44
Check out - @LoneGhoul
Thats it..."""

IF_TEXT = "<b>Message of:</b> {}\n<b>User:</b> {}\n\n{}"


###### BUTTONS ######
START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('About', callback_data="info_"),
        InlineKeyboardButton('Moi Senpai', url="https://t.me/dazai_xxx")
        ]]  
)

BACK_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data="back")
        ]]
)


#### CALLBACKS ######
@miku.on_callback_query()
async def cb_data(miku, update):  
    if update.data == "info_":
        await update.message.edit_text(
            text=INFO_TEXT,
            reply_markup=BACK_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )  

@miku.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True
    )
    
    
@miku.on_message(filters.private & filters.text)
async def pm_miku(miku, message):
    if message.from_user.id == Config.BOT_OWNER:
        await reply_text(miku, message)
        return
    info = await miku.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await miku.send_message(
        chat_id=Config.BOT_OWNER,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )
    
    
@miku.on_message(filters.user(Config.BOT_OWNER) & filters.text & filters.private)
async def reply_text(miku, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await miku.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )        
