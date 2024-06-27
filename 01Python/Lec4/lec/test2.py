import psutil
from pynotifier import notification 
battery=psutil.sensors_battery()
percent=battery.percent
print(percent)
notification("Battery Percentage ", str(percent)+"%percent Remaining",duration=10).send()
