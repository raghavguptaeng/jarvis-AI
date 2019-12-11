#-- a virtual assistant to help you . his name is jarvis --------------------------------------------
# --- version 1.0 -----------------------------------------------------------------------------------
#--- DEVELOPED BY - RAGHAV GUPTA --------------------------------------------------------------------
#--- contact - raghavgermany@gmail.com or E19CSE258@bennett.edu.in ----------------------------------
#-------------- THANKS FOR YOUR SUPPORT -------------------------------------------------------------


import pyttsx3 #pip install pyttsx3
import speech_recognition as speech #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from urllib.request import urlopen
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def search(query):
    driver = webdriver.Chrome(r'C:\Users\RAGHAV GUPTA\PycharmProjects\automation\drivers\chromedriver.exe')
    driver.set_page_load_timeout(10)
    driver.get('https://www.google.com')
    driver.fullscreen_window()
    driver.find_element_by_name("q").send_keys(query)
    driver.find_element_by_name("q").send_keys(Keys.ENTER)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<20:
        speak("Good Evening!")
    else :
        speak("Good Night")

    speak('I am Jarvis Sir.Your personal assistant. Please tell me how may I help you')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    return 0;



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\Users\RAGHAV GUPTA\Desktop'
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "enter the senders email id here "
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")
        elif 'search' in query:
            speak(" what shall i search for you ? ")
            quer= takeCommand()
            search(quer)




