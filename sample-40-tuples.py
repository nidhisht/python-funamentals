# Tuples are similar to list. Tuples are immutable datatypes. Meaning, once assigned cannot be changed.
# Advantage of tuple is it takes less memory compared to list. And hence faster.
# There are 2 ways to create tuple.
# 1) use paranthesis - ()
# 2) use tuple function

# use paranthesis to create tuple
hours = (1,2,3,4,5,6,7,8,9,10,11,12)  #output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  #output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(hours)
print(days)



# use tuple function
list = tuple([3.14, 2.25, 10])  #output: (3.14, 2.25, 10)
hello = tuple("hello")          #output: ('h', 'e', 'l', 'l', 'o')

print(list)
print(hello)