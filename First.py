from playsound import playsound
import time

def alarm(seconds):
    left_time=0
    while left_time<seconds:
        print(f"{left_time}:{seconds}")
        left_time = left_time +1



seconds = int(input("Enter the during time : "))
alarm(seconds)