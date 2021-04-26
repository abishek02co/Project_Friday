import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import smtplib
import wikipedia
import pyjokes
import webbrowser as wb
from email.message import EmailMessage
wb.register('chrome', None)
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk(" Happy Morning Assassin, have a good start like a thunder with a light!")

    elif hour >= 12 and hour < 18:
        talk(" healthy afternoon! Assassin , don't be lazy like a turtle!!! run fast  !")

    else:
        talk("energetic, Evening Assassin , practice like you never win before !")

    assname = ("friday")
    talk("I am your Assistant" + assname)


wishMe()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
    except Exception as e:
        print("take command exception" + str(e))
        print('''sorry i can't get you... please try again
your Exception errors:''')

        pass
    return command


def usrname():
    talk("What should i call you sir")
    uname = take_command()
    talk("Welcome" + uname)
    print("Welcome " + uname)
    talk("How can i Help you " + uname)
    print("How can i Help you " + uname)


usrname()


def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('serabishek@gmail.com', 'abishek abishek')
    email = EmailMessage()
    email['from'] = 'serabishek@gmail.com'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        wb.open("https://www.youtube.com/")

    elif 'open google' in command:
        talk("Here you go to Google\n")
        flex = "https://www.google.com/"
        wb.open(flex)

    elif 'open github' in command or 'open git hub' in command:
        talk("Here you go to github\n")
        wb.open("https://github.com/")

    elif 'open gmail' in command or 'open email' in command:
        talk("Here you go to g-mail\n")
        wb.open("https://accounts.google.com/signin/v2/identifier?sacu=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    elif 'information' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('curret time is ' + time)

    elif 'how are you' in command:
        talk("iam fine, thank you sir!")
        talk("How are you, Sir")
        print("get input")

        try:
            to = take_command()
            print("got input:" + str(to))
            if "i'm fine" in to or "iam fine" in to or "i am fine" in to or "iam good" in to or "i am good" in to or "i'm good" in to:
                print("t's good to know that your fine")
                talk("It's good to know that your fine")
        except Exception as e:
            print('exception:' + str(e))
            print("i wish u will have a better time1z")
            talk("i wish u will have a better time")

    elif "who made you" in command or "who created you" in command:
        talk("I have been created by ABISHEK.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'search' in command:
        command = command.replace("search", "")
        talk("here we go to chrome browser")
        she5 = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        wb.get(she5).open(
            format(f'https://www.google.com/search?q={command}'))

    elif 'send a mail' in command:
        try:
            talk("whome should i send")
            print("whome should i send")
            receiver = input()
            talk("what is the subject of ur mail?")
            subject = take_command()
            talk("what is message")
            message = take_command()
            sendEmail(receiver, subject, message)
            talk("Email has been sent !")
        except Exception as e:
            print(e)
            talk("I am not able to send this email")

    elif 'exit' in command:
        talk("Thanks for giving me your time")
        exit()


run_friday()
