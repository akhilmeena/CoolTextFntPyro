import json
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup
import re

NewsPapers = InlineKeyboardButton('The Hindu', callback_data='thehindu')
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


NewspaperType = InlineKeyboardMarkup([
  [NewsPapers],
  [HomeToStart]
  ])


############## THE HINDU NEWSPAPER FUNCITON START ############## 

TheHindu30Result = []


async def gettingAllHinduresult(bot,update):
  c = 0
  url="https://dailyepaper.in/the-hindu-pdf-free-download-04-dec-2021/"
  response=requests.get(url)
  data = response.text
  htmlParse = BeautifulSoup(data, 'html.parser') 
  for para in htmlParse.find_all("p"): 
    if c <= 30:
      fullstring = f"{para}"
      substring = "https://vk.com/"
      if substring in fullstring:
        #akh = re.findall(r'(https?://[^\s]+)', fullstring)
        msg = await update.message.reply_text(fullstring)
        c+=1
        #print(para.text)
      else:
        pass
    else:
      break
    #print(akh)
    #['http://www.google.com', 'http://stackoverflow.com/questions/839994/extracting-a-url-in-python']
    
      #htmlParse = BeautifulSoup(data, 'html.parser') 



############## THE HINDU NEWSPAPER FUNCITON END ############## 