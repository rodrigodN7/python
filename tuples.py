#
#By Rodrigo Noriega
#
#tuples
#
#
#

#tuples are immutable and typically store
#heterogeneous data, but the data can be homogeneous. A tuple’s length is its number of
#elements and cannot change during program execution.

#creating tuples
student_tuple = ('John', 'Green', 3.3)
print(len(student_tuple))
print(type(student_tuple))

#When you output a tuple, Python always displays its contents in parentheses. You may
#surround a tuple’s commaseparatedlist of values with optional parentheses:
another_student_tuple = ('Mary', 'Red', 3.3)
print(another_student_tuple)

#The following code creates a one-element tuple:
#The comma (,) that follows the string 'red' identifies a_singleton_tuple as a
#tuple—the parentheses are optional. If the comma were omitted, the parentheses would
#be redundant, and a_singleton_tuple would simply refer to the string 'red' rather than a tuple.
a_singleton_tuple = ('red',) #note the comma
print(a_singleton_tuple)

#Accessing tuple elements
time_tuple = (9, 16, 1)
print(time_tuple)
print(time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2])

#Assigning a value to a tuple element causes a TypeError.
#time_tuple[0] = 12

#Adding Items to a String or Tuple
#As with lists, the += augmented assignment statement can be used with strings and tuples, even though they’re immutable.
tuple1 = (10,20,30)
tuple2 = tuple1
print(tuple1)
print(tuple2)
tuple1 += (40,50)
print(tuple1)
print(tuple2)

#Appending Tuples to Lists
#You can use += to append a tuple to a list:
nums = [1,2,3,4,5]
nums += (6,7)
print(nums)

#Tuples May Contain Mutable Objects
studnt_tuple = ('Amanda', 'Red', [98,75,87])
print(studnt_tuple)
studnt_tuple[2][1] = 85
print(studnt_tuple)

#unpacking sequences
firstname, second_name, grades = studnt_tuple
print(firstname)
print(grades)

#The following code unpacks a string, a list and a sequence produced by range:
first, second = 'hi'
print(f'{first} {second}')

num1, num2, num3 = [2,3,5]
print(f'{num1} {num2} {num3}')

number1, number2, number3 = range(10, 40, 10)
print(f'{number1} {number2} {number3}')

#Accessing Indices and Values Safely with Built-in Function enumerate, pag 182 del libro python for programmers
#The preferred mechanism for accessing an element’s index and value is the builtin-function enumerate
colors = ['red','orange', 'yellow']
print(list(enumerate(colors)))
print(tuple(enumerate(colors)))

for index,value in enumerate(colors):
    print(f'{index}:{value}')

#Creating a primitive bar chart
"""Displaying a bar chart"""
numbers = [19,3,15,7,11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" * value}')

#sequence slicing
#You can slice sequences to create new sequences of the same type containing subsets of
#the original elements

numbers = [2,3,5,7,11,13,17,19]
print(numbers[2:6])

#Specifying a Slice with Only an Ending Index
#If you omit the starting index, 0 is assumed. So, the slice numbers[:6] is equivalent to
#the slice numbers[0:6]:
print(numbers[:6])
print(numbers[0:6])

#Specifying a Slice with Only a Starting Index
#If you omit the ending index, Python assumes the sequence’s length (8 here), so snippet
#[5]’s slice contains the elements of numbers at indices 6 and 7:
print(numbers[6:])
print(len(numbers))
print(numbers[6:len(numbers)])

#Specifying a Slice with No Indices
#Omitting both the start and end indices copies the entire sequence:
print(numbers[:])

#Slicing with Steps
#The following code uses a step of 2 to create a slice with every other element of numbers:
print(numbers[::2])

#Slicing with Negative Indices and Steps
print(numbers[::-1])
#this is equivalent to
print(numbers[-1:-9:-1])

#Modifying Lists Via Slices
numbers[0:3] = ['two', 'three', 'five']
print(numbers)
numbers[0:3] = []
print(numbers)

numbers = [2,3,5,7,11,13,17,19]
print(id(numbers))
numbers[::2] = [100,100,100,100]
print(numbers)
print(id(numbers))
numbers[:] = []
print(id(numbers))
