import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
from plugins import helper

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  if update.data == "libraryopen":
    await update.message.edit_text(
      text="Not Added Yet",
      disable_web_page_preview=True,
      reply_markup=helper.LBRYOPEN_BUTTONS
      )
  elif update.data == "home2start":
    await update.message.edit_text(
    text=helper.STARTText.format(update.from_user.mention),
    disable_web_page_preview=True,
    reply_markup=helper.START_BUTTONS
    )
  elif update.data == "help":
    await update.message.edit_text(
    text=helper.HELPTEXT,
    disable_web_page_preview=True,
    reply_markup=helper.HELP_BUTTONS
    )
  else update.data == "close":
    await update.message.delete()
