import pyautogui
import requests
import webbrowser
from time import sleep

webbrowser.open('https://192.168.1.1/')
sleep(5)
pyautogui.write('admin')
sleep(1)
pyautogui.hotkey('tab')
sleep(1)
pyautogui.write('0100hemA')
sleep(1)
pyautogui.hotkey('enter')
sleep(3)
location=pyautogui.locateOnScreen('/home/ibrahim/screenshots/wlan.png')
sleep(3)
pyautogui.moveTo(location)
pyautogui.click()
sleep(2)
location=pyautogui.locateOnScreen('/home/ibrahim/screenshots/off.png')
pyautogui.moveTo(location)
sleep(1)
pyautogui.click()
sleep(1)
location=pyautogui.locateOnScreen('/home/ibrahim/screenshots/apply.png')
pyautogui.moveTo(location)
sleep(1)
pyautogui.click()
print("done bro ")

exit()



