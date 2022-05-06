#
#By Rodrigo Noriega
#
#Dictionaries
#
#
#

#A dictionary associates keys with values. Each key maps to a specific value. The
#following table contains examples of dictionaries with their keys, key types, values and
#value types:
country_codes = {'Finland':'fi','South Africa':'za','Nepal':'np'}
print(len(country_codes))

def check_dict():
    if country_codes:
        print('Not empty')
    else:
        print('empty')

print(check_dict())
country_codes.clear()
print(check_dict())

#iterating through a dictionary
days_per_month = {'January': 31, 'February':28, 'March':31}
print(days_per_month)

#The following for statement iterates through days_per_month’s key–value pairs.
#Dictionary method items returns each key–value pair as a tuple, which we unpack into
#month and days:
for month,days in days_per_month.items():
    print(f'{month} has {days} days.')

#basic dictionary operations
roman_numerals = {'I':1, 'II':2, 'III':3, 'V':5, 'X':100}
print(roman_numerals)

#Accessing the value associated with a key
roman_numerals['X'] = 10
print(roman_numerals)

#adding a new key-value pair
roman_numerals['L'] = 50
print(roman_numerals)

#removing a key-balue pair
del roman_numerals['III']
print(roman_numerals)       

#You also can remove a key–value pair with the dictionary method pop, which returns
#the value for the removed key:
print(roman_numerals.pop('X'))

#Attempting to Access a Nonexistent Key
#this will show an error:
#print(roman_numerals['III'])
#you can prevent this error by using dictionary method get, which normally returns its
# #argument’s corresponding value. If that key is not found, get returns None
print(roman_numerals.get('III'))
print(roman_numerals.get('V'))

#testing wether a dictionary contains a specified key
print('V' in roman_numerals)
print('III' in roman_numerals)
print('III' not in roman_numerals)

#dictionary methods keys and values
months = {'January':1, 'February':2, 'March':3}

for month_name in months.keys():
    print(month_name, end=' ')

for month_number in months.values():
    print(month_number, end=' ')

#dictionary views
months_view = months.keys()

for key in months_view:
    print(key, end = ' ')

months['December'] = 12 
print(months)

for key in months_view:
    print(key, end = ' ')

#converting dictionary keys, values and key-value pairs to lists
print(list(months.keys()))
print(list(months.values()))
print(list(months.items()))

#processing keys in sorted order
for month_name in sorted(months.keys()):
    print(month_name, end=' ')

#dictionary comparisons
country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussels'}
print(country_capitals1 == country_capitals2)
print(country_capitals1 == country_capitals3)
print(country_capitals1 != country_capitals2)

#e.g. dictionary of students grade
"""Using a dictionary to represent an instructor's grade book."""
grade_book = {

        'Susan': [92,85,100],
        'Eduardo': [83,95,79],
        'Azizi': [91, 89, 82],
        'Pantipa': [97,91,92]
}

all_grades_total = 0
all_grades_count = 0

for name,grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total / len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)

print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

#e.g word counts
"""Tokenizing a string and counting unique words"""

text = ('this is a sample text with several words'
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORD:<12"}COUNT')

for word,count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))

#python standard library module collections
from collections import Counter

text = ('this is sample text with several words'
        'this is more sample twxt with some different words')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

#dictionary method update
country_code = {}
country_code.update({'South Africa': 'za'})
print(country_code)
#Method update can convert keyword arguments into key–value pairs to insert.
country_code.update({'Australia': 'ar'})
print(country_code)
#Method update also can receive an iterable object containing key–value pairs, such as
#a list of twoelement tuples.
country_code.update(({'Mexico': 'mx', 'United States': 'us'}))
print(country_code)
#dictionary comprehensions
months = {'January':1, 'February':2, 'March':3}
months2 = {number:name for name, number in months.items()}
print(months2)
grade = {'Sue':[98,87,94], 'Bob':[84,95,91]}
grade2 = {k : sum(v) / len(v) for k, v in grade.items()}
print(grade2)