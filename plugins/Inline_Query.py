import pyrogram
from config import Config
from pyrogram import Client, filters
from pyrogram.types import (InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup)


@Client.on_inline_query()
async def inline(bot, inline_query):
  string = inline_query.query.lower()
  
  if string == "":
    await inline_query.answer(
      results=[
        InlineQueryResultArticle(
          title="🔄 Share With Others",
          input_message_content=InputTextMessageContent(
            "This is Library Bot"
            ),
            #url="https://t.me/Libraryinbot",
            description="Tap To Share",
            thumb_url="https://i.imgur.com/JyxrStE.png",
            reply_markup=InlineKeyboardMarkup([
              [InlineKeyboardButton("Open Library Bot 📚",url="https://t.me/Libraryinbot")]
            ])
            )
        ],
        cache_time=1
    )
 
