"""Write a function that takes a number,
if the number is less than 50,
return double the number,
otherwise, return the square of the number"""

def double_or_square(num1):
    if num1 < 50:
        return num1 * 2
    else:
        return num1 * num1

test = double_or_square(25)
print(test)
test = double_or_square(51)
print(test)