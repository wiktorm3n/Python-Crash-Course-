sandwich_order = ['cheeseburger','hamburger','jalapenoburger','chickenburger','fishburger']
finished_sandwiches = []

while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f"I made your {current_sandwich.title()}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made : ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

