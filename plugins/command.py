import os
import re
import string
import logging
import requests
import pyrogram
from config import Config
from plugins import helper
from plugins import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.private & filters.command(["admin"]))
async def settings(bot,message):
  if int(message.chat.id) in Config.OWNER_ID:
    await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  else:
    Chat_Id = message.chat.id
    await message.reply_text("<b>💔 Only Admin Command!!</b>")
   

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  #await message.reply_chat_action("typing")
  UserID = message.chat.id
  await Database.AddNewUser(bot,UserID)
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.HOME_PAGE)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

