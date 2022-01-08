from replit import db
import config

cmdBuffer = "$buffer"

cmdBufferEmpty = "{Blank}"
cmdBufferEmptyD = "Check notification minutes before actual bossing"

cmdBufferSet = "{integers}"
cmdBufferSetD = "Set notification minutes before actual bossing"

allcmdBuffer = [
                [cmdBufferEmpty, cmdBufferEmptyD], 
                [cmdBufferSet,cmdBufferSetD]
                ]

config.cmdDict[cmdBuffer] = allcmdBuffer

async def checkBufferCommands(message):
  getMessage = message.content.strip().lower().replace("$buffer", "")
  if getMessage == "":
    await message.channel.send(f'Current buffer is {db["bossNotifierTime"]} minutes')
    return
  try:
    newBossNotifierTime = int(getMessage)
    if newBossNotifierTime > 720:
      await message.channel.send('Buffer time is too high!! Please enter minutes less than 720')
      return
    else:
      db["bossNotifierTime"] = newBossNotifierTime
      await message.channel.send(f'Updated bossing early noitifier time to {db["bossNotifierTime"]} minutes')

      db["bufferFlag"] = False
      print("Channging triggered to False")                
            
  except:
    await message.channel.send('Please enter only integer numbers in minutes less than 720')
    return