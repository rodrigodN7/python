#
# 
# By Rodrigo Noriega
# 
# Variables and assignment statements.
# 
# 

#using print to output the result of an addition
print(45+72)

#creating a variable and adding two numbers
x = 7
y = 3
print(x + y)
total = (x + y) + 7
print(total)

#using type()
print(type(total))
myFloat = total / 2
print(myFloat)
print(type(myFloat))

#addition
newTotal = total + 10
print(newTotal)
#substraction
mySubstraction = newTotal - 7
print(mySubstraction)
#multiplication
myMultiplication = mySubstraction * newTotal
print(myMultiplication)
#exponetiation
print(2**10)
#we can calculate the square root using exponentiation
print( 9 ** ( 1/2 ) )
#true division
print(7/4)
#floor division
#divides a numerator by denominator, yielding the highest integer thats's not greater than the result, truncating the fractional part.
print(7 // 4)
print(3 // 5)
print(14 // 7)
#in the next case floor division gives the closest integer that's not greater than 3.25, which is -4
print(-13 // 4)
#Exception! division by zero or variable not defined
#print(12/0)
#print(z+7)
#reminder
print(17%5)
print(7.5%3.5)

#Operator Precedence Rule
#Expression in parentheses evaluates first
#Exponentiation operations evaluate next, If an expression contains several exponentiation operations, 
#Python applies them from RIGHT to LEFT.
#Multiplication, division and modulus operations evaluate next. If an expression contains several multiplication, 
#true-division, floor-division and modulus operations, Python applies them from left to right. Multiplication,
#division and modulus are "on the same level of precedence"
#Addition and substraction opeations evaluate last. If an expression contains several addition and substraction operations,
#Python applies them from left to eight. Addition and substraction also have the same level of precedence