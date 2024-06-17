
from gtts import gTTS
import vlc
myjob=gTTS(text='صباااااح الفل يا حاتم   ', lang='ar',slow=False)
myjob.save("welecome.mp4")
p=vlc.MediaPlayer("./welecome.mp4")
p.play()
while True :
    pass


