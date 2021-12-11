import json
import pyrogram
from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
import html2markdown
        

NewsPapers = InlineKeyboardButton('The Hindu', callback_data='thehindu')
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


NewspaperType = InlineKeyboardMarkup([
  [NewsPapers],
  [HomeToStart]
  ])


############## Notification For Copyrighted ############## 
TheHinduNotification = """<b>Important Notice</b>

This e-paper is shared only for the educational purposes & We suggest you please Don't Download From Here just go to The Hindu Official Website and buy The Hindu Paid Version and support the publisher.
We are not the publisher or owner of this e-paper.

Have any complaints just write us."""
############## News Paper Code Head ############## 
NewsCodeHead = {
  "thehindu" : "THE HINDU"
}
############## THE HINDU NEWSPAPER FUNCITON START ############## 
TheHindu30Resultfinal = {}


async def gettingAllHinduresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/the-hindu-pdf-free-download-04-dec-2021/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  TheHindu30Result = []
  for para in htmlParse.find_all("p"): 
    btn = []
    tempdict = {}
    if c <= 30:
      fullstring = f"{para}"
      substring = "https://vk.com/"
      if substring in fullstring:
        items = para.text
        itmelist = items.split(":")
        linklist = re.findall(r'(https?://[^\s]+)', fullstring)
        addDict = {}
        addList = ["dwnldnewspaper"]
        addDict["CallBtnTedt"] = str(f"📆 {itmelist[0]}")
        addList.append(str(str(c+1)))
        addList.append("thehindu")
        addDict["CallBtnData"] = f"{addList}"
        #print(addList)
        Source_List.append(addDict)
        try:
          tempdict["Date"] = f"{itmelist[0]}"
        except:
          tempdict["Date"] = f"_"
        try:
          tempdict["NP"] = f"{linklist[0]}"
        except:
          tempdict["NP"] = f"_"
        try:
          tempdict["AL"] = f"{linklist[1]}"
        except:
          tempdict["AL"] = f"_"
        c+=1
      else:
        pass
    else:
      break
    TheHindu30Resultfinal[c] = tempdict
  return Source_List

async def makeBtnFromDict(Source_List):
  Btn = []
  for d in Source_List:
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    print(CallbackText)
    print(CallbackData)
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+2] for i in range(0, len(Btn), 2)]
  x = InlineKeyboardButton("🔙",callback_data="libraryopen")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns


async def captionfornewslink(Id,Forwhat):
  Textfornewspaperwithanylss1 = """Here is your Result:
🎟️ {}
📆 Date : {}
📥 <a href='{}'>NewsPaper</a>
📥 <a href='{}'>Analysis</a>
"""
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],TheHindu30Resultfinal[int(Id)]["Date"],TheHindu30Resultfinal[int(Id)]["NP"],TheHindu30Resultfinal[int(Id)]["AL"])
  return Textfornewspaperwithanylss


###############EXTRA#####################







async def gettingAllHinduresult1(bot,update):
  c = 0
  url="https://dailyepaper.in/the-hindu-pdf-free-download-04-dec-2021/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  TheHindu30Result = []
  for para in htmlParse.find_all("p"): 
    btn = []
    tempdict = {}
    if c <= 30:
      fullstring = f"{para}"
      substring = "https://vk.com/"
      if substring in fullstring:
        items = para.text
        itmelist = items.split(":")
        linklist = re.findall(r'(https?://[^\s]+)', fullstring)
        datebtn = InlineKeyboardButton(f"📆 {itmelist[0]}", callback_data="nothing")
        try:
          dwnldbtn = InlineKeyboardButton(f"📥 {itmelist[1]}", callback_data="['dwnldnewspaper','NP','" + str(c+1) + "']")
        except:
          dwnldbtn = InlineKeyboardButton(f"N/A", callback_data="['dwnldnewspaper','NP','" + str(c+1) + "']")
        try:
          anylsisbtn = InlineKeyboardButton(f"📄 {itmelist[2]}", callback_data="['dwnldnewspaper','AL','" + str(c+1) + "']")
        except:
          anylsisbtn = InlineKeyboardButton(f"N/A", callback_data="['dwnldnewspaper','AL','" + str(c+1) + "']")
        btn.append(datebtn)
        #btn.append(dwnldbtn)
        #btn.append(anylsisbtn)
        try:
          tempdict["NP"] = f"{linklist[0]}"
        except:
          tempdict["NP"] = f"_"
        try:
          tempdict["AL"] = f"{linklist[1]}"
        except:
          tempdict["AL"] = f"_"
        c+=1
      else:
        pass
    else:
      break
    TheHindu30Result.append(btn)
    TheHindu30Resultfinal[c] = tempdict
  ak = [TheHindu30Result[i:i+2] for i in range(0, len(TheHindu30Result), 2)]
  HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')
  #TheHindu30Result.append([HomeToStart])
  ak.append([HomeToStart])
  NewpaperBtn = InlineKeyboardMarkup(ak)
  return NewpaperBtn


async def geturlfornewpaper(Id,Ctgry):
  Url = TheHindu30Resultfinal[int(Id)][Ctgry]
  print(Url)
  return Url
############## THE HINDU NEWSPAPER FUNCITON END ############## 

#Textfornewspaperwithanylss = """Here is your Result:
#📆 Date : {}
#📥 <h href='{}'>NewsPaper</a>
#📥 <h href='{}'>Analysis</a> 
#""".format(TheHindu30Resultfinal["Date"],TheHindu30Resultfinal["NP"],TheHindu30Resultfinal["AL"])


