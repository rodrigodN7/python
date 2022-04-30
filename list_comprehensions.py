#
#By Rodrigo Noriega
#
#lists comprehensions
#
#
#

list1 = []
print(list1)

for item in range(1,6):
    list1.append(item)

print(list1)

#Using a List Comprehension to Create a List of Integers3
#We can accomplish the same task in a single line of code with a list comprehension:
list2 = [item for item in range(1,6)]
print(list2)

#Mapping: Performing Operations in a List Comprehension’s Expression
list3 = [item ** 3 for item in range(1,6)]
print(list3)

#Filtering: List Comprehensions with if Clauses
list4 = [item for item in range(1,11) if item % 2 == 0]
print(list4)

#List Comprehension That Processes Another List’s Elements
colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print(colors2)
print(colors)

