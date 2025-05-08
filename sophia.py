import ctypes
import datetime
import os
import subprocess
import time
import webbrowser
from tkinter import *
import cv2
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

PASSWORD = "chingu"


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    mic_index = 1
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query.lower()


def authenticate():
    global root
    root = Tk()
    root.title("Sofia - Personal Assistant")
    root.geometry("500x500")

    label = Label(root, text="Welcome to Sofia", font=("Helvetica", 16, "bold"), pady=10)
    label.pack()

    label_pass = Label(root, text="Enter Password:", font=("Helvetica", 14))
    label_pass.pack()

    password_entry = Entry(root, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)

    def check_password():
        password = password_entry.get()
        if password == PASSWORD:
            root.destroy()

        else:
            speak("Incorrect password. Please try again.")
            password_entry.delete(0, END)

    button = Button(root, text="Authenticate", command=check_password, font=("Helvetica", 14))
    button.pack(pady=10)

    root.mainloop()


def sendemail():
    sendemail = "https://mail.google.com/mail/u/0/#inbox?compose=new"
    os.startfile(sendemail)
    speak("Opening Email")


def wish():
    hour = datetime.datetime.now().hour
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak(f"It's {current_time}. I am Sofia. How can I assist you?")


def opennotepad():
    notepad_path = "C:\\Windows\\System32\\notepad.exe"
    os.startfile(notepad_path)
    speak("Opening Notepad")


def run(self):
    speak("please say wakeup to continue")
    while True:
        self.query = self.takecommand()


def opencommandprompt():
    os.system("start cmd")
    speak("Opening Command Prompt")


def opencamera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow("webcam", img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    speak("Closing Camera")


def searchwikipedia():
    speak("What do you want to search on Wikipedia?")
    query = takecommand()
    speak("Searching Wikipedia")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("It seems there are multiple possible pages matching your query. Please specify.")
        for option in e.options[:5]:  # Limiting to the first 5 options for clarity
            speak(option)
        speak("Please refine your query.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information related to your query.")


def openchrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(chrome_path)
    speak("Opening Chrome")


def openspotify():
    webbrowser.open("https://open.spotify.com/")
    speak("Opening Spotify")


def openyoutube():
    webbrowser.open("https://www.youtube.com/")


def opengoogle(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")


def switchtabs():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('alt')


def getcurrenttime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def taskexecution(input_mode="speech"):
    wish()
    while True:
        if input_mode == "speech":
            query = takecommand().lower()
        else:
            query = input("Enter your command: ").lower()

        print("User query:", query)

        if "hi sofia" in query or "hello sofia" in query:
            speak("Hello! How can I assist you today?")

        elif "open notepad" in query:
            speak("Opening Notepad")
            opennotepad()

        elif "open command prompt" in query:
            opencommandprompt()

        elif "open camera" in query:
            opencamera()

        elif "wikipedia" in query:
            searchwikipedia()

        elif "open chrome" in query:
            openchrome()

        elif "open spotify" in query:
            openspotify()

        elif "open youtube" in query:
            openyoutube()

        elif "open google" in query:
            speak("What should I search for?")
            if input_mode == "speech":
                search_query = takecommand()
            else:
                search_query = input("Enter search query: ")
            opengoogle(search_query)

        elif "switch tabs" in query:
            switchtabs()

        elif "current time" in query:
            getcurrenttime()

        elif "hello" in query or "hey" in query:
            speak(" Hello , I'm Sofia")
            speak(" How can I help you?")

        elif "how are you" in query:
            speak(" i am fine,what about you?")

        elif "also good" in query or "fine" in query:
            speak(" that's good to hear from you")

        elif "thank you" in query or "thanks" in query:
            speak(" thank you,its my pleasure")

        elif "temperature" in query:
            search = "temperature in amravati"
            url = f"https://www.google.com/search?q=temperature+in+amravati&rlz=1C1ONGR_enIN1096IN1096&oq=tempreature+in+amaravti&gs_lcrp=EgZjaHJvbWUqCQgBEAAYDRiABDIGCAAQRRg5MgkIARAAGA0YgAQyCQgCEAAYDRiABDIJCAMQABgNGIAEMgsIBBAAGAoYDRiABDIICAUQABgNGB4yCAgGEAAYDRgeMggIBxAAGA0YHjIICAgQABgNGB4yCAgJEAAYDRge0gEJMTQwNzhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write?")
            note = takecommand()
            file = open('sophia.txt', 'w')
            speak("Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("sophia.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "set reminder" in query:
             set_reminder()

        elif "bye" in query or "goodbye" in query:
            speak("Goodbye!")
            break  # Exit the while loop

        elif "where is" in query:
            query = query.replace("where is", "").strip()
            location = query
            speak("User asked to Locate")
            speak(location)
            show_location(location)

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop sophia from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)

        elif "change background" in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by SHREYA-PRANJALI.")

        elif "send a mail" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                url = f"https://mail.google.com/mail/u/0/#inbox?compose=new"
                webbrowser.open(url)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "search places in google maps" in query:
            speak("Sure, please specify the place you want to search for.")
            place_query = takecommand()
            search_google_maps(place_query)

        elif "set reminder" in query:
            set_reminder()


def show_location(location):
    search_query = f"{location} map"
    url = f"https://www.google.com/maps/search/{search_query}"
    webbrowser.open(url)


def search_google_maps(query):
    search_query = query.replace(" ", "+")
    url = f"https://www.google.com/maps/search/{search_query}"
    webbrowser.open(url)


def set_reminder():
    speak("What would you like me to remind you about?")
    reminder_text = takecommand()

    speak("When should I remind you?")
    speak("Please specify the time in the format HH:MM (24-hour format)")
    reminder_time = input("Enter the time in HH:MM format: ")

    current_time = datetime.datetime.now()
    reminder_hour, reminder_minute = map(int, reminder_time.split(":"))

    # Calculate the time difference for the reminder
    reminder_datetime = current_time.replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)
    time_diff = (reminder_datetime - current_time).total_seconds()

    # Wait until it's time for the reminder
    if time_diff > 0:
        speak(f"Reminder set for {reminder_time}. I will remind you about '{reminder_text}' then.")
        time.sleep(time_diff)
        speak(f"Reminder: {reminder_text}")
    else:
        speak("Invalid time. Please try again.")


if __name__ == "__main__":
    authenticate()
    speak(" Hi ,Do you want to interact via speech or text? Say 'speech' or 'text'.")
    mode = takecommand().lower()  # Get the input mode from the user
    while mode not in ['speech', 'text']:
        speak("Please say 'speech' or 'text' to select the input mode.")
        mode = takecommand().lower()
    taskexecution(mode)
