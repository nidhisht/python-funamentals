# use Sets  to remove duplicate values from list

cities = ["Bangalore", "London", "Bangalore", "Bangalore", "Mysore"]
print(set(cities))          #output: {'Mysore', 'Bangalore', 'London'}


# convert set to list
print(list(set(cities)))    #output: ['London', 'Bangalore', 'Mysore']