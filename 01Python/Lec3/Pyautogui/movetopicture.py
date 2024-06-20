import pyautogui
from time import sleep
location=pyautogui.locateOnScreen('/home/ibrahim/screenshots/play.png',confidence='.8')
print(location)    