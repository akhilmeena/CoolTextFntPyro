import re 
import logging
import os
from config import Config
import pyrogram
from plugins import helper
import requests
from pyrogram import Client, filters
from plugins.display_progress import progress_for_pyrogram,get_size,TimeFormatter
import time

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
  isExist = os.path.exists(path)
  if not isExist:
    os.mkdir(path)
  else:
    pass
  file_name = url.split('/')[-1]
  file_path = os.path.join(path, file_name)
  response = requests.get(url)
  total_length = int(response.headers["Content-Length"])
  content_type = response.headers["Content-Type"]
  msg = await msg.edit(helper.DonloadFiletext.format(url,file_path,total_length,content_type),disable_web_page_preview=True)
  start = time.time()
  total = total_length
  #total = response.headers.get('content-length'])
  #if total is None:
  try:
    thumb_image_path =  open(Config.LoGoPath, 'rb')
    CHUNK_SIZE = 1024*6 # 2341
    downloaded = 0
    #display_message = ""
    humanbytes = get_size
    with open(file_path, 'wb') as f:
      if total_length is None:
        f.write(response.content)
      else:
        print("akhil")
        downloaded = 0
        total = int(total_length)
        #for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
        for data in response.iter_content(chunk_size=CHUNK_SIZE):
          downloaded += len(data)
          f.write(data)
          done = int(25*downloaded/total)
          now = time.time()
          diff = now - start
          elapsed_time = round(diff) * 1000
          progressBar = '[{}{}]'.format('●' * done, '○' * (25-done))
          totalInMb = round(total/1024/1024,2)
          downloadedInMb = round(downloaded/1024/1024,2)
          speed = downloaded / diff
          speedInMb = round(downloadedInMb / diff,2)
          time_to_completion = (round((total - downloaded) / speed) * 1000)
        #time_to_completion = (round((total - downloaded) / speed) * 1000)
        #estimated_total_time = (elapsed_time + time_to_completion)/1000
          progressText = '''<b>File is Downloading ⌛
 
🗂️ File Name :</b> <code>{}</code>
<b>📥 Download Progess :</b> <code>{}</code>/<code>{}</code>
<b>⚡ Speed :</b> <code>{}</code> Mbps
<b>🕛 Est :</b> <code>{}</code>
{}'''
          progstext = progressText.format(file_name,downloadedInMb,totalInMb,speedInMb,TimeFormatter(milliseconds=time_to_completion),progressBar)
          await msg.edit(progstext)
      #f.write(response.content)
    os.rename(file_path,os.path.join(path,f"{Config.Bot_Username} {file_name}"))
    newfilename = f"@LibraryInBot {file_name}"
    newfile_path = os.path.join(path, newfilename)
    with open(newfile_path, 'rb') as doc:
      c_time = time.time()
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=doc,
        file_name=newfilename,
        thumb=thumb_image_path,
        force_document=True,
        caption=f"{file_name}",
        progress=progress_for_pyrogram,
        progress_args=(
          "Uploading Document",
          msg, 
          c_time
          )
        )
    os.remove(newfile_path)
  except Exception as e:
    msg = await msg.edit("Exit with error : {}".format(e))
  #prpgressmsg = bot.send_message(chat_Id,text="📥 Trying to Download...",parse_mode="HTML")
  
  
  