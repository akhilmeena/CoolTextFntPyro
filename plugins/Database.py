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
ak = client.open("CoolTextPyro")
UserData = ak.worksheet("Users")

async def Clear_Cell(UserID):
  cellnumber = await FintUserLine(UserID)
  UserData.batch_clear([f"A{cellnumber}:B{cellnumber}"])
def
async def FintUserLine(UserID):
  cells = UserData.findall(str(UserID))
  return cellurowuser = cells.row
  

async def AddNewUser(bot,UserID):
  cells = UserData.findall(str(UserID))
  if len(cells) > 0:
    return
  else:
    h = UserData.get('A45000').first()
    h1 = int(h) + 1
    UserData.update_cell(int(h1),1 ,f"{h1}")
    UserData.update_cell(int(h1),2 ,UserID)
    return

async def GetAllUsersList(bot, update):
  values_list3 = UserData.col_values(2)
  ttlusers = len(values_list3)
  while("" in values_list3):
    values_list3.remove("")
  return values_list3,ttlusers
