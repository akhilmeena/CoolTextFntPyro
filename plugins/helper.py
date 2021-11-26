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

############### General Text #####################

STARTText = """<b>Hi {}!
This Is Library Bot😇
Get all the updates Daily</b>
"""

HELPTEXT = """⚠️ This is Help Pannel:

This Is A Library Bot. If u Need any Type study Material Just send us in Complaint & Suggestions Pannel.
"""

############### BUTTONS Text #####################

OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
HelpBtn = InlineKeyboardButton('🆘 Help', callback_data='help')
AboutDev = InlineKeyboardButton('About Dev ❤️', callback_data='abtadmin')

CurrentAfrsBtn = InlineKeyboardButton('⚡ Current Affairs', callback_data='libraryopen')
HomeToStart = InlineKeyboardButton('🏘️ Home', callback_data='home2start')

UpdateOfBot = InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/HeimanSupports/')
SupportPfBot = InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/HeimanSupport/')

ClosePannel = InlineKeyboardButton('❌ Close', callback_data='close')

############### BUTTONS Add #####################


START_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary],
  [HelpBtn,AboutDev]
  ])

LBRYOPEN_BUTTONS = InlineKeyboardMarkup([
  [CurrentAfrsBtn],
  [HomeToStart]
  ])
  
HELP_BUTTONS = InlineKeyboardMarkup([
  [UpdateOfBot,SupportPfBot],
  [HomeToStart]
  ])
