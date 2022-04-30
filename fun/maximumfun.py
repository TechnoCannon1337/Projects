import datetime
import time
def maximumFun(LookOutWeekend):
    dayofTheWeek = datetime.datetime.now()
    day = dayofTheWeek.strftime("%A")
    while day  == 'Friday' or day == 'Saturday' or day == 'Sunday':
        print('Today is '+day+' and was made for fun! \n'+LookOutWeekend)
        time.sleep(86400)

maximumFun('https://github.com/TechnoCannon1337/Projects/raw/master/videos/LookOutWeekend2.mp4')
