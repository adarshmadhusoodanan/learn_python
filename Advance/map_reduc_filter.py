# def filter_five(n):
#     if n%5==0:
#         return True
#     return False

# l=[10,3,5,7,40,45,30]
# res=[]
# for i in l:
#     if filter_five(i):
#         res.append(i)
# print(res)

# # Lambda / Ananoymous function : lambda is used to create small, anonymous (nameless) functions in a single line
# #   Syntax ; lambda Arguments : Expression 

# add= lambda a,b:a+b
# print(add)
# # <function <lambda> at 0x000002912ACEE2A0>
# print(type(add))
# # <class 'function'>
# print(add(10,20))
# # 30

# cube = lambda a: a**3
# print(cube(3))
# # 27

# # Filter(): filter() used to select items from an iterable based on a condition
# #   filter(function,iterable) --> filter_object 

# l=[10,3,5,7,40,45,30]
# res =list(filter(lambda n: n%5==0,l))
# print(res)
# # [10, 5, 40, 45, 30]

# movies=['Kgf','Kantara','kgf2','devil','gaja','Banglore Days']
# ch=input('Enter a starting letter movie name ').lower()
# movies=list(filter(lambda n:n.lower().startswith(ch),movies ))
# print(movies)
# # Enter a starting letter movie name kgf
# # ['Kgf', 'Kantara', 'kgf2']

# chr=input('Enter a movie name ').lower()
# movies= list(filter(lambda n:n.lower()==chr, movies))
# print(movies)
# # Enter a movie name Gaja
# # ['gaja']

# # Map : map() is used to apply a function to every item in an iterable (list, tuple, etc.)
# #   It returns a map object (an iterator), which you can convert into a list or tuple.
# #   map(function ,*iterable) --> map object

# l1=[1,2,3,4,5]
# res=list(map(lambda n:n**2,l1))
# print(res)
# # [1, 4, 9, 16, 25]

# l1=[1,2,3,4]
# l2=[10,20,30,40]
# res=list(map(lambda x,y:x+y ,l1,l2))
# print(res)
# # [11, 22, 33, 44]

# l1=[100,200,0,1,55,45,3,0,1,0]
# res=list(map(bool,l1))
# print(res)
# # [True, True, False, True, True, True, True, False, True, False]

# Reduce(): Reduce() takes a list and keeps reducing it until only one value is left

# from functools import reduce 
# l1=[1,2,3,4,5]
# res=reduce(lambda x,y:x+y , l1)
# print(res)
# # 15 