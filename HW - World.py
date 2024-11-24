database = {
    'London': 'United Kingdom',
    'Paris': 'France',
    'Berlin': 'Germany',
    'Washington DC': 'USA',
    'New Delhi': 'India'
}

#Displaying all Cities
print(database.keys())

#Displaying all Countries
print(database.values())

#Inserting a Pair
database['Vienna'] = 'Austria'
print(database)

#Removing A Pair
del(database['Washington DC'])
print(database)

#Checking if a key exists
if 'London' in database:
    print(database['London'])
else:
    print('Key not found')

#Modifying Values
database['London'] = 'England'