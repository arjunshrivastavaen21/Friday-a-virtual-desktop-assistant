from PyQt5 import QtCore, QtGui, QtWidgets
import threading

class Ui_friday(object):
    def setupUi(self, friday):
        friday.setObjectName("friday")
        friday.resize(706, 516)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shriv\\Desktop\\new jarvis gui\\network.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        friday.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(friday)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\shriv\\Downloads\\gif for jarvis\\d13449fb76b34cb71584f5bfb7c6dee9.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 370, 181, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\shriv\\Downloads\\gif for jarvis\\f59876d316abc628202df9012706d68f.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 151, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\shriv\\Downloads\\gif for jarvis\\hud-designs-for-dune-v0-8rjih1obym491.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 181, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\shriv\\Downloads\\gif for jarvis\\a4504e13717549.562773a2f2bb2.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, -40, 251, 161))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\shriv\\Downloads\\gif for jarvis\\Jarvis_Loading_Screen.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        friday.setCentralWidget(self.centralwidget)

        self.retranslateUi(friday)
        QtCore.QMetaObject.connectSlotsByName(friday)

    def retranslateUi(self, friday):
        _translate = QtCore.QCoreApplication.translate
        friday.setWindowTitle(_translate("friday", "F.R.I.D.A.Y"))
        # animation work
        self.movie = QtGui.QMovie("C:\\Users\\shriv\\Downloads\\gif for jarvis\\d13449fb76b34cb71584f5bfb7c6dee9.gif")
        self.label.setMovie(self.movie)
        self.movie2 = QtGui.QMovie("C:\\Users\\shriv\\Downloads\\gif for jarvis\\f59876d316abc628202df9012706d68f.gif")
        self.label_2.setMovie(self.movie2)
        self.movie3 = QtGui.QMovie("C:\\Users\\shriv\\Downloads\\gif for jarvis\\hud-designs-for-dune-v0-8rjih1obym491.gif")
        self.label_3.setMovie(self.movie3)
        self.movie4 = QtGui.QMovie("C:\\Users\\shriv\\Downloads\\gif for jarvis\\a4504e13717549.562773a2f2bb2.gif")
        self.label_4.setMovie(self.movie4)
        self.movie5 = QtGui.QMovie("c:\\Users\\shriv\\Downloads\\gif for jarvis\\Jarvis_Loading_Screen.gif")
        self.label_5.setMovie(self.movie5)
        self.startanimation()

    def startanimation(self):
        self.movie.start()
        self.movie2.start() 
        self.movie3.start()
        self.movie4.start()
        self.movie5.start()




#-------------------------------------main module for Friday ----------------------------------
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import socket #ip
import subprocess
import time

#------------------------------------AI-----------------------------------------------
'''
import openai
from config import apikey


chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Arjun: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def AI(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

#---------------------------------------------------------------------------------------------------
'''

#------ pc voice setup -----------------------------------------
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#---------- speak function -------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#------take input form microphone and convert into string-------
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Friday is listening.....")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = 250 
        audio = r.listen(source)
    try:
        print("please wait, Friday is recognining...") 
        query = r.recognize_google(audio, language="en-in")
        print("User said: ",query)
        #print(f"User said: {query}\n")

    except Exception as e:
        print("say it again please")    
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
        print("good morning sir")
    elif hour>=12 and hour<17:
        speak("good afternoon sir")
        print("good afternoon sir")
    else:
        speak("good evening sir")
        print("good evening sir")       
    speak("I am friday. how i can help you")
    print("I am Friday. how i can help you")

#------------changed the defult browser-----------------------------------------
def web(site):
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
    webbrowser.get('chrome').open(site)

def sleepm():
    while True:
        q = takecommand().lower()
        if 'wake up' in q:
            speak("i am back sir")
            break

def obbreak():
    while True:
        q =takecommand().lower()
        #Friday back to the main program 
        if 'back to' in q:
            speak("what else i can do for you sir")
            break

