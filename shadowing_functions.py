#
#By Rodrigo Noriega
#
#Shadowing
#
#
#

#If you define avariable named sum, it shadows the builtin
#function, making it inaccessible in your code.

#remember, sum is a built-in function
#if you declare it as a variable, the identifier
#no longer references the built-in function

print(sum([10,5]))

sum = 10 + 5
print(sum)

#this will show an error
print(sum([10,5]))