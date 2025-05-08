import cv2
import pyttsx3
import speech_recognition as sr

# Initialize pyttsx3 for speech synthesis
engine = pyttsx3.init()

# Initialize speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't understand. Can you repeat?")
        return None

def recognize_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

def process_intent(intent):
    if intent == 'greet':
        speak("Hello! How can I help you today?")
    elif intent == 'open_notepad':
        speak("Opening Notepad")
        # Add your code to open Notepad here
    elif intent == 'open_browser':
        speak("Opening Browser")
        # Add your code to open a browser here
    else:
        speak("Sorry, I'm not sure how to handle that.")

def main():
    speak("Initializing assistant. Please look at the camera for face recognition.")
    recognize_face()
    speak("Face recognized. How can I assist you?")

    while True:
        user_input = listen()
        if user_input:
            if "hello" in user_input:
                process_intent('greet')
            elif "notepad" in user_input:
                process_intent('open_notepad')
            elif "browser" in user_input:
                process_intent('open_browser')
            else:
                speak("Sorry, I'm not sure how to handle that.")

if __name__ == "__main__":
    main()
