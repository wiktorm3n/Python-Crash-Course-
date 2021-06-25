filename = 'guest_book.txt'

prompt = '\nHello, what is your name? : '
active = True
print("Press 'q' to quit the program")
while active:
    name_book = input(prompt)
    if name_book == 'q':
        active = False
    else:
        with open(filename,'a') as file_object:
            file_object.write(f"Hello, {name_book.title()} welcome to the learning of Python!\n")
