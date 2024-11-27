# dict() function provide an alternative way to create dictionary in python

computers = dict()
print(computers)    #output: {}

computers = dict(Apple= "Macbook Pro", Dell="Latitude 5530")
print(computers)    #output: {'Apple': 'Macbook Pro', 'Dell': 'Latitude 5530'}

copy_of_computer = dict(computers)
print(copy_of_computer) #output: {'Apple': 'Macbook Pro', 'Dell': 'Latitude 5530'}