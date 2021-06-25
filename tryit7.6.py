prompt = "\nWhat's your age? : "
prompt += "\nEnter 'quit' to exit the program.\t"
while True:
    answer = input(prompt)
    if answer == 'quit':
        break
    else:
        answer = int(answer)
        if answer < 3:
            print("You are free of charge.")
        elif answer < 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")