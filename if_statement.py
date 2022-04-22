#
#By Rodrigo Noriega
#
#
#IF statement
#
#

grade = 85

if grade >= 60:
    print('Passed!')

if 1:
    print('Non zero values are true, so this will print')

if 0:
    print('Zero is false, so this will not print')

#if else and if elif else statements
grade = 87

if grade >= 60:
    print('Passed!')
else:
    print('Failed!')

grade = 57

if grade >= 60:
    print('Passed!')
else:
    print('Failed!')

#conditional expression
result = ('Passed!' if grade >= 60 else 'Failed!')
print(result)

#or
print('Passed' if grade >= 60 else 'Failed!')

#if elif else statement
grade = 77
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')