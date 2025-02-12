#Task 1

import datetime
from datetime import timedelta
x = datetime.datetime.now()
new_date = x - timedelta(days=5)
print("current date:", x.strftime("%Y-%m-%d"))
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))

#Task 2

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("yesterday:",yesterday.strftime("%Y-%m-%d"))
print("today:",today.strftime("%Y-%m-%d"))
print("tomorrow:",tomorrow.strftime("%Y-%m-%d"))

#Task 3

current_time = datetime.datetime.now()
new_time = current_time.replace(microsecond=0)
print("Original time:",current_time.strftime("%H-%M-%S-%f"))
print("Without microsecond:",new_time)

#Task 4

date1 = datetime.datetime(2025, 2, 12, 15,0,0)  
date2 = datetime.datetime(2025, 1, 11, 16, 30, 0)  
difference = abs((date2 - date1).total_seconds())
print(f"Difference in seconds: {difference}")


