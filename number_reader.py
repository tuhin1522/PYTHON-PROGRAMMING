import json

#numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)