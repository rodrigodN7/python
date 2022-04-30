#
#By Rodrigo Noriega
#
#generator expressions
#
#
#

#generator expressions can reduce your program’s
#memory consumption and improve performance if the whole list is not needed at once.

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

#To show that a generator expression does not create a list, let’s assign the preceding
#snippet’s generator expression to a variable and evaluate the variable:
squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print('\n', squares_of_odds)

#The text "generator object <genexpr>" indicates that square_of_odds is a
#generator object that was created from a generator expression (genexpr).