""" Iterate through numbers 1-10,
keep a running total (sum) that keeps adding each new number,
print current number and running total """

start = 0

for i in range (1,11):
    start += i
    print(f"current number: {i}, running total: {start}")