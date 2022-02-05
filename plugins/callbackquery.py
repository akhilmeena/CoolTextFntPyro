import os
import ast
import time
import logging
import pyrogram
from config import Config
from config import Config
from pyrogram import Client, filters
from plugins import helper
from pyrogram import types
from pyrogram.types import CallbackQuery, ChatPermissions, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import Database
from plugins import Wallet



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

Current_Operation = []

async def GetRunningOprtn():
  Current_Operation1 = Current_Operation[0]
  return Current_Operation1

@Client.on_callback_query()
async def cb_data(bot, update):
  if (update.data.startswith("['MnthlyCA'")):
    Title = ast.literal_eval(update.data)[1]
    Lan = ast.literal_eval(update.data)[2]
    DwnldUrl = await currentaffairs.GetLinkOfMonthlyCurrentAdda24x7(Title,Lan)
    await Urlleaccher(bot,update,DwnldUrl)
  if update.data == "Add24x7":
    await currentaffairs.MonthlyCureentAffaisrsAdd247x7()
    newbtns = await currentaffairs.MakeButtonFor27x7Add()
    await update.message.edit_text(text="<b>🧭 Choose Your Month</b>",reply_markup=newbtns)
  if update.data == "BooksCollction":
    newbtns = await Books.BookTypeButton()
    await update.message.edit_text(text="<b>🎯 Choose Your Books</b>",reply_markup=newbtns)
  if update.data == "requestnewspaper":
    Current_Operation.clear()
    Current_Operation.append("requestnewspaper")
    await TextHandler.NewspaperName(bot, update)
    #print(update)
    #await update.message.reply_text(f"Good")
  if update.data == "sarakriresult":
    URL = "https://www.sarkariresult.com/result.php"
    ResultList = await Job.GetAllResultsOrAdmitCardLink(URL)
    await update.message.edit_text(text=f"<b>Here is Result From Sarakri Result Website</b>{ResultList}",reply_markup=Job.RESULT_BUTTONS,disable_web_page_preview=True)
  if update.data == "sarakariadmitcards":
    URL = "https://www.sarkariresult.com/admitcard.php"
    ResultList = await Job.GetAllResultsOrAdmitCardLink(URL)
    await update.message.edit_text(text=f"<b>Here is Admit Cards From Sarakri Result Website</b>{ResultList}",reply_markup=Job.ADMITCARD_BUTTONS,disable_web_page_preview=True)
  if update.data == "jobalert":
    jobList = await Job.GetAllLatestJobs()
    await update.message.edit_text(text=f"<b>Here is Latest Jobs From Sarakri Result Website</b>{jobList}",reply_markup=Job.JOB_BUTTONS,disable_web_page_preview=True)
  if (update.data.startswith("['dwnldmagz'")):
    Id = ast.literal_eval(update.data)[1]
    MagziCompany = ast.literal_eval(update.data)[2]
    Month,LinkMagzine,Lang = await Magzines.GetLinkDateLang(Id,MagziCompany)
    Url2Dowload = f"{LinkMagzine}".replace(" ","%20")
    await Urlleaccher(bot,update,Url2Dowload)
    #await update.message.reply_text(f"<b>{Month}\n{LinkMagzine}\n{Lang}</b>")
  if (update.data.startswith("['MazFromChahal'")):
    DwnldCode = ast.literal_eval(update.data)[1]
    Lang = ast.literal_eval(update.data)[2]
    Data = await Magzines.getDataChahalMagzResult(bot,update,Lang,DwnldCode)
    #print(Data)
    Source_List = await Magzines.getAllChahalMagzResult(bot,update,Data,DwnldCode)
    newbtns = await Magzines.makeBtnFromDict(Source_List)
    await update.message.edit_text(text="<b>🎯 Choose Your Magzine</b>",reply_markup=newbtns)
  if update.data == "magzines":
    await update.message.edit_text(text="<b>🎯 Choose Your Magzines To Download</b>",reply_markup=Magzines.MagzinesType)
  if (update.data.startswith("['indxchlacdmy'")):
    try:
      CHAT_ID = update.message.chat.id
    except:
      CHAT_ID = update.chat.id
    Date = ast.literal_eval(update.data)[1]
    Code = ast.literal_eval(update.data)[2]
    msg = await update.message.reply_text("<b>Generating Link....</b>")
    UrlToChlAcdyCrnAfr = "https://chahalacademy.com/daily-current-affairs/" + str(Date) + "/" + str(Code)
    msg = await msg.edit("<b>Generating Images....</b>")
    file_path = await WorkWithPDF.GenerateScrennshotFromUrl(UrlToChlAcdyCrnAfr,update)
    msg = await msg.edit("<b>Generating PDF....</b>")
    await WorkWithPDF.CropImage(0,280,0,500,file_path)
    mfile_path,newFileName = await WorkWithPDF.GenratePdfFromImg(update,file_path,Date)
    msg = await msg.edit("<b>Uploading PDF....</b>")
    doc =  open(mfile_path, 'rb')
    c_time = time.time()
    thumb_image_path =  open(Config.LoGoPath, 'rb')
    await bot.send_document(chat_id=CHAT_ID,document=doc,file_name=newFileName,
      thumb=thumb_image_path,force_document=True,caption=f"<b>{newFileName}</b>",progress=progress_for_pyrogram,
      progress_args=(f"<b>File is Uploading ⌛</b>\n\n<b>🗂️ File Name :</b> <code>{newFileName}</code>",msg, c_time))
    doc.close()
    await msg.delete()
    os.remove(mfile_path)
  if update.data == "chahalacdmy":
    Source_List = await currentaffairs.getalldateswithlinkfromchahalacadmy(bot,update)
    newbtns = currentaffairs.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Your Date</b>",reply_markup=newbtns)
  if (update.data.startswith("['dwnldnewspaper'")):
    Id = ast.literal_eval(update.data)[1]
    Forwhat = ast.literal_eval(update.data)[2]
    #try:
    #except:
    #Textfornewspaperwithanylss = await Newspapers.captionfornewslink(Id,Forwhat)
    if str(Forwhat) == "dainikjagaran":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkdainikjagaran(Id,Forwhat)
    elif str(Forwhat) == "thehindu":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslink(Id,Forwhat)
    elif str(Forwhat) == "amarujala":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkAmarujala(Id,Forwhat)
    elif str(Forwhat) == "navbharattimes":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkNavbharattimes(Id,Forwhat)
    elif str(Forwhat) == "newduniyaa":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkNewduniyaa(Id,Forwhat)
    elif str(Forwhat) == "rjpatrika":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkRjpatrika(Id,Forwhat)
    elif str(Forwhat) == "dainikbhaskar":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkDainikbhaskar(Id,Forwhat)
    elif str(Forwhat) == "financialexpress":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkfinancialexpress(Id,Forwhat)
    elif str(Forwhat) == "economictimes":
      Textfornewspaperwithanylss = await Newspapers.captionfornewslinkEconomictimes(Id,Forwhat)
    else:
      Textfornewspaperwithanylss = await Newspapers.captionfornewslink1(Id,Forwhat)
    newbtns = InlineKeyboardMarkup([[InlineKeyboardButton("🔙",callback_data=Forwhat)]])
    await update.message.edit_text(text=Textfornewspaperwithanylss,reply_markup=newbtns)
  if (update.data.startswith("['dwldboobsncert'")):
    classnumber = ast.literal_eval(update.data)[1]
    subject = ast.literal_eval(update.data)[2]
    Url2Dowload = await ncertbooks.geturlforclasssunjevt(classnumber,subject)
    #Url2Dowload = "https://s3-us-west-2.amazonaws.com/visionresources/daily_current_affairs/{}.pdf".format(getcodeheadwithday)
    print(Url2Dowload)
    await Urlleaccher(bot,update,Url2Dowload)
  if (update.data.startswith("['getsubjctofclass'")):
    classnmbr = ast.literal_eval(update.data)[1]
    Source_List,totalsubjcet = await ncertbooks.addsubjectbutton(bot,update,classnmbr)
    newbtns = await ncertbooks.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=ncertbooks.ClasssubjctText.format(classnmbr,classnmbr,totalsubjcet),reply_markup=newbtns)
  if (update.data.startswith("['crnttodayvsnias'")):
    getcodeheadwithday = ast.literal_eval(update.data)[1]
    Url2Dowload = "https://s3-us-west-2.amazonaws.com/visionresources/daily_current_affairs/{}.pdf".format(getcodeheadwithday)
    await Urlleaccher(bot,update,Url2Dowload)
  if (update.data.startswith("['getcurrentofmonthvsnias'")):
    month_num = ast.literal_eval(update.data)[1]
    year_num = ast.literal_eval(update.data)[2]
    Source_List = currentaffairs.currentdaypdfbuttonvsnias(month_num,year_num)
    newbtns = currentaffairs.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Your Date</b>",reply_markup=newbtns)
  if update.data == "amarujala":
    await update.answer(text = Newspapers.AmarujalaNotification, show_alert=True)
    Source_List = await Newspapers.gettingallAmarujalaresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "navbharattimes":
    await update.answer(text = Newspapers.NavbharattimesNotification, show_alert=True)
    Source_List = await Newspapers.gettingallNavbharattimesresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "newduniyaa":
    await update.answer(text = Newspapers.NewduniyaaNotification, show_alert=True)
    Source_List = await Newspapers.gettingallNewduniyaaresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "dainikbhaskar":
    await update.answer(text = Newspapers.DainikbhaskarNotification, show_alert=True)
    Source_List = await Newspapers.gettingallDainikbhaskarresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "rjpatrika":
    await update.answer(text = Newspapers.RjpatrikaNotification, show_alert=True)
    Source_List = await Newspapers.gettingallRjpatrikaresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "dainikjagaran":
    await update.answer(text = Newspapers.DainikJagranNotification, show_alert=True)
    Source_List = await Newspapers.gettingallDainikJagranresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "economictimes":
    await update.answer(text = Newspapers.EconomicTimesNotification, show_alert=True)
    Source_List = await Newspapers.gettingallEconomictimesresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "financialexpress":
    await update.answer(text = Newspapers.FinancialExpressNotification, show_alert=True)
    Source_List = await Newspapers.gettingallFinancialExpressresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "timesofindia":
    await update.answer(text = Newspapers.TimesOfIndiaNotification, show_alert=True)
    Source_List = await Newspapers.gettingallTOIresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "thehindu":
    await update.answer(text = Newspapers.TheHinduNotification, show_alert=True)
    Source_List = await Newspapers.gettingAllHinduresult(bot,update)
    newbtns = await Newspapers.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Date.</b>\n{Newspapers.DisclaimerForAll}",reply_markup=newbtns)
  if update.data == "newepapers":
    await update.message.edit_text(text="<b>Choose Your News-Paper</b>",reply_markup=Newspapers.NewspaperType)
  if update.data == "vsniascrnt":
    Source_List = currentaffairs.getallmonthfromiasvsncurrentafr(bot,update)
    newbtns = currentaffairs.makeBtnFromDict(Source_List)
    await update.message.edit_text(text="<b>Choose Your Month</b>",reply_markup=newbtns)
  if update.data == "ncertbooks":
    Source_List = await ncertbooks.addclasslist(bot,update)
    newbtns = await ncertbooks.makeBtnFromDict(Source_List)
    await update.message.edit_text(text="<b>Choose Your Class</b>",reply_markup=newbtns)
  if update.data == "crnafrsdaily":
    await update.message.edit_text(text="<b>Choose Your Source</b>",reply_markup=currentaffairs.CRNTAFRSOURCEBTN)
  if update.data == "libraryopen":
    await update.message.edit_text(text="<b>Choose Your Study Material Items</b>",reply_markup=helper.LBRYOPEN_BUTTONS)
  if update.data == "home2start":
    await update.message.edit_text(text=helper.STARTText.format(update.from_user.mention),reply_markup=helper.START_BUTTONS)
  if update.data == "account":
    try:
      CHAT_ID = update.message.chat.id
    except:
      CHAT_ID = update.chat.id
    UserInvited,BALANCE = await Database.GetBlanceCoinOfUser(CHAT_ID)
    await update.message.edit_text(text=Wallet.AccntDetails.format(BALANCE,UserInvited,CHAT_ID),reply_markup=helper.WALLET_BUTTONS,disable_web_page_preview=True)
  if update.data == "help":
    await update.message.edit_text(text=helper.HELPTEXT,reply_markup=helper.HELP_BUTTONS)
  if update.data == "abtdvlngbot":
    await update.message.edit_text(text=helper.BotAboutText.format(update.message.from_user.mention),reply_markup=helper.DVLGBTN)
  if update.data == "BacktoAdminpnl":
    try:
      await update.message.edit_text(text="<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
    except Exception as e:
      print(e)
  if update.data == "maintainanceoff":
    Config.MaintainaceYN.clear()
    Config.MaintainaceYN.append("YES")
    await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyY)
  if update.data == "maintainanceon":
    Config.MaintainaceYN.clear()
    Config.MaintainaceYN.append("No")
    await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyN)
  if update.data == "chngemaintaincemode":
    if str(Config.MaintainaceYN[0]) == "No":
      await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyN)
    else:
      await update.message.edit_text(text="Change Maintainace Mode",reply_markup=helper.MaintainanceKeyY)
  if update.data == "close":
    await update.message.delete()
  ####################ADMIN PANNEL####################
  if update.data == "vrfyusers":
    values_list3,ttlusers = await Database.GetAllUsersList(bot, update)
    i=0
    j=0
    ak = ""
    msg = await update.message.reply_text(helper.usrststext.format(ttlusers,i,j))
    print(values_list3)
    for p in values_list3:
      try:
        await bot.send_chat_action(chat_id = int(p), action = "typing")
        i+=1
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
      except Exception as e:
        j+=1
        try:
          print(e)
          error = f"{e}".split(":")[0]
          ak+=f"\n{p} {error}"
        except Exception as ex:
          print(ex)
          ak+=f"\n{p} {ex}"
        await msg.edit(helper.usrststext.format(ttlusers,i,j))
    try:
      await update.message.reply_text(f"{ak}")
    except:
      await update.message.reply_text(f"All Users are Active")
  if update.data == "#":
    await update.answer(text = "🛠️ Under Maintenance", show_alert=True)
    

