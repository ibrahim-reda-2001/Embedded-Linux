import pyautogui
from time import sleep
import webbrowser
url=["https://www.youtube.com/results?search_query=moatasem+el+sayed",
     "https://www.youtube.com/results?search_query=bein+sport",
     "https://www.youtube.com/results?search_query=%D8%A7%D9%84%D9%85%D8%AE%D8%A8%D8%B1+%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A"

    ]
for link in url:
    webbrowser.open(link)
    sleep(10)
    pyautogui.click('/home/ibrahim/screenshots/unsub.png')
    sleep(5)
    pyautogui.click('/home/ibrahim/screenshots/unsub2.png')
    sleep(5)
    pyautogui.click('/home/ibrahim/screenshots/unsub3.png')
    sleep(5)

        
            

    
