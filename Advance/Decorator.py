# Decorator:

# The process of extending the functionality of a function without 
#   changing the implementation is called decoration

# To perform decoration decorator is required 
# A special function used to decorate other functions is called decorator 

# A callable ,receiving callable and returning callable is called decorator.

def my_decorator(f):
    def inner_fun():
        print('I am superman')
        f()
        print('Superman saves world')
    return inner_fun
def f():
    print('I am iron man')
print('Start')
f()
print('end')
# Start
# I am iron man
# end

def my_decorator(f):
    def inner_fun():
        print('I am superman')
        f()
        print('Superman saves world')
    return inner_fun
@my_decorator
def f():
    print('I am iron man')
print('Start')
f()
print('end')
# Start
# I am superman
# I am iron man
# Superman saves world
# end

# When we call @my_decorator def f(): now the original function is replaced with another function 
# This wrapper has extra code before and after your function.
# So when we call f(), we are actually calling the wrapper, not the original f()

def my_decorator(f):
    def inner_fun():
        print('I am superman')
        f()
        print('Superman saves world')
    return inner_fun
def f():
    print('I am iron man')
print('Start')
r=my_decorator(f)
r()
print('end')
# Start
# I am superman
# I am iron man
# Superman saves world
# end

# Ex:
def verifydecorator(f):
    def zerodivision(a,b):
        if b==0:
            return 'Not division by zero'
        else:
            return f(a,b)
    return zerodivision
@verifydecorator
def divide(a,b):
    return(a/b)
print(divide(10,5))
# 2.0print(divide(10,0))
# Not division by zero