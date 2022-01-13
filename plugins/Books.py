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


BookTypeList = {
  "NCERT BOOKS":"ncertbooks"
  }


async def BookTypeButton():
  for d in Source_List:
    print(d)