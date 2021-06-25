class User:
    """A simple example of how classes works"""

    def __init__(self, first_name, last_name, age, heigth, weight,login_attempts):
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
        print(f"Number of times user has been logged has just been increased : {self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Number of times user has been logged has just been reseted : {self.login_attempts}")


maciek = User('maciek', 'roszczyniały', 21, 198, 60,45)
maciek.describe_user()
maciek.increment_login_attempts()
maciek.describe_user()
maciek.reset_login_attempts()
maciek.describe_user()
maciek.increment_login_attempts()
maciek.reset_login_attempts()

