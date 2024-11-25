# Function accept celsius as input parameter and return Fahrenheit
def convertToFahrenheit(celsius):
    return ((9/5)*celsius)+32

# Function accept Fahrenheit as input parameter and return celsius
def convertToCelsius(fahrenheit):
    return (5/9)*(fahrenheit-32)


print(convertToFahrenheit(30))
print(convertToCelsius(86))