            # object oriented programming in python

# class is blueprint / design / structure of real world object
# -----
# object is an instance of class
# ------

# attributes are the members of class
# ----------
    # -> 2 types
    #     - variables
                # + class variable
                # + instance variable
    #     - methods
                # + class method
                # + static method
                # + instance method
                #     = normal instance method
                #     = magic / dunder instance method


            # implementation oops

# for defining a class 
    # class Class_name:

class Student:
    college_name= "JSS"                                 # class variable
    
    def __init__(self, name, roll_no, branch):          # constructor (__init__()) for creating instance variable
                                                    
        self.name = name                                # here the parameter name, roll_no, branch are local variables
        self.roll_no = roll_no                          # self.name, self.roll_no, self.branch are instance variables
        self.branch = branch

    def student_info(self):                             # instance method 

        print(f" College Name: {self.college_name}")    # we can access class variable by using self [self.college_name]. and this is universal variable don't need to pass it in while creating object.
        print(f" Student name: {self.name}")            # we can access instance variable using self [self.name].
        print(f" Student roll number: {self.roll_no}")
        print(f" Branch: {self.branch}")
        print("*************************")


student1 = Student("Keerthana G", 1, "CSE")
student2 = Student("Adarsh M", 2, "CSE")

student1.student_info()
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

