
car = {"make": "Honda", "Model": "Civic", "year": 2018}

car.setdefault("transmission", "manual")
print(car)  #output: {'make': 'Honda', 'Model': 'Civic', 'year': 2018, 'transmission': 'manual'}

# Calling setdefault will only work if key does not exist. 
# setdefault will not change the default value if its alread assigned to the key
car.setdefault("transmission", "automatic")
print(car)  #output: {'make': 'Honda', 'Model': 'Civic', 'year': 2018, 'transmission': 'manual'}