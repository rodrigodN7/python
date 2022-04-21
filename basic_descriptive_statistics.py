#
#By Rodrigo Noriega
#
#
#Basic descriptive statistics
#
#

print("""Find the minimum of three values""")

number1 = int(input('Enter first integer:'))
number2 = int(input('Enter first integer:'))
number3 = int(input('Enter first integer:'))

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('Minimum value is', minimum)

print("""Determining the Minimum and Maximum with Built-in functions main and max""")

#function main and max can receive any number of arguments
print(min(36,7,12))
print(max(36,27,12))
