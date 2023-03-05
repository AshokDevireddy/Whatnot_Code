from instabot import Bot
import os 
import glob
import time, random


try: 
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
except Exception:
    None

bot = Bot()
bot.login(username="nally2345", password="testingwhatnot")

usernames = ["ashok.dvrddy", "shrinandan.kn", "allison23liu", "yashwang23", "maria.xuu", "amandaleong_", "euniceyoon_", "keely_ford", "michelle.j.chen", "ryan.ck8", "berkeleyventure", "kirby.forgor", "waddledeesnutz", "sollem_luv4", "kirbyreelz", "kono.ch", "xionghea", "yoshimayu_", "julie.m.engel", "punkybunny", "ryo.so.ha", "draw_one_draw_two", "figgypuddin_", "zz.mama", "reminababy", "naptimedoodler", "kimi.3t2", "numsiri_", "ahmet_ayy33", "saskueofsharigan", "asiabarbie", "1224heart", "moon195hdoll", "bobajeons", "sopi326"]
messages = "Hi! We’re running marketing and outreach tests on behalf of our company. Please disregard this message and have a great day!"

 


for user in usernames:
        
    bot.send_message(messages, [user])
    print("Sent to ", user)
    time.sleep(random.randrange(15,20))







# os.rmdir("config")

