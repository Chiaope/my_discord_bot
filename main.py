import config
import Reminder_Function as rf
from replit import db
from keep_alive import keep_alive
import Commands

client = config.myClient

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    if db["bossTime"]:
      print("Reloading boss timer")
      client.loop.create_task(rf.setBossTime())
    print(f'Role is {db["role"]}')
    print(f'Role: {type(db["role"])}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await Commands.checkCommands(message)
            
keep_alive()        
client.run(config.TOKEN)