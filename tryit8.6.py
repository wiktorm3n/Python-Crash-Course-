def city_country(name,country):
    returnes = f"'{name}, {country}'"
    return returnes.title()

test1 = city_country('Gdansk','Poland')
test2 = city_country('Warsaw','Russai')
test3 = city_country('Szczecin','USA')
print(test1)
print(test2)
print(test3)

