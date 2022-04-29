#
#By Rodrigo Noriega
#
#Other list Methods
#
#
#

from urllib import response


color_names = ['orange', 'yellow', 'green']
print(color_names)
color_names.insert(0, 'red')
print(color_names)

#adding an element to the end of a list
color_names.append('blue')
print(color_names)

#Adding all the elements of a sequence to the end of a list
color_names.extend(['indigo','violet'])
print(color_names)

#This is the equivalent of using +=. The following code adds all the characters of a string
#then all the elements of a tuple to a list:

sample_list = []
s = 'abc'
sample_list.extend(s)
print(sample_list)
t = (1,2,3)
sample_list.extend(t)
print(sample_list)
sample_list.extend((4,5,6))
print(sample_list)

#removing the firs occurence of an element in a list
color_names.remove('green')
print(color_names)

#emptying a list
color_names.clear()
print(color_names)

#counting the numbers of occurrences of an item
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,
             1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
    
for i in range(1,6):
    print(f'{i} appears {responses.count(i)} times in responses')

#reversing a lists elements
#List method reverse reverses the contents of a list in place, rather than creating a
#reversed copy, as we did with a slice previously:
color_names = ['red', 'orange', 'yellow', 'green', 'blue']
print(color_names)
color_names.reverse()
print(color_names)

#copying a list
copied_list = color_names.copy()
print(copied_list)

#this is equivalent to the previously demonstrated slice operation.