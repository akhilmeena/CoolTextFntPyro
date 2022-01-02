import json
import pyrogram
from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
import html2markdown
        

TheHinduu = InlineKeyboardButton('The Hindu', callback_data='thehindu')
TmsOfInd = InlineKeyboardButton('Times Of India', callback_data='timesofindia')
FinancialExpress = InlineKeyboardButton('Financial Express', callback_data='financialexpress')
EconomicTimes = InlineKeyboardButton('Economic Times', callback_data='economictimes')
Dainikjagaran = InlineKeyboardButton("दैनिक जागरण", callback_data='dainikjagaran')
Rjpatrika = InlineKeyboardButton('राजस्थान पत्रिका', callback_data='rjpatrika')
Dainikbhaskar = InlineKeyboardButton('दैनिक भास्कर', callback_data='dainikbhaskar')
Newduniyaa = InlineKeyboardButton('नयी दुनिया', callback_data='newduniyaa')
Navbharattimes = InlineKeyboardButton('नवभारतटाइम्स', callback_data='navbharattimes')
Amarujala = InlineKeyboardButton('अमर उजाला', callback_data='amarujala')
RequestNewsPaper = InlineKeyboardButton('💌 Request NewsPaper', callback_data='requestnewspaper')
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


NewspaperType = InlineKeyboardMarkup([
  [TheHinduu,TmsOfInd],
  [FinancialExpress,EconomicTimes],
  [Dainikjagaran,Rjpatrika],
  [Dainikbhaskar,Newduniyaa],
  [Navbharattimes,Amarujala],
  [RequestNewsPaper],
  [HomeToStart]
  ])


DisclaimerForAll = """
<b>⚠️ Note:-</b> <i>This pdf is shared only for educational purposes. We are not the publisher or owner of this e-paper.
Have any complaints Please write us.</i>
"""

Textfornewspaperwithanylss1 = """<b>Here is your Result:

🎟️ {}
📆 Date :</b><code> {}</code>
📥 <a href='{}'>NewsPaper</a>
"""
############## Notification For Copyrighted ############## 
TheHinduNotification = """We suggest you please Don't Download From Here just go to The Hindu Official Website and buy The Hindu Paid Version and support the publisher."""
TimesOfIndiaNotification = """We suggest you please Don't Download From Here just go to The Times Of India Official Website and buy The T.O.I Paid Version and support the publisher."""
FinancialExpressNotification = """We suggest you please Don't Download From Here just go to The Financial Express Official Website and buy The Financial Express Paid Version and support the publisher."""
EconomicTimesNotification = """We suggest you please Don't Download From Here just go to Economic Times Official Website and buy Economic Times Paid Version and support the publisher."""
DainikJagranNotification = """We suggest you please Don't Download From Here just go to The Dianik Jagran Official Website and buy The Dainik Jagran Paid Version and support the publisher."""
RjpatrikaNotification = """We suggest you please Don't Download From Here just go to Rajsthan Patrika Official Website and buy Rajsthan Patrika Paid Version and support the publisher."""
DainikbhaskarNotification = """We suggest you please Don't Download From Here just go to Dainik Bhaskar Official Website and buy Dainik Bhaskar Paid Version and support the publisher."""
NewduniyaaNotification = """We suggest you please Don't Download From Here just go to Nayi Duniya Official Website and buy Nayi Duniya Paid Version and support the publisher."""
NavbharattimesNotification = """We suggest you please Don't Download From Here just go to Nav-Bharat Times Official Website and buy Nav-Bharat Times Paid Version and support the publisher."""
AmarujalaNotification = """We suggest you please Don't Download From Here just go to Amar Ujala Official Website and buy Amar Ujala Paid Version and support the publisher."""
############## News Paper Code Head ############## 
NewsCodeHead = {
  "thehindu" : "THE HINDU",
  "timesofindia" : "TIMES OF INDIA",
  "financialexpress" : "Financial Express",
  "economictimes" : "Economic Times",
  "dainikjagaran" : "दैनिक जागरण",
  "rjpatrika" : "राजस्थान पत्रिका",
  "dainikbhaskar" : "दैनिक भास्कर",
  "newduniyaa" : "नयी दुनिया",
  "navbharattimes" : "नवभारतटाइम्स",
  "amarujala" : "अमर उजाला"
}
############## BUTTONS FROM SOURCE CODE ############## 
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
############## THE HINDU NEWSPAPER FUNCITON START ############## 
TheHindu30Resultfinal = {}

async def gettingAllHinduresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/the-hindu-pdf-free-download-19-dec-2021/"
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

