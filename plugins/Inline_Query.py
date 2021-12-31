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
            url="https://t.me/Libraryinbot",
            description="Just Read Here",
            thumb_url="https://i.imgur.com/JyxrStE.png",
            reply_markup=InlineKeyboardMarkup([
              [InlineKeyboardButton("Open website",url="https://docs.pyrogram.org/intro/install")]
            ])
            )
        ],
        cache_time=1
    )
 
