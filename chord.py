import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# "Setting up the voice engine"
engine = pyttsx3.init('sapi5')
# Voice 
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
# Speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate',150)



# Code for speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Wish function code starts here
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("Hi I am chord, How may i help you")  


def take_commands():
    ''' this function is about taking commands'''

    r = sr.Recognizer()
    # print(sr.Microphone().list_microphone_names())
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        Query = r.recognize_google(audio, language='en-in')
        print(f"You said: '{Query}'")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return Query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("Your Gmail account","Your Password")
    server.sendmail("your gmail account",to,content)
    server.close()





if __name__ == '__main__':
    wishMe()
    while True:
        command = take_commands().lower()
        if "stop" in command:
            speak("Sure sir! as your wish, bai")
            print("Sure sir! as your wish, bai")
            break
        if "who are you" in command:
            speak("Hi I am Chord and I'm your virtual assistance to help you")
        if "wikipedia" in command:
            speak("Searching on wikipedia...")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        if "youtube" in command:
            browser = 'windows-default'
            webbrowser.get(browser).open("https://www.youtube.com/")
        if "google" in command:
            browser = 'windows-default'
            webbrowser.get(browser).open("https://www.googel.com/")
        if "stack overflow" in command:
            browser = 'windows-default'
            webbrowser.get(browser).open("https://www.stackoverflow.com/")
        if "github" in command:
            browser = 'windows-default'
            webbrowser.get(browser).open("https://github.com/surajsoni2")
        if "linkedin" in command:
            browser = 'windows-default'
            webbrowser.get(browser).open("https://www.linkedin.com/in/suraj-soni-81020a201/")

        if "play music" in command:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        if "time" in command:
            starTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"sir the time is  {starTime}")
        
        if "open vs code" in command:
            codepath = "C:\\Users\\suraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        if "command prompt" in command:
            codepath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(codepath)

        if "powershell" in command:
            codepath = "C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(codepath)

        if "open calculator" in command:
            codepath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codepath)

        if "hibernate" in command:
            os.system("shutdown /h")


        if "email" in command:
            try:
                speak("what should i say?")
                content = take_commands()
                to = "reciever email id"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry i unable to send mail")
        




