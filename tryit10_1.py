file_path = 'learning_python.txt'
with open(file_path) as file_object:
    contnents = file_object.read()
    print(contnents.rstrip())

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())