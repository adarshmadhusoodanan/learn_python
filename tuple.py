            # defining tuple

# t=,                   SyntaxError: invalid syntax
# t = (,)               SyntaxError: invalid syntax
# t = (10)              10 <class 'int'>

# t = 10,               (10,) <class 'tuple'>                define without paranthesis
# t = (10,)             (10,) <class 'tuple'>                define
# t=()                  () <class 'tuple'>                   empty tuple
# t=(1,3,5,(2,4,6))     (1, 3, 5, (2, 4, 6)) <class 'tuple'> nested tuple



            # property of tuples

# t = (10,10)           (10, 10) <class 'tuple'>            have duplicate elements
# t = (1,2,3,4,5)       (1, 2, 3, 4, 5) <class 'tuple'>     ordered collection
# t = ('het', 1, 1.0)   ('het', 1, 1.0) <class 'tuple'>     hetero or homo

# t = 1,2,3
# t[0] = 3        TypeError: 'tuple' object does not support item assignment     immutable
# print(t,type(t))


            # tuple supports indexing

# t = 1,2,3,4
# print(t[1])     op: 2
# t=(1,3,5,(2,4,6)) 
# print(t[3])     op: (2, 4, 6)
# print(t[3][1])  op: 4

            # tuple supports slicing

# t =(1,2,3,4)
# print(t[1:])      op: (2, 3, 4)
# print(t[-1::-1])  op: (4, 3, 2, 1)
# print(t[1::2])    op: (2, 4)
# print(t[:3])      op: (1, 2, 3)

            # tuple built-in functions
# t=(1,2,3,1,4,1,5)
# print(t.count(1))     op:3 

# print(t.index(1))     op:0
# print(t.index(1,4))   op:5
# print(t.index(1,1,4)) op:3
