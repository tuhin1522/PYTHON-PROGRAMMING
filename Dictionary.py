# create a dictionary using {}
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# create a dictionary using dict()
person = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# create a dictionary from sequence having each item as a pair
person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
print(person)

# create dictionary with mixed keys keys
# first key is string and second is an integer
sample_dict = {"name": "Jessa", 10: "Mobile"}
print(sample_dict)
# output {'name': 'Jessa', 10: 'Mobile'}

# create dictionary with value as a list
person = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
print(person)
# output {'name': 'Jessa', 'telephones': [1178, 2563, 4569]}

# Accessing elements of a dictionary
# create a dictionary named person
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# access value using key name in []
print(person['name'])
# Output 'Jessa'

#  get key value using key name in get()
print(person.get('telephone'))
# Output 1178

# Get all keys and values
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Get all keys
print(person.keys())
# output dict_keys(['name', 'country', 'telephone'])
print(type(person.keys()))
# Output class 'dict_keys'

# Get all values
print(person.values())
# output dict_values(['Jessa', 'USA', 1178])
print(type(person.values()))  
# Output class 'dict_values'

# Get all key-value pair
print(person.items())
# output dict_items([('name', 'Jessa'), ('country', 'USA'), ('telephone', 1178)])
print(type(person.items()))
# Output class 'dict_items'

#Iterating a dictionary
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

#Iterating the dictionary using for loop
print('key', ':', 'value')
for key in person:
    print(key, ':', person[key])

# using items() method
print('key', ':', 'value')
for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])

# Adding items to the dictionary
person = {"name": "Jessa", 'country': "USA", "telephone": 1178}

# update dictionary by adding 2 new keys
person["weight"] = 50
person.update({"height": 6})

# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# Adding 2 new keys at once
# pass new keys as dict
person.update({"weight": 50, "height": 6})
# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6}

# pass new keys as as list of tuple
person.update([("city", "Texas"), ("company", "Google",)])
# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6, 'city': 'Texas', 'company': 'Google'}

# Set default value to a key
person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# set default value if key doesn't exists
person_details.setdefault('state', 'Texas')
# key doesn't exists and value not mentioned. default None
person_details.setdefault("zip")

# key exists and value mentioned. doesn't  change value
person_details.setdefault('country', 'Canada')

# Display dictionary
for key, value in person_details.items():
    print(key, ':', value)

# Modify the values of the dictionary keys
person = {"name": "Jessa", "country": "USA"}

# updating the country name
person["country"] = "Canada"
# print the updated country
print(person['country'])
# Output 'Canada'

# updating the country name using update() method
person.update({"country": "USA"})
# print the updated country
print(person['country'])
# Output 'USA'

#Removing items from the dictionary
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# Remove last inserted item from the dictionary
deleted_item = person.popitem()
print(deleted_item)  # output ('height', 6)
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50}

# Remove key 'telephone' from the dictionary
deleted_item = person.pop('telephone')
print(deleted_item)  # output 1178
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'weight': 50}

# delete key 'weight'
del person['weight']
# display updated dictionary
print(person)
# Output {'name': 'Jessa', 'country': 'USA'}

# remove all item (key-values) from dict
person.clear()
# display updated dictionary
print(person)  # {}

# Delete the entire dictionary
del person

# Checking if a key exists
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# Get the list of keys and check if 'country' key is present
key_name = 'country'
if key_name in person.keys():
    print("country name is", person[key_name])
else:
    print("Key not found")
# Output country name is USA

# Join two dictionary
dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}

# copy second dictionary into first dictionary
dict1.update(dict2)
# printing the updated dictionary
print(dict1)
# output {'Jessa': 70, 'Arul': 80, 'Emma': 55, 'Kelly': 68, 'Harry': 50, 'Olivia': 66}

# Nested dictionary

# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# Display dictionary
print("person:", person)

# Get nested dictionary key 'city'
print("City:", person['address']['city'])

# Iterating outer dictionary
print("Person details")
for key, value in person.items():
    if key == 'address':
        # Iterating through nested dictionary
        print("Person Address")
        for nested_key, nested_value in value.items():
            print(nested_key, ':', nested_value)
    else:
        print(key, ':', value)

# Dictionary comprehension
# output_dictionary = {key : value for key,value in iterable [if key,value condition1]}
# calculate the square of each even number from a list and store in dict
numbers = [1, 3, 5, 2, 8]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_squares)

# output {2: 4, 8: 64}

















