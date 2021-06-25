def make_cars(manufacturer,model,**car):
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car
car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)