def whatismyip():
    hostcomputer = socket.gethostname()
    ipv4 = socket.gethostbyname(hostcomputer)
    speak(f'your ip address {ipv4}')

def cmdd(b):
    subprocess.run(b,shell= True)


#________________________________main function__________________________________
def Execution():
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'who are you' in query:
            print("I am friday, a desktop voice assistant")
            speak("I am friday, a desktop voice assistant")

        elif 'how can you help me' in query:
            speak("sir i can help you to do any task with your voice command")

        elif 'open youtube' in query:
            print("opening youtube")
            speak("opening youtube")
            web("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            web("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            web('stackoverflow.com')  
        
        elif 'open facebook' in query:
            speak("opening facebook")
            web("facebook.com")
        
        elif 'open insta' in query:
            speak("opening instagram")
            web("instagram.com")
        
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            web("whatsapp.com")
        
        elif 'open twitter' in query:
            speak("opening twitter")
            web("twitter.com")
        
        elif 'open gmail' in query:
            speak("opening gmail")
            web("gmail.com")

        elif 'open file converter' in query:
            speak("opening file converter")
            web("cloudconvert.com")  
        
        elif 'internet speed' in query:
            speak("wait a second sir")
            web("speedtest.net")

        elif "play music" in query:
            speak("wait a second sir")
            print("wait a second sir, playing music...")
            music_loc = "C:\\Users\\shriv\\Music"
            songs = os.listdir(music_loc)
            os.startfile(os.path.join(music_loc, songs[0]))

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S %p")
            speak(f"Sir the time is {strtime}")   
      
        elif "open vs code" in query:
            speak("opening vs code")
            os.startfile("C:\\Users\\shriv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code") 

        elif "sleep" in query:
            speak("take care sir")
            sleepm()    
        
        elif "stop the program" in query:
            speak("good by sir")
            exit()

        elif 'ip' in query:
            speak("wait a second showing your ip address")
            whatismyip()

        elif 'open notepad' in query:
            print("opening notepad")
            speak("opening notepad")
            codePath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(codePath)
        elif 'open cmd' in query:
            speak("opening CMD")
            codePath = "C:\\windows\\system32\\cmd.exe"
            os.startfile(codePath)  
        elif 'open camera' in query:
            speak("opening camera")
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif 'open calendar' in query:
            speak("opening calendar")
            os.startfile('C:\\Users\\shriv\\Desktop\\Calendar')    

        elif 'open my computer' in query:
            speak('opening my computer')
            os.startfile("C:\\Users\\shriv\\Desktop\\This PC - Shortcut")
        
        
        elif 'open clock' in query:
            speak("opening clock") 
            cmdd("timedate.cpl")   
        elif 'open setting' in query:
            speak('opening settings')
            cmdd("desk.cpl")    

        elif 'open ms word' in query:
            speak("opening ms word")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word")
        
        elif 'open excel' in query:
            speak("opening excel")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel")

        elif 'open powerpoint' in query:
            speak("opening powerpoint")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint")    

        elif 'open task manager' in query:
            speak("opening task manager")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager")    

        elif 'open paint' in query:
            speak("opening paint")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint")    

        elif 'open photos' in query:
            speak("opening photos")
            os.startfile("C:\\Users\\shriv\\Pictures") 

        elif 'open calculator' in query:
            speak("opening calculator")
            os.startfile("C:\\Users\\shriv\\Desktop\\Calculator")    

        elif 'open object detection' in query:
            speak("wait few minutes sir, the program is starting")
            os.startfile("C:\\Users\\shriv\\Desktop\\obecjt detedction\\dist\\object_detecting\\object_detecting.exe")
            obbreak()

 

'''

        elif "using artificial intelligence" in query:
            AI(query)

        elif "reset chat" in query:
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)     
'''            

#--------------------------------gui main function's--------------------------------------------------------------

def fun():
    thread.start()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    friday = QtWidgets.QMainWindow()
    ui = Ui_friday()
    ui.setupUi(friday)
    friday.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    thread = threading.Thread(target=Execution)

    fun()
    thread.join()   