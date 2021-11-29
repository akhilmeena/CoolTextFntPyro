import re 
import logging
import os
from config import Config
import pyrogram
from plugins import helper
import requests
from pyrogram import Client, filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



async def Find(string): 
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex,string)       
  return [x[0] for x in url] 

async def Urlleaccher(bot,update,Url2Dowload):
  msg = await update.message.reply_text("Validating Url...")
  try:
    Url = await Find(Url2Dowload)
    url = Url[0]
  except:
    msg = await update.message.reply_text("Couldn't Found Url in Given Text...")
    return
  msg = await msg.edit("Url Matched : {}".format(url),disable_web_page_preview=True)
  directory = f"{update.message.chat.id}"
  print(directory)
  parent_dir = "DownloadPdf/"
  path = os.path.join(parent_dir, directory) 
  #isExist = os.path.exists(path)
  #if not isExist:
  try:
    os.remove(path)
    os.mkdir(path)
  except:
    os.mkdir(path)
  msg = await msg.edit("Url Matched : {}".format(url),disable_web_page_preview=True)
  file_name = url.split('/')[-1]
  file_path = os.path.join(path, file_name)
  response = requests.get(urlforpdf)
  total_length = int(response.headers["Content-Length"])
  content_type = response.headers["Content-Type"]
  msg = await msg.edit(helper.DonloadFiletext.format(url,total_length,file_path,content_type),disable_web_page_preview=True)
  
  #prpgressmsg = bot.send_message(chat_Id,text="📥 Trying to Download...",parse_mode="HTML")
  
  
  