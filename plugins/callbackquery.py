import os
import logging
import traceback
import pyrogram
#from pyrogram import 
import ast
import asyncio
from config import Config
from pyrogram import types
from plugins import helper,Fonts,TextHandler,TextDecorator,Database
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ChatPermissions, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  if update.data == "help":
    await update.message.edit_text(text=helper.HELPTEXT,reply_markup=helper.HELPBTN)
  if update.data == "abtdvlngbot":
    await update.message.edit_text(text=helper.BotAboutText.format(update.message.from_user.mention),reply_markup=helper.DVLGBTN)
  if update.data == "homeTostart":
    await update.message.edit_text(text=helper.STARTText.format(update.message.chat.first_name),reply_markup=helper.HOME_PAGE)
  if update.data == "MoreBots":
    await update.message.edit_text(text=helper.MoreBotsText.format(update.message.from_user.mention),reply_markup=helper.MoreBots_BTN)
  if update.data == "STARTFonting":
    await update.message.edit_text(text="Choose Your Methods",reply_markup=helper.STARTFontingBTN)
  if update.data == "CoolFonts":
    Fotnkeyboard = await Fonts.GenerateButtonForF9ntList(0)
    await update.message.edit_text(text="Choose Your Fonts",reply_markup=Fotnkeyboard)
  if update.data == "DecorateText":
    Designkeyboard = await TextDecorator.GenerateButtonForDecorate()
    await update.message.edit_text(text="Choose Your Design",reply_markup=Designkeyboard)
  if (update.data.startswith("['ChangePage'")):
    page = ast.literal_eval(update.data)[1]
    Fotnkeyboard = await Fonts.GenerateButtonForF9ntList(int(page))
    await update.edit_message_reply_markup(reply_markup=Fotnkeyboard)#inline_message_id = update.message.message_id,text="akhil")#reply_markup=helper.MoreBots_BTN)#InlineKeyboardMarkup([[InlineKeyboardButton("New button", callback_data="new_data")]]))
  if (update.data.startswith("['CF'")):
    Font_Name = ast.literal_eval(update.data)[1]
    Page_No = ast.literal_eval(update.data)[2]
    Fotnkeyboard = await Fonts.GenerateButtonForF9ntList(int(Page_No))
    TextToChange = await TextHandler.GetCurrentTextToStyle(update.message.chat.id)
    if str(TextToChange) =="Nonee":
      await update.message.reply_text("<b>Send Some Text</b>")
      await update.message.delete()
    else:
      TextWithFont = await Fonts.CreateFontFromText(TextToChange,Font_Name)
      await update.message.edit_text(text=f"{TextWithFont}",reply_markup=Fotnkeyboard)
  if (update.data.startswith("['DSGN'")):
    DesignNumber = ast.literal_eval(update.data)[1]
    Designkeyboard = await TextDecorator.GenerateButtonForDecorate()
    TextToChange = await TextHandler.GetCurrentTextToStyle(update.message.chat.id)
    if str(TextToChange) =="Nonee":
      await update.message.reply_text("<b>Send Some Text</b>")
      await update.message.delete()
    else:
      TextWithFont = await TextDecorator.DesignWithText(TextToChange,DesignNumber)
      await update.message.edit_text(text=f"{TextWithFont}",reply_markup=Designkeyboard)
  if update.data == "vrfyusers":
    values_list3,ttlusers = await Database.GetAllUsersList(bot, update)
    i=0
    j=0
    ak = "ak"
    msg = await update.message.reply_text(helper.usrststext.format(ttlusers,i,j))
    #print(values_list3)
    for p in values_list3:
      #print("1")
      try:
        Chtid = int(p)
        #print("2")
        await bot.send_chat_action(chat_id = Chtid, action=pyrogram.enums.ChatAction.TYPING)
        #print("3")
        i+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
      except FloodWait as e:
        await asyncio.sleep(e.x)
        await bot.send_chat_action(chat_id = int(p), action=pyrogram.enums.ChatAction.TYPING)
        i+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
        #return await broadcast_messages(user_id, message)
      except InputUserDeactivated:
        await Database.Clear_Cell(int(p))
        j+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
        #await db.delete_user(int(user_id))
        #logger.info(f"{user_id}-Removed from Database, since deleted account.")
        #return False, "Deleted"
      except UserIsBlocked:
        await Database.Clear_Cell(int(p))
        j+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
        #logger.info(f"{user_id} -Blocked the bot.")
        #return False, "Blocked"
      except Exception as e:
        await Database.Clear_Cell(int(p))
        print(traceback.format_exc())
        j+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
        print(e)
        error = f"{e}".split(":")[0]
        ak+=f"\n{p} {error}"
        #return False, "Error"
        
      #except Exception as e:
        #j+=1
      #  try:
    #      print(e)
      #  except Exception as ex:
   #       print(ex)
       #   ak+=f"\n{p} {ex}"
        #await msg.edit(helper.usrststext.format(ttlusers,i,j))
      await asyncio.sleep(1)
    try:
      await update.message.reply_text(f"{ak}")
    except:
      await update.message.reply_text(f"All Users are Active")
