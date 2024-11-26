# Read 4th index from the list
list1 = [5,6,7,8,9,10,11,12,13]
print(list1[4]) #output: 9

# List within another list
list2 =[[1,2,3], [4,5,6],[7,6,9]]
print(list2[1][1])  #output: 5


list3 = ["OpenAI", "Meta AI", "Bard", "Gemini"]
print(list3[1][1])  #output: e

#Negative index
print(list1[-1])    #output: 13
print(list1[-2])    #output: 12


# Mixed list
list4 = ["Sachin Tendulkar", 420, 55.5]
print(list4[0][1])  #output: a
print(list4[1])     #output: 420