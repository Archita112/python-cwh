# good morning sir exercise

import time

current_time = time.localtime().tm_hour
print("current time is", current_time)

if current_time >= 4 and current_time <= 12:
    print("A very Good Morning!")
elif current_time >= 12 and current_time <= 20:
    print("Good evening!")
else:
    print("Good night!!")