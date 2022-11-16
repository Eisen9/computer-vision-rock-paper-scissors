'''
Create a list of 10 strings

Create a lambda function that takes in a string and returns True if the
string is longer than 5 characters, and False if it is not. Then use filter
and the lambda function to filter out all strings that are longer than 5 characters
Create a lambda function that takes in a string and returns True if the string is longer
than 5 characters and starts with a vowel, and False if it is not. Then use filter and the
lambda function to filter out all strings that are longer than 5 characters and start with a vowel
'''
list = ['hello', 'my', 'name', 'is', 'x', 'and', 'i', 'am', 'enjoying', 'python']
# print(list)

filter_longer_than_5 = filter(lambda x: len(x) > 5, list)
print(list(filter_longer_than_5))

filter_longer_than_5_starts_with_vowel = filter(lambda x: len(x) > 5 and x[0] in 'aeiou', list)
print(list(filter_longer_than_5_starts_with_vowel))

