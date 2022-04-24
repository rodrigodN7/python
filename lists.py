#
#By Rodrigo Noriega
#
#lists
#
#
#

#Lists typically store homogeneous data, that is, values of the same data type.
#Consider the list c, which contains five integer elements:

myList = [-45, 6, 0, 72, 1543]
#determining list type
print(type(myList))
#determining list length
print(len(myList))

#They also may store heterogeneous data, that is, data of many different types. For
#example, the following list contains a student’s first name (a string), last name (a
#string), grade point average (a float) and graduation year (an int):

myList1 = ['Mary', 'Smith', 3.57, 2022]
print(type(myList1))
print(len(myList1))

#Accessing elements of a list
print(myList[0])

#Accessing Elements from the End of the List with Negative Indices
#So, list c’s last element (myList[4]), can be accessed with myList[-1]
#and its first element with myList[-5]
print(myList[-1])
print(myList[-5])

#Indices Must Be Integers or Integer Expressions
a = 1
b = 2
print(myList[a + b])

#Lists are mutable—their elements can be modified:
myList[4] = 17
print(myList)

#Some Sequences Are Immutable
#Python’s string and tuple sequences are immutable—they cannot be modified. You can
#get the individual characters in a string, but attempting to assign a new value to one of
#the characters causes a TypeError:

s = 'hello'
print(s[0])
#s[0] = 'H' #This will cause an error

#Attempting to Access a Nonexistent Element
#Using an outofrange list, tuple or string index causes an IndexError:
#print(myList(100))#This will cause an error

#Using List Elements in Expressions
mySum = myList[0] + myList[-1] + myList[3]
print(mySum)

#Appending to a List with +=
a_list = []
print(a_list)

for number in range(1,6):
    a_list += [number]
print(a_list)

letters = []
letters += 'Python'
print(letters)

#Concatenating Lists with +
list1 = [10,20,30]
list2 = [40,50]

concatenated_list = list1 + list2
print(concatenated_list)

#Using for and range to Access List Indices and Values
for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')

#Comparison Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
print(a == b) # True: corresponding elements in both are equal
print(a == c) # False: a and c have different elements and lengths
print(a < c) # True: a has fewer elements than c
print(c >= b )# True: elements 02
