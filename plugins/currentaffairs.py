import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from itertools import islice

Btn = []

@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  for i in range(10):
    x = InlineKeyboardButton(str(i),callback_data="akhil")
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  #ak =  [Btn[i:i+3] for i in range(0,len(l),3)]
#Out[17]: [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13]]
#Share Edit Follow
  #ak = list(list(t) for t in zip(*[iter(Btn)]*3))
  #print(ak)
  #ak = list(chunk(Btn, 3))
  #[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13)]
  #await message.reply_text(text=ak)
  #await message.reply_text(text=LBRYOPEN_BUTTONS)
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
   
@Client.on_callback_query()
async def cb_data(bot, update):
  if update.data == "akhil":
    print("Done process")
      
    
  

  

