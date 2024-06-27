import requests
import pyautogui
import webbrowser
from time import sleep
x="https://web.whatsapp.com/"
url=requests.get(x)
if url.status_code==200:
    webbrowser.open(x)
sleep(15)
location=pyautogui.locateCenterOnScreen('/home/ibrahim/screenshots/groub.png',confidence=.9)
print(location)
pyautogui.moveTo(location)
sleep(2)
pyautogui.click()
sleep(1)
pyautogui.moveTo('/home/ibrahim/screenshots/groub2.png')
sleep(1)
pyautogui.click()
sleep(1)
for i in range(5):
    pyautogui.write('i am scribt writed by ibrahim')
    sleep(1)
    pyautogui.hotkey('enter')
