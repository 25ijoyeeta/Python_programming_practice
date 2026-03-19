"""Write a function that takes two integers,
if the first number is divisible by the second,
return the division result,
otherwise return their product"""

def multiply_or_divide(num1, num2):
    divisble = num1/ num2
    
    if num1 % num2 == 0:
        return divisble
    else:
        return num1 + num2
    
result = multiply_or_divide(12,6)
print(result)
result = multiply_or_divide(6,12)
print(result)