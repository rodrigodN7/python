#
#By Rodrigo Noriega
#
#Simulating stacks with lists
#
#
#

#push (append) two strings onto it, then pop
#the strings to confirm they’re retrieved in lastin, firstout(LIFO) order:

stack = []
print(stack)
stack.append('red')
print(stack)
stack.append('green')
print(stack)

#list method pop with no arguments, removes and returns the item at the end of the list.
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()#this will cause an error

