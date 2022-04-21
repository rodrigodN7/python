#
#By Rodrigo Noriega
#
#
#Getting input from the user
#
#

name = input("What's your name?")
print('Hi!', name)

value1 = input('Enter first number')
print(type(value1))
value2 = input('Enter second number')
print(type(value2))

#This is a tring concatenation
print('The string concatenation is:', value1 + value2)

#convert the string to integer using the int function
value1 = int(value1)
value2 = int(value2)

total = value1 + value2
print('The new value is:', total)

#or we can use int like this
value3 = int(input('Enter third number'))
print(type(value3))
value4 = int(input('Enter third number'))
print(type(value4))
print('The sum is:', value3 + value4)

#If the string passed to int cannot be converted to an integer, a ValueError occurs:

bad_value = int(input('Enter another integer: '))

#int function also can convert a floating-point value to an integer
floatToInt = int(10.7)
print(floatToInt)