class User:
    """A simple example of how classes works"""

    def __init__(self, first_name, last_name, age, heigth, weight, login_attempts):
        """Initializing attributes to descripe User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.heigth = heigth
        self.weight = weight
        self.login_attempts = login_attempts

    def describe_user(self):
        """Simple description of User"""
        description = f"First name : {self.first_name.title()}\n"
        description += f"Last name : {self.last_name.title()}\n"
        description += f"Age : {self.age}\n"
        description += f"Heigth : {self.heigth}\n"
        description += f"Weight : {self.weight}\n"
        description += f"Login attempts : {self.login_attempts}\n"
        print(description)

    def greet_user(self):
        """Simple greeting of a User"""
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}, have a great day!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(
            f"Number of times user has been logged has just been increased : {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(
            f"Number of times user has been logged has just been reseted : {self.login_attempts}")

class Admin(User):
    def __init__(self, first_name, last_name, age, heigth, weight, login_attempts):
        super().__init__(first_name, last_name, age, heigth, weight, login_attempts)
        self.privilages = ['can add post','can delete post','can ban user']
    
    def show_privilages(self):
        for privilage in self.privilages:
            print(f"{privilage}\n")

test1 = Admin('Adam','Bujnowski',55,178,98,12)
test1.show_privilages()