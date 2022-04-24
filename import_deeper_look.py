#
#By Rodrigo Noriega
#
#import: a deeper look
#
#
#

#importing multiple identifiers from a module
from math import ceil,floor
print(ceil(10.3))
print(floor(10.7))

#AVOID WILDCAR IMPORTS
#You can import all identifiers defined in a module with a wildcard import of the form
#from modulename import *
#This makes all of the module’s identifiers available for use in your code. Importing a
#module’s identifiers with a wildcard import can lead to subtle errors—it’s considered a
#dangerous practice that you should avoid.

e = 'Hello'
from math import *
#the e number will be printed, not the e variable, BE CAREFUL!
print(e)

#binding names for modules and module identifiers
import statistics as stats

grades = [85, 93, 45, 87, 93]
print(stats.mean(grades))

