"""Iterate through the list: [5, 8, 2, 7, 7, 10],
for each number, print whether it is higher, lower,
or the same as the previous number,
treat the first number as having no previous"""

previous_num = None

numbers = [5, 8, 2, 7, 7, 10]

for current in numbers:
    if previous_num is None:
        print(f"Current: {current} (no previous number)")
    elif current > previous_num:
        print(f"Current: {current}, Previous: {previous_num} Higher")
    elif current < previous_num:
        print(f"Current: {current}, Previous: {previous_num} Lower")
    else:
        print(f"Current: {current}, Previous: {previous_num} Same")
        
    previous_num = current