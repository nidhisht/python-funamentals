# Sets are similar to list. It differ from list in 2 ways.
# 1) It can not have duplicate values in them.
# 2) Items are unordered

# Unlike list or tuple, values from the sets cannot be accessed by index. 
# Use for loop for accessing the item from set

# use paranthesis to create tuple
hours = {1,2,3,4,5,6,7,8,9,10,11,12}  #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}  #output: {'Thursday', 'Tuesday', 'Sunday', 'Wednesday', 'Saturday', 'Friday', 'Monday'}

print(hours)
print(days)



# use tuple function
list = set([3.14, 2.25, 10])  #output: {10, 2.25, 3.14}
hello = set("hello")          #output: {'o', 'e', 'h', 'l'}

print(list)
print(hello)

# duplicate values are ignored
days = {"Monday", "Monday", "Monday", "Monday", "Monday", "Saturday", "Sunday"}  
print(days)                 #output: {'Monday', 'Sunday', 'Saturday'}