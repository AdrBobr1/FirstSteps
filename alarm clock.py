#clock_for_windows_os by Adrian Bobrowski
#Python_practise

import time
import os

clear = lambda: os.system('cls')

while True:
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    sec = current_time.tm_sec
    year = current_time.tm_year
    month = current_time.tm_mon
    day = current_time.tm_mday
    today = current_time.tm_wday

    while True:
        if today == 0:
            today = 'Poniedziałek'
        elif today == 1:
            today = 'Wtorek'
        elif today == 2:
            today = 'Środa'
        elif today == 3:
            today = 'Czwartek'
        elif today == 4:
            today = 'Piątek'
        elif today == 5:
            today = 'Sobota'
        else: today = 'Niedziela'
        break

    str_hour = str(hour)
    str_min = str(minute)
    str_sec = str(sec)
    str_year = str(year)
    str_month = str(month)
    str_day = str(day)

    if day<10:
        str_day = ('0'+str_day)
    else: pass

    if month<10:
        str_month = ('0'+str_month)
    else: pass

    if hour<10:
        str_hour = ('0'+str_hour)
    else: pass

    if minute<10:
        str_min = ('0'+str_min)
    else: pass

    if sec<10:
        str_sec = ('0'+str_sec)
    else: pass

    czas = (str_hour+':'+str_min+':'+str_sec)
    data = (str_day+'-'+str_month+'-'+str_year)

    print(' The time now is: ')
    print('',czas,'\n',today,data)
    time.sleep(1)
    clear()


