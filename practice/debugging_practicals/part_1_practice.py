x = 'Dog'
y = 'Cat'
z = x + ' ' + y

len = len(z) # Obtain the number of characters of z
print(len) # [FINE]
print(y.count('') - 1) # Obtain the number of characters of y

my_ls = [z.split()] # Separate each word of z and store the result in a list
# FIX: we need to wrap it with [] to make it a list [DONE]
print(my_ls[0][1]) # Print the second element in the list
# FIX: we need to close the brackets [DONE]
################
'''
elements of computational thinking:
1. abstraction 
2. decomposition
3. pattern recognition
4. algorithms

'''