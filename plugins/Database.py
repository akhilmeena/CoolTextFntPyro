import logging
import os
from config import Config
import pyrogram
from pyrogram import Client
import gspread
from oauth2client.service_account import ServiceAccountCredentials


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(creds)
ak = client.open("LibraryData")
UserData = ak.worksheet("User")


async def AddNewUser(bot,UserID,ReferredBy):
  cells = UserData.findall(str(UserID))
  if len(cells) > 0:
    return
  else:
    h = UserData.get('A10000').first()
    h1 = int(h) + 1
    UserData.update_cell(int(h1),1 ,f"{h1}")
    UserData.update_cell(int(h1),2 ,UserID)
    UserData.update_cell(int(h1),3 ,1000)
    UserData.update_cell(int(h1),4 ,0)
    if ReferredBy == "None":
      pass
    else:
      NowBalance = await CreditCoin(ReferredBy)
      TotalInvited = await UserInvited(ReferredBy)
      await bot.send_message(chat_id=int(ReferredBy),text="<b>💐 Congrats!!  You are credited with 600 coins.</b>")
    return

async def CreditCoin(CHAT_ID):
  cellx = UserData.find(str(CHAT_ID))
  row = cellx.row
  #UserInvited = UserData.get('C' + f"{row}").first()
  BALANCE = UserData.get('D' + f"{row}").first()
  NowBalance = int(BALANCE) + 600
  UserData.update_cell(int(row),3 ,int(NowBalance))

async def UserInvited(CHAT_ID):
  cellx = UserData.find(str(CHAT_ID))
  row = cellx.row
  UserInvited = UserData.get('C' + f"{row}").first()
  #BALANCE = UserData.get('D' + f"{row}").first()
  TotalInvited = int(UserInvited) + 1
  UserData.update_cell(int(row),4 ,int(TotalInvited))
  


async def GetAllUsersList(bot, update):
  values_list3 = UserData.col_values(2)
  ttlusers = len(values_list3)
  while("" in values_list3):
    values_list3.remove("")
  return values_list3,ttlusers
  
async def GetBlanceCoinOfUser(CHAT_ID):
  cellx = UserData.find(str(CHAT_ID))
  row = cellx.row
  UserInvited = UserData.get('C' + f"{row}").first()
  BALANCE = UserData.get('D' + f"{row}").first()
  return UserInvited,BALANCE
  
  
