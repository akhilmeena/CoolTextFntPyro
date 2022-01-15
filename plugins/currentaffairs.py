import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
from bs4 import BeautifulSoup
import requests
import datetime
from itertools import islice

async def getdata(url):
  r = requests.get(url)
  return r.text

VisionIas = InlineKeyboardButton('✨ Vision IAS', callback_data='vsniascrnt')
ChahalAcdmy = InlineKeyboardButton('Chahal Academy 🥇', callback_data='chahalacdmy')
Add24x7 = InlineKeyboardButton('🌍 Add 24 × 7 🌍', callback_data='Add24x7')
BackToLibrary = InlineKeyboardButton('🔙', callback_data='libraryopen')

CRNTAFRSOURCEBTN = InlineKeyboardMarkup([
  [VisionIas,ChahalAcdmy],
  [Add24x7],
  [BackToLibrary]
  ])


async def getalldateswithlinkfromchahalacadmy(bot,update):
  url = "https://chahalacademy.com/daily-current-affairs-analysis"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  urls = []
  for link in soup.find_all('a'):
    SedoUrl = link.get('href')
    if "https://chahalacademy.com/daily-current-affairs/" in SedoUrl:
      urls.append(link.get('href'))
  Source_List = []
  for Url in urls:
    addDict = {}
    addList = ["indxchlacdmy"]
    date = Url.split("/")[4]
    code = Url.split("/")[5]
    Maindate = date.replace("-"," ")
    addDict["CallBtnTedt"] = str(Maindate)
    addList.append(str(date))
    addList.append(str(code))
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List
  



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
    incpltDatestrngwitoutdash = incpltDatestrng.replace("-"," ")
    addList = ["crnttodayvsnias"]
    addList.append(f"{getpdfcodehead}-{incpltDatestrng}")
    addDict["CallBtnTedt"] = str(incpltDatestrngwitoutdash)
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List
 

Add24x7_DataDict = {}
async def MonthlyCureentAffaisrsAdd247x7():
  #MainButtons = []
  #MainButtons.append([InlineKeyboardButton("❤️ Monthly Current Affairs ❤️", callback_data="Nothing")])
  #DwnldBtn = []
  #DwnldBtn.append([InlineKeyboardButton(f"{Month} {Year}", callback_data="Nothing")])
  #DwnldBtn.append([InlineKeyboardButton("📥English", callback_data="Eng")])
  #DwnldBtn.append([InlineKeyboardButton("📥English", callback_data="Eng")])
  #DwnldBtn.append([InlineKeyboardButton("📥हिंदी", callback_data="Hin")])
  htmldata = await getdata("https://www.bankersadda.com/monthly-current-affairs-pdf")
  soup = BeautifulSoup(htmldata, 'html.parser')
  for li in soup.find_all("tbody"):#, id="post")
    for para in li.find_all("td"):
      if "pdf" in f"{para}":
        AllLinks = {}
        AllLink = []
        Title = para.get_text().strip()
        TitleSplit = Title.split(" ")
        Month = TitleSplit[0][:3]
        Year = TitleSplit[4].replace(":","")#[-:]
        for a in para.find_all('a', href=True):
          Link = a['href']
          AllLink.append(Link)
        if len(AllLink) == 2:
          AllLinks["Eng"] = AllLink[0]
          AllLinks["हिंदी"] = AllLink[1]
        else:
          AllLinks["English"] = AllLink[0]
        Add24x7_DataDict[f"{Month} {Year}"] = AllLinks
  #print(Add24x7_DataDict)


async def MakeButtonFor27x7Add():
  ak = []
  x1 = InlineKeyboardButton("❤️ Monthly Current Affairs ❤️", callback_data="Nothing")
  ak.append([x1])
  for Title in Add24x7_DataDict:
    Btn = []
    #for d in Source_List:
    #print(d)
    #CallbackText = d['CallBtnTedt']
    #CallbackData = d['CallBtnData']
    MonthButton = InlineKeyboardButton(f"🗂️ {Title}",callback_data=Title)
    Btn.append(MonthButton)
    DataInsideMonth = Add24x7_DataDict[Title]
    for Lan in DataInsideMonth:
      LanBtn = InlineKeyboardButton(f"📥 {Lan}",callback_data=Lan)
      Btn.append(LanBtn)
    ak.append(Btn)
  #ak = [Btn[i:i+2] for i in range(0, len(Btn)-1, 2)]
  x = InlineKeyboardButton("🔙",callback_data="crnafrsdaily")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns
  #print(Title)
















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
   

  
      
    
  

  

