import sys
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    print(f"Assistant: {text}")
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except:
        return "none"


speak("Hello, I am your Virtual Voice Assistant.")

while True:
    query = listen()
    if query=="none" or len(query)<2:
        continue
    
    if 'stop' in query:
        speak("Goodbye...!!!")
        sys.exit()
        
    elif 'time' in query:
        t = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {t}")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.open('www.youtube.com')
        
    elif 'date' in query:
        d=datetime.datetime.now().strftime('%d %B %Y')
        speak(f"Today's date is {d}")
        
    elif 'day' in query:
        e=datetime.datetime.now().strftime('%B %d %A')
        speak(f"Today is {e}")

    elif 'search' in query:
        topic = query.replace("search", "")
        speak(f"Searching for {topic}")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={topic}")
    
    elif 'hello' in query:
        speak("Hi there!! How can I help You today?")
        
    else:
        if query!="none":
            speak("Sorry...I didn't catch that..Try again.")

