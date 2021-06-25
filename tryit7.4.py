prompt = "\nWhat topping do you want? : "
prompt += "\nEnter 'quit' to exit this program \t"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"I will add {message.title()} to the pizza.\n")

