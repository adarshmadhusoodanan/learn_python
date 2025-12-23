# Abstraction :
#   Hiding the implementation and providing functionality is called abstration 
#   ex: Built-in-list, print() , input()

# Steps to achieve abstraction
# 1. import ABC(Abstract Base class) and Abstract method(decorator) from abc
#       (absolut base class)
# 2. Create an abstract class 
#    An abstract class is a class having Abstract method inherting ABC
#    Abstract Method : with no implementation and decorated with abstract 
#    method decorator defined in abstract class is called abstract method 
# 3. Define a class which is inheriting abstract class having implementation 
# of abstract method

from abc import ABC , abstractmethod
# Creating an abstract class one 
class One(ABC):
    @abstractmethod
    def meth(self):
        pass