import json
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


NewsPapers = InlineKeyboardButton('The Hindu', callback_data='thehindu')
HomeToStart = InlineKeyboardButton('🔙', callback_data='libraryopen')


NewspaperType = InlineKeyboardMarkup([
  [NewsPapers],
  [HomeToStart]
  ])
