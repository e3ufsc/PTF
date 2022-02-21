from selenium import webdriver
import pyttsx3 as p
import speech_recognition as sr
import time as t

PATH = "C:\Program Files (x86)\chromedriver.exe"

r = sr.Recognizer()
engine = p.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

class Time():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)

    def say_time(self):
        try:
            self.driver.get(url="https://www.google.com/")
            
            search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            search.click()
            search.send_keys("What time is")

            t.sleep(1)
            enter = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
            enter.click()

            t.sleep(1)
            text = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div[1]')
            readable_text = text.text
            readable_text = str(readable_text)
            readable_text = readable_text.split(":")

            readable_text[0] = int(readable_text[0])
            readable_text[1] = int(readable_text[1])

            time = "It is {} {}".format(readable_text[0], readable_text[1])
            
            engine.say(time)
            engine.runAndWait()
        except:
            engine.say("An error has occurred, please try again")
            engine.runAndWait()
            return True
        return False
