'''
Create a lambda function for each of the following bullet points:

A lambda function that takes in a number and returns that number squared
A lambda function that takes in a number and returns that number cubed
A lambda function that takes two numbers and returns the sum of those numbers
A lambda function that takes two numbers and returns the product of those numbers
'''
square_num = lambda x: x**2
print(f"Squred num: {square_num(3)}")
######################
cubed_num = lambda x: x**3
print(f"Cubed num: {cubed_num(3)}")
######################
return_sum = lambda x, y: x + y
print(f"sum: {return_sum(2,3)}")
######################
return_product = lambda x, y: x*y
print(f"product: {return_product(2,3)}")