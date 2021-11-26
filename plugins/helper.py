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

#🤖 Name :''' + "<a href='t.me/{}'>{}</a>" + '''
BotAboutText = """<b>About Me 😎
<b>----------------------------------------------------</b>
🤖 Name : {}
👨‍💻 Developer : @Jai_Mahakal_Ji
📝 Language : </b><code>Python 3. 9.7</code>
<b>📲 Version :</b> <code>1.0.2</code>
<b>🧰 Framework :</b> <code>Pyrogram</code>
<b>📡 Server :</b> <code>Heroku</code>
<b>----------------------------------------------------</b>
<b>Made With ❤️ In India 🇮🇳 </b>"""

############### BUTTONS Text #####################

OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
HelpBtn = InlineKeyboardButton('🆘 Help', callback_data='help')
AboutDev = InlineKeyboardButton('About Dev ❤️', callback_data='abtdvlngbot')

CurrentAfrsBtn = InlineKeyboardButton('⚡ Current Affairs', callback_data='libraryopen')
HomeToStart = InlineKeyboardButton('🔙', callback_data='home2start')

UpdateOfBot = InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/HeimanSupports/')
SupportPfBot = InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/HeimanSupport/')

ClosePannel = InlineKeyboardButton('❌ Close', callback_data='close')

############### BUTTONS Add #####################


START_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary],
  [HelpBtn,AboutDev],
  [UpdateOfBot,SupportPfBot],
  ])

LBRYOPEN_BUTTONS = InlineKeyboardMarkup([
  [CurrentAfrsBtn],
  [HomeToStart]
  ])
  
HELP_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary]
  [HomeToStart,AboutDev],
  [UpdateOfBot,SupportPfBot],
  ])

DVLGBTN = InlineKeyboardMarkup([
  [OpenLibeary]
  [HelpBtn,HomeToStart],
  [UpdateOfBot,SupportPfBot],
  ])
