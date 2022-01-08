from replit import db
from datetime import datetime, timedelta
import Formate_Datetime as fdt
import Reminder_Function as rf
import config
import pytz

client = config.myClient

cmdRemind = "$remind"
cmdRemindEmpty = "{Blank}"
cmdRemindEmptyD = "Check boss date/time"
cmdRemindFormate1 = "DD/MM hhmm"
cmdRemindFormate1D = "Set/Update reminder"
cmdRemindFormate2 = "{Name of Day} hhmm"
cmdRemindFormate2D = "Set/Update reminder"
cmdRemindCancel = "cancel"
cmdRemindCancelD = "Cancel reminder"

allCmdRemind = [
                [cmdRemindEmpty, cmdRemindEmptyD], 
                [cmdRemindFormate1,cmdRemindFormate1D], 
                [cmdRemindFormate2,cmdRemindFormate2D], 
                [cmdRemindCancel, cmdRemindCancelD]
                ]

config.cmdDict[cmdRemind] = allCmdRemind

async def checkRemindCommands(message):
  getMessage = message.content.strip().lower().replace("$remind", "")

  channelName = client.get_channel(db["channel_to_run_id"])

  # Empty message after $remind
  if getMessage == "":
      if db["bossTime"] != None:
          getBossTime = datetime.fromisoformat(db["bossTime"]) # convert the string in database to datetime object
          earlyTime = datetime.fromisoformat(db["bossTime"]) - timedelta(minutes=db["bossNotifierTime"])
          
          await message.channel.send(f'Reminder will be sent to\nChannel: {channelName}\nRoles: {config.defaultRole}\nCurrent Boss Time is {getBossTime.strftime("%a")}, {getBossTime.date()}, {getBossTime.time()}\nEarly Notification Time is {earlyTime.strftime("%a")}, {earlyTime.date()}, {earlyTime.time()}')
          return
      else:
          await message.channel.send("No Boss Time Set Yet!!")
          return

  # "cancel" after $remind
  if getMessage == "cancel":
      if db["bossTime"] == None:
          await message.channel.send('There is nothing to cancel')
      else:
          db["bossTime"] = None
          await message.channel.send('Reminder has been cancelled')
      return
      
  validateInput = fdt.setDateTime(getMessage)
  print("ValidateInput : " + str(validateInput))
  if validateInput == None:
    print("Cannot validate")
    await message.channel.send(f'Invalid datetime!! Please enter 1 of 3 valid formats.\n \n1. Name of day: {config.daysInWeek} followed by time\n"(Name of Day) HHMM" format\n2. "DD/MM HHMM" format.\n3. "today HHMM" format."')
    return
  if db["bossTime"] != None:
      db["bossTime"] = str(validateInput)
      getBossTime = datetime.fromisoformat(db["bossTime"])
      earlyTime = (datetime.fromisoformat(db["bossTime"]) - timedelta(minutes=db["bossNotifierTime"])).replace(tzinfo=config.myTimeZone)
      check = datetime.now(pytz.timezone('Asia/Singapore'))
      if check < earlyTime:
        db["bufferFlag"] = False
        print("Changing triggered to False")

      await message.channel.send(f'{db["role"]}\nReminder will be sent to {channelName}\nUpdated Boss Time to {getBossTime.strftime("%a")}, {getBossTime.date()}, {getBossTime.time()}\nEarly Notification Time to {earlyTime.strftime("%a")}, {earlyTime.date()}, {earlyTime.time()}')
  else:
      db["bossTime"] = str(validateInput)
      getBossTime = datetime.fromisoformat(db["bossTime"])
      earlyTime = datetime.fromisoformat(db["bossTime"]) - timedelta(minutes=db["bossNotifierTime"])
      client.loop.create_task(rf.setBossTime())
      await message.channel.send(f'{db["role"]}\nReminder will be sent to {channelName}\nSetting Boss Time to {getBossTime.strftime("%a")}, {getBossTime.date()}, {getBossTime.time()}\nEarly Notification Time to {earlyTime.strftime("%a")}, {earlyTime.date()}, {earlyTime.time()}')
      
  return