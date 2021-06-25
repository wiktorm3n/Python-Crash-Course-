import json
prompt = input("What is your favourite number? : ")

filename = 'favourite_number.json'
with open(filename,'w') as f:
    json.dump(prompt,f)
    