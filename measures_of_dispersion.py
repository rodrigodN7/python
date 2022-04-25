#
#By Rodrigo Noriega
#
#Measures of dispersion
#
#
#

import statistics
import math

#variance
print(statistics.variance([1,3,4,2,6,5,3,4,5,2]))

#standard deviation
print(statistics.pstdev([1,3,4,2,6,5,3,4,5,2]))
#Passing the pvariance function’s result to the math module’s sqrt function confirms our result
print(math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2])))