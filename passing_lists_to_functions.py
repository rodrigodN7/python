#
#By Rodrigo Noriega
#
#passing lists to funtions
#
#
#

#passing an entire list to a function
def modify_elements(items):
    """Multiplies al element values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2

numbers = [10,3,7,1,9]
print(numbers)
modify_elements(numbers)
print(numbers)

#passing a tuple to a function
myTuple = (10,20,30)
#When you pass a tuple to a function, attempting to modify the tuple’s immutable
#elements results in a TypeError:
#this will caue an error
#modify_elements(myTuple)

#sorting lists
#List method sort modifies a list to arrange its elements in ascending order:
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(numbers)
numbers.sort()
print(numbers)

#Sorting a List in Descending Order
#To sort a list in descending order, call list method sort with the optional keyword
#argument reverseset to True (False is the default):
numbers.sort(reverse=True)
print(numbers)

#built-in function sorted
#Builti function sorted returns a new list containing the sorted elements of its
#argument sequence—the original sequence is unmodified. The following code
#demonstrates function sorted for a list, a string and a tuple:
print(sorted(numbers))
letters='fadgchjebi'
print(letters)
print(sorted(letters))
colors = ('red', 'orange', 'yellow', 'green', 'blue')
print(sorted(colors))
