# city_functions.py
# CSD-325 Module 7
# Author: Natasha Foreman

def city_country(city, country, population=None, language=None):
    """
    Return a string in the form:
      City, Country
      City, Country - population xxx
      City, Country - population xxx, Language
    depending on which arguments are provided.
    """
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language.title()}"

    return result

print(city_country("santiago", "chile"))                 
print(city_country("santiago", "chile", 5000000))
print(city_country("santiago", "chile", 5000000, "spanish"))