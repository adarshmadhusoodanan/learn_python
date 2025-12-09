# Functions: Block of code written for reuseability and modularity.
#            Functions are defined using the 'def' keyword followed by the function name and parentheses.
#            Syntax: def function_name(parameters):

# Types of functions:
# 1. Built-in functions: 
# 2. User-defined functions: 
#       - Without parameters and without return type
#       - With parameters and without return type
#       - Without parameters and with return type
#       - With parameters and with return type
#       - Recursive functions:
# 3. Miscellaneous functions: 
# 4. Anonymous functions (lambda functions):

def greet():
    print("Hello, welcome to the world of Python functions!")
greet()
# Hello, welcome to the world of Python functions!

def add(a, b):
    result = a + b
    print("The sum is:", result)
add(5, 10)
# The sum is: 15
add(20, 30)
# The sum is: 50

# we can also pass the function as an argument to another function  
def greet():
    return "Hello"
def call_func(func):
    print(func())
call_func(greet)

# output
        # Hello 
        
# Built-in functions examples:

a,b,c,d=10,20,30,40
print(max(a,b,c,d))                 # op: 40

print(min(a,b,c,d))                 # op: 10

print(sum(a,b))                     # op: TypeError: 'int' object is not iterable

print(sum(a,b,c,d))                 # op: sum() takes at most 2 arguments (4 given)

print(round(3.6))                   # op: 4

print(pow(2,3))                     # op: 8    

print(pow(2,3,3))                   # op: 2  -> (2**3)%3

print(bin(10))                      # op: 0b1010

print(oct(10))                      # op: 0o12  

print(hex(10))                      # op: 0xa

print(abs(-7))                      # op: 7

l1=[1,2,3]
print(sum(l1))                      # op: 6