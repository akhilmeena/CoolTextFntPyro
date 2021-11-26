import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


STARTText = """<b>Hi {}!
This Is Library Bot😇
Get all the updates Daily</b>
"""

OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
HelpBtn = InlineKeyboardButton('🆘 Help', callback_data='help')
START_BUTTONS = InlineKeyboardMarkup(
  [[
    OpenLibeary
  ],[
    HelpBtn,
    InlineKeyboardButton('About Dev ❤️', callback_data='abtadmin')
  ],[
    InlineKeyboardButton('❌ Close', callback_data='close')
  ]]
  )

LBRYOPEN_BUTTONS = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton('⚡ Current Affairs', callback_data='libraryopen')
  ],[
    InlineKeyboardButton('🏘️ Home', callback_data='home'),
  ]]
  )
  
HELPTEXT = """⚠️ This is Help Pannel:

This Is A Library Bot. If u Need any Type study Material Just send us in Complaint & Suggestions Pannel.
"""

################Danger
# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"



HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/HeimanSupports/'),
        InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/HeimanSupport/'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
