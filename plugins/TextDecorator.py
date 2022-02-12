import json
import pyrogram
from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

DecorateList = {
  "1" : "★彡 @# 彡★",
  "2" : "◦•●◉✿ @# ✿◉●•◦",
  "3" : "╰☆☆ @# ☆☆╮",
  "4" : "╚»★«╝ @# ╚»★«╝",
  "5" : "*•.¸♡ @# ♡¸.•*",
  "6" : "↤↤↤↤↤ @# ↦↦↦↦↦",
  "7" : "↫↫↫↫↫ @# ↬↬↬↬↬",
  "8" : "▀▄▀▄▀▄ @# ▄▀▄▀▄▀",
  "9" : "💙💜💛🧡❤️️ @# ❤️️🧡💛💜💙",
  "10" : "💖💘💞 @# 💞💘💖",
  "11" : "░▒▓█ @# █▓▒░",
  "12" : "░▒▓█►─═ @# ═─◄█▓▒░",
  "13" : "▌│█║▌║▌║ @# ║▌║▌║█│▌",
  "14" : "ıllıllı @# ıllıllı",
  "15" : "【｡_｡】 @# 【｡_｡】",
  "16" : "(-_-) @# (-_-)",
  "17" : "•´¯`•. @# .•´¯`•",
  "18" : ".•♫•♬• @# •♬•♫•.",
  "19" : "·.¸¸.·♩♪♫ @# ♫♪♩·.¸¸.·",
  "20" : "★·.·´¯`·.·★ @# ★·.·´¯`·.·★",
  "21" : "➶➶➶➶➶ @# ➷➷➷➷➷",
  "22" : "▁ ▂ ▄ ▅ ▆ ▇ █ @# █ ▇ ▆ ▅ ▄ ▂ ▁",
  "23" : "✿.｡.:* ☆:**:. @# .:**:.☆*.:｡.✿",
  "24" : "ღ(¯`◕‿◕´¯) ♫ ♪ ♫ @# ♫ ♪ ♫ (¯`◕‿◕´¯)ღ",
  "25" : "(¯`*•.¸,¤°´✿.｡.:* @# *.:｡.✿`°¤,¸.•*´¯)",
  "26" : "๑۞๑,¸¸,ø¤º°`°๑۩ @# ๑۩ ,¸¸,ø¤º°`°๑۞๑",
  #"16" : "Sample",
  #"16" : "Sample",
  }

async def GenerateSingleButton(Text,callback_data):
  Button = InlineKeyboardButton(Text,callback_data=callback_data)
  return Button

async def GetDesignTitle(DesignNumber):
  DesignTitle = DecorateList[DesignNumber]
  return DesignTitle

async def GenerateButtonForDecorate():
  ButtonList = []
  #TotalPageFormed = await GetTotalPageAfterSplit()
  #print(TotalPageFormed)
  #PageOfFonts = await GetPageOfFont(Page_No)
  for DesignNumber in DecorateList:
    Data = await GetDesignTitle(DesignNumber)
    NewBtn = await GenerateSingleButton(Data,"['CF','" + DesignNumber + "']")
    #NewBtn = await GenerateSingleButton(Data,"['CF','" + DesignNumber + "','" + str(Page_No) + "']")
    ButtonList.append(NewBtn)
  FinalKeyboard = [ButtonList[i:i+2] for i in range(0, len(ButtonList), 2)]
  x = InlineKeyboardButton("🔙",callback_data="STARTFonting")
  #BackPreclvBtn =  await MakePrevNextKeyboardForFont(TotalPageFormed,Page_No)
  #FinalKeyboard.append(BackPreclvBtn)
  FinalKeyboard.append([x])
  NewKeyBoard = InlineKeyboardMarkup(FinalKeyboard)
  return NewKeyBoard