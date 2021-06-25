import json
filename = 'number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favourite number ? : ")
    with open(filename,'w') as f:
        json.dump(number,f)
        print(f"Your favourite number is : {number}")
else:
    print(f"I remember, your favourite number is {number}")