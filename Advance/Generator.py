def fun():
    return 1
    return 2
    return 3
print(fun())        # 1
print(fun())        # 1
print(fun())        # 1

# - fun() is a normal fun user defined. whenever fun() is called it returns1 and control 
#   will never go the return 2 or return 3 as first return terminates the function.
# - In order to create generator first we should define a generator function 
# - A function which yields value instead of returning is called a generator function 
# - When we call a generator function it returns an object.This obj is generator.
# - All generator are iterator as the directory of generator contains __iter__() as well 
#   as __next__() methods
# - Generator are more memory efficient than iterator's as it doesnt stores the values 
#   instead it yields the value 
# - In order to create an iterator there must be an iterable where as to create generator 
#   iterable is not required 

def gen_fun():
    yield 1
    yield 2
    yield 3
gen1=gen_fun()
print(dir(gen1))
print(type(gen1))          # op: <class 'generator'>
print(next(gen1))          # op: 1
print(next(gen1))          # op: 2
print(next(gen1))          # op: 3

# print(next(gen1))
#     print(next(gen1))
#           ^^^^^^^^^^
# StopIteration