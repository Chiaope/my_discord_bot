from datetime import datetime, timedelta
import config
import asyncio
import pytz
from replit import db
from discord.utils import get


sleepTime = config.sleepTime
myTimeZone = config.myTimeZone
thingsToRemember = config.thingsToRemember

def checkTime():
    try:
      currBossTime = datetime.fromisoformat(db["bossTime"]).replace(tzinfo=myTimeZone)
      earlyTime = (datetime.fromisoformat(db["bossTime"]) - timedelta(minutes=db["bossNotifierTime"])).replace(tzinfo=myTimeZone)
    except:
      currBossTime = None
      earlyTime = None
      
    print(f'EarlyTime: {earlyTime}')
    print(f'currBossTime: {currBossTime}')
    check = datetime.now(pytz.timezone('Asia/Singapore'))
    
    if currBossTime == None:
        print("Reminder has been cancelled")
        return 1
    
    if currBossTime <= check:
        print("Real Trigger~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return 3

    elif db["bufferFlag"] == False and earlyTime <= check:
        print("Trigger~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return 2

    else:
        print(f"Current time is {check}")

async def setBossTime():
    check = datetime.now(pytz.timezone('Asia/Singapore'))
    earlyTime = (datetime.fromisoformat(db["bossTime"]) - timedelta(minutes=db["bossNotifierTime"])).replace(tzinfo=myTimeZone)
    if check < earlyTime:
      db["bufferFlag"] = False
      print("Changing triggered to False")
      
    while True:
        condition = checkTime()
        if condition == 1:
            break
        elif condition == 2:
            if db["bufferFlag"] == False:
                channel = config.myClient.get_channel(db["channel_to_run_id"])
                
                await channel.send(f'{db["role"]} \nGet Ready to Boss at {datetime.fromisoformat(db["bossTime"]).time()} or isvckdick will come svckysvcky')
                db["bufferFlag"] = True
        elif condition == 3:
            channel = config.myClient.get_channel(db["channel_to_run_id"])

            myStr = ""
            for i in thingsToRemember:
              myStr = myStr + "- " + str(i) +"\n"
            await channel.send(f'{db["role"]} \nIt is bossing time: {datetime.fromisoformat(db["bossTime"]).time()} \nReminder to check the following:\n{myStr}')
            
            db["bossTime"] = None
            break
        await asyncio.sleep(sleepTime)
    print("Ended Loop")
    condition = None