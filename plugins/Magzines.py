import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ChlacdmycrntafrmagzineHindi = InlineKeyboardButton('Chahal (Hindi)', callback_data="['Chlacdmycrntafrmagzine','Hindi']")
ChlacdmycrntafrmagzineEnglish = InlineKeyboardButton('Chahal (English)', callback_data="['Chlacdmycrntafrmagzine','English']")
YoznaMagzineHindi = InlineKeyboardButton('Yojana (Hindi)', callback_data="['YoznaMagzine','Hindi']")
YoznaMagzineEnglish = InlineKeyboardButton('Yojana (English)', callback_data="['YoznaMagzine','English']")
KurukshetraMagzineHindi = InlineKeyboardButton('Kurukshetra (Hindi)', callback_data="['KurukshetraMagzine','Hindi']")
KurukshetraMagzineEnglish = InlineKeyboardButton('Kurukshetra (English)', callback_data="['KurukshetraMagzine','English']")
#"['KurukshetraMagzine','Hindi']"
#"['KurukshetraMagzine','English']"
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


MagzinesType = InlineKeyboardMarkup([
  [ChlacdmycrntafrmagzineEnglish,ChlacdmycrntafrmagzineHindi],
  [YoznaMagzineEnglish,YoznaMagzineHindi],
  [KurukshetraMagzineEnglish,KurukshetraMagzineHindi],
  [HomeToStart]
  ])
  
############## CHAHAL ACADEMY ############## 
AllChahalMagzResult = {}

async def getAllChahalMagzResult(bot,update,Data):
  #print(Data)
  Source_List = []
  tempdict = {}
  c = 0
  for i in Data:
    MagzineTitle = i.split(" = ")[0]
    Link = i.split(" = ")[1]
    print(Link)
    Lang = i.split(" = ")[2]
    words = MagzineTitle.split()[:2]
    MonthName =" ".join(words)
    addDict = {}
    addList = ["dwnldmagz"]
    addDict["CallBtnTedt"] = str(f"📆 {MonthName}")
    addList.append(str(str(c+1)))
    addList.append("chahal")
    addDict["CallBtnData"] = f"{addList}"
    #print(addList)
    Source_List.append(addDict)
    tempdict["Month"] = f"{MonthName}"
    tempdict["LinkMagzine"] = f"{Link}"
    tempdict["Lang"] = f"{Lang}"
    c+=1
    AllChahalMagzResult[c] = tempdict
  return Source_List

async def getDataChahalMagzResult(bot,update,Lang):
  url = "https://chahalacademy.com/current-affairs-magazine"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  Data=[]
  Lang= "English"
  if str(Lang) == "Hindi":
    for link in soup.find_all('a'):
      Header = link.text.strip().split("\r")[0]
      SedoUrl = link.get('href')
      if "Current Affairs Magazine" in Header and ".pdf" in SedoUrl:
        content =  f"{Header} = {SedoUrl}"
        if str(Lang) in content:
          Data.append(f"{content} = {Lang}")
        else:
            pass
  else:
    for link in soup.find_all('a'):
      Header = link.text.strip().split("\r")[0]
      SedoUrl = link.get('href')
      if "Current Affairs Magazine" in Header and ".pdf" in SedoUrl:
        content =  f"{Header} = {SedoUrl}"
        if "Hindi" in content:
          pass
        else:
          Data.append(f"{content} = {Lang}")
  return Data
  
async def GetLinkDateLang(Id,MagziCompany):
  if str(MagziCompany) == "chahal":
    MainData = AllChahalMagzResult
  Month = MainData[int(Id)]["Month"]
  LinkMagzine = MainData[int(Id)]["LinkMagzine"]
  Lang = MainData[int(Id)]["Lang"]
  return Month,LinkMagzine,Lang
  
async def makeBtnFromDict(Source_List):
  Btn = []
  for d in Source_List:
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    #print(CallbackText)
    #print(CallbackData)
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+2] for i in range(0, len(Btn), 2)]
  x = InlineKeyboardButton("🔙",callback_data="libraryopen")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns
  