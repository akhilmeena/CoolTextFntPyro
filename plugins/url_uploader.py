from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from plugins.download_from_url import download_file, get_size

download_path = "Downloads/"
 
async def leecher2(bot , update,url):
  sw = "direct"
  directory = f"{update.chat.id}"
  mainpath = os.path.join(download_path, directory) 
  os.mkdir(path)
  file_name = url.split('/')[-1]
  file_path = os.path.join(mainpath, file_name)
  filename = filename.replace('%25','_')
  filename = filename.replace(' ','_')
  filename = filename.replace('%40','@')
  start = time.time()
  #try:
    #msg ka pangaa h yhaa pr
    #file_path = await download_file(url, filename, msg, start, bot)
    #print(f"file downloaded to {file_path} with name: {filename}")

  #m = u.reply_to_message