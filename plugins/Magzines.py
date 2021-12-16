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

async def getAllChahalMagzResult(bot,update,Lang):
  Source_List = []
  url = "https://chahalacademy.com/current-affairs-magazine"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  data = []
  for link in soup.find_all('a'):
    Header = link.text
    SedoUrl = link.get('href')
    if "Current Affairs Magazine" in Header and ".pdf" in SedoUrl:
      content = f"{Header.strip()} = {SedoUrl}"
      if str(Lang) == "Hindi":
        if str(Lang) in content:
          data.append(content)
        else:
          pass
      else:
        if str(Lang) in content:
          pass
        else:
          data.append(content)
  print(data)
  