class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descripe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name.title()}\n")
        print(f"Type of the cuisine : {self.cuisine_type.title()}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open !!!\n ")

restaurant = Restaurant('Hamilton','French')
restaurant.open_restaurant()
restaurant.descripe_restaurant()
