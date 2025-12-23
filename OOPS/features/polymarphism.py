# Polymarphism : A function or operator showing different behaviour during its life cycle 
#       based on types of operants or arguments is called polymarphsim 

# ex: Polymorphism in operators:
#       + -> number - addition 
#         -> list,string - concatenation 

# Types :
#      - compile time/static polymorphism 
#      - Run time/dynamic polymorphism 

# ------------------------------------------------------------------------------------------

# Compile Time Polymorphism :
#       Method Overloading :
# Defining a method more than one time within the same class with different 
# number of arguments or different type of argument is called method overloading 

# Method overloading is not supported in python 

class One:
    def meth(self):
        print("I am meth")
    def meth(self,a):
        print(a)
    def meth(self,a,b):
        print(a,b)
    def meth(self,a,b):
        print(a+b)
obj=One()
# obj.meth()
#     obj.meth()
#     ~~~~~~~~^^
# TypeError: One.meth() missing 2 required positional arguments: 'a' and 'b'

# obj.meth(1)
#     obj.meth(1)
#     ~~~~~~~~^^^
# TypeError: One.meth() missing 1 required positional argument: 'b'

# obj.meth(1,2)
# 3

class Two:
    def meth(self):
        print("I am meth")
    def meth(self,a,b):
        print(a)
    def meth(self,a):
        print(a)
obj1=Two()

# obj1.meth(1,2)
#     obj1.meth(1,2)
#     ~~~~~~~~^^^^^
# TypeError: One.meth() takes 2 positional arguments but 3 were given

# obj1.meth()
#     obj1.meth()
#     ~~~~~~~~~^^
# TypeError: Two.meth() missing 1 required positional argument: 'a'

obj1.meth(1)
# 1

#--------------------------------------------------------------------- 

# Run time Polymorphism :
# Method Overiding :
# Changing the implementation of parent class into child class 

class One():
    def meth(self):
        print("I am meth one")
class Two(One):
    def meth(self):
        print("I am meth two")
obj=Two()
obj.meth()
# I am meth two