#Alarm Clock
import time
from datetime import datetime, timedelta
import pygame

current_time = datetime.now()

def set_alarm(alarm_time) :
    duration = alarm_time - current_time
    print(f"Alarm is set for {duration}")
    sound_file = "Alarm Clock.mp3"
    is_running = True

    while is_running :
        now = datetime.now()  # Update current time as a datetime object
        print(f"Current Time: {now.strftime('%H:%M:%S')}")


        if now >= alarm_time :
            print(f"***Alarm for {alarm_time}***")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() :
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == "__main__" :
    print(f"Time : {current_time}")
    alarm_time_str = input("Enter the alarm time in 24hr format (HH:MM:SS) : ")
    alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").replace(
        year=current_time.year, month=current_time.month, day=current_time.day)
    set_alarm(alarm_time)