list1 = [12, 'Haslemere Close', 'Roundshaw', 'Wallington', 'London', 'England', 'SM6 9JW']

dict1 = {
    'houseNo': 12,
    'streetName': 'Alcock Close',
    'area': 'Roundshaw',
    'town': 'Wallington',
    'county': 'London',
    'country': 'England',
    'postCode': 'SM6 9JW'
}

print(dict1)
print(dict1['town'])
print(dict1['area'])
print(dict1['houseNo'])

#Printing all the keys
print(dict1.keys())
print(dict1.values())

for i in dict1:
    print(i, dict1[i])

# #Adding new keys and values
dict1['nearestStation'] = 'Wallington Train Station'
print(dict1)

# #Removing key and value pair
del(dict1['area'])
print(dict1)

#Checking if a key exists
if 'area' in dict1:
    print(dict1['area'])
else:
    print('Key does not exist')

#Modifying values
dict1['houseNo'] = 15
print(dict1)

#Nested Dictonaries
dict2 = {
    'Aryan': {
        'age': 12,
        'DOB': '16/05/12',
        'grade': 8,
        'marks': [80, 96, 78, 100, 87]
    },
}