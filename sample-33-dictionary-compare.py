# Dictionaries are unordered.  
# Here’s an example of comparing two dictionaries: 
# both must contain the same key-value pairs, but the order of those pairs doesn’t matter.

first = {0:2.1, 1:2.2, 2:2.3, 3:2.4}
second = {1:2.2, 0:2.1, 3:2.4, 2:2.3}

print(first==second)    #output: True