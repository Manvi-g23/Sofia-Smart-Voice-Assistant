import datetime
import os
from _pydatetime import time

import pyttsx3
import speech_recognition as sr
import webbrowser
import cv2
import wikipedia
import pyautogui

engine = pyttsx3.init("sapi5")
voices: object = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query


def takecommand():
    pass


def run(self):
    speak("say Hi Jarvis to wakeup")
    while True:
        query = takecommand().lower()
        if 'Hi Jarvis' in query or 'hello' in query or 'wakeup' in query:
            self.TaskExecution()


def taskexecution(self):
    wish()
    while True:
        self.query = self.takeCommand()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. How can I help you?")


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            notepad_path = "C:\\Windows\\System32\\notepad.exe"  # Adjust the path if needed
            os.startfile(notepad_path)
            speak("Opening Notepad")

        elif "open command prompt" in query:
            os.system("start cmd prompt")
            speak("Opening Command Prompt")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(58)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            speak("Opening Camera")

        elif "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")

            print(results)
            speak(results)

        elif "open chrome" in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
            speak("Opening Chrome")

        elif "open spotify" in query:
            webbrowser.open_new_tab("https://open.spotify.com/")
            speak("Opening Spotify")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("What should I search for?")
            cmd = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q=" + cmd)

        elif "switch tabs" in query:
            pyautogui.keyDown('alt')
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "exit" in query:
            speak("Goodbye!")
            break
