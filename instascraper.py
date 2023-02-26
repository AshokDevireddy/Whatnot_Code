from instabot import Bot
import os 
import glob

bot = Bot()

#clearing data from previous request
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

#sending the message
bot.login(username="yashwang23", password="testingwhatnot")
bot.send_message("This is a test message", ["ashok.dvrddy"])