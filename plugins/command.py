import logging
import os
import requests
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import helper
from plugins import url_uploader



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  await message.reply_chat_action("typing")
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.START_BUTTONS)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

#@Client.on_message(filters.command(["admin"]) & filters.private & filters.user(Config.OWNER_ID) & ~filters.edited)
@Client.on_message(filters.private & filters.command(["admin"]))
async def settings(bot,message):
  if int(message.chat.id) in Config.OWNER_ID:
    await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  else:
    Chat_Id = message.chat.id
    #message.delete_messages(Chat_Id, message.message_id)
    await message.reply_text("<b>💔 Only Admin Command!!</b>")
    #message.message.delete_messages(Chat_Id, message.message_id)

@Client.on_message(filters.regex('http') & filters.private)
async def DownloadTest(bot, update):
  url = update.text
  await url_uploader.leecher2(bot , update,url)
  
@Client.on_message(filters.private & filters.command(["folders"]))
async def settings(bot,message):
  start_path = 'Downloads/'
  try:
    for path,dirs,files in os.walk(start_path):
      for filename in files:
        print(os.path.join(path,filename))
  except Exception as e:
    print(e)
        #await message.reply_text(akhil)
    #message.message.delete_messages(Chat_Id, message.message_id)
