import os
import discord
from replit import db
from datetime import timezone, timedelta

TOKEN = os.environ['TOKEN']

myClient = discord.Client()

myTimeZone = timezone(timedelta(hours=8))

general_id = int(os.environ['GENERAL_ID'])
test_id = int(os.environ['TEST_ID'])
HBoss_id = int(os.environ['HBOSS_ID'])

defaultRole = "derp"

thingsToRemember = ["Union", "Link Skills", "V Matrix Especially Will Skill", "No Drop Gears", "Hyper Stats", "Feed Your God Dam Pets Fking Animal Abusers"]

cancelFlag = False

daysInWeek = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]

sleepTime = 5

cmdDict = {}

dataBaseKeys = [
  "bossTime", 
  "bossNotifierTime", 
  "bossTimeFlag", 
  "channel_to_run_id", 
  "bufferFlag",
  "role",
  ]
for i in dataBaseKeys:
  if i not in db.keys():
    db[i] = None

if db["bossTime"] == None:
  db["bossTime"] = None

if db["bossNotifierTime"] == None:
  db["bossNotifierTime"] = 1

if db["bossTimeFlag"] == None:
  db["bossTimeFlag"] = None

print("Checking channel_to_run_id")
if db["channel_to_run_id"] == None:
  db["channel_to_run_id"] = HBoss_id

if db["bufferFlag"] == None:
  db["bufferFlag"] = False

print("Checking Role")
if db["role"] == None:
  db["role"] == "@everyone"