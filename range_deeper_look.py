#
#By Rodrigo Noriega
#
#
#built-in function range: a deeper look
#
#
import decimal
from decimal import Decimal
from os import sep

for number in range(5,10):
    print(number, end=' ')

#the third argument is known as step
#it will count two by two

for number in range(0, 10, 2):
    print(number, end=' ')

for number in range(10, 0, -2):
    print(number, end=' ')

#type decimal for monetary amounts

value = 117.11
print(value)
print(f'{value:.20f}')


#decimal is included in the decimal module
principal = Decimal('1000.00')
print(type(principal))
print(principal)
rate = Decimal('0.05')

#decimal arithmetic
x = Decimal('10.5')
y = Decimal('2')

print(x + y)
print(x // y)
x += y
print(x)

#compound interest
#a=p(1+r)^n
#p is the original amount invested (i.e., the principal),
#r is the annual interest rate,
#n is the number of years and
#a is the amount on deposit at the end of the nth year.

for year in range(1,11):
    amount = principal * ( (1 + rate) ** year )
    print(f'{year:>2}{amount:>10.2f}')

#break and continu statements

for number in range(100):
    if number == 10:
        break
    print(number, end=' ')

for number in range(10):
    if number == 5:
        continue
    print(number, end=' ')