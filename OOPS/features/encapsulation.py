# Encapsulation
# -----------------

# binding of data members (attributes) and member functions (methods) together in a single unit (class)
# and restricting the access to some of the object's components is called encapsulation

# it is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit
# in encapsulation the variables of a class will be hidden from other class and can be accessed only through the methods of their current class
# data hiding is one of the main features of encapsulation

#----------------------------------------------------------------------------------------------------------

# access specifiers

# attributes of a class can be accessed
# 1. within the class
# 2. outside the class within the module
# 3. outside the module within the package
# 4. outside the package in another module within the main package

# these can be controlled using access specifiers
# 1. public (no underscore)
# 2. protected (single underscore)
# 3. private (double underscore)
#-------------------------------------------

# 1. public

# attributes and methods are accessible from anywhere

# public access specifier can be accessed from
# 1. within the class
# 2. outside the class within the module
# 3. outside the module within the package
# 4. outside the package in another module within the main package

# example

class Car:
    def __init__(self, name, model):
        self.name = name      # public variable
        self.model = model    # public variable

    def info(self):          # public method
        print("Car name: {}, model: {}".format(self.name, self.model))
        # public method can be accessed from outside the class
c = Car("BMW", 2020)
print(c.name)      # accessing public variable
print(c.model)     # accessing public variable
c.info()           # accessing public method
# Car name: BMW, model: 2020

#----------------------------------------------------------------------------------------------------------
# 2. protected

# attributes and methods are accessible within the class and its subclasses
# single underscore is used to declare protected attributes and methods

# protected access specifier can be accessed from
# 1. within the class
# 2. outside the class within the module
# 3. outside the module within the package
# 4. outside the package in another module within the main package through inheritance

# example
class Person:
    def __init__(self, name, age):
        self._name = name    # protected variable
        self._age = age      # protected variable

    def info(self):          # protected method
        print("Name: {}, Age: {}".format(self._name, self._age))
        # protected method can be accessed from outside the class through inheritance

class Employee(Person):     # inheritance
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id  # public variable

    def emp_info(self):      # public method
        print("Employee ID: {}".format(self.emp_id))
        self.info()          # accessing protected method from parent class

e = Employee("John", 30, "E123")
print(e.emp_id)      # accessing public variable
e.emp_info()        # accessing public method
# Employee ID: E123
# Name: John, Age: 30

print(e._name)  # accessing protected variable (not recommended)
print(e._age)   # accessing protected variable (not recommended)

#----------------------------------------------------------------------------------------------------------

# 3. private

# attributes and methods are accessible only within the class
# double underscore is used to declare private attributes and methods

# private access specifier can be accessed from
# 1. within the class

# twoways to access private variables and methods from outside the class
# 1. using public methods (getter and setter methods)
# 2. using name mangling (not recommended)


# example of getter and setter methods
class Student:
    def __init__(self, name, age):
        self.__name = name    # private variable
        self.__age = age      # private variable

    def get_name(self):     # getter method
        return self.__name   # accessing private variable through public method

    def set_name(self, name): # setter method
        self.__name = name   # setting private variable through public method

    def get_age(self):      # getter method
        return self.__age    # accessing private variable through public method

    def set_age(self, age):  # setter method
        if age > 0:
            self.__age = age  # setting private variable through public method
        else:
            print("Invalid age")
    def info(self):          # public method
        print("Name: {}, Age: {}".format(self.__name, self.__age))
        # public method can be accessed from outside the class

s = Student("Alice", 20)
print(s.get_name())      # accessing private variable through public method
print(s.get_age())       # accessing private variable through public method
s.info()                 # accessing public method

# example 2

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance                # private variable

    def deposit(self, amount):                 # public method
        if amount > 0:
            self.__balance += amount
            print("Deposited: {}".format(amount))
        else:
            print("Invalid amount")

    def withdraw(self, amount):                # public method
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew: {}".format(amount))
        else:
            print("Invalid amount or insufficient balance")

    def get_balance(self):    #getter method                 # public method
        return self.__balance                  # accessing private variable through public method

    def get_account_number(self):              # public method
        return self.__account_number           # accessing private variable through public method
    
account = BankAccount("123456789", 1000)
account.deposit(500)                          # accessing public method
account.withdraw(200)                         # accessing public method
print("Balance: {}".format(account.get_balance()))  # accessing public method
print("Account Number: {}".format(account.get_account_number()))  # accessing public method
# Deposited: 500
# Withdrew: 200
# Balance: 1300
# Account Number: 123456789
# print(account.__balance)  # accessing private variable (will raise AttributeError)
# print(account.__account_number)  # accessing private variable (will raise AttributeError)

