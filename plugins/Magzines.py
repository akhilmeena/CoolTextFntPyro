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


ChlacdmycrntafrmagzineHindi = InlineKeyboardButton('Chahal Acdmy Crnt Afrs(Hindi)', callback_data="['Chlacdmycrntafrmagzine','Hindi']")
ChlacdmycrntafrmagzineEnglish = InlineKeyboardButton('Chahal Acdmy Crnt Afrs(English)', callback_data="['Chlacdmycrntafrmagzine','English']")
YoznaMagzineHindi = InlineKeyboardButton('Yojana Monthly Magazines(Hindi)', callback_data="['YoznaMagzine','Hindi']")
YoznaMagzineEnglish = InlineKeyboardButton('Yojana Monthly Magazines(English)', callback_data="['YoznaMagzine','English']")
KurukshetraMagzineHindi = InlineKeyboardButton('Kurukshetra Monthly Magazines(Hindi)', callback_data="['KurukshetraMagzine','Hindi']")
KurukshetraMagzineEnglish = InlineKeyboardButton('Kurukshetra Monthly Magazines(English)', callback_data="['KurukshetraMagzine','English']")
#"['KurukshetraMagzine','Hindi']"
#"['KurukshetraMagzine','English']"
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


MagzinesType = InlineKeyboardMarkup([
  [ChlacdmycrntafrmagzineHindi],
  [ChlacdmycrntafrmagzineEnglish],
  [YoznaMagzineHindi],
  [YoznaMagzineEnglish],
  [KurukshetraMagzineHindi],
  [KurukshetraMagzineEnglish],
  [HomeToStart]
  ])