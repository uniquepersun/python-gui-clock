import tkinter as tk
from tkinter import font
from time import strftime, time, sleep

def time_label():
    current_time = strftime("%H:%M:%S %a %d/%m/%Y")
    label.config(text=current_time)
    label.after(1000, time_label)

def set_alarm():
    alarm_time = input("Enter time in HH:MM:SS format: ")
    while True:
        current_time = strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm is buzzzing")
            break

def start_stop():
    global start_time, stopped
    if stopped:
        start_time = time.time()
        stopped = False
    else:
        elapsed_time = time.time() - start_time
        stopped = True

def set_timer():
    timer_seconds = int(input("Enter timer time in second: "))
    while timer_seconds > 0:
        mins, secs = divmod(timer_seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        timer_seconds -= 1

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")

clock_font = font.Font(family="Helvetica", size=24, weight="bold")

label = tk.Label(root, font=clock_font, bg="black", fg="red")
label.pack()

alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
alarm_button.pack()

stopwatch_button = tk.Button(root, text="Start/Stop", command=start_stop)
stopwatch_button.pack()

timer_label = tk.Label(root)
timer_label.pack()
timer_button = tk.Button(root, text="Set Timer", command=set_timer)
timer_button.pack()

start_time = 0
stopped = True

time_label()

root.mainloop()
