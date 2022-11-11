# STATUS: All errors fixed. Note: see inital code in hidden doc string.

'''
initial code:
x = 'Dog'
y = 'Cat'
z = x + ' ' + y

len = len(z) # Obtain the number of characters of z
print(len)
print(len(y)) # Obtain the number of characters of y

my_ls = z.split() # Separate each word of z and store the result in a list
print(my_ls[2] # Print the second element in the list
'''

x = 'Dog'
y = 'Cat'
z = x + ' ' + y

len = len(z) # Obtain the number of characters of z
print(len)

# print(len(y)) # Obtain the number of characters of y
# FIX: len(y) is not callable; y is not an int; commented the line above out.
print(y.count('') - 1)
# FIX: call the count method on y -- did -1 due to python zero-index.



my_ls = [z.split()] # Separate each word of z and store the result in a list
# FIX: wrap the value of my_ls with a list brackets
print(my_ls[0][1]) # FIX: this list has one index, return the second item in that index -- cat.
# print(my_ls[1]) # Print the second element in the list -- ERRONOUS
