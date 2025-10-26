# The raise statement in Python is used to manually trigger (raise) an exception.
# raise ExceptionType("optional message")

l1=[10,20,30,40]
print("Start")
try:
    i=int(input("enter index:"))
    if i>len(l1)-1 or i<-len(l1):
        raise IndexError
except:
    print("some error occured")
else:
    print(l1)
print("End")

# Start
# enter index:3
# [10, 20, 30, 40]
# End

# Start
# enter index:-1
# [10, 20, 30, 40]
# End

# Start
# enter index:5
# some error occured
# End

# ---------------------------------------------------------------------------------------

# without rise:

# Start
# enter index:6
# [10, 20, 30, 40]
# End

# ----------------------------------------------------------------------------------------

