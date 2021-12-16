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


ChlacdmycrntafrmagzineHindi = InlineKeyboardButton('Chahal (Hindi)', callback_data="['Chlacdmycrntafrmagzine','Hindi']")
ChlacdmycrntafrmagzineEnglish = InlineKeyboardButton('Chahal (English)', callback_data="['Chlacdmycrntafrmagzine','English']")
YoznaMagzineHindi = InlineKeyboardButton('Yojana (Hindi)', callback_data="['YoznaMagzine','Hindi']")
YoznaMagzineEnglish = InlineKeyboardButton('Yojana (English)', callback_data="['YoznaMagzine','English']")
KurukshetraMagzineHindi = InlineKeyboardButton('Kurukshetra (Hindi)', callback_data="['KurukshetraMagzine','Hindi']")
KurukshetraMagzineEnglish = InlineKeyboardButton('Kurukshetra (English)', callback_data="['KurukshetraMagzine','English']")
#"['KurukshetraMagzine','Hindi']"
#"['KurukshetraMagzine','English']"
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


MagzinesType = InlineKeyboardMarkup([
  [ChlacdmycrntafrmagzineEnglish,ChlacdmycrntafrmagzineHindi],
  [YoznaMagzineEnglish,YoznaMagzineHindi],
  [KurukshetraMagzineEnglish,KurukshetraMagzineHindi],
  [HomeToStart]
  ])