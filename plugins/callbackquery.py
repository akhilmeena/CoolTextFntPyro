import os
import logging
import pyrogram
import ast
from config import Config
from pyrogram import types
from plugins import helper,Fonts,TextHandler
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ChatPermissions, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
  if (update.data.startswith("['ChangePage'")):
    #print(update.message.message_id)
    page = ast.literal_eval(update.data)[1]
    await Client.edit_inline_reply_markup(inline_message_id = str(update.message.message_id),reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("New button", callback_data="new_data")]]))
  if (update.data.startswith("['CF'")):
    #Title = ast.literal_eval(update.data)[1]
    Font_Name = ast.literal_eval(update.data)[1]
    Fotnkeyboard = await Fonts.GenerateButtonForF9ntList(0)
    if len(TextHandler.Current_Text) ==1:
      TextToChange = TextHandler.Current_Text[0]
      TextWithFont = await Fonts.CreateFontFromText(TextToChange,Font_Name)
      await update.message.edit_text(text=f"{TextWithFont}",reply_markup=Fotnkeyboard)
    else:
      TextHandler.Current_Text.clear()
      await update.message.reply_text("<b>Send Some Text</b>")
      await update.message.delete()
  