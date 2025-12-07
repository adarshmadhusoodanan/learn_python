# Non Iterable: An object from which values can not be fetched are called non iterable
# Iterable: An object from which values can be fetched one by one is called iterable 

a=100
# for i in a:
#     print(i)
#     for i in a:
#              ^
# TypeError: 'int' object is not iterable

l1=[10,20,30,40]
for i in l1:
    print(i)
# op:
# 10
# 20
# 30
# 40

# a is not iterable object. Hence iteration through a is not possible 
# if we try python will rise Type Error 

# l1 is a iterable object iterating through l1 is possible

# If we check the directory of a __iter__ magic method is not present.
# Hence python consider it as a non iterable object 

# If we check the directory of l1 __iter__ magic method is present.
# Hence python consider l1 as a iterable object 

print(l1.__len__())
# 4
ite=l1.__iter__()
it1=iter(l1)
print(it1.__next__())
# 10
print(next(it1))
# 20