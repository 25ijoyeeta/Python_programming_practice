""" A function that takes two numbers,
if the first number is greater than the second,
return their difference, otherwise
return their sum"""

def bigger_number_logic(num1, num2):
    difference = num1 - num2
    
    if num1 > num2:
        return difference
    else:
        return num1 + num2
    
result = bigger_number_logic(17,12)
print(result)
result = bigger_number_logic(12,17)
print(result)