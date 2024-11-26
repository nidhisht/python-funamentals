def greeting():
    print("--------------------------")
    print("welcome to the function!!")
    print("--------------------------")

# Function accepting parameters
def add(num1, num2):
    print(num1 + num2)

# Function accepting default parameter values
def sub(num1=10, num2=5):
    print(num1-num2)

greeting();
add(10, 20);
sub();