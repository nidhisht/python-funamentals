planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

#delete item by index
print(planets)  #output: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
del planets[8]
print(planets)  #output: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


#Remove item from the list
planets.remove("Mars")
print(planets)  #output: ['Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']