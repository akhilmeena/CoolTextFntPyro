import logging
import os
import requests
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import helper
import re
from plugins import Newspapers

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.private & filters.command(["check"]))
async def settinguisjj(bot,message):
  #await message.reply_text(Newspapers.TheHindu30Resultfinal)
  print(Newspapers.TheHindu30Resultfinal)
  
@Client.on_message(filters.private & filters.command(["admin"]))
async def settingsjj(bot,message):
  print(f"{message.chat.id}")
  if int(message.chat.id) in Config.OWNER_ID:
    await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  else:
    Chat_Id = message.chat.id
    await message.reply_text("<b>💔 Only Admin Command!!</b>")
   

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  await message.reply_chat_action("typing")
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.START_BUTTONS)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

@Client.on_message(filters.regex('http') & filters.private)
async def pdisk(bot, message):
  Url2Dowload = message.text
  await Urlleaccher(bot,message,Url2Dowload)
    
