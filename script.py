from twilio.rest import Client
from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler


client = Client("AC5b2bc9a7cde14639bdec576bb47f23ae",
                "be1d07503187fc8fe8bdfab9db2c4fde")


print("Enter time as HH:MM(24 Hour-Format)")
input_time = input()
print("Enter text for Reminder")
input_text = input()
print("Enter Mobile Number you want to recieve reminder on:(format-+9198765643210)")
input_number = input()
data = [input_time, input_text, input_number]
print("Reminder Saved")


a = data[0]
h = a[0:2]
m = a[3:len(a)+1]


def send():
    client.messages.create(to=data[2],
                           from_="+15106613164",
                           body=data[1])


ist = pytz.timezone('Asia/Kolkata')
sched = BlockingScheduler()
# Schedule the python script to be called everyday from monday to friday at 7:17 P.M. You change the time as per your need.
sched.add_job(send, 'cron', day_of_week='mon-sun',
              hour=int(h), minute=int(m), timezone=ist)
sched.start()
