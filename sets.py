#
#By Rodrigo Noriega
#
#Sets
#
#
#

#A set is an unordered collection of unique values. Sets may contain only immutable
#objects, like strings, ints, floats and tuples that contain only immutable elements
#Though sets are iterable, they are not sequences and do not support indexing and
#slicing with square brackets, []. Dictionaries also do not support slicing.

#creating a set with curly braces
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}

#notice that the duplicate string 'red' was ignored
print(colors)

#determining the length
print(len(colors))
print('red' in colors)
print('purple' in colors)
print('purple' not in colors)

#iterating through a set
for color in colors:
    print(color.upper(), end=' ')

#creating a set with the built-in function set function
numbers = list(range(10)) + list(range(5))
print(numbers)
print(type(numbers))
print(set(numbers))
print(numbers)
print(type(numbers))

#frozenset: an immutable set type
#Sets are mutable—you can add and remove elements, but set elements must be
#immutable. Therefore, a set cannot have other sets as elements. A frozenset is an
#immutable set—it cannot be modified after you create it, so a set can contain frozensets
#as elements. The builtin function frozenset creates a frozenset from any iterable.

#comparing sets
print({1,3,5} == {3,5,1})
print({1,3,5} != {3,5,1})
print({1,3,5} < {3,5,1})
print({1,3,5} < {7,3,5,1})
print({1,3,5} <= {3,5,1})
print({1,3} <= {3,5,1})

#check for an impropers subset with the set method issubset
print({1,3,5}.issubset({3,5,1}))
print({1,2}.issubset({3,5,1}))
print({1,3,5}>{3,5,1})
print({1,3,5,7}>{3,5,1})
print({1,3,5}>={3,5,1})
print({1,3,5}>={3,1})
print({1,3}>={3,1,7})

#check for an improper superset with the set method issuperset
{1,3,5,}.issuperset({3,5,1})
{1,3,5,}.issuperset({3,2})

#mathematical set operations

#union
#The union of two sets is a set consisting of all the unique elements from both sets
print({1,3,5} | {2,3,4})
print({1,3,5}.union([20,20,3,40,40]))

#intersection
#The intersection of two sets is a set consisting of all the unique elements that the two
#sets have in common
print({1,3,5} & {2,3,4})
print({1,3,5}.intersection([1,2,2,3,3,4,4]))

#difference
#The difference between two sets is a set consisting of the elements in the left operand
#that are not in the right operand.
print({1,3,5} - {2,3,4})
print({1,3,5,7}.difference([2,2,3,3,4,4]))

#symmetric difference
#The symmetric difference between two sets is a set consisting of the elements of
#both sets that are not in common with one another.
print({1,3,5}^{2,3,4})
print({1,3,5,7}.symmetric_difference([2,2,3,3,4,4]))

#disjoint
#Two sets are disjoint if they do not have any common elements.
print({1,3,5}.isdisjoint({2,4,6}))
print({1,3,5}.isdisjoint({4,6,1}))

#mutable set operators and methods
#mutable mathematical set operations

#union augmented assignment |= performs a set unio,3,4n operation,
#but |= modifies its left operand
numbers = {1,2,3}
numbers |= {2,3,4}
print(numbers)

#Similarly, the set type’s update method performs a union operation modifying the set
#on which it’s called—the argument can be any iterable:
numbers.update(range(10))
print(numbers)

#other mutable methods are
#intersection augmented assignment &=
#difference augmented assignment -=
#symmetric difference augmented assignment ^=

#and their corresponding methods with iterable arguments are:
#intersection_update
#difference_update
#symmetric_difference_update

#methods for adding and removing elements
numbers.add(17)
numbers.add(3)
print(numbers)

#Set method remove removes its argument from the set—a KeyError occurs if the
#value is not in the set:
numbers.remove(3)
print(numbers)

#Method discard also removes its argument from the set but does not cause an
#exception if the value is not in the set.
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

#set comprehensions
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
print(numbers)
evens = {item for item in numbers if item % 2 == 0}
print(evens)

