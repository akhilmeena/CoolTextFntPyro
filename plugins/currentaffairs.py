import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from bs4 import BeautifulSoup
import requests
import datetime
from itertools import islice


VisionIas = InlineKeyboardButton('✨ Vision IAS', callback_data='vsniascrnt')
BackToLibrary = InlineKeyboardButton('🔙', callback_data='libraryopen')

CRNTAFRSOURCEBTN = InlineKeyboardMarkup([
  [VisionIas],
  [BackToLibrary]
  ])

def getallmonthfromiasvsncurrentafr(bot,update):
  url = "http://www.visionias.in/resources/daily_current_affairs.php?type=1"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  urls = []
  for link in soup.find_all('a'):
    urls.append(link.get('href'))
  urls = urls[:-1]
  Source_List = []
  for Url in urls:
    addDict = {}
    addList = ["getcurrentofmonth"]
    monthstring = Url.split("&")[1]
    month_num = monthstring.split("=")[1]
    full_month_name = getMonthnamefromnu(month_num)
    yearstring = Url.split("&")[2]
    YearFull = yearstring.split("=")[1]
    MonthNamewithYer = f"{full_month_name} {YearFull}"
    addDict["CallBtnTedt"] = str(MonthNamewithYer)
    addList.append(str(month_num))
    addList.append(str(YearFull))
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  #BackDict = {}
  #BackDict["CallBtnTedt"] = "🔙"
  #BackDict["CallBtnData"] = "crnafrsdaily"
  #Source_List.append(BackDict)
  return Source_List
  
  




def makeBtnFromDict(Source_List):
  print("ak")
  Btn = []
  for d in Source_List:
    print(d)
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn)-1, 3)]
  x = InlineKeyboardButton("🔙",callback_data="crnafrsdaily")
  am.append(x)
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns

def getMonthnamefromnu(month_num):
  datetime_object = datetime.datetime.strptime(str(month_num), "%m")
  full_month_name = datetime_object.strftime("%B")
  return full_month_name
  













Source_Dict1 = [
  {"Name":"✨ Vision IAS","CallBack":"vsniascrnt"},
  {"Name":"test","CallBack":"test"}
  ]

@Client.on_message(filters.command('btn') & filters.private)
async def start(bot, message):
  Btn = []
  for i in range(10):
    x = InlineKeyboardButton(str(i),callback_data="akhil")
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  START_BUTTONS = InlineKeyboardMarkup(ak)
  await message.reply_text(text=START_BUTTONS,reply_markup=START_BUTTONS)
   

  
      
    
  

  