# getter and setter methods are used to access private variables from outside the class
# getter method is used to get the value of private variable
# setter method is used to set the value of private variable


#----------------------------------------------------------------------------------------------------------


# BEAN class

# a class which contains attributes with getter and setter methods is called BEAN class
# BEAN class is used to encapsulate the data and provide methods to access and modify the data


# rules for BEAN class

# 1. all instance variables should be private
# 2. all instance variables should have getter and setter methods
# 3. all getter and setter methods should be public


# this can be achieved by several ways

# 1. by normal methods (getter and setter methods)
# 2. using property() function

# 1. by normal methods (getter and setter methods)
# example

class BEAN:
    def __init__(self, a):
        self.__a = a    # private variable
    def get_a(self):     # getter method
        return self.__a   # accessing private variable through public method
    
    def set_a(self, a): # setter method
        self.__a = a   # setting private variable through public method

b = BEAN(10)
print(b.get_a())      # accessing private variable through public method
#10
b.set_a(20)          # setting private variable through public method
print(b.get_a())      # accessing private variable through public method
#20
    

# 2. using property() function

# property() function is used to wrap the getter and setter methods
# it creates and returns a property object
# example

class BEAN2:
    def __init__(self, a, b):
        self.__a = a    # private variable

    def get_a(self):     # getter method
        return self.__a   # accessing private variable through public method

    def set_a(self, a): # setter method
        self.__a = a   # setting private variable through public method

    def del_a(self):  # deleter method
        del self.__a  # deleting private variable through public method

    def get_b(self):     # getter method
        return self.__b   # accessing private variable through public method
    
    def set_b(self, b): # setter method
        self.__b = b   # setting private variable through public method

    def del_b(self):  # deleter method
        del self.__b  # deleting private variable through public method

    a = property(get_a, set_a)  # creating property object              
    b = property(get_b, set_b)  # creating property object
    # property object is created using getter and setter methods
    # property object can be accessed like a variable

bean = BEAN2(10, 20)
print(bean.a)      # accessing private variable through public method
#10
bean.a = 30       # setting private variable through public method
print(bean.a)      # accessing private variable through public method
#30
print(bean.b)      # accessing private variable through public method
#20
bean.b = 40       # setting private variable through public method
print(bean.b)      # accessing private variable through public method
#40
del bean.a        # deleting private variable through public method
# print(bean.a)      # accessing private variable through public method (will raise AttributeError)
# del bean.b        # deleting private variable through public method
# print(bean.b)      # accessing private variable through public method (will raise AttributeError)

#----------------------------------------------------------------------------------------------------------









# class Product:
#     def __init__(self, name, price):
#         self.__name = name    # private variable
#         self.__price = price  # private variable

#     def get_name(self):     # getter method
#         return self.__name   # accessing private variable through public method

#     def set_name(self, name): # setter method
#         self.__name = name   # setting private variable through public method

#     def get_price(self):    # getter method
#         return self.__price  # accessing private variable through public method

#     def set_price(self, price): # setter method
#         if price > 0:
#             self.__price = price  # setting private variable through public method
#         else:
#             print("Invalid price")

#     def info(self):          # public method
#         print("Product Name: {}, Price: {}".format(self.__name, self.__price))
#         # public method can be accessed from outside the class

# p = Product("Laptop", 1000)
# print(p.get_name())      # accessing private variable through public method
# print(p.get_price())     # accessing private variable through public method
# p.info()                 # accessing public method
# p.set_price(1200)       # setting private variable through public method
# p.info()                 # accessing public method
# p.set_price(-500)      # setting private variable through public method


# # example
# class Computer:
#     def __init__(self):
#         self.__maxprice = 900   # private variable
    
#     def sell(self):
#         print("selling price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price
#         # setter method to change the value of private variable
#         # we can also use getter method to access the value of private variabl
#         # but here we are directly accessing the private variable using sell method
#         # but it is not a good practice to access private variable directly
#         # so we are using setter method to change the value of private variable
#     def getMaxPrice(self):
#         return self.__maxprice
#         # getter method to access the value of private variable
#     def info(self):
#         print("This is a computer")
#         # public method
#         # public method can be accessed from outside the class
# c = Computer()
# c.sell()
# # selling price: 900

# # c.__maxprice = 1000    # we cannot access the private variable directly
# # selling price: 900 

# c.setMaxPrice(1000)    # using setter method to change the value of private variable
# #selling price: 1000

# c.sell()
# # selling price: 1000

# print(c.getMaxPrice()) # using getter method to access the value of private variable
# # 1000
# c.info()               # accessing public method
# # This is a computer
#----------------------------------------------------------------------------------------------------------
