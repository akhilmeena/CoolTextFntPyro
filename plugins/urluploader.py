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
  parent_dir = "Downloads/"
  path = os.path.join(parent_dir, directory) 
  #isExist = os.path.exists(path)
  #if not isExist:
  try:
    os.remove(path)
    os.mkdir(path)
  except:
    os.mkdir(path)
  file_name = url.split('/')[-1]
  file_path = os.path.join(path, file_name)
  response = requests.get(url)
  total_length = int(response.headers["Content-Length"])
  content_type = response.headers["Content-Type"]
  msg = await msg.edit(helper.DonloadFiletext.format(url,total_length,file_path,content_type),disable_web_page_preview=True)
  #start = time.time()
  #total = response.headers.get('content-length')
  #if total is None:
  thumb_image_path =  open("images.jpeg", 'rb')
  with open(file_path, 'wb') as f:
    f.write(response.content)
  with open(file_path, 'rb') as doc:
    await bot.send_document(
      chat_id=update.message.chat.id,
      file_name=file_name,
      document=doc,
      thumb=thumb_image_path,
      force_document=True,
      caption=f"{file_name}"
      )
  #prpgressmsg = bot.send_message(chat_Id,text="📥 Trying to Download...",parse_mode="HTML")
  
  
  