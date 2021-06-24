countries = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}

userInput = input('''Type anyone of the following
print - Print All countries along with their population
add - add a country name to my list
remove - remove a country
query - Ask for which particular country u want the details
''')

print('\n')


def print_all_countries(country):
    for countryName, countryPopulation in country.items():
        print(f"{countryName}==>{str(countryPopulation)} Crores")


def add_country(country):
    country_input = input("Enter Country Name: ")

    if country_input in country:
        return print("Country Already Exists!")
    else:
        population_input = input(f"Enter Population for {country_input}: ")
        country[country_input] = population_input
        print(f"{country_input} Added Successfully")
        print("\n")
        return print_all_countries(countries)  # To show that the country is actually added


def delete_country(country):
    country_input = input("Enter Country name to delete: ")

    if country_input in country:
        del country[country_input]
        print(f"Deleted {country_input} from the dictionary")
        print("\n")
        return print_all_countries(country)
    else:
        print(f"There is no country with the name {country_input} in this list")


def query_country(country):
    country_input = input("Enter Country Name you want the details: ")

    if country_input in country:
        country_population = country[country_input]
        return print(f"Name: {country_input}\nPopulation: {country_population} Crores")
    else:
        return print("There is no country like that!!!!!")


if userInput.lower() == "print":
    print_all_countries(countries)
elif userInput.lower() == "add":
    add_country(countries)
elif userInput.lower() == "remove":
    delete_country(countries)
elif userInput.lower() == "query":
    query_country(countries)
