"""Iterate through numbers 1-10,
after each number, print the average
of all numbers seen so far by keeping track
of both sum so far and count of numbers"""

total_sum = 0
number = 0

for i in range(1,11):
    total_sum += i
    number += 1
    average = total_sum/number
    print(f"Current number: {i}, Running average: {average}")
    