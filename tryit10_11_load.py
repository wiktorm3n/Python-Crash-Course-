import json
filename = 'favourite_number.json'
with open(filename) as f:
    favourite_number = json.load(f)
print(favourite_number)