import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup


async GenarateRandomName(charachter):
  password_length = int(charachter)
  possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
  random_character_list = [random.choice(possible_characters) for i in range(password_length)]
  random_password = "".join(random_character_list)
  return random_password


async GenerateScrennshotFromUrl(Url):
  BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?' # you can modify size, format, zoom
  url = urllib.parse.quote_plus(url) #service needs link to be joined in encoded format
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
    with open(file_path, 'wb') as file:
      for chunk in response:
        file.write(chunk)
  return file_path

