'''
Create a list of 5 numbers

Create a lambda function that squares a number. Then use map to square each number in the list
Create a lambda function that cubes a number. Then use map to cube each number in the list
Create a lambda function that takes in a number and returns that number squared if it is even, and
'''
list = [1,2,3,4,5]
# Create a lambda function that squares a number. Then use map to square each number in the list
list_sqrd = map(lambda x: x**2, list)
# Create a lambda function that cubes a number. Then use map to cube each number in the list
list_cubed = map(lambda x: x**3, list)

# Create a lambda function that takes in a number and returns that number squared if it is even, and
# returns that number cubed if it is odd. Then use map to apply this lambda function to each number in the list
list_even_sqrd_odd_cubed = map(lambda x: x**2 if x%2==0 else x**3, list)

########################################################################################
# Another way for doing it
sqrd = lambda x: x**2
map(sqrd, list)
