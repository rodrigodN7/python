#
#By Rodrigo Noriega
#
#
#sequence-controlled iteration; formatted strings
#
#

"""Class average program with sequence-controlled iteration."""

#initialization phase 
total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

#processing phase
for grade in grades:
    total += grade
    grade_counter += 1

#termination phase
average = total / grade_counter
print(f'Class average is {average}')