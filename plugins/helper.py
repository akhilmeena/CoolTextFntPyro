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


############### Additional Functional #####################

def create_markup(_list: list=[[]]):
  result = []
  for row in _list:
    result.append([])
    for item in row:
      btn = cb(item)
      result[-1].append(btn)
  return InlineKeyboardMarkup(result)
############### General Text #####################

STARTText = """<b>Hi {}!

This Is Library Bot😇.........
Get all the updates Daily
================================
Note:</b> <i>All the Content uploaded here is taken out from other sources.if anybody have issue with that,just write ur msg...we will remove that.
Thanks ❤️</i>
"""

HELPTEXT = """⚠️ This is Help Pannel:

This Is A Library Bot. If u Need any Type study Material Just send us in Complaint & Suggestions Pannel.
"""


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

#AdminPannel = """👤 Admin Pannel:"""

MaintainanceProgress = """<b>🛠 Maintenance in Progress....

▪Bot's ADMINISTRATION Updating Some Modules In The Bot.
▪Due to this reason content will not be available till further notice.
▪All functionality will be back after completion.

🙏 Try Few Time Later…</b>"""
############### BUTTONS Text #####################

OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
HelpBtn = InlineKeyboardButton('🆘 Help', callback_data='help')
AboutDev = InlineKeyboardButton('About Dev ❤️', callback_data='abtdvlngbot')

CurrentAfrsBtn = InlineKeyboardButton('⚡ Current Affairs', callback_data='libraryopen')
HomeToStart = InlineKeyboardButton('🔙', callback_data='home2start')
BacktoAdminpnl = InlineKeyboardButton('🔙', callback_data='backtoAdminpnl')

UpdateOfBot = InlineKeyboardButton('🚀 Update ', url='https://telegram.dog/channelanalyser/')
SupportPfBot = InlineKeyboardButton(' Support 💌', url='https://telegram.dog/channelanalyser/')
MainTainanceMode = InlineKeyboardButton('Maintainance ', callback_data='chngemaintaincemode')
ClosePannel = InlineKeyboardButton('❌ Close', callback_data='close')
MainTainanceModeY = InlineKeyboardButton('✅ Maintainance ON', callback_data='maintainanceon')
MainTainanceModeN = InlineKeyboardButton('◻️ Maintainance OFF', callback_data='maintainanceoff')

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
  [OpenLibeary],
  [HomeToStart,AboutDev],
  [UpdateOfBot,SupportPfBot],
  ])

DVLGBTN = InlineKeyboardMarkup([
  [OpenLibeary],
  [HelpBtn,HomeToStart],
  [UpdateOfBot,SupportPfBot],
  ])

AdminKeyboard = InlineKeyboardMarkup([
  [MainTainanceMode],
  [ClosePannel]
  ])
  
#Conditional BUTTONS

MaintainanceKeyY = InlineKeyboardMarkup([
  [MainTainanceModeY],
  [BacktoAdminpnl]
  ])
  
MaintainanceKeyN = InlineKeyboardMarkup([
  [MainTainanceModeN],
  [BacktoAdminpnl]
  ])


