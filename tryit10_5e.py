filename = 'guest_book.txt'


prompt = '\nHello, what is your name? : '
active = True
flag = True
print("Press 'q' to quit the program")
while active:
    name_book = input(prompt)
    if name_book == 'q':
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(
                f"Hello {name_book.title()}, what is your reason to code? :\n")
        reason = input("Reason:")
        with open(filename,'a') as file_response:
            file_response.write(f"{reason}\n")