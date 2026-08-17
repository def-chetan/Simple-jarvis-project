import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from google import genai


r=sr.Recognizer()

engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = genai.Client(
        api_key="AIzaSyCsx358wKxL9E54u9D2aazKBdsAMmbILlw"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {
                        "text": """You are a virtual assistant named Jarvis,
                        skilled in general tasks like Alexa and Google Assistant.""",
                        "comtent":command
                    }
                ]
            }
        ]
    )

    return (response.text)

def processcommand(c):
    print("command:" , c)
    c=c.lower()
    if "open google" in c:
          webbrowser.open("https://google.com")
    elif "open facebook" in c:
          webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
          webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
          webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
         song=c.split(" ")[1]
         link = musiclibrary.music[song]
         webbrowser.open(link)
    
    else:
        speak(aiprocess(c))


if __name__=="__main__":
    speak("Command Jarvis to initialize.....")
    #listen for jarvis
    while True:
        r = sr.Recognizer()
        
        # recognize speech using 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                
            
            print("recognizing....")
            word=r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("initializing jarvis")
                while True:
                    speak("Jarvis active...")
                    with sr.Microphone() as source:
                        print("Jarvis active...")
                        
                        audio = r.listen(source)                
                        print("recognizing....")
                        command=r.recognize_google(audio)
                        if (command.lower()=="jarvis stop"):
                            speak("jarvis stopped")
                            break
                        processcommand(command)


        except Exception as e:
            print("error; {0}".format(e))




