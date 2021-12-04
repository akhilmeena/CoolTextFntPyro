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
    'Maths' : 'https://freehomedelivery.net/wp-content/uploads/2017/02/NCERT-Class-5-Mathematics.pdf',
    'EVS' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-5-Environmental-Science.pdf',
    'English' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-5-English.pdf'
  },
  'Class 6' : {
    'English (Part 1)' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-6-English-Part-1.pdf',
    'English (Part 2)' : 'https://freehomedelivery.net/wp-content/uploads/2017/03/NCERT-Class-6-English-Part-2.pdf',
    'Hindi (Part 1)' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-6-Hindi-Part-1.pdf',
    'Hindi (Part 2)' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-6-Hindi-Part-2.pdf',
    'Hindi (Part 3)' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-6-Hindi-Part-3.pdf',
    'Maths':'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-6-Mathematics.pdf',
    'Science':'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-6-Science.pdf',
    'History':'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-6-History.pdf',
    'Political Science':'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-6-Political-Science.pdf',
    'Geography':'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-6-Geography.pdf',
    'Sanskrit':'https://freehomedelivery.net/wp-content/uploads/2019/04/fhsk1dd.zip'
  },
  'Class 7' : {
    'English-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-7-English-Part-1.pdf',
    'English-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-7-English-Part-2.pdf',
    'Hindi' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-7-Hindi.pdf',
    'Mathematics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Mathematics.pdf',
    'Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Science.pdf',
    'History' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-History.pdf',
    'Political-Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Political-Science.pdf',
    'Geography' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Geography.pdf',
    'Sanskrit' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Sanskrit.pdf',
    'Environmental-Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-7-Environmental-Science.pdf'
  },
  'Class 8' : {
    'English-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-8-English-Part-1.pdf',
    'English-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-8-English-Part-2.pdf',
    'Hindi-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-8-Hindi-Part-1.pdf',
    'Hindi-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-8-Hindi-Part-2.pdf',
    'Hindi-Part-3' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-8-Hindi-Part-3.pdf',
    'Mathematics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-8-Mathematics.pdf',
    'Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-8-Science.pdf',
    'History' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-8-History.pdf',
    'Political-Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-8-Political-Science.pdf',
    'Geography' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-8-Geography.pdf',
    'Sanskrit' : 'https://freehomedelivery.net/wp-content/uploads/2019/04/hhsk1dd.zip'
  },
  'Class 9' : {
    'English-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-English-Part-1.pdf',
    'English-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-English-Part-2.pdf',
    'Hindi-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-9-Hindi-Part-1.pdf',
    'Hindi-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-9-Hindi-Part-2.pdf'
    #'Hindi-Part-3' : '',
    'Hindi-Part-4' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-9-Hindi-Part-4.pdf',
    'Mathematics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Mathematics.pdf',
    'Mathematics-Exemplar-Problems' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Mathematics-Exemplar-Problems.pdf',
    'Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Science.pdf',
    'Economics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Economics.pdf',
    'Geography' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Geography-1.pdf',
    'Political-Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-Political-Science.pdf',
    'History' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-9-History.pdf',
    'Sanskrit' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-9-Sanskrit.pdf'
  },
  'Class 10' : {
    'English-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-English-Part-1.pdf',
    'English-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-English-Part-2.pdf',
    'Hindi-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-10-Hindi-Part-1.pdf'
    #'Hindi-Part-2' : '',
    'Hindi-Part-3' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-10-Hindi-Part-3.pdf',
    'Hindi-Part-4' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Hindi-Class-10-Hindi-Part-4.pdf',
    'Mathematics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Mathematics.pdf',
    'Mathematics-Exemplar-Problems' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Mathematics-Exemplar-Problems.pdf'
    #'Science' : '',
    'Science-Exemplar-Problems' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Science-Exemplar-Problems-1.pdf',
    'Economics' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Economics.pdf',
    'Geography' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Geography.pdf',
    'Political-Science' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Political-Science.pdf',
    'History' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-History.pdf',
    'Sanskrit' : 'https://freehomedelivery.net/wp-content/uploads/2016/12/NCERT-Class-10-Sanskrit.pdf'
  },
  'Class 11' : {
    'Economics' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Economics.pdf',
    'English Woven Words' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-English-Part-1.pdf',
    'English Horn Bill' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-English-Part-2.pdf',
    'Geography-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Geography-Part-1.pdf',
    'Geography-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Geography-Part-2.pdf',
    'Geography-Practical' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Geography-Practical.pdf',
    'Hindi-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Hindi-Class-11-Hindi-Part-1.pdf',
    'Hindi-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Hindi-Class-11-Hindi-Part-2.pdf',
    'Hindi-Part-3' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Hindi-Class-11-Hindi-Part-3.pdf',
    'Hindi-Part-4' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Hindi-Class-11-Hindi-Part-4.pdf',
    'Mathematics' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Mathematics-1.pdf',
    'Physics-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Physics-Part-1-1.pdf',
    'Physics-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Physics-Part-2-1.pdf',
    'Indian Constitution at Work' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Political-Science-Part-1.pdf',
    'Political Theory' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Political-Science-Part-2-1.pdf',
    'Sanskrit (Shashvati)' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Sanskrit-Part-1.pdf',
    'Sanskrit (Bhaswati)' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Sanskrit-Part-2.pdf',
    'Sociology-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Sociology-Part-1.pdf',
    'Sociology-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Sociology-Part-2.pdf',
    'Urdu-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Urdu-Part-1.pdf',
    'Urdu-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-11-Urdu-Part-2.pdf'
  },
  'Class 12' : {
    'Accountancy-Part-1' : 'https://freehomedelivery.net/wp-content/uploads/2017/07/NCERT-Class-12-Accountancy-Part-1.pdf',
    'Accountancy-Part-2' : 'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Accountancy-Part-2.pdf',
    'Biology':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Biology.pdf',
    'Chemistry-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Chemistry-Part-1.pdf',
    'Chemistry-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Chemistry-Part-2.pdf',
    'Micro Economics Part 1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Economics-Part-1.pdf',
    'Economics Macro – Part 2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Economics-Part-2.pdf',
    'English Flamingo':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-English-Part-2.pdf',
    'Geography-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Geography-Part-1.pdf',
    'Mathematics-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Mathematics-Part-1.pdf',
    'Mathematics-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Mathematics-Part-2.pdf',
    'Physics-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Physics-Part-1.pdf',
    'Physics-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Physics-Part-2.pdf',
    'Political-Science-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Political-Science-Part-1.pdf',
    'Political-Science-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Political-Science-Part-2.pdf',
    'Psychology':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Psychology.pdf',
    'Sanskrit-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Sanskrit-Part-1.pdf',
    'Sanskrit-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Sanskrit-Part-2-1.pdf',
    'Sociology-Part-1':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Sociology-Part-1.pdf',
    'Sociology-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Sociology-Part-2.pdf',
    'Urdu-Part-1':'https://freehomedelivery.net/wp-content/uploads/2019/07/NCERT-Class-12-Urdu-Part-1.pdf',
    'Urdu-Part-2':'https://freehomedelivery.net/wp-content/uploads/2016/11/NCERT-Class-12-Urdu-Part-2.pdf'
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


def geturlforclasssunjevt(classnumber,subject):
  Url2Dowload = NCERTBOOKSPDF[f"Class {classnumber}"][f"{subject}"]
  return Url2Dowload


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
