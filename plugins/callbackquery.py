import logging
import os
from config import Config
import pyrogram
from pyrogram import Client, filters
from plugins import helper
from plugins import currentaffairs
from plugins import ncertbooks
from plugins.urluploader import Urlleaccher
from plugins import Newspapers
import ast


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_callback_query()
async def cb_data(bot, update):
  #print(update.data)
  if (update.data.startswith("['dwnldnewspaper'")):
    #print(update.data)
    Ctgry = ast.literal_eval(update.data)[1]
    Id = ast.literal_eval(update.data)[2]
    Url2Dowload = await Newspapers.geturlfornewpaper(Id,Ctgry)
    await update.reply_text(Url2Dowload)
    #await bot.send_document(chat_id=update.message.chat.id,document=Url2Dowload)
    #Url2Dowload = ncertbooks.geturlforclasssunjevt(classnumber,subject)
    #Url2Dowload = "https://s3-us-west-2.amazonaws.com/visionresources/daily_current_affairs/{}.pdf".format(getcodeheadwithday)
    #print(Url2Dowload)
    #await Urlleaccher(bot,update,Url2Dowload)
  if (update.data.startswith("['dwldboobsncert'")):
    classnumber = ast.literal_eval(update.data)[1]
    subject = ast.literal_eval(update.data)[2]
    Url2Dowload = ncertbooks.geturlforclasssunjevt(classnumber,subject)
    #Url2Dowload = "https://s3-us-west-2.amazonaws.com/visionresources/daily_current_affairs/{}.pdf".format(getcodeheadwithday)
    #print(Url2Dowload)
    await Urlleaccher(bot,update,Url2Dowload)
  if (update.data.startswith("['getsubjctofclass'")):
    classnmbr = ast.literal_eval(update.data)[1]
    Source_List,totalsubjcet = ncertbooks.addsubjectbutton(bot,update,classnmbr)
    newbtns = ncertbooks.makeBtnFromDict(Source_List)
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
    await update.message.edit_text(text="<b>Choose Your Date</b>",reply_markup=newbtns)
  if update.data == "thehindu":
    newbtns = await Newspapers.gettingAllHinduresult(bot,update)
    await update.message.edit_text(text="<b>Searching Latest Newspapers..…..</b>",reply_markup=newbtns)
  if update.data == "newepapers":
    await update.message.edit_text(text="<b>Choose Your News-Paper</b>",reply_markup=Newspapers.NewspaperType)
  if update.data == "vsniascrnt":
    Source_List = currentaffairs.getallmonthfromiasvsncurrentafr(bot,update)
    newbtns = currentaffairs.makeBtnFromDict(Source_List)
    await update.message.edit_text(text="<b>Choose Your Month</b>",reply_markup=newbtns)
  if update.data == "ncertbooks":
    Source_List = ncertbooks.addclasslist(bot,update)
    newbtns = ncertbooks.makeBtnFromDict(Source_List)
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
