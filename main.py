import speech_recognition as sr
from subprocess import Popen
import pyttsx3
import streamlit as st
# import PyAudio
import openApplicationData as ss
from pynput.keyboard import Key, Controller

r=sr.Recognizer()
mic=sr.Microphone()
keyboard=Controller()

st.title("Welecome to Window Speech")

# speak text function
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()
# ----------------

# main said command
command=""
# ----------------

def listenAgain():
    try:
        audio=r.listen(source)
        r.adjust_for_ambient_noise(source)
        commandNext=r.recognize_google(audio)
        print("You Said \""+commandNext + "\"")
        affection(commandNext)
    except:
        listenAgain()

def affection(command):
    # Code for opening application
    st.write(command)
    def runApplication(data):
        p=Popen(data['code'],shell=True)
        if p.poll() is None:
            speak("Opening " + data["original"])
        listenAgain()
        # os.system(data['code'])
        # p.terminate|()
    def openProgram():
        program=command[command.find("open")+4:].lstrip().lower()
        if program in ss.paint['key']:runApplication(ss.paint)
        elif program in ss.word['key']:runApplication(ss.word)
        elif program in ss.vscode['key']:runApplication(ss.vscode)
        elif program in ss.browser['key']:runApplication(ss.browser)
        elif program in ss.facebook['key']:runApplication(ss.facebook)
        elif program in ss.amazon['key']:runApplication(ss.amazon)
        elif program in ss.discord['key']:runApplication(ss.discord)
        elif program in ss.notepad['key']:runApplication(ss.notepad)
        else:
            speak("I can't open " + program + " application")
            openMissing=open("./improvement/miss_open.txt","a")
            speak("Saying Bittu, to add this functionality")
            openMissing.write(command + "\n")
            speak("Try Again!")
            
    # ------------------------------------

    if "open" in command:
        openProgram()
        listenAgain()
    if command=='exit' or command == "quit" or command == "good":
        speak("Ok, Good Bye...")
        Popen("exit()",shell=True)
    if command=="shutdown":
        speak("This will turn off this machine and also me, are you sure sir!")
        audio=r.listen(source)
        response=r.recognize_google(audio)
        if response == "yes" or response=="ok" or response=="do it":
            Popen("shutdown /s /t 5",shell=True)
            speak("Ok, turning off this machine in 5 second")
            speak(3)
            speak(2)
            speak(1+ " Noooooooo")

        else:
            speak("Ufff, I thought you really want me to go down.")
            speak("Thank God")
            listenAgain()
    # keyboard Use
    elif "fullscreen" in command:
        keyboard.press(Key.f11)
        listenAgain()
    elif "type" in command:
        text=command[command.find("type")+4:].lstrip()
        keyboard.type(text)
        listenAgain()
    elif "press" in command or "Press" in command:
        if "key" in command:
            command=command.replace("key", "")
        if "ki" in command:
            command=command.replace("ki", "")

        code=command.replace("press","").strip()
        if code == "alt":
            keyboard.press(Key.alt)
            keyboard.release(Key.alt)
        elif code == "control" or code == "ctrl":
            keyboard.press(Key.ctrl)
        elif code == 'space':
            keyboard.press(Key.space)
        elif code == 'enter':
            keyboard.press(Key.enter)
        elif code == "f1":
            keyboard.press(Key.f1)
        elif code == "f2":
            keyboard.press(Key.f2)
        elif code == "f3":
            keyboard.press(Key.f3)
        elif code == "f4":
            keyboard.press(Key.f4)
        elif code == "f5":
            keyboard.press(Key.f5)
        elif code == "f6":
            keyboard.press(Key.f6)
        elif code == "f7":
            keyboard.press(Key.f7)
        elif code == "f8":
            keyboard.press(Key.f8)
        elif code == "f9":
            keyboard.press(Key.f9)
        elif code == "f10": 
            keyboard.press(Key.f10)
        elif code == 'f11':
            keyboard.press(Key.f11)
        elif code == "f12": 
            keyboard.press(Key.f12)
        else:
            keyboard.press(code)
        listenAgain()
    
    # simple conversation

    elif command == "goodbye" or command=="Goodbye" or command=="bye":
        speak("Ok, I am active in Background")
        speak("Ask me if need any help")
        listenAgain()




    
    # listenAgain()
        

# def micInit():
with mic as source:
    try:
        speak("What you want me to do")
        audio=r.listen(source)
        r.adjust_for_ambient_noise(source)
        command=r.recognize_google(audio)
        print("You Said \""+command + "\"")
        affection(command)
    except:
        print("Not Understand")
        listenAgain()



    
