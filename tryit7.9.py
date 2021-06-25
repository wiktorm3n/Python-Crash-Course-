sandwich_order = ['cheeseburger', 'pastrami' ,'hamburger', 'pastrami' ,'jalapenoburger', 'pastrami' ,'chickenburger','fishburger']
finished_sandwiches = []
print("The deli has run out of 'pastrami'.\n")

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f"I made your {current_sandwich.title()}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made : ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())