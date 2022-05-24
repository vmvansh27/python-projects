import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from datetime import date
from PIL import Image,ImageGrab
import time
from plyer import notification

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 200) #speed of the voice assistant
engine.setProperty('voice', voices[1].id) # 1 for female, 0 for male 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def random_no_generator(start,end):
    randno=random.randint(start,end)
    return randno



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<23:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")

    speak("My name is ZeroTwo!Your personal assistant,How may i help you?")

def takecommand():
    '''it takes microphone inputs from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold=1
        r.energy_threshold = 300
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def happy_birthday():
    speak('''Happy Birthday to You
Happy Birthday to You
Happy Birthday Dear friend
Happy Birthday to You.

From good friends and true,
From old friends and new,
May good luck go with you,
And happiness too.''')


def greetings():
    list_of_greetings=['Welcome sir!','my pleasure sir']
    length=len(list_of_greetings)
    randomno=random_no_generator(0,length-1)
    speak(list_of_greetings[randomno])

def application_opener(path):
    os.startfile(path)


def study_remainder(stime):
    hour=int(datetime.datetime.now().hour)
    if hour==stime:
        notification.notify(
 			title = "STUDYY!!",
 			message ="Remeber that you have to become succssfull!!",
 			timeout= 12
 			)
        speak("Go and study!!Good Luck")
        return stime+2
        


def music_player():
    music_dir='V:\\song'
    songs=os.listdir(music_dir) #it will store all songs name in a list
    randomusic=len(songs) #finding length of number of songs in that list
    randomno=random.randint(0,randomusic-1) #generating a random number from 0 to the number of songs-1
    os.startfile(os.path.join(music_dir,songs[randomno])) #playing a random song through from that folder

if __name__=='__main__':
    hour=int(datetime.datetime.now().hour) #for study remainder
    stime=hour+1 #for study remiander
    thankyou_reply=["thank you","thanks"] #for zerotwo reply for thankyou
    wishme()
    '''setting up a different browser because otherwise it will open internet explorer browser'''
    brave_path=r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe' #saving path of the browser
    webbrowser.register('brave',None,webbrowser.BackgroundBrowser(brave_path))
    while True:
        stime=study_remainder(stime) #it will remind me to study every 2 hours
        query=takecommand().lower()# logics for executing tasks based on queries 
        

        if "wikipedia" in query:
            print("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif "sing happy birthday" in query:
            happy_birthday()
            

            '''Browser related'''


        elif "youtube" in query:
            webbrowser.get('brave').open("youtube.com") #opening a site with that browser
        elif "open google" in query:
            webbrowser.get('brave').open("google.com") #opening a site with that browser
        elif "anime"  in query:
            webbrowser.get('brave').open("9anime.to") 

                
        #Music related
        elif "music" in query:
            music_player()
        
        #date and time
        elif "time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current Time is {strTime}")

        elif "date" in query:
            today=date.today()
            d2 = today.strftime("%B %d, %Y")
            print(d2)
            speak(f"Date is {d2}")


        elif "sad" in query:
            speak("Do you want me to play some music?")
            abc=takecommand().lower()
            if "yes" in abc:
                music_player()
                
        elif query in thankyou_reply:
            greetings()

            #application opener
        elif "code" in query:
            path="C:\\Users\\vansh\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            application_opener(path)    
        
        elif "whatsapp" in query:
            path="C:\\Users\\vansh\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            application_opener(path)

        elif "spotify" in query:
            path="C:\\Users\\vansh\\AppData\\Roaming\\Spotify\\Spotify.exe"
            application_opener(path)

        elif "discord" in query:
            path="C:\\Users\\vansh\\AppData\\Local\\Discord\\Update.exe"
            application_opener(path)

        # Screenshot
        elif "screenshot" in query:
            image=ImageGrab.grab()
            image.show()

        # Exit
        elif "quit" in query:
            exit()
        # Shutdown
        elif "shutdown" in query:
            speak("Do you really want to shutdown?")
            query=takecommand().lower() 
            if query=="yes":
                os.system("shutdown /s /t 10")
