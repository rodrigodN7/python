#
#By Rodrigo Noriega
#
#arrays with numpy
#
#
#

from timeit import timeit
import numpy as np
from numpy import dtype

numbers = np.array([2,3,5,7,11])
print(type(numbers))
print(numbers)

#multidimensional arguments
myArray = np.array([[1,2,3],[4,5,6]])
print(myArray)

#array attributes
integers = np.array([[1,2,3],[4,5,6]])
print(integers)

floats = np.array([[0.0,0.1,0.2,0.3,0.4]])
print(floats)

#determining an array's element type
print(integers.dtype)
dtype('int64')
print(floats.dtype)

#determining an array's dimensions
print(integers.ndim)
print(integers.shape)
print(floats.ndim)
print(floats.shape)

#determining array's number of elements and element size
#You can view an array’s total number of elements with the attribute size and the
#number of bytes required to store each element with itemsize:
print(integers.size)
print(integers.itemsize)
print(floats.size)
print(floats.itemsize)

#Note that integers’ size is the product of the shape tuple’s values—two rows of
#three elements each for a total of six elements. In each case, itemsize is 8 because
#integers contains int64 values and floats contains float64 values, which each
#occupy 8 bytes.

#iterating through a multidemsional array's elements
for row in integers:
    for column in row:
        print(column, end=' ')
    print()

#You can iterate through a multidimensional array as if it were onedimensional
#by using its flat attribute:
for i in integers.flat:
    print(i, end=' ')

#filling arrays with specific values
zeroArray = np.zeros(5)
print(zeroArray)

oneArray = np.ones((2,4), dtype=int)

#The array returned by full contains elements with the second argument’s value and type:
fullArray = np.full((3,5), 13)
print(fullArray)

#creating arrays from ranges
#creating integer ranges with arange
arangeArray = np.arange(5)
print(arangeArray)
arangeArray = np.arange(5,10)
print(arangeArray)
arangeArray = np.arange(10,1,-2)
print(arangeArray)

#creating floating-point ranges with linspace
#The optional keyword argument num specifies the number of evenly spaced values to produce—this
#argument’s default value is 50:
linspaceArray = np.linspace(0.0, 1.0, num = 5)
print(linspaceArray)

#reshaping an array
reshapeArray = np.arange(1,21).reshape(4,5)
print(reshapeArray)

#displaying large arrays
largeArray = np.arange(1,100001).reshape(4,25000)
print(largeArray)
largeArray = np.arange(1,100001).reshape(100,1000)
print(largeArray)

#list vs array performance: introducing %timeit
#we’ll use the IPython %timeit magic command, which times the average duration of operations. 
# Note that the times displayed on your system may vary from what we show here

#NOTE: investigate about timeit!!!

#other ipython magics
#%load to read code into IPython from a local file or URL.
#%save to save snippets to a file.
#%run to execute a .py file from IPython.
#%precision to change the default floatingpoint
#precision for IPython outputs.
#%cd to change directories without having to exit IPython first.
#%edit to launch an external editor—handy if you need to modify more complex
#snippets.
#%history to view a list of all snippets and commands you’ve executed in the
#current IPython session.

#array operators
numbers = np.arange(1,6)
print(numbers)
print(numbers * 2) #is equivalent to:
#this, also called broadcasting
print(numbers * [2,2,2,2,2]) 
print(numbers ** 3)
print(numbers)
numbers += 10
print(numbers)
#print(numbers += 10) - this will cause an error, an assignment cannot be done inside the print function

#arithmetic operations between arrays
numbers2 = np.linspace(1.1, 5.5, 5)
print(numbers2)
print(numbers * numbers2)

#comparing arrays
print(numbers)
print(numbers >= 13)
print(numbers2)
print(numbers2 < numbers)
print(numbers == numbers2)
print(numbers == numbers)

#numpy calculation methods
grades = np.array([
                    [87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]
                ])#end of array

print(grades)

#we can use methods to calculate sum, min, max, mean, std and var
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.min())
print(grades.std())
print(grades.var())

#calculations by row or column
print(grades.mean(axis = 0))
print(grades.mean(axis = 1))

#universal functions
numbers = np.array([1,4,9,16,25,36])
print(numbers)
print(np.sqrt(numbers))

