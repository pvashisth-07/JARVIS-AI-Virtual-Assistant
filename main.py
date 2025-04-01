import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
from openai import OpenAI
import pygame


recogniser=sr.Recognizer()
engine=pyttsx3.init()
newsapi="your news api"  # use your own api key

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_new(text):  #a faster and better way
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize the mixer module
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("your_music.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running to let the music play
    while pygame.mixer.music.get_busy():  # Check if music is still playing
        pygame.time.Clock().tick(10)  # Reduce CPU usage
    

def aiProcess(command):
    client = OpenAI(
    api_key="your own openAI api"
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

    


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            # Print the headlines
            for article in articles:
                speak(article['title'])

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    else:
        #LET AI handle the commands
        output= aiProcess(c)
        speak(output)

        

if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer() #recogniser object
        
        
        print("recognizing...")
        # recognize speech using Google
        try:

            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
            word=r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Yes, listening for command")
                #listen for command
                with sr.Microphone() as source:
                    print("JARVIS active")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    print(f"Command received: {command}")

                    processCommand(command)

            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))