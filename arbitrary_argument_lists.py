#
#By Rodrigo Noriega
#
#Arbitrary Argument Lists
#
#
#

print(min(88, 75, 96, 55, 83))

#The function’s documentation states that min has two required parameters (named
#arg1 and arg2) and an optional third parameter of the form *args, indicating that
#the function can receive any number of additional arguments. The * before the
#parameter name tells Python to pack any remaining arguments into a tuple that’s
#passed to the args parameter.

def average(*args):
    return sum(args) / len(args)

print(average(5,10))
print(average(5,10,15))
print(average(5,10,15,20))

#You can unpack a tuple’s, list’s or other iterable’s elements to pass them as individual
#function arguments. The * operator, when applied to an iterable argument in a
#function call, unpacks its elements. The following code creates a fiveelement
#grades list, then uses the expression *grades to unpack its elements as average’s arguments:

grades = [88, 75, 96, 55, 83]
print(average(*grades))