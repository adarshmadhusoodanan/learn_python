# Miscellaneous Functions: defining a new variable which takes the address of a function 
#                          and accessing function through that variable.

def greet():
    print("Hello")
greeting=greet
print(greeting)
greet()
greeting()

# output
        #<function greet at 0x00000182F5CECA40>
        # Hello
        # Hello

def outer_function():   
    print("i am outer function")
    def inner_function():
        print("i am inner function")
    return inner_function
inner_func = outer_function()   # here inner_func is a variable which holds the reference of inner_function
print(inner_func)
inner_func()                    # calling inner_function using inner_func variable
# output
        # i am outer function   
        # <function outer_function.<locals>.inner_function at 0x0000026B7719D260>
        # i am inner function