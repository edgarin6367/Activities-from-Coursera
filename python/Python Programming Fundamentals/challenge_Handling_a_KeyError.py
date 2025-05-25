def get_city_population(populations, city):
    """Returns the population of a specified city from a dictionary of city populations."""
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'City "Tampa" not found in population data.')
        
# Y luego llamar así, manejando el error tú mismo:
try:
    city_populations1 = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
    city_name1 = "Tampa"
    get_city_population(city_populations1, city_name1)
except KeyError as e:
    print(e)

try:
    city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
    city_name = "New York"
    get_city_population(city_populations, city_name)
except KeyError as e:
    print(e)
