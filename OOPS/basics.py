# object oriented programming in python

# s = 'OOPS - Object Oriented Programming System'
# print(s)            #OOPS - Object Oriented Programming System
# print(type(s))      #<class 'str'>
# print(len(s))       #41

# a = 10
# print(a)            #10
# print(type(a))      #<class 'int'>
# print(len(a))       #TypeError: object of type 'int' has no len()

# here in class int we can't use len() function because it is not defined in int class

# in python everything is object

# in python we have some predefined classes like str, int, float, list, tuple, dict, set etc
# we can check the members of class by using dir() function

# print(dir(int))     # members of int class

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
#  '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
#  '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', 
#  '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
#  '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
#  '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
#  '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
#    '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
#    '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
#    'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

print(dir(str))     # members of str class

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
# 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']

# like above we can check the members of any class for example list, tuple, dict, set etc

#----------------------------------

s = 'OOPS - Object Oriented Programming System'
print(len(s))       #41
# here len() function is defined in str class that's why we can use len() function with

print(s.__len__())   #41  
# this is called dunder method (double underscore method) or magic method 

print(s.upper())    #OOPS - OBJECT ORIENTED PROGRAMMING SYSTEM
# here upper() function is defined in str class that's why we can use upper() function with string object

#------------------------------------------------
# why we need OOPS
# basically Oops is required to create our own data types

# for example we have predefined class str to represent string data type
# similarly we have predefined class int to represent integer data type
# but if we want to represent student data type then we have to create our own class

# features of OOPS
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

#------------------------------------------------
