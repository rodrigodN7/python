#
#By Rodrigo Noriega
#
#Default parameter value
#
#
#

def rectangle_area(length=2,width=3):
    """Return a rectangle's area"""
    return length * width

print(rectangle_area())
print(rectangle_area(10,5))

#keyword arguments
#When calling functions, you can use keyword arguments to pass arguments in any
#order. To demonstrate keyword arguments, we redefine the rectangle_area
#function—this time without default parameter values:

def rectangle_area1(length1, width1):
    """Return a rectangle's area"""
    return length1 * width1

print(rectangle_area1(width1=5, length1=10))

