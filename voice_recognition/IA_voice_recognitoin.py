import speech_recognition as sr
import pyttsx3 as p
import time
from web_auto import *
from calculator_auto import *
from time_auto import *

r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')           # getting details of current speaking rate
engine.setProperty('rate', 125)             # setting up new voice rate
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)

functions = ["information", "weather", "time", "calculator", "E3", "help"]
                                                                   

FRIST_RUN = True

def run():
    global FRIST_RUN
    while True:

        with sr.Microphone() as source:
            text = r.listen(source)

            try:
                recognised_text = r.recognize_google(text)
                if recognised_text == "assistant":
                    engine.say("Hello {}".format("Sir"))
                    if FRIST_RUN == True:
                        #change_name()
                        engine.say("I'm equipped with the following functions")
                        for word in functions:
                            engine.say(word)
                            time.sleep(1)
                        FRIST_RUN = False
                    engine.say("What do you need?")
                    engine.runAndWait()

                func()
                    
            except sr.UnknownValueError:
                print("")

            except sr.RequestError as e:
                print("")

def func():
    with sr.Microphone() as source:
        text = r.listen(source)
        error = True
        try:
            recognised_text = r.recognize_google(text)
            print(recognised_text)
            recognised_text = str(recognised_text)
            for i in range(len(functions)):
                if recognised_text == functions[i]:
                    answer(i)

            if error == True:   
                engine.say("I didn't understand the function, can you repeat please?")
                engine.runAndWait()
                func()

        except sr.UnknownValueError:
            print("")

        except sr.RequestError as e:
            print("")

        
def answer(i):
    if i == 0:
        engine.say("This feature is under development")
        engine.runAndWait()
        func()

    if i == 1:
        engine.say("This feature is under development")
        engine.runAndWait()
        func()

    if i == 2:
        clock = Time()
        clock.say_time()
        run()

    if i == 3:
        cal = Calculator()
        cal.calculation()
        run()
        

    if i == 4:
        assistant = info_E3()
        error = assistant.get_info()
        if error == True:
            func()
        run()

    if i == 5:
        engine.say("I'm equipped with the following functions")
        for word in functions:
            engine.say(word)
            time.sleep(1)
        engine.say("What do you need?")
        engine.runAndWait()
        func()

    return False

run()
