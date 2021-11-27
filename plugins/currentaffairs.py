import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from itertools import islice


VisionIas = InlineKeyboardButton('✨ Vision IAS', callback_data='vsniascrnt')
BackToLibrary = InlineKeyboardButton('🔙', callback_data='libraryopen')

CRNTAFRSOURCEBTN = InlineKeyboardMarkup([
  [VisionIas],
  [BackToLibrary]
  ])

def getallmonthfromiasvsncurrentafr():
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
    Dict["CallBtnTedt"] = str(MonthNamewithYer)
    addList.append(str(month_num))
    addList.append(str(YearFull))
    Dict["CallBtnData"] = f"{addList}"
  return Source_List
  #Source_List = {}
  




def makeBtnFromDict(Source_List):
  Btn = []
  for d in Source_Dict:
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+3] for i in range(0, len(Btn), 3)]
  newbtns = InlineKeyboardMarkup(ak)
  #newbtns.add(BackToLibrary)
  return newbtns







Source_Dict = [
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
   

  
      
    
  

  

