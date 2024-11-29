cities = {"Bangalore", "London", "Mysore", "Mumbai", "Bangkok"}

cities.add("Chennai")
print(cities)                #output:

cities.remove("Mysore")
print(cities)                #output:

# Difference between remove and discard is remove will throw error if item doesn't exist. However discard will ignore it.
cities.discard("Beijing")
print(cities)               #output: {'Mumbai', 'Chennai', 'Bangkok', 'Bangalore', 'London'}


# Every items on the set will be removed
cities.clear()
print(cities)               #output: set()