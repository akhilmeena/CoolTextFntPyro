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


#@app.on_message(filters.text & ~filters.edited)
#def my_handler(client, message):
#    print(message)

@Client.on_message(filters.private & filters.text)
async def TextHandlewithFont(bot,message):
  await message.reply_text("Choose Your Methods",reply_markup=helper.STARTFontingBTN)

