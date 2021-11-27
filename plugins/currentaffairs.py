import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())




Btn = []
finalbtn = []

@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  for i in range(10):
    x = InlineKeyboardButton(i,callback_data=i)
    Btn.append(x)
  ak = list(list(t) for t in zip(*[iter(Btn)]*3))
  #print(ak)
  #ak = list(chunk(Btn, 3))
  #[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13)]
  LBRYOPEN_BUTTONS = InlineKeyboardMarkup([ak])
  await message.reply_text(text=LBRYOPEN_BUTTONS,reply_markup=LBRYOPEN_BUTTONS)
  #await message.reply_text(text="akh",reply_markup=LBRYOPEN_BUTTONS)
  

      
    
  

  

