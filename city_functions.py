def city_country(city,country,population = ''):
    '''Function returns a single string of the form : 'City, Country' f.e Santiago, Chile'''
    '''Better version also gives additional information about population of certain city'''
    if population:
        c_c_name = f"{city.title()}, {country.title()} - {population}"
    else:
        c_c_name = f"{city.title()}, {country.title()}"
    return c_c_name
