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

usrststext = '''<b>Bot Users Statics 📊
➖➖➖➖➖➖➖➖➖➖➖➖➖
Total Users:</b> <code>{}</code>
<b>Active Users:</b> <code>{}</code>
<b>InActive Users:</b> <code>{}</code>'''

STARTText = """<b>👋 Hii {} !!!,
<i>
A fancy cool ✓ font generator that 
helps create stylish text font styles 
with beautiful symbols and fancy 
characters for social networks & 
any other platforms.
</i>
=======================
❤️ From 🇮🇳</b>"""

HELPTEXT = """<b>=========================
😆 Sorry, I can't help u.
=========================</b>"""

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

MoreBotsText = """<b>=========================
🙏 Thanks to visite here ......

➣ There are few bots:-
<i>  ➥ @Love
  ➥ @akhil
</i>
=========================</b>"""
#AdminPannel = """👤 Admin Pannel:"""

MaintainanceProgress = """<b>🛠 Maintenance in Progress....

▪Bot's ADMINISTRATION Updating Some Modules In The Bot.
▪Due to this reason content will not be available till further notice.
▪All functionality will be back after completion.

🙏 Try Few Time Later…</b>"""

############### Additional Functional #####################

def create_markup(_list: list=[[]]):
  result = []
  for row in _list:
    result.append([])
    for item in row:
      btn = cb(item)
      result[-1].append(btn)
  return InlineKeyboardMarkup(result)

############### BUTTONS Text #####################

OpenLibeary = InlineKeyboardButton('📚 Open Library', callback_data='libraryopen')
#Account = InlineKeyboardButton('💼 Account', callback_data='#')
Account = InlineKeyboardButton('💼 Account', callback_data='account')
HelpBtn = InlineKeyboardButton('🆘 Help 🆘', callback_data='help')
AboutDev = InlineKeyboardButton('Dev. ❤️', callback_data='abtdvlngbot')
Feedback = InlineKeyboardButton('💌 Feedback', url='https://telegram.dog/amtgbots/30')
Share = InlineKeyboardButton('Share 🔄', switch_inline_query='')

CurrentAfrsBtn = InlineKeyboardButton('⚡ Current Affairs', callback_data='crnafrsdaily')
BooksCollction = InlineKeyboardButton('📚 BOOKS', callback_data='BooksCollction')
NcertBooks = InlineKeyboardButton('📚 NCERT BOOKS', callback_data='ncertbooks')
NewsPapers = InlineKeyboardButton('📰 News Papers', callback_data='newepapers')
Magzines = InlineKeyboardButton('📔 Magzines', callback_data='magzines')
JobAlert = InlineKeyboardButton('🔔 Job Alert ', callback_data='jobalert')
#PYQ = InlineKeyboardButton('📃 PYQ ', callback_data='pyearq')
PYQ = InlineKeyboardButton('📃 PYQ ', callback_data='#')
#HNotes = InlineKeyboardButton('📝 H-Notes ', callback_data='HandNotes')
HNotes = InlineKeyboardButton('📝 H-Notes ', callback_data='#')
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
  [CurrentAfrsBtn,BooksCollction],
  [NewsPapers,Magzines],
  [PYQ,HNotes],
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


