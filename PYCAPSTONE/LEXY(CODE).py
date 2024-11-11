#import speech recognition
import speech_recognition as sr
# importing the text to speech library
import pyttsx3
# import the wikipedia Library
import wikipedia
# importing the pyjokes library
import pyjokes
# importing the datetime library
import datetime
# importing the pywhatkit library
import pywhatkit
# import the OpenAI library
import openai
# import the OS library
import os


listener = sr.Recognizer()
# initializing text to speech
engine = pyttsx3.init()
# getting available voices
voices = engine.getProperty('voices')
# setting the voice
engine.setProperty('voice', voices[-2].id)
# intro message using the set voice
engine.say("Heyy, I'm Lexy, your voice Assistant")
# running the text to speech function
engine.runAndWait()

# defining a function to convert text to speech
def talk(text):
    # converting text to speech
    engine.say(text)
    # running the text to speech function
    engine.runAndWait()

# defining function to get commamds from user
def take_command():
    try:
        # Using microphone to get commands(Microphone Object)
        with sr.Microphone() as source:
            print('listening...')
            talk('listening...')
            # Listening to the user
            voice = listener.listen(source)
            # recognizing user's voice
            command = listener.recognize_google(voice)
            # converting user's voice to lowercase
            command = command.lower()
            print(command)
    except:
        pass
    # returning user's command
    return command

# defining function to run the assistant(Lexy)
def run_lexy():
    # take user's command
    command = take_command()
    print(command)

    # if user's command contains 'play'
    if 'play' in command:
        # remove word 'play' from user's command
        song = command.replace('play', '')
        # say 'playing' + name of song
        talk('playing ' + song)
        # plays song on YouTube
        pywhatkit.playonyt(song)

    # if user's command contains 'time'
    elif 'time' in command:
        # get current time
        time = datetime.datetime.now().strftime('%I:%M %p')
        # say current time
        talk('Current time is ' + time)

    # if user's command contains 'who is'
    elif 'who is' in command:
        # remove 'who is' from user's command
        person = command.replace('who is', '')
        # getting info from wikipedia
        info = wikipedia.summary(person, 1)
        # providing info in text and voice
        print(info)
        talk(info)

    # if user's command contains 'date'
    elif 'date' in command:
        # say text
        talk('sorry, I have a headache')

    elif 'what do you do' in command:
        # say given text
        talk('I am a simple personal assistant created by Desmond, to showcase different python concepts,'
             
             'I can play music from youtube, spotify, get different kinds of jokes, not the best but still ,'
             
             'I can also get information from wikipedia, as well and tell time,'
             
             'I am made up of different modules, that ensure, I run smoothly,'
             
             'I can also, integrate data from OpenAI, API')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        # say jokes from pyjokes library
        talk(pyjokes.get_joke())

elif 'spotify' in command:
    talk('Opening Spotify...')
    # open spotify from my sytem
    # os.system(r'path to your spotify apllication')

    # AI command removed
        # removed for security reasons

    elif 'hello' in command:
        talk('hello')

    elif 'how are you' in command:
        talk('I am doing good, hope you are too!, Thanks')

    else:
        talk('please say the command again')


# call function to run the assistant Lexy
run_lexy()
