prompt = "\nWhat's your age? : "
while True:
    answer = input(prompt)
    answer = int(answer)
    if answer < 3 :
        print("You are free of charge.")
    elif answer < 12 :
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")