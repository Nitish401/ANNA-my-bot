import os 
import pyttsx3
import wikipedia as w
import datetime
import time
import webbrowser as wb
import subprocess 
import random

en = pyttsx3.init('sapi5')
vo = en.getProperty('voices')
rate = en.getProperty("rate")
en.setProperty("rate",120)
print(vo[0].id)
en.setProperty('voices',vo[0].id)
def speak(audio = None):
    en.say(audio)
    en.runAndWait()

def wishme():
    localtime = time.asctime(time.localtime(time.time()))
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING SIR MY NAME IS ANNA YOUR ASSISTANT")
        speak("today's day, date, time"+localtime)
    elif hour>=12 and hour<12:
        speak("GOOD AFTERNOON SIR MY NAME IS ANNA YOUR ASSISTANT")
        speak("today's day, date, time"+localtime)
    else:
        speak("GOOD EVENING SIR MY NAME IS ANNA YOUR ASSISTANT")
        speak("today's day, date, time"+localtime)       
wishme()
while True:
    speak("what do you want to do")
    a = str()
    a =  input("WHAT DO YOU WANT TO DO :")

    if 'i want to search something' in a :
        speak("what do you want to search")
        y = input("WHAT DO YOU WANT TO SEARCH:")
        speak("according to wikipedia")
        speak(w.summary(y,sentences=3))
    elif 'open browser' in a:
        speak("WHICH SITE YOU WANT TO LAUNCH")
        c = input("WHICH SITE YOU WANT TO LAUNCH:")
        wb.open(c)
    
    elif 'play games' in a:
        speak("WHICH GAME DO YOU WANT TO PLAY")
        b = input("WHICH GAME DO YOU WANT TO PLAY:")
        if 'mummy maze' in b:
                speak("OPENING MUMMY MAZE")
                subprocess.call('C://Program Files (x86)//PopCap Games//Mummy Maze Deluxe//WinMM')
        elif 'nfs' in b:
            speak("OPENING NFS")
            subprocess.call('E://DC//Need For Speed Most Wanted Black Edition repack Mr DJ//Mr DJ//Need For Speed Most Wanted Black Edition//speed.exe')       
        else:
            if 'prototype'in b:
                speak("OPENING PROTOTYPE")
                subprocess.call('F://Games//prototype//Prototype//prototypef')
    elif 'open vscode' in a:
        speak("OPENING V S CODE")
        subprocess.call('F://visual studio//Microsoft VS Code//Code')
    elif 'open utorrent' in a:
        speak("OPENING U TORRENT")
        subprocess.call('C://Users//ADMIN//AppData//Roaming//uTorrent//uTorrent')  
    elif 'open teams' in a:
        speak("OPENING MICROSOFT TEAMS")   
        subprocess.call('C://Users//ADMIN//AppData//Local//Microsoft//Teams//Update.exe --processStart "Teams.exe"')      
    elif 'play my list' in a:
        n = random.randint(0,167)
        ml = 'C://Users//ADMIN//Desktop//my list'
        songs = os.listdir(ml)
        os.startfile(os.path.join(ml,songs[n]))
    
