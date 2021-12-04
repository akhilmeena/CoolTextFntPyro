import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
import string
import json

Classes = ["1⃣","2⃣","3⃣","4⃣","5⃣","6⃣","7⃣","8⃣","9⃣","🔟","1⃣1⃣","1⃣2⃣"]

NCERTBOOKSPDF = {
  'Class 1' : {
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-1-Hindi.pdf',
    'Maths' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-1-Mathematics.pdf',
    'English' : 'https://freehomedelivery.net/wp-content/uploads/2017/02/NCERT-Class-1-English.pdf'
  },
  'Class 2' : {
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-2-Hindi.pdf',
    'Maths' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-2-Mathematics.pdf',
    'English' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-2-English.pdf'
  },
  'Class 3' : {
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-3-Hindi.pdf',
    'Maths' : 'https://freehomedelivery.net/wp-content/uploads/2017/02/NCERT-Class-3-Mathematics.pdf',
    'EVS' : 'https://freehomedelivery.net/wp-content/uploads/2019/04/ceap1dd.zip',
    'English': 'https://freehomedelivery.net/wp-content/uploads/2017/02/NCERT-Class-3-English.pdf'
  },
  'Class 4' : {
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-4-Hindi.pdf',
    'Maths' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-4-Mathematics.pdf',
    'EVS' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-4-Environmental-Science.pdf',
    'English' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-4-English.pdf'
  },
  'Class 5' : {
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-5-Hindi.pdf',
    'Maths' : '',
    'EVS' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-5-Environmental-Science.pdf',
    'English' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-5-English.pdf'
  },
}

ClasssubjctText = """<b>Class {} NCERT Books PDF Download – All Subjects</b>

<i>NCERT Books For Class {} download for {} in PDF are available for download here . Latest New Edition.</i>"""




def addsubjectbutton(bot,update,classnmbr):
  classsnumber = NCERTBOOKSPDF[f"Class {classnmbr}"]
  Source_List = []
  totalsubjcet = ""
  for subject,url in classsnumber.items():
    addDict = {}
    addList = ["dwldboobsncert"]
    addList.append(str(classnmbr))
    addList.append(str(subject))
    totalsubjcet+=f"{subject},"
    addDict["CallBtnTedt"] = str(f"{subject}")
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List,totalsubjcet


def addclasslist(bot,update):
  Source_List = []
  for clss in range(12):
    addDict = {}
    addList = ["getsubjctofclass"]
    addDict["CallBtnTedt"] = str(f"Class {Classes[clss]}")
    addList.append(str(int(clss) + 1))
    addDict["CallBtnData"] = f"{addList}"
    Source_List.append(addDict)
  return Source_List
        

def makeBtnFromDict(Source_List):
  Btn = []
  for d in Source_List:
    CallbackText = d['CallBtnTedt']
    CallbackData = d['CallBtnData']
    print(CallbackText)
    print(CallbackData)
    x = InlineKeyboardButton(str(CallbackText),callback_data=CallbackData)
    Btn.append(x)
  ak = [Btn[i:i+2] for i in range(0, len(Btn), 2)]
  x = InlineKeyboardButton("🔙",callback_data="libraryopen")
  ak.append([x])
  newbtns = InlineKeyboardMarkup(ak)
  return newbtns
