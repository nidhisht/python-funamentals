
car = {"make": "Honda", "Model": "Civic", "year": 2018}

car.pop("Model")
print(car)  #output: {'make': 'Honda', 'year': 2018}


car.popitem()
print(car)  #output: {'make': 'Honda'}