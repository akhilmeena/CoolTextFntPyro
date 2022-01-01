import json
import pyrogram
from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re

#BALANCECOINS = 

AccntDetails = """<b>💼 Account Details:
 ===========================
💰 Balance : </b><code> {} Coins</code>
<b>📨 Invited : </b><code> {} Users</code>
<b>📡 Refer & Earn : https://t.me/LibraryInbot?start={}

◆ <i>Per Refer you will get 600 Free Coins Or Else You can Recharge Your account through Buying Coints @ 500 Coins/1 Rs.

💝 <u>Account Balance for Super user will be INFINITE COINS. To become Super User You must invite atleast 10 Users.
</u></i></b>"""