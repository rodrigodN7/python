#
#By Rodrigo Noriega
#
#Methods: functions that belongs to objects
#
#
#

#A method is simply a function that you call on an object using the form
#object_name.method_name(arguments)

s = 'Hello'
print(s.lower())
print(s.upper())
print(s)

#scope rules
#accesing a global variable
def access_global():
    print('s printed from access_global:', s)
access_global()

def try_modify_global():
    s = 'Good Bye'
    print('s printed from try_modify_global: ', s)
try_modify_global()

#you cannot modify a global variable in a function—when you first
#assign a value to a variable in a function’s block, Python creates a new local variable:

#modify global
def modify_global():
    global s
    print(s) #original value of the s variable
    s = 'Global modified'
    print('s printed from modify_global: ',s )

modify_global()
#we can verify that s now has a new value changed in the function modify_global
print('New value of s: ', s)
