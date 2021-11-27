import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from itertools import islice


VisionIas = InlineKeyboardButton('✨ Vision IAS', callback_data='crnafrsdaily')
BackToLibrary = InlineKeyboardButton('🔙', callback_data='libraryopen')

CRNTAFRSOURCEBTN = InlineKeyboardMarkup([
  [VisionIas],
  [BackToLibrary]
  ])









Btn = []

@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  for i in range(10):
    x = InlineKeyboardButton(str(i),callback_data="akhil")
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
   

  
      
    
  

  

