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
            "I Invite You to join a LIBRARY BOT 🏦. Here you can search 🔍 Any Type of reading materials...📖 Eg. Textbooks 📚, Novels 📗, Daily Newspapers🗞️ , magazines📑 , Current Affairs,UPSC/PSC NOTES Etc"
            ),
            #url="https://t.me/Libraryinbot",
            description="Tap To Share",
            thumb_url="https://imgur.com/gallery/FZUbdGk",
            reply_markup=InlineKeyboardMarkup([
              [InlineKeyboardButton("Open Library Bot 📚",url="https://t.me/Libraryinbot")]
            ])
            )
        ],
        cache_time=1
    )
 