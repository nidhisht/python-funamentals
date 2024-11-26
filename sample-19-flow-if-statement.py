def getPrice(fruit):
    if(fruit=="apple"):
        return 120
    elif (fruit=="orange"):
        return 100
    elif (fruit=="grape"):
        return 110
    else:
        return 0
    
print(getPrice("orange"))
print(getPrice("strawberry"))