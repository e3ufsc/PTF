from selenium import webdriver
import pyttsx3 as p
import speech_recognition as sr


r = sr.Recognizer()
engine = p.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

class Calculator():

    def calculation(self):
        operations = ["Plus", "Minus", "Multiply", "Divided by"]
        engine.say("I have the following operations")
        for i in range(len(operations)):
            engine.say(operations[i])
        engine.runAndWait()
        engine.say("What is the calculation?")
        engine.runAndWait()
        with sr.Microphone() as source:
                text = r.listen(source)
                

                try:
                    recognised_text = r.recognize_google(text)
                    print(recognised_text)
                    recognised_text = str(recognised_text)
                    recognised_text = recognised_text.split(" ")
                    if recognised_text[1] == "+":
                        result = int(recognised_text[0]) + int(recognised_text[2])
                    if recognised_text[1] == "-":
                        result = int(recognised_text[0]) - int(recognised_text[2])
                    if recognised_text[1] == "*":
                        result = int(recognised_text[0]) * int(recognised_text[2])
                        recognised_text[1] = "multiply"
                    if recognised_text[1] == "/":
                        recognised_text[1] = "divided by"
                        result = int(recognised_text[0]) / int(recognised_text[2])
                    engine.say("The result of {} {} {} is: {}".format(recognised_text[0],recognised_text[1],recognised_text[2], result))
                    engine.runAndWait()
                
                except sr.UnknownValueError:
                    print("")

                except sr.RequestError as e:
                    print("")
