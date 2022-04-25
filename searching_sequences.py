#
#By Rodrigo Noriega
#
#searching sequences
#
#
#

#list method index

numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print(numbers)
print(numbers.index(5))
numbers *= 2
print(numbers)

#The following code searches the updated list for the value 5 starting from index 7
#and telling the position where the value is
print(numbers.index(5,7))

#The following looks for the value 7 in the range of elements with indices 0 through 3:
#where is the number 7 in range 0,4
print(numbers.index(7, 0, 4))

#operators in and not in
#is 1000 in numbers?
print(1000 in numbers)
print(5 in numbers)
print(1000 not in numbers)
print(5 not in numbers)

#Using Operator in to Prevent a ValueError
key = 1000
search_key = 3
if key in numbers:
    print(f'found value {key} at index {numbers.index(search_key)}') #search key is the key of list where we want to search
else:
    print(f'value {key} not found')

#Built-In Functions any and all
#Sometimes you simply need to know whether any item in an iterable is True or
#whether all the items are True. The builtin function any returns True if any item in
#its iterable argument is True. The builtin function all returns True if all items in its
#iterable argument are True. Recall that nonzero values are True and 0 is False. Nonempty
#iterable objects also evaluate to True, whereas any empty iterable evaluates toFalse. 
# Functions any and all are additional examples of internal iteration infunctionalstyle programming.