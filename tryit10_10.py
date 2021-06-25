file = '65659-0.txt'
result = 0
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
         result += line.count('the')
    print(result)
    