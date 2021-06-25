class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def descripe_restaurant(self):
        print(f"Name of the restaurant : {self.restaurant_name.title()}\n")
        print(f"Type of the cuisine : {self.cuisine_type.title()}\n")
        print(f"Number of guests : {self.number_served}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open !!!\n ")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','white-chocolate','mint','strawberry']

    def ice_cream_flavors(self):
        print(f"Ice Cream Flavors : {self.flavors}")

test1 = IceCreamStand('Lody na Patyku','Italian')
test1.ice_cream_flavors()