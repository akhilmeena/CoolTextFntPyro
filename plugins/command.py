import logging
import os
import requests
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import helper
from plugins import Database
from plugins import urluploader
import re
import string
from plugins import Newspapers
from plugins import Magzines


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

Process = ["Nothing"]

@Client.on_message(filters.private & filters.command(["admin"]))
async def settings(bot,message):
  #print(f"{message.chat.id}")
  if int(message.chat.id) in Config.OWNER_ID:
    await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  else:
    Chat_Id = message.chat.id
    await message.reply_text("<b>💔 Only Admin Command!!</b>")
   
@Client.on_message(filters.private & filters.command(["test"]))
async def settingsjj(bot,message):
  if int(message.chat.id) in Config.OWNER_ID:
    RequestNewsPaper = InlineKeyboardButton('💌 Request NewsPaper', callback_data='requestnewspaper')
    ClosePannel = InlineKeyboardButton('❌ Close', callback_data='close')
    buttonnnn = InlineKeyboardMarkup([
      [RequestNewsPaper],
      [ClosePannel]
      ])
    await message.reply_text("<b>Testing Pannel</b>",reply_markup=buttonnnn)
  else:
    Chat_Id = message.chat.id
    await message.reply_text("<b>💔 Only Admin Command!!</b>")


@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  UserID = message.chat.id
  print(message.text)
  await message.reply_chat_action("typing")
  ReferredBy=""
  try:
    ReferredBy+= f"{message.text}".split("/start")[1].strip()
  except:
    ReferredBy+="None"
  print(f"|{ReferredBy}|")
  await Database.AddNewUser(bot,UserID,ReferredBy)
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.START_BUTTONS)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

@Client.on_message(filters.text & filters.regex(r"^(?!http|https|I Invite You to).*") & filters.private)
async def give_filter(bot,message):
  Chat_Id = message.chat.id
  Text = message.text
  if str(Config.MaintainaceYN[0]) == "No":
    if Process[0] == "Nothing":
      await message.reply_text(text="<b>Please /start The Bot And Find Your Require Materials.</b>")
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

@Client.on_message(filters.regex('^http') & filters.private)
async def pdisk(bot, message):
  Url2Dowload = re.search("(?P<url>https?://[^\s]+)", message.text).group("url")
  await urluploader.Urlleaccher(bot,message,Url2Dowload)
    
