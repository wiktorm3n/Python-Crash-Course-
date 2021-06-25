cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(cats_file,'r') as cf:
        clines = cf.readlines()
    for lines in clines:
        print(lines.rstrip())
except FileNotFoundError:
    print("Sorry! Seems like this file does not exist...")

try:
    with open(dogs_file, 'r') as df:
        dlines = df.readlines()
    for lines in dlines:
        print(lines.rstrip())
except FileNotFoundError:
    print("Sorry! Seems like this file does not exist...")
