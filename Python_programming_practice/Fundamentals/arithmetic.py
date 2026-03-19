""" Python function that takes two integers as inputs and returns 
their product if the product is less than or equal to 1000, 
otherwise it returns their sum."""

def arithmetic_product_or_sum(num1, num2):

    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
    
# Test cases
result = arithmetic_product_or_sum(20, 30)
print(result)  
result = arithmetic_product_or_sum(40, 30)
print(result)