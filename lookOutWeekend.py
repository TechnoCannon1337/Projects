#Python
import time
from datetime import datetime
def maximumTwitterFun(LookOutWeekend):
    dayofTheWeek = datetime.now().isoweekday()
    while(dayofTheWeek >=5):
        if dayofTheWeek == 5:
            day = 'Friday'
        elif dayofTheWeek == 6:
            day = 'Saturday'
        elif dayofTheWeek ==7:
            day = 'Sunday'
        print('Today is '+day+' and was made for fun! \n'+LookOutWeekend)
        time.sleep(86400)

maximumTwitterFun('')
