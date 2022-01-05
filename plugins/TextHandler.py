import re 
import logging
import os
import math
from config import Config
import pyrogram
from plugins import helper
import requests
import urllib.request
from pyrogram import Client, filters
from plugins.display_progress import progress_for_pyrogram,get_size,TimeFormatter
import time
#from callbackquery import GetRunningOprtn
from plugins.callbackquery import GetRunningOprtn

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

#@Client.on_message()
async def NewspaperName(bot, message):
  msg = await update.message.edit_text(text=f"<b>Send me Your NESPAPAER Name</b>",reply_markup=ForceReply(True),disable_web_page_preview=True)
  #await bot.send_message(
    #message.reply_to_message.from_user.id,
    #"Enter new name for media\n\nNote : Extension not required",
    #reply_to_message_id=message.reply_to_message.message_id,
    #reply_markup=ForceReply(True)
    #)

@Client.on_message(filters.private & filters.reply & filters.text)
async def cus_name(bot, message):
  if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
    print("good")
    #asyncio.create_task(rename_doc(bot, message))     
  else:
    print('No media present')
 
async def onMsg(client,message):
    #global messages
    #print("onMessage event")
    #print(message)
    Current_Operation = await GetRunningOprtn()
    chat_id = message.chat.id
    user_id = message.from_user.id
    chat_type = message.chat.type
    #cmd = message.text.split(" ")
    if chat_type == "private":
      if Current_Operation == "requestnewspaper":
        print("goodddd")
