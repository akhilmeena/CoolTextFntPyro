from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from pyromod import listen
from urllib.parse import quote_plus, unquote
import math
import os
import time
import datetime
import aiohttp
import asyncio
import mimetypes
import gdown
from plugins.download_from_url import download_file, get_size
from plugins.ffprobe import stream_creator
from plugins.thumbnail_video import thumb_creator
from plugins.display_progress import progress_for_pyrogram, humanbytes
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from plugins.tools import execute
from plugins.file_handler import send_to_transfersh_async, progress

download_path = "Downloads/"
 
#async def leecher2(bot , update,Url):
async def leecher2(bot , update,Url):
  sw = "direct"
  
  directory = f"{update.chat.id}"
  mainpath = os.path.join(download_path, directory) 
  try:
    os.mkdir(mainpath)
  except:
    pass
  if "|" in Url:
    url , cfname = Url.split("|", 1)
    url = url.strip()
    cfname = cfname.strip()
    cfname = cfname.replace('%40','@')
  else:
    url = Url.strip()
    if os.path.splitext(url)[1]:
      ofn = os.path.basename(url)
    else:
      try:
        await update.reply_text(text=f"I Could not Determine The FileType !\nPlease Use Custom Filename With Extension\nSee /help", quote=True)
      except:
        await update.message.reply_text(text=f"I Could not Determine The FileType !\nPlease Use Custom Filename With Extension\nSee /help", quote=True)
      return
  try:
    msg = await update.reply_text(text=f"`Analyzing Your Link ...`", quote=True)
  except:
    msg = await update.message.reply_text(text=f"`Analyzing Your Link ...`", quote=True)
  file_path = os.path.join(mainpath, os.path.basename(url))
  filename = os.path.join(mainpath, os.path.basename(url))
  filename3 = url.split('/')[-1]
  filename2 = filename3.replace('%25','_')
  filename1 = filename2.replace(' ','_')
  #filename = filename1.replace('%40','@')
  start = time.time()
  try:
    file_path = await download_file(url, filename, msg, start, bot)
    print(f"file downloaded to {file_path} with name: {filename}")
  except Exception as e:
    if 'drive.google.com' in url:
      await msg.edit(f"Google Drive Link Detected !\n\n`Downloading ...`\n\n**Please Wait.**")
      sw = "gd"
    else:
      print(e)
      await msg.edit(f"Download Link is Invalid or not Accessible !\n\n**Error:** {e}")
      return
  if sw == "gd":
    file_path = os.path.join(mainpath, cfname)
    if 'uc?id' in url:
      gdown.download(url, file_path, quiet=False)
    elif '/file/d/' in url:
      url2 = url.split("/file/d/", 1)[1]
      gid = url2.split("/", 1)[0]
      url = "https://drive.google.com/u/0/uc?id=" + str(gid) + "&export=download"
      gdown.download(url, file_path, quiet=False)
    else:
      await msg.edit(f"❌ Gdrive Link is Invalid ! \n\n **Error:** {e}")
      return
  await msg.edit(f"✅ **Successfully Downloaded**")
  filename = os.path.basename(file_path)
  filename = filename.replace('%40','@')
  filename = filename.replace('%25','_')
  filename = filename.replace(' ','_')
  mt = mimetypes.guess_type(str(file_path))[0]
  if mt and mt.startswith("video/"):
    fsw = "vid"
  elif mt and mt.startswith("audio/"):
    fsw = "aud"
  else:
    fsw = "app"
  if "|" in Url:
    filename = cfname
    cfnmt = mimetypes.guess_type(str(cfname))[0]
    if cfnmt and cfnmt.startswith("video/"):
      fsw = "vid"
    elif cfname and cfnmt.startswith("audio/"):
      fsw = "aud"
    else:
      fsw = "app"
  #size_of_file = os.path.getsize(file_path)
  #size = get_size(size_of_file)
  size = "akhil"
  if fsw == "vid":
    try:
      probe = await stream_creator(file_path)
      video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
      width = int(video_stream['width'] if 'width' in video_stream else 0)
      height = int(video_stream['height'] if 'height' in video_stream else 0)
      duration = int(float(probe["format"]["duration"]))
      await msg.edit(f"🏞 Generating thumbnail")
      thumbnail = await thumb_creator(file_path)
      await msg.edit(f"⬆️ Trying to Upload as Video ...")
      start = time.time()
      await bot.send_video(
        chat_id=update.chat.id,
        progress=progress_for_pyrogram,
        progress_args=(
          "⬆️ Uploading as Video:",
          msg,
          start
        ),
        file_name=filename,
        video=file_path,
        width=width,
        height=height,
        duration=duration,
        thumb=str(thumbnail),
        caption=f"`{filename}` [{size}]",
        reply_to_message_id=None
      )
      await msg.delete()
      try:
        os.remove(file_path)
      except:
        pass
      return
    except Exception as e:
      fsw = "app"
      await msg.edit(f"❌ Uploading as Video Failed **Error:** {e} \n Trying to Upload as File in 3 second!")
    await asyncio.sleep(3)
  
  if fsw == "aud":
    try:
      duration = 0
      metadata = extractMetadata(createParser(file_path))
      if metadata and metadata.has("duration"):
        duration = metadata.get("duration").seconds
 
        start = time.time()
        await msg.edit(f"⬆️ Trying to Upload as Audio ...")
        await bot.send_audio(
          chat_id=update.chat.id,
          progress=progress_for_pyrogram,
          progress_args=(
            "⬆️ Uploading as Audio:",
            msg,
            start
          ),
          file_name=filename,
          duration=duration,
          audio=file_path,
          caption=f"`{filename}` [{size}]",
          reply_to_message_id=None
        )
        await msg.delete()
        try:
          os.remove(file_path)
        except:
          pass
          return
    except Exception as e:
      fsw = "app"
      await msg.edit(f"❌ Uploading as Audio Failed **Error:** {e}\nTrying to Upload as Document in 3 second!")
      await asyncio.sleep(3)
    
  if fsw == "app":
    try:
      start = time.time()
      await msg.edit(f"⬆️ Trying to Upload as Document ...")
      await bot.send_document(
        chat_id=update.chat.id,
        progress=progress_for_pyrogram,
        progress_args=(
          "⬆️ Uploading as Document:",
          msg,
          start
        ),
        file_name=filename,
        document=file_path,
        force_document=True,
        caption=f"`{filename}` [{size}]",
        reply_to_message_id=None
      )
      await msg.delete()
      try:
        os.remove(file_path)
      except:
        pass
    except Exception as e:
      await msg.edit(f"❌ Uploading as Document Failed !\n\n**Error:** {e}")
      try:
        os.remove(file_path)
      except:
        pass
      return