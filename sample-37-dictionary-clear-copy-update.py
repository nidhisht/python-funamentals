
car = {"make": "Honda", "Model": "Civic", "year": 2018}

vehicle = car.copy()
print(vehicle)  #output: {'make': 'Honda', 'Model': 'Civic', 'year': 2018}

car.clear()
print(car)  #output: {}


transmission = {"transmission":"manual"}
vehicle.update(transmission)
print(vehicle)  #output: {'make': 'Honda', 'Model': 'Civic', 'year': 2018, 'transmission': 'manual'}


vehicle["transmission"] = "automatic"
print(vehicle)  #output: {'make': 'Honda', 'Model': 'Civic', 'year': 2018, 'transmission': 'automatic'}