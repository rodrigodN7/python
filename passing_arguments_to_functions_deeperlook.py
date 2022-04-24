#
#By Rodrigo Noriega
#
#passing arguments to functions: a deeper look
#
#
#

#built-in function id and object identities

x = 7
#The integer result of calling id is known as the object’s identity
print(id(x))

#passing an onject to a function
def cube(number):
    print('id(number): ', id(number))
    return number ** 3

print(cube(x))

def cube(number):
    print('number is: ', number)
    return number ** 3

print(cube(x))

#immutable objects as arguments
def cube(num):
    print('id(number) before modifying number: ', id(num))
    num **= 3
    print('id(number) after modifying number: ', id(num))
    return num

#Numeric values are immutable, so the statement
#actually creates a new object containing the cubed value, then assigns that object’s
#reference to parameter number.
print(cube(x)) 

print(f'x = {x}; id(x) = {id(x)}')