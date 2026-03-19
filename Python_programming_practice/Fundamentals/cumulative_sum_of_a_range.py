"""Iterate through the first 10 numbers (0–9).
In each iteration, print the current number,
the previous number, and their sum."""

previous_num = 0

for i in range(10):
    # i is the current number
    #  previous_num is the number before i
    total_sum = previous_num + i
    print(f" Current number : {i}, previous number: {previous_num}, sum: {total_sum}")
    
    #updated to the curent number for the next iteration
    previous_num = i
    