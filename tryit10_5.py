filename = 'responses.txt'

prompt = "Hello, why do you like Programming? : "
print("Press 'q' to quit program")
active = True
while active:
    reason = input(prompt)
    if reason == 'q':
        active = False
    else:
        with open(filename,'a') as file_object:
            file_object.write(f"{reason}\n")
            
