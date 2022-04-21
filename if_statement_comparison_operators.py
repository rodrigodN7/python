#
#By Rodrigo Noriega
#
#
#Decision making: The if statement and comparison operators
#
#

print(7 > 4)
print(7 < 4)

#comparison operators
#>, <, >=, <=, ==, !=

print('Enter two integers, and I will tell you \
the relationship they satisfy')

number1 = int(input('Enter first integer'))
number2 = int(input('Enter second integer'))

if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print('The numbers are not equal')

if number1 != number2:
    print(number1, 'is note equal to', number2)
else:
    print('The numbers are equal')

if number1 < number2:
    print(number1, 'is less than ', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

#chaining comparisons
x = 3
print(1 <= x <= 5)

x = 10
print(1 <= x <= 5)