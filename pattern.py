# solving 22 patterns problems

# tips
# 1. for the outer loop, count the no. of lines
# 2. for the inner loop, focus on the columns and connect with them somehow to the rows
# 3. print them " * " inside the inner for loop
# 4. observe symmetry { optional }


def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
# enter n:5
# *****
# *****
# *****
# *****
# *****
def pattern2(n):
    for i in range(n):
        for j in range (i+1):
            print("*",end='')
        print()
# enter n:5
# *     
# **     
# ***     
# ****
# *****
def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        print()
# enter n:5
# 1
# 12
# 123
# 1234
# 12345
def pattern4(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()
# enter n:5
# 1
# 22
# 333
# 4444
# 55555
def pattern5(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()
# enter n:5
# *****
# ****
# ***
# **
# *
def pattern6(n):
    for i in range (n,0,-1):
        for j in range(i,0,-1):
            print(j,end="")
        print()
# enter n:5
# 54321
# 4321
# 321
# 21
# 1
n=int(input("enter n:"))
pattern6(n)




