import config
from replit import db

async def getRole(myRoles = config.defaultRole):

  for guild in config.myClient.guilds:
    print(guild.name)

    for role in guild.roles:
      print(guild.name)
      print(role.name)
      if role.name == myRoles:
        return role.mention

  return "@everyone"

async def checkRoleCommands(message):
  getMessage = message.content.strip().lower().replace("$role", "")
  
  if getMessage == "":
    await message.channel.send(f'Role: {db["role"]}')

  else:
    flag = getRole(getMessage)
    if flag == False:
      await message.channel.send("Dont have role, will use @everyone instead")
      db["role"] = "@everyone"
    else:
      db["role"] = flag
      
  return