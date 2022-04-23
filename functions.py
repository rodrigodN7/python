#
#By Rodrigo Noriega
#
#
#Functions
#
#

def square(number):
    """Calculate the square of a number"""
    return number ** 2

print(square(7))

#IPython can help you learn about the modules and functions you intend to use in your
#code, as well as IPython itself. For example, to view a function’s docstring to learn how
#to use the function, type the function’s name followed by a question mark (?):
#only works in python screen
#square?

#functions with multiple parameters
def maximum(value1, value2, value3):
    """Return the maximum of three values"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(maximum(12, 27, 36))
print(maximum(17.1 , 22.20, 150.8))
print(maximum('red', 'orange', 'yellow'))

#The call maximum(13.5, 'hello', 7) results in TypeError because strings and
#numbers cannot be compared to one another with the greaterthan
#(>) operator.

#getting the maximum and minimum using built-in functions
myList = [99, 107, 56, 36, 99]
print(max(myList))
print(min(myList))