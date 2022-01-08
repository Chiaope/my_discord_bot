import config
from replit import db

client = config.myClient

cmdNotifyHere = "$notifyhere"

cmdNotifyHereEmpty = "{Blank}"
cmdNotifyHereEmptyD = "Will direct the reminders to this channel"

cmdNotifyHereSet = "{channal ID}"
cmdNotifyHereSetD = "Will direct the reminders to this channel via channel ID"

allcmdNotifyHere = [
                [cmdNotifyHereEmpty, cmdNotifyHereEmptyD], 
                [cmdNotifyHereSet,cmdNotifyHereSetD]
                ]

config.cmdDict[cmdNotifyHere] = allcmdNotifyHere

async def notifyThisChannelCommands(message):
  getMessage = message.content.strip().lower().replace("$notifyhere", "")
  if getMessage == "":
    try:
      db["channel_to_run_id"] = message.channel.id
      channelName = client.get_channel(db["channel_to_run_id"])
      
      await message.channel.send(f'Notification will be sent to channel {channelName}.')
      return
    except:
      await message.channel.send(f'Please try again.')
      return
  else:
    try: 
      channelID = int(getMessage)
      channelName = client.get_channel(channelID)
      if channelName != None:
        db["channel_to_run_id"] = channelID
        await message.channel.send(f'Notification will be sent to channel {channelName}')
      else:
        raise Exception
    except:
      await message.channel.send(f'Please enter correct Channel ID')
      return