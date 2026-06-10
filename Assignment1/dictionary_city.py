# 11. Create a dictionary representing the population of different cities with keys as city names
# and values as population numbers and print it. Remove a city from the dictionary and print
# the modified dictionary.

cities = {
    "Kathmandu": 1500000,
    "Pokhara": 500000,
    "Biratnagar": 300000
}

print(cities)

del cities["Pokhara"]

print("Modified Dictionary: ",cities)