# User defined functions: Functions created by the user to perform specific tasks.
def adarsh():
    print("Hello, I am Adarsh")
adarsh()
# Hello, I am Adarsh

def keerthana():
    return "Hello, I am Keerthana"
print(keerthana())
# Hello, I am Keerthana
print(keerthana)
# <function keerthana at 0x00000227282DE2A0>

# Function with parameters and return type
def add(a, b):
    return a + b
print(add(5, 10))  # op: 15

# Function without parameters and with return type
def add():
    a=int(input("Enter a: "))   
    b=int(input("Enter b: "))
    return a + b
print(add())  # op: Enter a: 5 Enter b: 10 15

# Function with parameters and without return type
def add(a, b):
    print("The sum is:", a + b) 
add(5, 10)  # op: The sum is: 15

# function without parameters and without return type
def add():
    a=int(input("Enter a: "))   
    b=int(input("Enter b: "))
    print("The sum is:", a + b)
add()  # op: Enter a: 5 Enter b: 10 The sum is: 15
    