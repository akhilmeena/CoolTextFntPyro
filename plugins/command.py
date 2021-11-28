import logging
import os
import requests
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import helper
from plugins import url_uploader



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  await message.reply_chat_action("typing")
  if str(Config.MaintainaceYN[0]) == "No":
    await message.reply_text(text=helper.STARTText.format(message.from_user.mention),reply_markup=helper.START_BUTTONS)
  else:
    await message.reply_text(text=helper.MaintainanceProgress)

#@Client.on_message(filters.command(["admin"]) & filters.private & filters.user(Config.OWNER_ID) & ~filters.edited)
@Client.on_message(filters.private & filters.command(["admin"]))
async def settings(bot,message):
  if int(message.chat.id) in Config.OWNER_ID:
    await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  else:
    Chat_Id = message.chat.id
    #message.delete_messages(Chat_Id, message.message_id)
    await message.reply_text("<b>💔 Only Admin Command!!</b>")
    #message.message.delete_messages(Chat_Id, message.message_id)

@Client.on_message(filters.regex('http') & filters.private)
async def DownloadTest(bot, update):
  url = update.text
  url_uploader.leecher2(bot , update,url)
  












################Danger
#@Client.on_message(filters.regex('http') & filters.private)
#async def pdisk(bot, message):
def pdisk(bot, message):
        text = message.text
        if 'cofilink.com' in text or 'www.cofilink.com' in text or 'pdisk.me' in text or 'www.pdisk.me' in text:
            spl = link.split('=')
            vd_id = spl[-1]
            auth = "http://linkapi.net/open/clone_item/?api_key="+Config.API_KEY+"&item_id="+vd_id
        else:
            try:
            # Solved https://github.com/HeimanPictures/Pdisk-Upload-Bot/issues/1#issue-1018422275
                spl = text.split(' | ')
                url = spl[0]
                title = spl[1]
                try:
                    thumb = spl[2]
                    auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title="+title+"&cover_url="+thumb 
                except Exception:
                    auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title="+title
            except Exception:
                url = text
                auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title=None"
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(auth,headers)
            res = r.json()
            #print(res)
            id = res["data"]["item_id"]
            #await message.reply_chat_action("typing")
            pdisk = "https://cofilink.com/share-video?videoid="+id      
            #await message.reply_photo(
#                photo="https://static10.tgstat.ru/channels/_0/f3/f3218a8a0d195d12e73f6b69e51bbb4f.jpg",
#                caption="**URL:** `"+pdisk+"`\n\n**The PDisk Link Is Below The Provided Link Will Be Uploaded in few minutes.\nThank You**\n\n**@HeimanSupports**",
#                reply_markup=InlineKeyboardMarkup([
#                    [ InlineKeyboardButton(text="🔗 PDisk 🔗", url=f"{pdisk}")]
#                ])
#            )

