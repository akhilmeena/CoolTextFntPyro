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

@Client.on_message(filters.command('btnu') & filters.private)
async def startu(bot, message):
  print("1")
  OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
  HelpBtn = InlineKeyboardButton('🆘 Help', callback_data='help')
  AboutDev = InlineKeyboardButton('About Dev ❤️', callback_data='abtdvlngbot')
  UpdateOfBot = InlineKeyboardButton('🚀 Update ', url='https://telegram.dog/channelanalyser/')
  SupportPfBot = InlineKeyboardButton(' Support 💌', url='https://telegram.dog/channelanalyser/')
  #print(SupportPfBot)
  ak = [[OpenLibeary],[HelpBtn,AboutDev],[UpdateOfBot,SupportPfBot]]
  #await message.reply_text(text=ak)
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
  
@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  for i in range(10):
    x = InlineKeyboardButton(i,callback_data=i)
    Btn.append(x)
  ak = list(list(t) for t in zip(*[iter(Btn)]*3))
  #print(ak)
  #ak = list(chunk(Btn, 3))
  #[(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13)]
  #await message.reply_text(text=ak)
  #await message.reply_text(text=LBRYOPEN_BUTTONS)
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
   

      
    
  

  