#add two arrays with the same shape, using add universal functions
numbers2 = np.arange(1,7) * 10
print(numbers2)
print(np.add(numbers,numbers2)) # this is equivalent to: numbers + numbers2
#multiply
print(np.multiply(numbers2, 5)) # this is equivalent to: numbers2 * 5

#reshape numbers2 into a 2-by-3 array, then multiply its values by a one dimensional array of three elements
numbers3 = numbers2.reshape(2,3)
print(numbers3)
numbers4 = np.array([2,4,6])
print(np.multiply(numbers3, numbers4))
#other universal functions
#Math—add, subtract, multiply, divide, remainder, exp, log, sqrt, power, and more.
#Trigonometry—sin, cos, tan, hypot, arcsin, arccos, arctan, and more.
#Bit manipulation—bitwise_and, bitwise_or, bitwise_xor, invert, left_shift and right_shift.
#Comparison—greater, greater_equal, less, less_equal, equal, not_equal, logical_and, logical_or, logical_xor, logical_not, minimum, maximum, and more.
#Floating point—floor, ceil, isinf, isnan, fabs, trunc, and more

#indexing and slicing
grades = np.array([
                    [87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]
                ])#end of array
print(grades)
print(grades[0,1])

#selecting a subset of two-dimensional array's rows
print(grades[1])#this print row 1
print(grades[0:2]) #select multiple sequential rows
print(grades[[1,3]]) #select multiple non-sequential rows

#select a subset of a two-dimwnsional array's columns
print(grades[:,0])# we only select column 0
print(grades[:, 1:3]) #select columns 1 to 3, three no print becaus it not exists!
print(grades[:, [0,2]]) #print specific columnsz

# VIEWS: Shallow copies
#The array method view returns a new array object with a view of the original array

numbers = np.arange(1,6)
print(numbers)
numbers2 = numbers.view()
print(numbers2)

#We can use the builtin id function to see that numbers and numbers2 are different objects:
print(id(numbers))
print(id(numbers2))

#To prove that numbers2 views the same data as numbers, let’s modify an element in numbers, then display both arrays:
numbers[1] *= 10
print(numbers2)
print(numbers)

#Similarly, changing a value in the view also changes that value in the original array:
numbers2[1] /= 10
print(numbers)
print(numbers2)

#slice views
numbers2 = numbers[0:3]
print(numbers2)

#Again, we can confirm that numbers and numbers2 are different objects with id:
print(id(numbers))
print(id(numbers2))

#We can confirm that numbers2 is a view of only the first three numbers elements by
#attempting to access numbers2[3], which produces an IndexError:
#print(numbers2[3])

numbers[1] *= 20
print(numbers)
print(numbers2)

#deep copies
#The array method copy returns a new array object with a deep copy of the original
#array object’s data.
numbers = np.arange(1,6)
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
numbers[1] *= 10
print(numbers)
print(numbers2)
print(id(numbers), id(numbers2))

#If you need deep copies of other
#types of Python objects, pass them to the copy module’s deepcopy function.

#reshaping and transposing
#reshape vs resize

grades = np.array([[87,96,70],[100,87,90]])
print(grades)
print(grades.reshape(1,6))
print(grades)

#Method resize modifies the original array’s shape:
grades.resize(1,6)
print(grades)

#flatten vs ravel
#You can take a multidimensional array and flatten it into a single dimension with the
#methods flatten and ravel. Method flatten deep copies the original array’s data:

grades = np.array([[87,96,71], [100,87,90]])
print(grades)
flattened = grades.flatten()
print(flattened)
flattened[0] = 100
print(flattened)
print(grades)

#Method ravel produces a view of the original array, which shares the grades
#array’s data:
raveled = grades.ravel()
print(raveled)
raveled[0] = 100
print(raveled)

#transpose rows and columns
#You can quickly transpose an array’s rows and columns—that is “flip” the array, so
#the rows become the columns and the columns become the rows. The T attribute
#returns a transposed view (shallow copy) of the array. The original grades array
#represents two students’ grades (the rows) on three exams (the columns).
print(grades.T)
#Transposing does not modify the original array:
print(grades)

#horizontal and vertical stacking
grades2 = np.array([[94,77,90],[100,81,82]])
#We can combine grades and grades2 with NumPy’s hstack
#(horizontal stack) function by passing a tuple containing the arrays to combine.
print(np.hstack((grades,grades2)))
print(np.vstack((grades,grades2)))