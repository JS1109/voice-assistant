import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer() 
engine = pyttsx3.init()
# engine.getProperty(voice)
# engine.setProperty('voice',voice[0].id)
# to change voice 0 for male voice and 1 for female voice
#we can also use getproperty to change speed and volume etc...

x=input("your name=")
y="hey "+x+" what can i do for you"
engine.say(y)
engine.runAndWait()



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tony' in command:
                command = command.replace('tony', '')
                print(command)
    except:
        pass
    return command


def run_tony():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        browse = command.replace('search', '')
        talk('searching' + browse)
        pywhatkit.search(browse)
    elif'power off' in command:
        talk('system will shutdown in 1 minute')
        pywhatkit.shutdown(time=60)
    elif'cancel' in command:
        talk('shutdown canceld')
        pywhatkit.cancel_shutdown()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)  
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        talk('bye have a good day!')
        sys.exit()
    else:
        talk('Please say the command again.')


while True:
    run_tony()