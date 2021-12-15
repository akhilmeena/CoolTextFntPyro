import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
from plugins import helper
from plugins import currentaffairs
from plugins import ncertbooks
from pyrogram import types
from pyrogram.types import CallbackQuery, ChatPermissions, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.urluploader import Urlleaccher
from plugins import Newspapers
from plugins import WorkWithPDF
import ast


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  if (update.data.startswith("['indxchlacdmy'")):
    try:
      CHAT_ID = update.message.chat.id
    except:
      CHAT_ID = update.chat.id
    Date = ast.literal_eval(update.data)[1]
    Code = ast.literal_eval(update.data)[2]
    UrlToChlAcdyCrnAfr = "https://chahalacademy.com/daily-current-affairs/" + str(Date) + "/" + str(Code)
    file_path = await WorkWithPDF.GenerateScrennshotFromUrl(UrlToChlAcdyCrnAfr,update)
    mfile_path = await WorkWithPDF.GenratePdfFromImg(update,file_path,Date)
    #print(SShotName)
    akhil =  open(mfile_path, 'rb')
    await bot.send_document(chat_id=CHAT_ID,document=akhil)
  if update.data == "chahalacdmy":
    Source_List = await currentaffairs.getalldateswithlinkfromchahalacadmy(bot,update)
    newbtns = currentaffairs.makeBtnFromDict(Source_List)
    await update.message.edit_text(text=f"<b>Choose Your Date</b>",reply_markup=newbtns)
  if (update.data.startswith("['dwnldnewspaper'")):
    Id = ast.literal_eval(update.data)[1]
    Forwhat = ast.literal_eval(update.data)[2]
    try:
      Textfornewspaperwithanylss = await Newspapers.captionfornewslink(Id,Forwhat)
    except:
      if str(Forwhat) == "dainikjagaran":
        Textfornewspaperwithanylss = await Newspapers.captionfornewslinkdainikjagaran(Id,Forwhat)
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
  if update.data == "help":
    await update.message.edit_text(text=helper.HELPTEXT,reply_markup=helper.HELP_BUTTONS)
  if update.data == "abtdvlngbot":
    await update.message.edit_text(text=helper.BotAboutText.format(update.message.from_user.mention),reply_markup=helper.DVLGBTN)
  if update.data == "BacktoAdminpnl":
    await update.message.edit_text(text="<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
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
