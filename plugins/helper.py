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

HELP = """
**Send Me Direct Download Link Like Mirror Or From @LinkXGenBot.

Send As This Format**

`link | Title`

**Or**

`Video link | Title | Thumbnail link`

**NOTE:
➢ Do Not Spam, Send Link One By One
➢ To Know Status Just Go To cofilink.com/home**
"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
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
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
