"""A function that takes two integers,
if their sum is even, returns the sum,
otherwise, return the product"""

def even_or_odd_sum(num1, num2):
    total_sum = num1 + num2
    
    if total_sum % 2 == 0:
        return total_sum
    else:
        return num1 * num2
    
result = even_or_odd_sum(12,17)
print(result)
result = even_or_odd_sum(12,12)
print(result)
