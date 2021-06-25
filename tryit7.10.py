prompt = "If you could visit one place in the world, where would you go?  : "
polling_active = True
responses = {}

while polling_active:
    name = input("\nWhat's your name? : ")
    response = input(prompt)
    responses[name] = response
    repeat = input("Would you like to let another person respond? : (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n-----Poll Results-----")
for name,response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
