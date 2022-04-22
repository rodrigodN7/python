#
#By Rodrigo Noriega
#
#
#sentinel-controlled iteration
#
#

"""Class average program with sentinel-controlled iteration"""

#initialization phase
total = 0 
grade_counter = 0

#processing phase
grade = int(input('Enter grade, -1 to end: '))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))

#termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'CLass average is {average:.2f}')
else:
    print('No grades were entered')