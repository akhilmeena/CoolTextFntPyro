import re 
import os
import logging
import pyrogram
from config import Config
from plugins import helper
from pyrogram import Client, filters
 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


Current_Text = {}


#@Client.on_message(filters.text & ~filters.command)
def my_handler(client, message):
    print(message)

@Client.on_message(filters.private & filters.text & filters.regex(r"^(?!/).*"))
async def TextHandlewithFont(bot,message):
  #Current_Text.clear()
  #Current_Text.append(message.text)
  Current_Text[message.chat.id] = message.text
  await message.reply_text("Choose Your Methods",reply_markup=helper.STARTFontingBTN)
  
