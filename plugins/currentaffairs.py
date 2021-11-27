import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from itertools import islice

Source_Dict = {
  "Name":"✨ Vision IAS","CallBack":"vsniascrnt",
  "Name":"test","CallBack":"test"
}


VisionIas = InlineKeyboardButton('✨ Vision IAS', callback_data='crnafrsdaily')
BackToLibrary = InlineKeyboardButton('🔙', callback_data='libraryopen')

CRNTAFRSOURCEBTN = InlineKeyboardMarkup([
  [VisionIas],
  [BackToLibrary]
  ])

def makeBtnFromDict():
  Btn = []
  for d in Source_Dict:
    print(d)
    CallbackText = d['Name']
    CallbackData = i['CallBack']
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns









@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  Btn = []
  for i in range(10):
    x = InlineKeyboardButton(str(i),callback_data="akhil")
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
   

  
      
    
  

  

