#
#By Rodrigo Noriega
#
#searching sequences
#
#
#

#list method index

from re import search


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

key = 1000
search_key = 3
if key in numbers:
    print(f'found value {key} at index {numbers.index(search_key)}') #search key is the key of list where we want to search
else:
    print(f'value {key} not found')
