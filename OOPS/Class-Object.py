            # object oriented programming in python

# class is blueprint / design / structure of real world object
# -----
# object is an instance of class
# ------

# attributes are the members of class
# ----------
    # -> 2 types
    #     - variables or states (variables which are declared inside class)
                # + class variable
                # + instance variable
    #     - methods or behaviors (function which are defined inside class)
                # + class method
                # + static method
                # + instance method
                #     = normal instance method
                #     = magic / dunder instance method

#-----------------------------------------------------------------

# variables

# 1. class variable : 

# - universal variable for all objects of class
# - it is also called static variable
# - it will be created at the time of class loading
# - it is defined inside class but outside any method
# - it is shared by all objects of class
# - it can be accessed by using class name or by using self keyword inside instance method
# - it is used to store common property of all objects of class

# 2. instance variable : 

# - unique variable for each object of class
# - it is defined inside constructor by using self keyword
# - it is created at the time of object creation
# - it can be accessed by using self keyword inside instance method
# - it is used to store unique property of each object of class


# 3. local variable : 

# - variable which are defined inside method / function
# - it is created at the time of method / function call
# - it can be accessed only inside the method / function
# - it is destroyed automatically when method / function call is completed

# ----------------------------------
# methods

# 1. class method : 

# - method which is defined by using @classmethod decorator and it takes cls as first parameter
# - it can access only class variable
# - it is used to access class variable and to create factory methods

#example:
class Example:
    class_variable = "I am a class variable"

    @classmethod    # decorator to define class method
    def class_method(cls):
        return cls.class_variable
    
print(Example.class_method())   # Output: I am a class variable

# in real time scenario class method is used to create factory methods( methods which return object of class)

#-------------------------------------------------

# 2. static method : 

# - method which is defined by using @staticmethod decorator and it doesn't take self or cls as first parameter
# - it can't access class variable and instance variable
# - it is used to create utility methods

class Math:
    @staticmethod    # decorator to define static method
    def add(a, b):
        return a + b
    
print(Math.add(5, 10))   # Output: 15

# in real time scenario static method is used to create utility methods like math module, random module etc

#-----------------------------------------------------------------

# 3. instance method : 

# - method which is defined without any decorator and it takes self as first parameter
# - it can access class variable and instance variable
# - it is used to access instance variable and to perform operations on instance variable
#     -> 2 types
#     - normal instance method
#       - method which is defined by using self as first parameter

#     - magic / dunder instance method
#         - method which is defined by using double underscore before and after the method name

#-----------------------------------------------------------------

# constructor

# - constructor is a special type of method which is used to initialize the instance variables of class
# - constructor is defined by using __init__() method
# - constructor is called automatically when we create an object of class
# - constructor is used to allocate memory for the object
# - constructor is used to initialize the instance variables of class

#-----------------------------------------------------------------

# self

# - self is a special keyword which is used to represent the current object of class
# - self is used to access the instance variables and instance methods of class
# - self is used to differentiate between instance variable and local variable
# - self is used to call the instance methods of class
# - self is not a keyword, it is just a convention, we can use any name instead of self but it is recommended to use self


#-----------------------------------------------------------------

            # implementation oops

# for defining a class 
    # class Class_name:

class Student:
    college_name= "JSS"                                 # class variable : universal variable for all objects of class Student
    
    def __init__(self, name, roll_no, branch):          # constructor __init__() for creating instance variable 
                                                    
        self.name = name                                # here the parameter name, roll_no, branch are local variables
        self.roll_no = roll_no                          # self.name, self.roll_no, self.branch are instance variables
        self.branch = branch

    def student_info(self):                             # instance method : normal instance method

        print(f" College Name: {self.college_name}")    # we can access class variable by using self [self.college_name]. and this is universal variable don't need to pass it in while creating object.
        print(f" Student name: {self.name}")            # we can access instance variable using self [self.name].
        print(f" Student roll number: {self.roll_no}")
        print(f" Branch: {self.branch}")
        print("*************************")


student1 = Student("Keerthana G", 1, "CSE")       # creating object of class Student
student2 = Student("Adarsh M", 2, "CSE")

student1.student_info()                         # calling instance method using object
student2.student_info()

# output
        #  College Name: JSS
        #  Student name: Keerthana G
        #  Student roll number: 1
        #  Branch: CSE
        # *************************
        #  College Name: JSS
        #  Student name: Adarsh M
        #  Student roll number: 2
        #  Branch: CSE
        # *************************

