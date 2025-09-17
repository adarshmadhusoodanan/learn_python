# Python Tuples Datatype
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple are written with round brackets ()
#------------------------------------------------------------------------------------------------------------------------------------------------

# defining tuple

# t=,                                           SyntaxError: invalid syntax
# t = (,)                                       SyntaxError: invalid syntax
# t = (10)                                      10 <class 'int'>

# t = 10,                                       (10,) <class 'tuple'>                define without paranthesis
# t = (10,)                                     (10,) <class 'tuple'>                define
# t = ()                                        () <class 'tuple'>                   empty tuple
# t = (1,3,5,(2,4,6))                           (1, 3, 5, (2, 4, 6)) <class 'tuple'> nested tuple
# print(len(t))                                 op: 4

# t = (1,2,3,[1,2,3])
# print(type(t[3]))                             <class 'list'>
# print(t,type(t))                              (1, 2, 3, [1, 2, 3]) <class 'tuple'>

# t =(1,2,3,{1,2,3})
# print(type(t[3]))                             <class 'set'>
# print(t,type(t))                              (1, 2, 3, {1, 2, 3}) <class 'tuple'>

# t = (1,2,3,{'a':"apple",'b':"bat"})
# print(type(t[3]))                             <class 'dict'>
# print(t,type(t))                              (1, 2, 3, {'a': 'apple', 'b': 'bat'}) <class 'tuple'>

# t1=(1,2,3)
# t2=(5,6,7,8)
# print(t1+t2)                                  op: (1, 2, 3, 5, 6, 7, 8)           <class 'tuple'> concatenation of tuple
# print(t1*3)                                   op: (1, 2, 3, 1, 2, 3, 1, 2, 3)     <class 'tuple'> repetition of tuple


# Note: 
#       tuple comprehension is not there because it will be considered as generator expression

# t = (x for x in range(10))
# print(t)                  #op: <generator object <genexpr> at 0x000001E2B0C8B040>
# print(type(t))            #op: <class 'generator'>
#------------------------------------------------------------------------------------------------------------------------------------------------

# property of tuples

            # tuple can be homogenous or heterogenous
             
# t = (1,2,3,4,5)            (1, 2, 3, 4, 5) <class 'tuple'>     homogenous collection
# t = ('het', 1, 1.0)        ('het', 1, 1.0) <class 'tuple'>     heterogenous collection

            # tuple can have duplicate elements

# t = (10,10)                (10, 10) <class 'tuple'>  

            # tuple are ordered collection 
                     
# t = (1,2,3,4,5)            (1, 2, 3, 4, 5) <class 'tuple'>     

            # tuple are immutable

# t = 1,2,3
# t[0] = 3                  TypeError: 'tuple' object does not support item assignment     

            # tuple supports indexing

# t = 1,2,3,4
# print(t[1])               op: 2
# t=(1,3,5,(2,4,6)) 
# print(t[3])               op: (2, 4, 6)
# print(t[3][1])            op: 4

            # tuple supports slicing

# t =(1,2,3,4)
# print(t[1:])              op: (2, 3, 4)
# print(t[-1::-1])          op: (4, 3, 2, 1)
# print(t[1::2])            op: (2, 4)
# print(t[:3])              op: (1, 2, 3)
# print(t[::-1])            op: (4, 3, 2, 1)

#------------------------------------------------------------------------------------------------------------------------------------------------

# tuple built-in functions

            # tuple.count(value) -> int

# t = (1,2,3,1,4,1,5)
# print(t.count(1))         op:3 

            # tuple.index(value,start:0,end:size of tuple) -> int

# t = (1,2,3,1,4,1,5)
# print(t.index(1))         op:0
# print(t.index(1,4))       op:5
# print(t.index(1,1,4))     op:3


