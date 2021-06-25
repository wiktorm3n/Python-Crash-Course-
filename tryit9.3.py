class User:
    """A simple example of how classes works"""
    def __init__(self,first_name,last_name,age,heigth,weight):
        """Initializing attributes to descripe User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.heigth = heigth
        self.weight = weight
    def describe_user(self):
        """Simple description of User"""
        description = f"First name : {self.first_name.title()}\n"
        description += f"Last name : {self.last_name.title()}\n" 
        description += f"Age : {self.age}\n"
        description += f"Heigth : {self.heigth}\n"
        description += f"Weight : {self.weight}\n"
        print(description)

    def greet_user(self):
        """Simple greeting of a User"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, have a great day!\n")

maciek = User('maciek','roszczyniały',21,198,60)
tomek = User('tomek','hakata',45,569,34)
ola = User('aleksandra','hajto',12,124,90)
maciek.describe_user()
maciek.greet_user()
tomek.greet_user()
tomek.describe_user()
ola.greet_user()
ola.describe_user()