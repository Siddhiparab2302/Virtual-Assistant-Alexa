import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone()as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
        
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time'in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Your current time is' + time)
    elif 'what is 'in command:
        person = command.replace('what is','')
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'help me' in command:
        talk('yes sure,Hoe can I help you')
    elif 'kai karte' in command:
        talk('nothing much,i m talking with my friend')
    elif 'ok' in command:
        talk('What are you doing chiku')
    elif 'doing' in command:
        talk('okay chiku')
    elif 'hi' in command:
        talk('hello chiku what can I do for you')
    elif 'bye' in command:
        talk('bye bye chiku')
    
    
    else:
        talk('Can you please say it again')
    
    

while True:
    run_alexa()
