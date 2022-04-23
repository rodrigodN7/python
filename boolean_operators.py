#
#By Rodrigo Noriega
#
#
#boolean operators AND, OR and NOT
#
#

from typing import final

gender = 'female'
age = 70
if gender == 'female' and age >= 65:
    print('Senior female')

#and truth table
andTruthTab = [

    'A', 'B', 'A and B'
    '0', '0', '0'
    '1', '0', '0'
    '0', '1', '0'
    '1', '1', '1'
]

semester_average = 83
final_exam = 95

if semester_average >= 90 or final_exam >= 90:
    print('Student gets an "A"')

#or truth table
orTruthTab = [

    'A', 'B', 'A or B'
    '0', '0', '0'
    '1', '0', '1'
    '0', '1', '1'
    '1', '1', '1'
]

grade = 87

if not grade == -1: #is the same: if grade != -1:
    print('The next grade is', grade)