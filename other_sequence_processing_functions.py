#
#By Rodrigo Noriega
#
#other sequence processing functions
#
#
#

#Finding the Minimum and Maximum Values Using a Key Function
#strings are compared by their characters’ underlying numerical values, 
#and lowercase letters have higher numerical values than uppercase letters.
print('Red' < 'orange')

#builtin function ord returns the numerical value of a character
print(ord('R'))
print(ord('o'))

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
print(min(colors, key = lambda s: s.lower()))
print(max(colors, key = lambda s: s.lower()))

#Iterating Backward Through a Sequence
#Builtin function reversed returns an iterator that enables you to iterate over a
#sequence’s values backward
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
reversed_numbers = [item ** 2 for item in reversed(numbers)]
print(reversed_numbers)

#Combining Iterables into Tuples of Corresponding Elements
#Builtin function zip enables you to iterate over multiple iterables of data at the same
#time. The function receives as arguments any number of iterables and returns an
#iterator that produces tuples containing the elements at the same index in each.

names = ['Bob', 'Sue', 'Amanda']
grade_point_average = [3.5, 4.0, 3.75]

for name, gpa in zip(names, grade_point_average):
    print(f'Name={name}; GPA={gpa}')

