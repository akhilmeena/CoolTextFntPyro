import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
from plugins import helper
from plugins import currentaffairs

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  if update.data == "crnafrsdaily":
    await update.message.edit_text(text="<b>Choose Your Source</b>",reply_markup=currentaffairs.CRNTAFRSOURCEBTN)
  if update.data == "libraryopen":
    await update.message.edit_text(text="<b>Choose Your Study Material Items</b>",reply_markup=helper.LBRYOPEN_BUTTONS)
  if update.data == "home2start":
    await update.message.edit_text(text=helper.STARTText.format(update.from_user.mention),reply_markup=helper.START_BUTTONS)
  if update.data == "help":
    await update.message.edit_text(text=helper.HELPTEXT,reply_markup=helper.HELP_BUTTONS)
  if update.data == "abtdvlngbot":
    await update.message.edit_text(text=helper.BotAboutText.format(update.message.from_user.mention),reply_markup=helper.DVLGBTN)
  if update.data == "BacktoAdminpnl":
    await update.message.edit_text(text="<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  if update.data == "maintainanceoff":
    Config.MaintainaceYN.clear()
    Config.MaintainaceYN.append("YES")
    await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyY)
  if update.data == "maintainanceon":
    Config.MaintainaceYN.clear()
    Config.MaintainaceYN.append("No")
    await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyN)
  if update.data == "chngemaintaincemode":
    if str(Config.MaintainaceYN[0]) == "No":
      await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyN)
    else:
      await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyY)
  if update.data == "close":
    await update.message.delete()
