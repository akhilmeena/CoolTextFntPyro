import re 
import logging
import os
import math
from config import Config
import pyrogram
from plugins import helper
import requests
import urllib.request
from pyrogram import Client, filters
from plugins.display_progress import progress_for_pyrogram,get_size,TimeFormatter
import time
#from callbackquery import GetRunningOprtn
import callbackquery.GetRunningOprtn

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message()
async def onMsg(client,message):
    #global messages
    #print("onMessage event")
    #print(message)
    Current_Operation = await GetRunningOprtn()
    chat_id = message.chat.id
    user_id = message.from_user.id
    chat_type = message.chat.type
    #cmd = message.text.split(" ")
    if chat_type == "private":
      if Current_Operation == "requestnewspaper":
        print("goodddd")
