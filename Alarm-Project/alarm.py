from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(total_seconds): 

    print(CLEAR)
    for i in range(total_seconds,-1,-1):
        seconds = i%60
        minutes = (i//60)%60
        hours = i//3600
        print(f"{CLEAR_AND_RETURN}ALARM TIME : {hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
    playsound('Alarm-Project/alarm.mp3')


seconds = int(input("Enter the during seconds : "))
minutes = int(input("Enter the during minutes : "))
hours = int(input("Enter the during hours : "))
total_seconds = hours*3600 + minutes*60 + seconds
alarm(total_seconds)