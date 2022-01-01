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
from plugins import Newspapers
from plugins import Magzines


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.private & filters.command(["check"]))
async def settinguisjj(bot,message):
  #for root, dirs, files in os.walk("/Downloads"):
    #for file in files:
        #if file.endswith('.txt'):
      #print(file)
  #await message.reply_text(Newspapers.TheHindu30Resultfinal)
  print(Magzines.AllChahalMagzResult)
  
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
  UserID = message.chat.id
  await message.reply_chat_action("typing")
  await Database.AddNewUser(UserID)
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.START_BUTTONS)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

@Client.on_message(filters.text)
async def give_filter(bot,message):
  Chat_Id = message.chat.id
  Text = message.text
  print(Text)
 

@Client.on_message(filters.regex('http') & filters.private)
async def pdisk(bot, message):
  Url2Dowload = re.search("(?P<url>https?://[^\s]+)", message.text).group("url")
  await urluploader.Urlleaccher(bot,message,Url2Dowload)
    
