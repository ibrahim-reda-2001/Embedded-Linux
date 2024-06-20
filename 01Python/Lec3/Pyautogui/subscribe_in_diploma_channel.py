import pyautogui
from time import sleep
import webbrowser
url="https://www.youtube.com/results?search_query=moatasem+el+sayed"
     
webbrowser.open(url)
sleep(7)
try:
    pyautogui.click('/home/ibrahim/screenshots/moataswm_channel.png')
    sleep(4)
    pyautogui.click('/home/ibrahim/screenshots/subscibe.png')
except pyautogui.ImageNotFoundException :
    pyautogui.moveTo('/home/ibrahim/screenshots/subscribed.png')
    print("you already subscribe")
    exit()    
