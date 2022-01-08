import config

cmdDict = config.cmdDict

async def checkHelpCommands(message):
  helpMessage = ""
  for key, value in cmdDict.items():
    for i in cmdDict[key]:
        helpMessage = helpMessage + str(f'{key} {i[0]} \n- {i[1]}\n\n')

  await message.channel.send(helpMessage)
  return