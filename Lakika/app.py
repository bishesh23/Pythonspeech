from flask import Flask, render_template, url_for, redirect
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser

app = Flask(__name__)


@app.route('/')
def voice():
    return render_template('voice.html')


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('toMp3 audio.mp3')


def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    if 'open youtube' in command:
        url = 'https://www.youtube.com'
        webbrowser.open(url)
        print('Done!')

    if 'open facebook' in command:
        url = 'www.facebook.com'
        webbrowser.open(url)
        print('Done!')

    if 'open classroom' in command:
        url = 'http://classroom.dwit.edu.np/login/index.php'
        webbrowser.open(url)
        print('Done!')

    if 'i am hungry' in command:
        url = 'http://system.deerwalkfoods.com'
        webbrowser.open(url)
        print("Done!")

    if 'open mail' in command:
        url = 'http://www.gmail.com'
        webbrowser.open(url)
        print("Done!")

    if 'open portal' in command:
        url = 'http://doko.dwit.edu.np/'
        webbrowser.open(url)
        print("Done!")

    if 'open google' in command:
        url = 'http://www.google.com'
        webbrowser.open(url)
        print("Done!")

    if 'shutdown' in command:
        os.system("shutdown.exe /s")

    if 'restart' in command:
        os.system("shutdown.exe /r")

    if 'hibernate' in command:
        os.system("shutdown.exe /h")


@app.route('/home', methods=['POST'])
def test():
    talkToMe('I am ready for your command')
    while True:
        assistant(myCommand())
