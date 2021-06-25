class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descripe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name.title()}\n")
        print(f"Type of the cuisine : {self.cuisine_type.title()}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open !!!\n ")


restaurant = Restaurant('Hamilton', 'French')
restaurant1 = Restaurant('Sfinx','Polish')
restaurant2 = Restaurant('Pizza Hut','Italian')
restaurant.open_restaurant()
restaurant.descripe_restaurant()
restaurant1.descripe_restaurant()
restaurant1.open_restaurant()
restaurant2.descripe_restaurant()
restaurant2.open_restaurant()