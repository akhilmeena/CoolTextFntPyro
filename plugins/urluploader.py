#preapred By Akhil Meena
from plugins import DowloadFromUrl

async def Urlleaccher(bot,update,Url2Dowload):
  try:
    msg = await update.reply_text(text=f"`Creating Path......`", quote=True)
  except:
    msg = await update.message.reply_text(text=f"`Creating Path......`", quote=True)
  directory = f"{update.chat.id}"
  parent_dir = "Downloads/"
  path = os.path.join(parent_dir, directory) 
  try:
    os.mkdir(path)
  except:
    try:
      os.remove(path)
      os.mkdir(path)
      pass
    except Exception as e:
      await msg.edit(f"Creating Directory Failed !\n\n**Error:** {e}")
      #break
  file_name = Url2Dowload.split('/')[-1]
  file_path = os.path.join(path, file_name)
  url = Url2Dowload 
  start = time.time()
  try:
    await DowloadFromUrl.download_file(url, file_path,file_name, msg, start, bot)
    print(f"file downloaded to {file_path} with name: {file_name}")
  except Exception as e:
    await msg.edit(f"Creating Directory Failed !\n\n**Error:** {e}")
    #break
  await msg.edit(f"✅ **Successfully Downloaded**")
  try:
    start = time.time()
    await msg.edit(f"⬆️ Trying to Upload as Document ...")
    await bot.send_document(chat_id=update.chat.id,
    progress=progress_for_pyrogram,
    progress_args=("⬆️ Uploading as Document:",msg,start),
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

  #response = requests.get(urlforpdf)
  
  
  