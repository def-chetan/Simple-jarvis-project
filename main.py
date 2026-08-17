import speech_recognition as sr
import webbrowser
import pyttsx3

r=sr.Recognizer()

engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    if "open google" in c.lower():
          webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")
    else:
        speak("wrong command")


if __name__=="__main__":
    speak("Command Jarvis to initialize.....")
    #listen for jarvis
    while True:
        r = sr.Recognizer()
        
        # recognize speech using 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            
            print("recognizing....")
            word=r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("initializing jarvis")
                while True:
                    with sr.Microphone() as source:
                            print("Jarvis active...")
                            audio = r.listen(source)                
                            print("recognizing....")
                            command=r.recognize_google(audio)
                            if (command.lower()=="jarvis stop"):
                                 break
                            processcommand(command)


        except Exception as e:
            print("error; {0}".format(e))




