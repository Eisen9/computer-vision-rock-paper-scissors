'''
Create a list with 5 tuples, where each tuple contains a name and a number
Then, using the sort function, create a lambda function for each of the following
bullet points:

Sort the list by the number in each tuple
Sort the list by the name in each tuple
Sort the list by the length of the name in each tuple
Sort the list by the length of the name in each tuple, but in reverse order
'''
list = [ ('John', 5), ('Mary', 3), ('Bob', 2), ('Jane', 1), ('Joe', 4)] # Create a list with 5 tuples
print(list)

list.sort(key=lambda x: x[1]) # Sort the list by the number in each tuple
print(list)
#########################################################################
list.sort(key=lambda x: x[0])
print(list)
#########################################################################
list.sort(key=lambda x: len(x[0]))
print(list)
#########################################################################
list.sort(key=lambda x: len(x[0]), reverse=True)
print(list)