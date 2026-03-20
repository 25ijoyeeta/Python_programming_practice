"""Write a Python program to display the current date and time."""

import datetime

current_time = datetime.datetime.now()

print("Current date and time:")
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
