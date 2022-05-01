#
#By Rodrigo Noriega
#
#two-dimensional lists
#
#
#

#creating a two dimwnsional list
a = [[77, 68, 86, 73], 
     [96, 87, 89, 81], 
     [70, 90, 86, 81]]

for row in a:
    for item in row:
        print(item, end=' ')
    print()

#how the nested loops execute
for i,row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}] = {item}', end = ' ')
        print()
