import speech_recognition as sr
import os
import pyttsx3
from wikipedia import languages
import webbrowser
#import openai
import datetime


def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # os.system(f"say {text}")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"
if __name__=='__main__':
    print('PyCharm')
    say("Hello I am Boogie A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"], ["wikipedia","https://wikipedia.com"], ["google","https://google.com"], ["geeto bitan", "https://www.geetabitan.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath=r"C:\Users\Soham Sabud\Desktop\Safar Notebook 128 Kbps.mp3"
            os.system(f"start {musicPath}")
            #print(f"On which website?")
            #query = takeCommand()
            #sites = [["spotify","https://open.spotify.com"], ["Gaana","https://gaana.com"]]
            #for site in sites:
             #   if f"Open {site[0]}".lower() in query.lower():
              #      say(f"Opening {site[0]} sir...")
               #     webbrowser.open(site[1])
        elif "the time" in query:      
            strfTime= datetime.datetime.now().strftime("%H:%M:%S")                         
            say(f"Sir,the time is {strfTime}")
        # say(query)
        
        elif "camera" in query: 
   
            import cv2
            
            
            cap = cv2.VideoCapture(0)
            
            while True:
                
                ret, frame = cap.read()
            
                
                cv2.imshow('Camera', frame)
            
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

# Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()
            
            
        elif "Quit".lower() in query.lower():
             exit()   
        
