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