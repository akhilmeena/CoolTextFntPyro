import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string


def addclasslist(bot,update):
  Source_List = []
  for clss in range(12):
    addDict = {}
    addList = ["getsubjctofclass"]
    addDict["CallBtnTedt"] = str(f"Class {clss}")
    addList.append(str(clss))
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List
        

def makeBtnFromDict(Source_List):
  Btn = []
  for d in Source_List:
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+2] for i in range(0, len(Btn)-1, 2)]
  x = InlineKeyboardButton("🔙",callback_data="libraryopen")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns
