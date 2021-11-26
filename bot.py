import logging
import os
from config import Config
import pyrogram
from pyrogram import Client


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__" :
  plugins = dict(root="plugins")
  app = Client(
    "LibraryBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins, 
    parse_mode = "HTML"
    )
  app.run()

