import random

class Lottery:
    def __init__(self) -> None:
        pass
    def lottery():
        lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 69, 'q', 'w', 'e', 'r', 't']
        firts_choice = random.choice(lottery)
        second_choice = random.choice(lottery)
        third_choice = random.choice(lottery)
        fourth_choice = random.choice(lottery)
        print(f"Any of ticket matching these four numbers or letters wins a prize: {firts_choice} , {second_choice} , {third_choice} , {fourth_choice}")
