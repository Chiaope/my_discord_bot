from datetime import datetime, timedelta
import config
import pytz

daysInWeek = config.daysInWeek

def nextWeekDay(theDay): # get the date for nearest "weekday name"
    currDate = datetime.now(pytz.timezone('Asia/Singapore'))
    daysAhead = theDay - currDate.weekday()
    if daysAhead <= 0:
        daysAhead += 7
    return currDate + timedelta(daysAhead)

def decodeDateInput(userInput): # convert the "day name" into number
    userInput = userInput.split(" ")
    userInput[0] = str(daysInWeek.index(userInput[0].lower()))
    return userInput

def nameFormat(userInput):
    try:
        userInput = decodeDateInput(userInput)
        getBossDatetime = nextWeekDay(int(userInput[0]))
        getBossDatetime = getBossDatetime.replace(hour = int(userInput[1][0:2]))
        getBossDatetime = getBossDatetime.replace(minute = int(userInput[1][2:]))
        getBossDatetime = getBossDatetime.replace(second = 0, microsecond = 0)       
        print(f"Setting reminder on, {getBossDatetime.strftime('%a')}, {getBossDatetime.date()}, {getBossDatetime.hour}:{getBossDatetime.minute}")
        return getBossDatetime

    except:
        print("Something wrong")
        return None

def dateFormat(userInput):
    userInput = datetime.strptime(userInput, "%d/%m %H%M")
    userInput = userInput.replace(year = datetime.now(pytz.timezone('Asia/Singapore')).year)
    return userInput

def todayFormat (userInput) :
  singaporeDateTime = datetime.now(pytz.timezone('Asia/Singapore'))
  getTimeOnly = userInput.split()[1]
  correctDateTime = datetime.strptime(getTimeOnly, "%H%M")
  correctDateTime = correctDateTime.replace(year = singaporeDateTime.year, month = singaporeDateTime.month, day = singaporeDateTime.day)

  return correctDateTime


def setDateTime(userInput):
    userInput = userInput.lower()
    if userInput.startswith(tuple(daysInWeek)):
        return nameFormat(userInput)
    elif userInput.split()[0] == "today":
      return todayFormat(userInput)
    else:
        try:
            return dateFormat(userInput)
        except:
            return None
    