async def captionfornewslink(Id,Forwhat):
  Textfornewspaperwithanylss2 = """<b>Here is your Result:

🎟️ {}
📆 Date :</b><code> {}</code>
📥 <a href='{}'>NewsPaper</a>
📥 <a href='{}'>Analysis</a>
"""
  Textfornewspaperwithanylss = Textfornewspaperwithanylss2.format(NewsCodeHead[str(Forwhat)],TheHindu30Resultfinal[int(Id)]["Date"],TheHindu30Resultfinal[int(Id)]["NP"],TheHindu30Resultfinal[int(Id)]["AL"])
  return Textfornewspaperwithanylss
 
###############TIMES OF INDIA#####################

TheTOI30Resultfinal = {}

async def gettingallTOIresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/times-of-india-epaper-pdf-download-2021/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("timesofindia")
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
        c+=1
      else:
        pass
    else:
      break
    TheTOI30Resultfinal[c] = tempdict
  return Source_List

async def captionfornewslink1(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],TheTOI30Resultfinal[int(Id)]["Date"],TheTOI30Resultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss


##############FINANCIAL EXPRESS#####################

FinancialExpressResultfinal = {}

async def gettingallFinancialExpressresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/financial-express-newspaper/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("financialexpress")
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
        c+=1
      else:
        pass
    else:
      break
    FinancialExpressResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkfinancialexpress(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],FinancialExpressResultfinal[int(Id)]["Date"],FinancialExpressResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss

##############Economic Times#####################

EconomictimesResultfinal = {}

async def gettingallEconomictimesresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/economic-times-newspaper-today/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("economictimes")
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
        c+=1
      else:
        pass
    else:
      break
    EconomictimesResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkEconomictimes(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],EconomictimesResultfinal[int(Id)]["Date"],EconomictimesResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss
###############DAINKK JAGARAN#####################

DainikJagranResultfinal = {}

async def gettingallDainikJagranresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/dainik-jagran-newspaper-2021/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("dainikjagaran")
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
        c+=1
      else:
        pass
    else:
      break
    DainikJagranResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkdainikjagaran(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],DainikJagranResultfinal[int(Id)]["Date"],DainikJagranResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss

###############RAJSHTHAN PATRIKA#####################

RjpatrikaResultfinal = {}

async def gettingallRjpatrikaresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/rajasthan-patrika-epaper/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("rjpatrika")
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
        c+=1
      else:
        pass
    else:
      break
    RjpatrikaResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkRjpatrika(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],RjpatrikaResultfinal[int(Id)]["Date"],RjpatrikaResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss


###############Dainik Bhaskar#####################

DainikbhaskarResultfinal = {}

async def gettingallDainikbhaskarresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/dainik-bhaskar-epaper/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("dainikbhaskar")
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
        c+=1
      else:
        pass
    else:
      break
    DainikbhaskarResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkDainikbhaskar(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],DainikbhaskarResultfinal[int(Id)]["Date"],DainikbhaskarResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss

###############New Duniyaa#####################

NewduniyaaResultfinal = {}

async def gettingallNewduniyaaresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/naidunia-newspaper/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("newduniyaa")
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
        c+=1
      else:
        pass
    else:
      break
    NewduniyaaResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkNewduniyaa(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],NewduniyaaResultfinal[int(Id)]["Date"],NewduniyaaResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss

###############Nav Bharat Times#####################

NavbharattimesResultfinal = {}

async def gettingallNavbharattimesresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/navbharat-times-epaper/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("navbharattimes")
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
        c+=1
      else:
        pass
    else:
      break
    NavbharattimesResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkNavbharattimes(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],NavbharattimesResultfinal[int(Id)]["Date"],NavbharattimesResultfinal[int(Id)]["NP"])
  return Textfornewspaperwithanylss


###############Amar Ujala#####################

AmarujalaResultfinal = {}

async def gettingallAmarujalaresult(bot,update):
  Source_List = []
  c = 0
  url="https://dailyepaper.in/amar-ujala-news-paper-today/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
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
        addList.append("amarujala")
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
        c+=1
      else:
        pass
    else:
      break
    AmarujalaResultfinal[c] = tempdict
  return Source_List

async def captionfornewslinkAmarujala(Id,Forwhat):
  Textfornewspaperwithanylss = Textfornewspaperwithanylss1.format(NewsCodeHead[str(Forwhat)],AmarujalaResultfinal[int(Id)]["Date"],AmarujalaResultfinal[int(Id)]["NP"])
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



