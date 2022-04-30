#
#By Rodrigo Noriega
#
#filter, map and reduce
#
#
#

#Filtering a Sequence’s Values with the Built-In filter Function
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort()

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0

#Function filter returns an iterator, so filter’s results are not produced until you
#iterate through them.
#filter’s first argument must be a function that receives one argument and returns True
print(list(filter(is_odd, numbers)))

#We can obtain the same results as above by using a list comprehension with an if clause:
myList = [item for item in numbers if is_odd(item)]
print(myList)

#Using a lambda Rather than a Function
#For simple functions like is_odd that return only a single expression’s value, you can
#use a lambda expression (or simply a lambda) to define the function inline where
#it’s needed—typically as it’s passed to another function
#Function filter returns an iterator, so filter’s results are not produced until you iterate through them.
#A lambda begins with the lambda keyword followed by a commaseparated
#parameter list, a colon (:) and an expression. In this case, the parameter list has one parameter
#named x. A lambda implicitly returns its expression’s value. So any simple function of the form
#def function_name(parameter_list):
#   return expression
#may be expressed as a more concise lambda of the form:
#lambda parameter_list: expression
print(list(filter(lambda x : x % 2 != 0, numbers)))

#Mapping a Sequence’s Values to New Values
#use builtin function map with a lambda to square each value in numbers:
#Function map’s first argument is a function that receives one value and returns a new
#value—in this case, a lambda that squares its argument
print(numbers)
print(list(map(lambda x: x ** 2, numbers)))

#equivalent list comprehension
myList1 = [item ** 2 for item in numbers]
print(myList1)

#Combining filter and map
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers))))

#Reduction: Totaling the Elements of a Sequence with sum
#As you know reductions process a sequence’s elements into a single value. You’ve
#performed reductions with the builtin functions len, sum, min and max. You also can
#create custom reductions using the functools module’s reduce function. See:
#https://docs.python.org/3/library/functools.html for a code example.