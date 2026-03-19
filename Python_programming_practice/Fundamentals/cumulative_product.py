"""Iterate through numbers 1-5,
keep multiplying the numbers sequentially(cumulative product),
print current number and cumulative product"""

product = 1

for i in range(1,6):
    product *= i
    print(f"Current number: {i}, cumulative product: {product}")
    