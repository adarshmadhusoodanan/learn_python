            # defining tuple

# t=,                   SyntaxError: invalid syntax
# t = (,)               SyntaxError: invalid syntax
# t = (10)              10 <class 'int'>

# t = 10,               (10,) <class 'tuple'>               define without paranthesis
# t = (10,)             (10,) <class 'tuple'>               define

            # property of tuples

# t = (10,10)           (10, 10) <class 'tuple'>            have duplicate elements
# t = (1,2,3,4,5)       (1, 2, 3, 4, 5) <class 'tuple'>     ordered collection
# t = ('het', 1, 1.0)   ('het', 1, 1.0) <class 'tuple'>     hetero or homo

# t = 1,2,3
# t[0] = 3        TypeError: 'tuple' object does not support item assignment     immutable
# print(t,type(t))


            # tuple supports indexing

# t = 1,2,3,4
# print(t[1])   op: 2

            # tuple supports slicing

# t =(1,2,3,4)
# print(t[1:])      op: (2, 3, 4)
# print(t[-1::-1])  op: (4, 3, 2, 1)
# print(t[1::2])    op: (2, 4)
# print(t[:3])      op: (1, 2, 3)


