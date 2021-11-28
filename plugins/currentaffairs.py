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
    addList = ["getcurrentofmonthvsnias"]
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
  ak = [Btn[i:i+2] for i in range(0, len(Btn)-1, 2)]
  x = InlineKeyboardButton("🔙",callback_data="crnafrsdaily")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns

def getMonthnamefromnu(month_num):
  datetime_object = datetime.datetime.strptime(str(month_num), "%m")
  full_month_name = datetime_object.strftime("%B")
  return full_month_name
  
def currentdaypdfbuttonvsnias(month_num,year_num):
  url = "http://www.visionias.in/resources/daily_current_affairs_programs.php?type=1&m={}&y={}".format(month_num,year_num)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  urls = []
  for link in soup.find_all('a'):
    urls.append(link.get('href'))
  Source_List = []
  for Url in urls:
    addDict = {}
    incpltDatestrng2 = Url.split("/")[5]
    getpdfcodehead = incpltDatestrng2[0:5]
    incpltDatestrng1 = incpltDatestrng2.replace(f"{getpdfcodehead}-","")
    incpltDatestrng = incpltDatestrng1.replace(".pdf","")
    addList = ["crnttodayvsnias"]
    addList.append(f"{getpdfcodehead}-{incpltDatestrng}")
    #addList.append(str(incpltDatestrng))
    addDict["CallBtnTedt"] = str(incpltDatestrng)
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List
 



















############# EXTRA ############# 

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
  await message.reply_text(text=ak,reply_markup=START_BUTTONS)
   

  
      
    
  

  

