import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox
from playsound import playsound

def update_remaining_time():
    remaining_time = alarm_datetime - datetime.now()

    if remaining_time.total_seconds() <= 0:
        playsound('C:\\Users\\HP\\Downloads\\Alarm.mp3')
        messagebox.showinfo("Alarm", "Alarm time is reached!")
        root.destroy()
        return

    remaining_days = remaining_time.days
    remaining_hours, remaining_minutes = divmod(remaining_time.seconds // 60, 60)
    remaining_seconds = remaining_time.seconds % 60

    time_label.config(text=f"{remaining_days} days\n\n{remaining_hours:02d} hours {remaining_minutes:02d} mins {remaining_seconds:02d} secs")
    time_label.after(1000, update_remaining_time)

    
def show_alarm_details(remaining_days, remaining_hours, remaining_minutes, remaining_seconds):
    details_window = tk.Toplevel(root)
    details_window.title("Alarm Details")

    alert_label = tk.Label(details_window, text="The Countdown clock title is:", font=("Arial", 12, "bold" ))
    alert_label.pack()

    alert_title = tk.Label(details_window, text=alarm_title, font=("Arial", 12, "bold"))
    alert_title.pack()

    saved_label = tk.Label(details_window, text="Alarm Saved On:", font=("Arial", 12, "bold" ))
    saved_label.pack()

    new = datetime.now()

    saved_datetime = tk.Label(details_window, text=new.strftime("%a, %B %d, %Y"), font=("Arial", 12, "bold" ))
    saved_datetime.pack()

    

    total_months = (alarm_datetime.year - datetime.now().year) * 12 + alarm_datetime.month - datetime.now().month

    remaining_days_adjusted = remaining_days + 1 if remaining_hours < 0 or (remaining_hours == 0 and remaining_minutes < 0) else remaining_days
    total_weeks = remaining_days_adjusted // 7

    total_days = remaining_days_adjusted % 7

    total_hours = remaining_days * 24 + remaining_hours
    total_minutes = remaining_days * 24 * 60 + remaining_hours * 60 + remaining_minutes
    total_seconds = remaining_days * 24 * 60 * 60 + remaining_hours * 60 * 60 + remaining_minutes * 60 + remaining_seconds

    months_label = tk.Label(details_window, text="Total Months to go:", font=("Arial", 12, "bold" ))
    months_label.pack()
    months_value = tk.Label(details_window, text=f"{total_months} months", font=("Arial", 13, "bold"))
    months_value.pack()

    weeks_label = tk.Label(details_window, text="Total Weeks to go:", font=("Arial", 12, "bold" ))
    weeks_label.pack()
    weeks_value = tk.Label(details_window, text=f"{total_weeks} weeks", font=("Arial", 13, "bold"))
    weeks_value.pack()

    days_label = tk.Label(details_window, text="Total Days to go:", font=("Arial", 12, "bold" ))
    days_label.pack()
    days_value = tk.Label(details_window, text=f"{remaining_days} days", font=("Arial", 13, "bold"))
    days_value.pack()

    hours_label = tk.Label(details_window, text="Total Hours to go:", font=("Arial", 12, "bold" ))
    hours_label.pack()
    hours_value = tk.Label(details_window, text=f"{total_hours} hours", font=("Arial", 13, "bold"))
    hours_value.pack()

    minutes_label = tk.Label(details_window, text="Total Minutes to go:", font=("Arial", 12, "bold" ))
    minutes_label.pack()
    minutes_value = tk.Label(details_window, text=f"{total_minutes} minutes", font=("Arial", 13, "bold"))
    minutes_value.pack()

    seconds_label = tk.Label(details_window, text="Total Seconds to go:",font=("Arial", 12, "bold" ))
    seconds_label.pack()
    seconds_value = tk.Label(details_window, text=f"{total_seconds} seconds", font=("Arial", 13, "bold"))
    seconds_value.pack()

# Create main window
root = tk.Tk()
root.title("Alarm Clock")

# Set alarm details
alarm_date = input("Enter your date here (format: yyyy/mm/dd): ")
alarm_time = input("Enter the time of the alarm (format: HH:MM AM/PM): ")
alarm_title = input("Alarm Title: ")
print("Countdown started Alert!!")

year, month, day = map(int, alarm_date.split('/'))
time_str, am_pm = map(str.strip, alarm_time.split())
hour, minute = map(int, time_str.split(':'))

if am_pm.lower() == 'pm' and hour != 12:
    hour += 12

alarm_datetime = datetime(year, month, day, hour, minute)

# Create frame for remaining time display
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text=alarm_title, font=("Arial", 24, "bold"))
title_label.pack()

saved_label = tk.Label(frame, text=alarm_datetime.strftime("%a, %B %d, %Y"), font=("Arial", 16))
saved_label.pack()

time_label = tk.Label(frame, text="", font=("Arial", 24, "bold"))
time_label.pack()

# Create link for alarm details
details_link = tk.Label(root, text="View Alarm Details", fg="blue", cursor="hand2")
details_link.pack()
details_link.bind("<Button-1>", lambda e: show_alarm_details(alarm_datetime.day - datetime.now().day, alarm_datetime.hour - datetime.now().hour, alarm_datetime.minute - datetime.now().minute, alarm_datetime.second - datetime.now().second))

update_remaining_time()

root.mainloop()
