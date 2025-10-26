# In Exception we have two types:
#   Built-in
#   Custom

# Built-in exception are already present in python sence can be handled already
# Custom exception are defined by user when such exception are not present in python 

class AgeLesserError(Exception):
    pass
class AgeGreaterError(Exception):
    def __init__(self,msg="U are too old"):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    age=int(input("enter age:"))
    if age<21:
        raise AgeLesserError("U are too young")
    if age>45:
        raise AgeGreaterError 
except ValueError as e:
    print(e)
#     enter age:Age
# invalid literal for int() with base 10: 'Age'
except AgeLesserError as e:
    print(e)
# enter age:8
# U are too young
except AgeGreaterError as e:
    print(e)
# enter age:49
# U are too old
else:
    print("Registration form accepted")
# enter age:21
# Registration form accepted

# ----------------------------------------------------------------------------------------

class NegativeError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg
class ZeroError(Exception):
    def __str__(self):
        return "zero is neither positive or negitive"

while True:
    try:
        n=int(input("Enter the number:"))
        if n<0:
            raise NegativeError("No negative value")
        if n==0:
            raise ZeroError
    except ValueError as e:
        print(e)
    except NegativeError as e:
        print(e)
    except ZeroError as e:
        print(e)
    else:
        print(n)
        break
    
# Enter the number:-8
# No negative value
# Enter the number:0
# zero is neither positive or negitive
# Enter the number:5
# 5