"""Iterate through numbers 0-9,
print the difference between the current number and
the previous number"""

previous_num = 0

for i in range(10):
    difference = i - previous_num
    print(f"Current number: {i}, previous number: {previous_num}, difference: {difference}")
    
    previous_num = i