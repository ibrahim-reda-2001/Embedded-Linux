import pyaudio 
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import playsound
import time
import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pywhatkit
import wikipedia


language='ar'
list_how_are_you=["اخبارك","ازيك","عامله ايه "]
list_of_good=["كويس","الحمدالله"]
list_of_hour=["الساعه","الوقت"]
list_of_date=["التاريخ","النهارده","تاريخ"]
list_of_thanks=["شكرا","برافو"]
list_of_matchs=["ماتشات","مباريات","مباراه"]
list_of_YT=["اغنيه","موسيق","سوره","ملخص"]
list_of_information=["كلميني عن"]
list_of_me=["تعرفيني","انا مين"]
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
def get_date():
    return datetime.datetime.now().strftime("%A %m/%d/%Y")
def matchs():
    os.system("python3 yalla-kora-alexia.py")
    # print(os.getcwd())
    # Load the CSV file
    file_path = '/home/ibrahim/Downloads/matches_details.csv'
    df = pd.read_csv(file_path)

    # Convert the entire dataframe to a single string
    data_str = df.to_string(index=False)

    # Convert the text to speech
    tts = gTTS(text=data_str, lang='ar')

    # Save the speech as an audio file
    audio_file = 'all_data.mp3'
    tts.save(audio_file)

    # Play the audio file
    playsound.playsound(audio_file)
    os.remove('all_data.mp3')
def speak(text):
    sound=gTTS(text=text,lang=language,slow=False)
    sound.save('hi.mp3')
    playsound.playsound('hi.mp3')
    os.remove('hi.mp3')
# speak("Guten Tag, wie geht es Ihnen?",'de')
listener = sr.Recognizer()
def listen():
    try:
    # Capture audio from the microphone
        with sr.Microphone() as source:
            
            print("Listening...")
            # Optional: Adjust for ambient noise
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source)
            print("Recognizing...")
            command = listener.recognize_google(audio,language=language)
            if 'اليكسا' in command:
                print(command)
                #speak(command)
                return command
            else:
                return ""
           
                
    except:   
            speak("لم استطع فهمك يا زميلي")
            return ""
def run():
    x=True
    while x:
        command=listen()
        if (language=='ar') and ('انهاء'    in command):
                x=False
        elif  any(word in command for word in list_of_hour) :
            speak("الساعه الَانِ هِي"+get_time())
        elif  any(word in command for word in list_how_are_you):
            speak("انا كويسه انتا عامل ايه ياصاحبي")
        elif any(word in command for word in list_of_date):
            speak("التاريخ الان هو "+get_date())
        elif any(word in command for word in list_of_good):
            speak(" يَارَبِّ دَايِمًا بِخَيْرِ ياصاحبي ")
        elif any(word in command for word in list_of_thanks):
            speak(" العفوا ياريس خلي عنك خالص  ")
        elif any(word in command for word in list_of_matchs):
            matchs()
        elif any(word in command for word in list_of_YT):
            command=command.replace("اليكسا","")
            speak("اتفضل يا عمنا "+command)
            pywhatkit.playonyt(command)
        elif any(word in command for word in list_of_information):
            command=command.replace("اليكسا","")
            command=command.replace("كلميني عن","")
            info=wikipedia.summary(command,1)
            speak(info)
        elif any(word in command for word in list_of_me):
            speak("طبعا اعرفك انتا اشهر من النار علي العلم يسطا ابراهيم")
            

    speak("مَعَ السَّلَامَهِ انتا الْخَسِرَان")
            
       
       
        
run()
    