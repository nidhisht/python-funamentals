str1 = 'this is string'
str2 = "this is also string!"
print(str1)
print(str2)

# Access by index
str3="orange"
print(str3[3])      #output: n
print("orange"[2])  #output: a

# Slice a string
str4 = "Everest Basecamp"
print(str4[0:7])    #output: Everest
print(str4[8:12])   #output: Base
print(str4[8:20])   #output: Basecamp
print(str4[8:])     #output: Basecamp

# Get the datatype
str5 = False
str6 = "Hello"
str7 = 200
str8 = 10.6
print(type(str5),type(str6),type(str7),type(str8)) #output: <class 'bool'> <class 'str'> <class 'int'> <class 'float'>


# Convert value to string
str5 = str(False)
str6 = str("Hello")
str7 = str(200)
str8 = str(10.6)
print(type(str5),type(str6),type(str7),type(str8)) #output: <class 'str'> <class 'str'> <class 'str'> <class 'str'>
