import json
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup
import re
import html2markdown
        

NewsPapers = InlineKeyboardButton('The Hindu', callback_data='thehindu')
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


NewspaperType = InlineKeyboardMarkup([
  [NewsPapers],
  [HomeToStart]
  ])


############## THE HINDU NEWSPAPER FUNCITON START ############## 

TheHindu30Resultfinal = {}

async def gettingAllHinduresult(bot,update):
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
        btn.append(dwnldbtn)
        btn.append(anylsisbtn)
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
  HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')
  TheHindu30Result.append([HomeToStart])
  NewpaperBtn = InlineKeyboardMarkup(TheHindu30Result)
  return NewpaperBtn


async geturlfornewpaper(Id,Ctgry):
  Url = TheHindu30Resultfinal[int(Id)][Ctgry]
  print(Url)
  return Url
############## THE HINDU NEWSPAPER FUNCITON END ############## 