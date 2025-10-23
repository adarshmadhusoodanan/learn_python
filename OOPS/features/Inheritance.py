# Inheritance

# it is the process where one class acquires the properties (methods and fields) of another class.

# a class can inherit the properties of another class

# class A -> parent class / base class / super class
#   ^
#   |
# class B -> child class / derived class / sub class

# a class whose properties are acquired by another class is called super class or parent class or base class

# a class which acquires the properties of another class is called sub class or child class or derived class

# Types of Inheritance
# 1. Single Inheritance
# 2. Multi Level Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# 1. Single Inheritance

# it is process where one class inherits or acquires properties from another class

# it will be having only one parent class and one child class
# child class object can access the properties of parent class except private members

# examlpe 1: without using constructor
class A:
    a=10
    def displayA(self):
        print("in A class")

class B(A):   # class B is inheriting the properties of class A
    b=20
    def displayB(self):
        print("in B class")

obj = B()   # creating the object of class B
print(obj.a)   # accessing the variable of class A using object of class B

obj.displayA()   # accessing the method of class A using object of class B
obj.displayB()   # accessing the method of class B using object of class B
print(obj.b)   # accessing the variable of class B using object of class B
# here class B is child class and class A is parent class

# we can also create a new python file and import the parent class and create the child class in that file

# example 2: using constructor

print("********** example 2: using constructor **********")
class A:
    def __init__(self):
        self.a=10
    def displayA(self):
        print("in A class")
        print("a =", self.a)

class B(A):   # class B is inheriting the properties of class A
    def __init__(self):
        self.b=20
        A.__init__(self)   # calling the constructor of class A inside the constructor of class B
    def displayB(self):
        print("in B class")
        print("b =", self.b)
        print("a =", self.a)   # this will give error because constructor of class A is not called
        self.displayA()   # calling the method of class A inside the method of class B

obj = B()   # creating the object of class B
obj.displayB()   # accessing the method of class B using object of class B

#-------------------------------------------------------------------------------------

# constructor chaining

# calling the parent class constructor from child class constructor is called constructor chaining

# constructor chaining is achieved to avoid error while accessing the parent class variables and methods
# if is not achieved parent class instance variables cannot be passed to child class instance variables

# constuctor chaining can be achieved in two ways
# 1. by using class name
# 2. by using super() function

# 1. by using class name
print("********** constructor chaining by using class name **********")
class A:
    def __init__(self):
        self.a=10
        print("in A class constructor")
    def displayA(self):
        print("in A class")
        print("a =", self.a)
class B(A):   # class B is inheriting the properties of class A
    def __init__(self):
        self.b=20
        A.__init__(self)   # calling the constructor of class A inside the constructor of class B
        print("in B class constructor")
    def displayB(self):
        print("in B class")
        print("b =", self.b)
        print("a =", self.a)   # this will give error because constructor of class A is not called
        self.displayA()   # calling the method of class A inside the method of class B

obj = B()   # creating the object of class B
obj.displayB()   # accessing the method of class B using object of class B

# 2. by using super() function
print("********** constructor chaining by using super() function **********")
class A:
    def __init__(self):
        self.a=10
        print("in A class constructor")

    def displayA(self):
        print("in A class")
        print("a =", self.a)
class B(A):   # class B is inheriting the properties of class A
    def __init__(self):
        self.b=20
        super().__init__()   # calling the constructor of class A inside the constructor of class B using super() function
        print("in B class constructor")
    def displayB(self):
        print("in B class")
        print("b =", self.b)
        print("a =", self.a)   # this will give error because constructor of class A is not called
        self.displayA()   # calling the method of class A inside the method of class B

obj = B()   # creating the object of class B
obj.displayB()   # accessing the method of class B using object of class B
