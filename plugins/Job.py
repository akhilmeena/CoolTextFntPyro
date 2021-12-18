import json
import pyrogram
from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re


Result = InlineKeyboardButton('Results', callback_data='sarakriresult')
Admitcards = InlineKeyboardButton('Admit card', callback_data='sarakariadmitcards')
Latestjobs = InlineKeyboardButton('Latest Jobs', callback_data='jobalert')
HomeToLib = InlineKeyboardButton('🔙', callback_data='libraryopen')

JOB_BUTTONS = InlineKeyboardMarkup([
  [Result,Admitcards],
  [HomeToLib],
  ])
ADMITCARD_BUTTONS = InlineKeyboardMarkup([
  [Result,Latestjobs],
  [HomeToLib],
  ])
RESULT_BUTTONS = InlineKeyboardMarkup([
  [Admitcards,Latestjobs],
  [HomeToLib],
  ])
  
async def getdata(url):
  r = requests.get(url)
  return r.text
  
async def GetAllLatestJobs():
  PaeatoPost = """\n\n<b>{}. 🎯<i>{}</i></b>
<b>📅 Last Date : </b><code>{}</code>
<a href="{}">🔗 More Details</a>"""
  res = ''
  htmldata = await getdata("https://www.sarkariresult.com/latestjob.php")
  soup = BeautifulSoup(htmldata, 'html.parser')
  c = 0
  for li in soup.find_all("div", id="post"):#, id="post"):
    for para in li.find_all("li"):
      if c <=14:
        for a in para.find_all('a', href=True):
          Link = a['href']
        Text = para.get_text()
        Title = Text.split("Last Date :")[0]
        Last_Date = Text.split("Last Date :")[1]
        res += PaeatoPost.format(c+1,Title,Last_Date,Link)
        #res += f"{c+1}. Post : {Title}\nLast Date : {Last_Date}\nFull Details : {Link}\n\n"
        c+=1
      else:
        break
  return res