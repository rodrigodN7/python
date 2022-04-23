#
#By Rodrigo Noriega
#
#
#intro to data science:
#mean, median and mode
#

import statistics
from statistics import *

grades = [85, 93, 45, 89, 85]

#getting mean by maths
myMean = sum(grades) / len(grades)
print(myMean)

#getting mean, meadian and mode using the built-in function
print(statistics.mean(grades))
print(statistics.median(grades))
print(statistics.mode(grades))

#we can use built-in function sorted
#to get a copy of grades with its values
#arranged in increased order
print(grades)
print(len(grades))
print(sorted(grades))
