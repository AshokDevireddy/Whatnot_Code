from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

my_username = "yashwang23"
my_password = "testingwhatnot"

usernames = ["ashok.dvrddy", "shrinandan.kn", "allison23liu"]

messages = ["this is a test message"]

#browser = webdriver.Chrome('chromedriver_mac_arm64')

def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2,4))

        input_username = browser.find_element("name", 'username')
        input_password = browser.find_element("name", 'password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(Keys.ENTER)
        time.sleep(random.randrange(1,2))

        
    except Exception as err:
        print(err)
        browser.quit()

def send_message(users, messages):
    try:
        #open messages tab
        time.sleep(random.randrange(3,5))
        browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div").click()
        time.sleep(random.randrange(3,5))
        #ignore notification
        browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        
        
        for user in users:

            time.sleep(random.randrange(3,5))
            #click on send message
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button"))).click()
            
            time.sleep(random.randrange(10,12))
            #search for user
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input"))).send_keys(user)

            #browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input").send_keys(user)
            time.sleep(random.randrange(20,30))

            #select user
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button"))).click()
            time.sleep(random.randrange(3,4))
            #click next
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button"))).click()
            time.sleep(random.randrange(3,4))
            #send a random message in the text box
            text_area = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
            text_area.send_keys(random.choice(messages))
            time.sleep(random.randrange(2,4))
            text_area.send_keys(Keys.ENTER)

            print("Succesfully sent to " + user)

            time.sleep(random.randrange(2,4))



    except Exception as err:
        print(err)
        browser.quit()

auth(my_username, my_password)
time.sleep(random.randrange(3,5))
send_message(usernames, messages)
