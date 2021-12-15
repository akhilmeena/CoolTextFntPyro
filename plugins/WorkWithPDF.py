import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import urllib.parse
import requests
import os
import random
import img2pdf
from PIL import Image


async def GenarateRandomName(charachter):
  password_length = int(charachter)
  possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
  random_character_list = [random.choice(possible_characters) for i in range(password_length)]
  random_password = "".join(random_character_list)
  return random_password


async def GenerateScrennshotFromUrl(Url,update):
  BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?' # you can modify size, format, zoom
  print(Url)
  url = urllib.parse.quote_plus(Url) #service needs link to be joined in encoded format
  try:
    CHAT_ID = update.message.chat.id
  except:
    CHAT_ID = update.chat.id
  directory = f"{CHAT_ID}"
  parent_dir = "Downloads/"
  path = os.path.join(parent_dir, directory) 
  isExist = os.path.exists(path)
  if not isExist:
    os.mkdir(path)
  else:
    pass
  file_name = await GenarateRandomName(6)
  file_namewithext = str(file_name) + ".jpg"
  file_path = os.path.join(path, file_namewithext)
  #path = 'target1.jpg'
  response = requests.get(BASE + url, stream=True)
  # save file, see https://stackoverflow.com/a/13137873/7665691
  if response.status_code == 200:
    print("response.status_code")
    with open(file_path, 'wb') as file:
      for chunk in response:
        file.write(chunk)
  return file_path


async def CropImage(start_x, start_y, width, height,ImagPath):
  input_img = Image.open(ImagPath)
  #input_img = Image.open(input_image)
  box = (start_x, start_y, start_x + width, start_y + height)
  output_img = input_img.crop(box)
  output_img.save(ImagPath)
  #output_img.save(output_image +".jpg")
  #im1 = im.crop((left, top, right, bottom))
  #im1.save(ImagPath)



async def GenratePdfFromImg(update,file_path,Date):
  try:
    CHAT_ID = update.message.chat.id
  except:
    CHAT_ID = update.chat.id
  directory = f"{CHAT_ID}"
  parent_dir = "Downloads/"
  path = os.path.join(parent_dir, directory) 
  newFileName = f"@LibraryInBot {Date}.pdf"
  mfile_path = os.path.join(path, newFileName )
  with open(mfile_path,"wb") as f:
    f.write(img2pdf.convert(file_path))
  os.remove(file_path)
  return mfile_path,newFileName
  
  
 