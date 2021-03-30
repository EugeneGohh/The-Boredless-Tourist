# Setting Up Project
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traverler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Travelling To Faraway Lands
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India")) # Avoid triggering valueError

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traverler_destination_index = get_destination_index(traveler_destination)
    return traverler_destination_index

test_destination_index = get_traveler_location(test_traverler)
print(test_destination_index)

# Visiting interesting places
attractions = []
for destination in destinations:
    attractions.append([])

print(attractions)

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)