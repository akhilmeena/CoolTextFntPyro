import os
import logging
import pyrogram
from config import Config
from pyrogram import types
from plugins import helper
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ChatPermissions, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  if (update.data.startswith("['MnthlyCA'")):
    Title = ast.literal_eval(update.data)[1]
    Lan = ast.literal_eval(update.data)[2]
  if update.data == "help":
    await update.message.edit_text(text=helper.HELPTEXT,reply_markup=helper.HELPBTN)
  if update.data == "abtdvlngbot":
    await update.message.edit_text(text=helper.BotAboutText.format(update.message.from_user.mention),reply_markup=helper.DVLGBTN)
  if update.data == "homeTostart":
    print(update.message.chat.mention)
    await update.message.edit_text(text=helper.STARTText.format(update.message.chat.first_name),reply_markup=helper.HOME_PAGE)
  if update.data == "MoreBots":
    await update.message.edit_text(text=helper.MoreBotsText.format(update.message.from_user.mention),reply_markup=helper.MoreBots_BTN)