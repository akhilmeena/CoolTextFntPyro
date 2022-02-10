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
  "Fraktur" : ['𝔄','𝔅','ℭ','𝔇','𝔈','𝔉','𝔊','ℌ','ℑ','𝔍','𝔎','𝔏','𝔐','𝔑','𝔒','𝔓','𝔔','ℜ','𝔖','𝔗','𝔘','𝔙','𝔚','𝔛','𝔜','ℨ','օ','յ','շ','Յ','կ','Տ','ճ','Դ','Ց','գ','𝔞','𝔟','𝔠','𝔡','𝔢','𝔣','𝔤','𝔥','𝔦','𝔧','𝔨','𝔩','𝔪','𝔫','𝔬','𝔭','𝔮','𝔯','𝔰','𝔱','𝔲','𝔳','𝔴','𝔵','𝔶','𝔷',' '],
  "Bold Fraktur Font" : ['𝕬','𝕭','𝕮','𝕯','𝕰','𝕱','𝕲','𝕳','𝕴','𝕵','𝕶','𝕷','𝕸','𝕹','𝕺','𝕻','𝕼','𝕽','𝕾','𝕿','𝖀','𝖁','𝖂','𝖃','𝖄','𝖅','օ','յ','շ','Յ','կ','Տ','ճ','Դ','Ց','գ','𝖆','𝖇','𝖈','𝖉','𝖊','𝖋','𝖌','𝖍','𝖎','𝖏','𝖐','𝖑','𝖒','𝖓','𝖔','𝖕','𝖖','𝖗','𝖘','𝖙','𝖚','𝖛','𝖜','𝖝','𝖞','𝖟',' '],
  "Fantasy Font" : ['ꪖ','ꪉ','ᨶ','ᦔ','ꫀ','ᠻ','ᦋ','ꫝ','ỉ','᧒','ƙ','ꪶ','ꪑ','᭢','ꪮ','ᩏ','ᧁ','ꪹ','క','ᡶ','ꪊ','ꪜ','᭙','᥊','ꪗ','ɀ','੦','౹','੨','੩','੫','Ƽ','Ϭ','Դ','੪','੧','ꪖ','ꪉ','ᨶ','ᦔ','ꫀ','ᠻ','ᦋ','ꫝ','ỉ','᧒','ƙ','ꪶ','ꪑ','᭢','ꪮ','ᩏ','ᧁ','ꪹ','క','ᡶ','ꪊ','ꪜ','᭙','᥊','ꪗ','ɀ',' '],
  "Flaky Font" : ['ᗩ','ᗷ','ᑕ','ᗪ','ᗴ','ᖴ','Ǥ','ᕼ','I','ᒎ','ᛕ','ᒪ','ᗰ','ᑎ','ᗝ','ᑭ','Ɋ','ᖇ','ᔕ','丅','ᑌ','ᐯ','ᗯ','᙭','Ƴ','乙','੦','౹','੨','੩','੫','Ƽ','Ϭ','Դ','੪','੧','ᗩ','ᗷ','ᑕ','ᗪ','ᗴ','ᖴ','Ǥ','ᕼ','I','ᒎ','ᛕ','ᒪ','ᗰ','ᑎ','ᗝ','ᑭ','Ɋ','ᖇ','ᔕ','丅','ᑌ','ᐯ','ᗯ','᙭','Ƴ','乙',' '],
  "Manga Font" : ['卂','乃','匚','ᗪ','乇','千','Ꮆ','卄','丨','ﾌ','Ҝ','ㄥ','爪','几','ㄖ','卩','Ҩ','尺','丂','ㄒ','ㄩ','ᐯ','山','乂','ㄚ','乙','੦','౹','੨','੩','੫','Ƽ','Ϭ','Դ','੪','੧','卂','乃','匚','ᗪ','乇','千','Ꮆ','卄','丨','ﾌ','Ҝ','ㄥ','爪','几','ㄖ','卩','Ҩ','尺','丂','ㄒ','ㄩ','ᐯ','山','乂','ㄚ','乙',' '],
  "Block Font" : ['🇦‌','🇧‌','🇨‌','🇩‌','🇪‌','🇫‌','🇬‌','🇭‌','🇮‌','🇯‌','🇰‌','🇱‌','🇲‌','🇳‌','🇴‌','🇵‌','🇶‌','🇷‌','🇸‌','🇹‌','🇺‌','🇻‌','🇼‌','🇽‌','🇾‌','🇿‌','0','1','2','3','4','5','6','7','8','9','🇦‌','🇧‌','🇨‌','🇩‌','🇪‌','🇫‌','🇬‌','🇭‌','🇮‌','🇯‌','🇰‌','🇱‌','🇲‌','🇳‌','🇴‌','🇵‌','🇶‌','🇷‌','🇸‌','🇹‌','🇺‌','🇻‌','🇼‌','🇽‌','🇾‌','🇿‌',' '],
  "Black bubble Font" : ['🅐','🅑','🅒','🅓','🅔','🅕','🅖','🅗','🅘','🅙','🅚','🅛','🅜','🅝','🅞','🅟','🅠','🅡','🅢','🅣','🅤','🅥','🅦','🅧','🅨','🅩','⓿','➊','➋','➌','➍','➎','➏','➐','➑','➒','🅐','🅑','🅒','🅓','🅔','🅕','🅖','🅗','🅘','🅙','🅚','🅛','🅜','🅝','🅞','🅟','🅠','🅡','🅢','🅣','🅤','🅥','🅦','🅧','🅨','🅩',' '],
  "Bold Script Font" : ['𝓐','𝓑','𝓒','𝓓','𝓔','𝓕','𝓖','𝓗','𝓘','𝓙','𝓚','𝓛','𝓜','𝓝','𝓞','𝓟','𝓠','𝓡','𝓢','𝓣','𝓤','𝓥','𝓦','𝓧','𝓨','𝓩','0','1','2','3','4','5','6','7','8','9','𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾','𝓿','𝔀','𝔁','𝔂','𝔃',' '],
  "Wierd Font" : ['Ȧ̶̵̗̳','B̟̈́̆̐̄̚͜','C̸̣̭͖̤̒̈͊͟','Ḋ̤͇̮͙ͥ','E̸̖̪̱͚ͨ̀͜','F̵̦̺͕́̐͟','G̛͔͇̞̹̈̀͘͘͟','H̶̪͍̒ͥ͑̓','I̶̴̗̗̦͍ͨͭ̉͢͟','J̸̧̪̫̫̩̿͗͑̇̕͟','K̦̖̙̱̮̐̌','L̳͈͉̅̊','M̶̷̲̊ͥ͋͟','N̰̜͉͔ͬ̽͢','O̵̷̪̰ͩ͆ͅ','P̘͎̀͊','Q̸̨͉̰̰ͬ','Ŗ̴̪̈̄͞','S̵̶̮̬͖̄͑͟','T̷̫͉̰͕̒́','U̸̫̠̰͈̕','V̷̬̈ͫ͢͢͝','W̸͈ͯ̾̒̿','X̸̵̨ͦ̒ͣ','Y̵̷̛̤͍̅́̕','Z̴̨͇͖͓̋̊','0̴̫͙͙̪̔̽̔͛͘','1̷̸̫̐͂̕','2̱̜̥̒̌̂̕͟','3̵̷̧̗͙̰̽̋͟','4̷̱ͧͩ̈̀͢͜','5̸̷͇̽̏ͥͤ','6̶̴̱ͧ̓͋̄͡','7̨͈͇̙̤ͩ͜','8̷̴̹̅̑ͬ̓͟','9̶̵̜͑͌͞','ă̶̸̝ͦ͊̿͋͞','b̵̸͙̅̽͡ͅ','c̷̹͖͋́̃','d̸̡̩͍̔ͥ͜','ę̷̵̧̖̫̗̆̊','f̷̵̫̞̉͢','g̴̶̛̮̣͙͠','h̶̯̰̝̻̿̓͢','i̵͓͙̱͚̎͟','j̧͉̺̤̎ͯ','k̶̸͙̭̹͆͟','ḻ̸͈ͧ͑̓̓̀͡','m̶̷͔ͪ̽͡','n̷̶̯͉̊̽̐ͦ͘','ȍ̸̢̢̮͚̐̚','p̶̸̨̺͊̍̒̓̀','q̷̝ͣ͑̌͢','r̶̷̲͍̭͐̾̀͟','s̩͙͖̋͛͟','t̴͕͖͓̀','û̶͙̽̿͆̈','v̸̵̝͙͆̈ͤ','ẅ̷̷̢̟͇͈̒','x̷̶͚͖͓̘̔','y̯̤͑́́̓́','z͕͓̼̼̽̃͘',' '],
}
  
  #"Bold " : [],
