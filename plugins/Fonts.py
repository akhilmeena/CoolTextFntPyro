import json
import pyrogram
from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re

FontsList = {
  "Small caps" : ['ᴀ','ʙ','ᴄ','ᴅ','ᴇ','ғ','ɢ','ʜ','ɪ','ᴊ','ᴋ','ʟ','ᴍ','ɴ','ᴏ','ᴘ','ǫ','ʀ','s','ᴛ','ᴜ','ᴠ','ᴡ','x','ʏ','ᴢ','𝟶','𝟷','𝟸','𝟹','𝟺','𝟻','𝟼','𝟽','𝟾','𝟿','ᴀ','ʙ','ᴄ','ᴅ','ᴇ','ғ','ɢ','ʜ','ɪ','ᴊ','ᴋ','ʟ','ᴍ','ɴ','ᴏ','ᴘ','ǫ','ʀ','s','ᴛ','ᴜ','ᴠ','ᴡ','x','ʏ','ᴢ',' '],
  "Currency" : ['₳','฿','₵','Đ','Ɇ','₣','₲','Ⱨ','ł','J','₭','Ⱡ','₥','₦','Ø','₱','Q','Ɽ','₴','₮','Ʉ','V','₩','Ӿ','Ɏ','Ⱬ','0','1','2','3','4','5','6','7','8','9','₳','฿','₵','Đ','Ɇ','₣','₲','Ⱨ','ł','J','₭','Ⱡ','₥','₦','Ø','₱','Q','Ɽ','₴','₮','Ʉ','V','₩','Ӿ','Ɏ','Ⱬ',' '],
  "Double Struck" : ['𝔸','𝔹','ℂ','𝔻','𝔼','𝔽','𝔾','ℍ','𝕀','𝕁','𝕂','𝕃','𝕄','ℕ','𝕆','ℙ','ℚ','ℝ','𝕊','𝕋','𝕌','𝕍','𝕎','𝕏','𝕐','ℤ','𝟘','𝟙','𝟚','𝟛','𝟜','𝟝','𝟞','𝟟','𝟠','𝟡','𝕒','𝕓','𝕔','𝕕','𝕖','𝕗','𝕘','𝕙','𝕚','𝕛','𝕜','𝕝','𝕞','𝕟','𝕠','𝕡','𝕢','𝕣','𝕤','𝕥','𝕦','𝕧','𝕨','𝕩','𝕪','𝕫',' '],
  "Antrophobia" : ['α','в','¢','∂','є','f','g','н','ι','נ','к','ℓ','м','и','σ','ρ','q','я','ѕ','т','υ','ν','ω','χ','у','z','0','1','2','3','4','5','6','7','8','9','α','в','¢','∂','є','f','g','н','ι','נ','к','ℓ','м','и','σ','ρ','q','я','ѕ','т','υ','ν','ω','χ','у','z',' '],
  "Bubble" : ['Ⓐ','Ⓑ','Ⓒ','Ⓓ','Ⓔ','Ⓕ','Ⓖ','Ⓗ','Ⓘ','Ⓙ','Ⓚ','Ⓛ','Ⓜ','Ⓝ','Ⓞ','Ⓟ','Ⓠ','Ⓡ','Ⓢ','Ⓣ','Ⓤ','Ⓥ','Ⓦ','Ⓧ','Ⓨ','Ⓩ','⓪','①','②','③','④','⑤','⑥','⑦','⑧','⑨','ⓐ','ⓑ','ⓒ','ⓓ','ⓔ','ⓕ','ⓖ','ⓗ','ⓘ','ⓙ','ⓚ','ⓛ','ⓜ','ⓝ','ⓞ','ⓟ','ⓠ','ⓡ','ⓢ','ⓣ','ⓤ','ⓥ','ⓦ','ⓧ','ⓨ','ⓩ',' '],
  "Invisible Ink" : ['A҉','B҉','C҉','D҉','E҉','F҉','G҉','H҉','I҉','J҉','K҉','L҉','M҉','N҉','O҉','P҉','Q҉','R҉','S҉','T҉','U҉','V҉','W҉','X҉','Y҉','Z҉','0҉','1҉','2҉','3҉','4҉','5҉','6҉','7҉','8҉','9҉','a҉','b҉','c҉','d҉','e҉','f҉','g҉','h҉','i҉','j҉','k҉','l҉','m҉','n҉','o҉','p҉','q҉','r҉','s҉','t҉','u҉','v҉','w҉','x҉','y҉','z҉',' ҉'],
  "Fraktur" : ['𝔄','𝔅','ℭ','𝔇','𝔈','𝔉','𝔊','ℌ','ℑ','𝔍','𝔎','𝔏','𝔐','𝔑','𝔒','𝔓','𝔔','ℜ','𝔖','𝔗','𝔘','𝔙','𝔚','𝔛','𝔜','ℨ','օ','յ','շ','Յ','կ','Տ','ճ','Դ','Ց','գ','𝔞','𝔟','𝔠','𝔡','𝔢','𝔣','𝔤','𝔥','𝔦','𝔧','𝔨','𝔩','𝔪','𝔫','𝔬','𝔭','𝔮','𝔯','𝔰','𝔱','𝔲','𝔳','𝔴','𝔵','𝔶','𝔷',' ']
}
AlphabetList =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz "

async def GenerateSingleButton(Text,callback_data):
  Button = InlineKeyboardButton(Text,callback_data=callback_data)
  return Button

async def CreateFontFromText(Text,Font_Name):
  GetFontList = FontsList[Font_Name]
  TextCharchaterList = list(Text)
  TextWithFont = ""
  for i in TextCharchaterList:
    try:
      position = AlphabetList.index(i)
      CharcheterInF9nt = GetFontList[position]
      TextWithFont+=f"{CharcheterInF9nt}"
    except Exception as e:
      TextWithFont+=f"{i}"
  TextWithFont+=""
  return TextWithFont
  
async def GenerateButtonForF9ntList():
  ButtonList = []
  for Font_Name in FontsList:
    Data = await CreateFontFromText(Font_Name,Font_Name)
    NewBtn = await GenerateSingleButton(Data,"['CF','" + Font_Name + "']")
    ButtonList.append(NewBtn)
  FinalKeyboard = [ButtonList[i:i+2] for i in range(0, len(ButtonList), 2)]
  x = InlineKeyboardButton("🔙",callback_data="STARTFonting")
  FinalKeyboard.append([x])
  NewKeyBoard = InlineKeyboardMarkup(FinalKeyboard)
  return NewKeyBoard
