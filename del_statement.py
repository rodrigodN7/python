#
#By Rodrigo Noriega
#
#del statement
#
#
#

#The del statement also can be used to remove elements from a list and to delete
#variables from the interactive session. You can remove the element at any valid index or
#the element(s) from any valid slice. Deleting

numbers = list(range(0,10))
print(numbers)
del(numbers[-1])
print(numbers)

#deleting a slice from a list
del numbers[0:2]
print(numbers)
del numbers[::2]
print(numbers)
del(numbers[:])
print(numbers)

#Deleting a variable from the current session
#The del statement can delete any variable. Let’s delete numbers from the interactive
#session, then attempt to display the variable’s value, causing a NameError:

del numbers
print(numbers)