AlphabetList =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz "
FontInOnePage = 10
async def GenerateSingleButton(Text,callback_data):
  Button = InlineKeyboardButton(Text,callback_data=callback_data)
  return Button

async def CreateFontFromText(Text,Font_Name):
  GetFontList = FontsList[Font_Name]
  TextCharchaterList = list(f"{Text}")
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
  
def split_dict(d,n):
  keys = list(d.keys())
  for i in range(0, len(keys), n):
    yield {k: d[k] for k in keys[i: i + n]}

async def GetPageOfFont(PageNo):
  Total_Pages = []
  for item in split_dict(FontsList, FontInOnePage):
    Total_Pages.append(item)
  return Total_Pages[PageNo]
    
async def GetTotalPageAfterSplit():
  TotalFont = len(FontsList)
  q = TotalFont//FontInOnePage
  mod = TotalFont % FontInOnePage
  if mod >= 1:
    q=+1
  return q

async def MakePrevNextKeyboardForFont(TotalPageFormed,CurrentPage):
  ButtonList = []
  print(TotalPageFormed)
  print(CurrentPage)
  x1 = InlineKeyboardButton("⏮️",callback_data="['ChangePage','0']")
  if int(CurrentPage) in [0]:
    pass
  else:
    ButtonList.append(x1)
  x2 = InlineKeyboardButton("◀️",callback_data="['ChangePage','"+str(CurrentPage-1)+"']")
  if int(CurrentPage) in [0,1]:
    pass
  else:
    ButtonList.append(x2)
  x3 = InlineKeyboardButton("▶️",callback_data="['ChangePage','"+str(CurrentPage+1)+"']")
  if int(CurrentPage) in [int(TotalPageFormed),int(TotalPageFormed)-1]:
    pass
  else:
    ButtonList.append(x3)
  x4 = InlineKeyboardButton("⏭️",callback_data="['ChangePage','"+str(TotalPageFormed)+"']")
  if int(CurrentPage) in [int(TotalPageFormed)]:
    pass
  else:
    ButtonList.append(x4)
  return ButtonList
  
async def GenerateButtonForF9ntList(Page_No):
  ButtonList = []
  TotalPageFormed = await GetTotalPageAfterSplit()
  PageOfFonts = await GetPageOfFont(Page_No)
  for Font_Name in PageOfFonts:
    Data = await CreateFontFromText(Font_Name,Font_Name)
    NewBtn = await GenerateSingleButton(Data,"['CF','" + Font_Name + "']")
    ButtonList.append(NewBtn)
  FinalKeyboard = [ButtonList[i:i+2] for i in range(0, len(ButtonList), 2)]
  x = InlineKeyboardButton("🔙",callback_data="STARTFonting")
  BackPreclvBtn =  await MakePrevNextKeyboardForFont(TotalPageFormed,0)
  FinalKeyboard.append(BackPreclvBtn)
  FinalKeyboard.append([x])
  NewKeyBoard = InlineKeyboardMarkup(FinalKeyboard)
  return NewKeyBoard
