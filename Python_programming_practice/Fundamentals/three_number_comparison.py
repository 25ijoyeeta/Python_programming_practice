"""Write a function that takes three numbers,
 if their sum is greater than 100, return the largest number,
 otherwise return the smallest number"""

def three_number_comparison(num1, num2, num3):
    total_sum = num1 + num2 + num3
    
    if total_sum > 100:
        return max(num1, num2, num3)
    else:
        return min(num1, num2, num3)

test =  three_number_comparison(12, 24, 23)
print(test)
test =  three_number_comparison(50, 100, 30,)
print(test)