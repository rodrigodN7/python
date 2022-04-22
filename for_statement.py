#
#By Rodrigo Noriega
#
#
#for statement
#
#

for character in 'Programming':
    print(character, end='  ')

print(10, 20, 30, sep=', ')

#iterables, lists and iterators

total = 0
for number in [2, -3, 0, 17, 9]:
    total = total + number

print(total)

#built in range function
for counter in range(10):
    print(counter, end=' ')

#augmented assignments
for number in [1,2,3,4,5]:
    total += number #is the same as total = total + number
print(total)

#list of the augmented assignments

augmented_assignment = [
                        '+=', '-=', '*=',
                        '**=', '/=', '//=',
                        '%='
                        ]

print(augmented_assignment)
