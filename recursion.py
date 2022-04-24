#
#By Rodrigo Noriega
#
#recursion
#
#
#

factorial = 1

for number in range(5, 0, -1):
    factorial *= number

print(factorial)

#implementing a recursive factorial function
#the factorial also can be seen as:
#n! = n * (n-1)!

def factorial(numb):
    """Return factorial number"""
    if numb <= 1:
        return 1
    return numb * factorial(numb - 1)#recursive call

for i in range(11):
    print(f'{i}! = {factorial(i)}')