from selenium import webdriver
import pyttsx3 as p
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

engine = p.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

class info_E3():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)

    def get_info(self):
        try:
            self.driver.get(url="https://e3.ufsc.br/en/index_en.html")
            
            time.sleep(2)

            text = self.driver.find_element_by_xpath('//*[@id="about"]/div[1]/div/div[2]/div/p[1]')
            readable_text = text.text
            
            engine.say(readable_text)
            engine.runAndWait()
        except:
            engine.say("An error has occurred, please try again")
            engine.runAndWait()
            return True
        return False

class info():
    def __init__(self):
        self.query = ""
        self.driver = webdriver.Chrome(PATH)

    def get_info(self, query):
        self.query = query
        try:
            self.driver.get(url="https://www.google.com/")
            
            search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            search.click()
            search.send_keys(self.query)

            text = self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[1]/div/div/div/span[1]')
            readable_text = text.text
            
            engine.say(readable_text)
            engine.runAndWait()
        except:
            engine.say("An error has occurred, please try again")
            engine.runAndWait()
            return True
        return False