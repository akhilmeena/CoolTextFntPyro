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

usrststext = '''<b>Bot Users Statics 📊
➖➖➖➖➖➖➖➖➖➖➖➖➖
Total Users:</b> <code>{}</code>
<b>Active Users:</b> <code>{}</code>
<b>InActive Users:</b> <code>{}</code>'''


STARTText = """<b>Hi {}!

This is LIBRARY BOT 🏦. Here you can search 🔍 Any Type of reading materials...📖 
Eg. <i>Textbooks 📚, Novels 📗, Daily Newspapers🗞️ , magazines📑 , Current Affairs,UPSC/PSC NOTES Etc</i>

Get all the updates Daily
================================
Note:</b> <i>All the Content uploaded here is taken out from other sources.if anybody have issue with that,just write ur msg...we will remove that.
Thanks ❤️</i>
"""

HELPTEXT = """<b>⚠️ This is Help Pannel</b>:

<i>This Is A Library Bot. If u Need any Type study Material Just send us in Complaint & Suggestions Pannel.
</i>"""

DonloadFiletext = """**Initiating Download**
**URL:** {}
**File Name:** {}
**File Size:** {}
**File Type:** {}"""

DownloadingProgress = """Downloading : {}%
URL: {}
File Name: {}
File Size: {}
Downloaded: {}
ETA: {}"""


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
#Account = InlineKeyboardButton('💼 Account', callback_data='#')
Account = InlineKeyboardButton('💼 Account', callback_data='account')
HelpBtn = InlineKeyboardButton('🆘 Help 🆘', callback_data='help')
AboutDev = InlineKeyboardButton('Dev. ❤️', callback_data='abtdvlngbot')
Feedback = InlineKeyboardButton('💌 Feedback', url='https://telegram.dog/amtgbots/30')
Share = InlineKeyboardButton('Share 🔄', switch_inline_query='')

CurrentAfrsBtn = InlineKeyboardButton('⚡ Current Affairs', callback_data='crnafrsdaily')
NcertBooks = InlineKeyboardButton('📚 NCERT BOOKS', callback_data='ncertbooks')
NewsPapers = InlineKeyboardButton('📰 News Papers', callback_data='newepapers')
Magzines = InlineKeyboardButton('📔 Magzines', callback_data='magzines')
JobAlert = InlineKeyboardButton('🔔 Job Alert ', callback_data='jobalert')
HomeToStart = InlineKeyboardButton('🔙', callback_data='home2start')
BacktoAdminpnl = InlineKeyboardButton('🔙', callback_data='backtoAdminpnl')

UpdateOfBot = InlineKeyboardButton('🚀 Update ', url='https://telegram.dog/channelanalyser/')
SupportPfBot = InlineKeyboardButton(' Support 💌', url='https://telegram.dog/channelanalyser/')
ClosePannel = InlineKeyboardButton('❌ Close', callback_data='close')

############### ADMIN PANNEL #####################

VerifyUsers = InlineKeyboardButton('🙋 Verify Users', callback_data='vrfyusers')
MainTainanceMode = InlineKeyboardButton('🔑 Maintainance ', callback_data='chngemaintaincemode')
MainTainanceModeY = InlineKeyboardButton('✅ Maintainance ON', callback_data='maintainanceon')
MainTainanceModeN = InlineKeyboardButton('◻️ Maintainance OFF', callback_data='maintainanceoff')

############### BUTTONS Add #####################


START_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary],
  [Account,HelpBtn,AboutDev],
  [Feedback,Share],
  ])

LBRYOPEN_BUTTONS = InlineKeyboardMarkup([
  [JobAlert],
  [CurrentAfrsBtn,NcertBooks],
  [NewsPapers,Magzines],
  [HomeToStart]
  ])
  
HELP_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary],
  [Account,HomeToStart,AboutDev],
  [Feedback,Share]
  ])

WALLET_BUTTONS = InlineKeyboardMarkup([
  [OpenLibeary],
  [HomeToStart,HelpBtn,AboutDev],
  [Feedback,Share]
  ])

DVLGBTN = InlineKeyboardMarkup([
  [OpenLibeary],
  [Account,HelpBtn,HomeToStart],
  [Feedback,Share]
  ])

AdminKeyboard = InlineKeyboardMarkup([
  [MainTainanceMode,VerifyUsers],
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


