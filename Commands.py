import config
import Commands_Remind as cmdRemind
import Commands_Help as cmdHelp
import Commands_Buffer as cmdBuffer
import Commands_NofiyHere as cmdNotify
import Commands_Role as cmdRole

client = config.myClient

async def checkCommands(message):
  msg = message.content.lower()
  if msg.startswith('$help'):
      await cmdHelp.checkHelpCommands(message)
  elif msg.startswith('$remind'):
    await cmdRemind.checkRemindCommands(message)
  elif msg.startswith('$buffer'):
    await cmdBuffer.checkBufferCommands(message)
  elif msg.startswith('$notifyhere'):
    await cmdNotify.notifyThisChannelCommands(message)
  elif msg.startswith('$role'):
    await cmdRole.checkRoleCommands(message)