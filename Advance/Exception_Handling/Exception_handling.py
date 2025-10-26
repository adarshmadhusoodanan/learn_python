# Errors: Errors are mistake in program which will not allow the program to exceute completely
# Three type of error:
#   Compile Time
#   Logical 
#   Run Time

# Run Time Error are Exception
# If Exception occurs program stops immediatly

# syntax: 

# try:
#     doubtfull code
# except:
#     handle code
# else:
#     relevent code 
# finally:
#     exceute always

# -----------------------------------------------------------------------------------------------

# simple example:

print('Start')
a=int(input("a:"))                  # doubtfull: Value Error
#     a=int(input("a:"))                  
#       ^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'a'
b=int(input("b:"))                  # doubtfull: Value Error
#     b=int(input("b:"))  
#       ^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'b'
c=a/b                               # doubtfull: Zero division Error
#     c=a/b                               
#       ~^~
# ZeroDivisionError: division by zero
print(c)
print("End")

# using exception handling

print("Start")
try:
    a=int(input("a:"))  
    b=int(input("b:")) 
    c=a/b
except:
    print("Some error occured")
else:
    print(c)
finally:
    print("I am finally")
print("End")

# Start
# a:a
# Some error occured
# I am finally
# End

# Start
# a:5
# b:0
# Some error occured
# I am finally
# End

# Start
# a:6
# b:3
# 2.0
# I am finally
# End

# -------------------------------------------------------------------------------------------------

# To specify exception we define multiple except blocks to handle each exception seperately

print("Start")
try:
    a=int(input("enter a:"))
    b=int(input("enter b:")) 
    c=a/b
except ValueError as e:
    print("Int type value must be entered")
    print(e)
# enter a:a
# Int type value must be entered
# invalid literal for int() with base 10: 'a'
# End
except ZeroDivisionError as e:
    print("Denominator most not be zero")
    print(e)
# Start
# enter a:6
# enter b:0
# Denominator most not be zero
# division by zero
# End
except:
    print("Some error occured")
else:
    print(c)
# Start
# enter a:50
# enter b:5
# 10.0
# End
print("End")

# ---------------------------------------------------------------------------------------------

l1=[10,20,30,40]
print("Start")
try:
    i=int(input("enter index:"))
    if i>len(l1)-1 or i<-len(l1):
        raise IndexError
except ValueError as e:
    print("Int value is expected")
    print(e)
# Start
# enter index:e
# Int value is expected
# invalid literal for int() with base 10: 'e'
# End
except IndexError as e:
    print("Invalid Index")
    print(e)
# Start
# enter index:7
# Invalid Index

# End
except:
    print("some error occured")
else:
    print(l1)
# Start
# enter index:3
# [10, 20, 30, 40]
# End
print("End")