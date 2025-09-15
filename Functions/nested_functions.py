# Nested functions: Functions defined inside another function.

def outer_function():
    print("i am outer function")
    def inner_function():
        print("i am inner function")
    inner_function()    
outer_function()

# output
    # i am outer function   
    # i am inner function
# inner_function()           NameError: name 'inner_function' is not defined

# inner_function is not accessible outside the outer_function

# to access inner_function outside the outer_function we can return the inner_function from outer_function

def outer_function():
    print("i am outer function")
    def inner_function():
        print("i am inner function")
    return inner_function
inner_func = outer_function()   # here inner_func is a variable which holds the reference of inner_function
inner_func()                    # calling inner_function using inner_func variable

# output
    # i am outer function   
    # i am inner function

# we can also return the inner_function and call it in a single line

def outer_function():   
    print("i am outer function")
    def inner_function():
        print("i am inner function")
    return inner_function

# calling inner_function using outer_function
outer_function()()              # here first outer_function() is called which returns the inner_function and then inner_function() is called        
# output
    # i am outer function   
    # i am inner function
