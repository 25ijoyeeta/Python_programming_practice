"""Write a function that takes a temperature (int),
if its below 10, return "cold",
if its between 10 and 25, return "warm",
otherwise, return "hot"""

def temperature(num1):
    if num1 < 10:
        return("cold")
    elif 10<= num1 <= 25:
        return("Warm")
    else:
        return("Hot")

temp = temperature(8)
print(temp)
temp = temperature(10)
print(temp)
temp = temperature(30)
print(temp)
