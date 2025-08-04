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
        for j in range(1,i+1):
            print(j,end="")
        print()
# enter n:5
# 12345
# 1234
# 123
# 12
# 1
def pattern7(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i+1):
            print("* ",end="")
        print()
# enter n:5
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(n-i):
            print("* ",end="")
        print()
# enter n:5
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *
def pattern9(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        for j in range(2*i+1):
            print("*", end="")
        print()
# enter n:5
#      *
#     ***
#    *****
#   *******
#  *********
def pattern10(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print("*",end="")
        print()
# enter n:5
# *********
#  *******
#   *****
#    ***
#     *
def pattern11(n):
    for i in range(n):
        star=1
        if i%2==0:
            star=0
        else:
            star=1
        for j in range(i+1):
            print(star,end="")
            star=1-star
        print()
# enter n:5
# 0
# 10
# 010
# 1010
# 01010
def pattern12(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n):  
        for j in range(n-i-1):
            print("*",end="")
        print()

        #or
        
def pattern12b(n):
    for i in range(2*n):
        s=i
        if i>n:
            s=2*n-i
        for j in range(s):
            print("*",end="")
        print()
# enter n:5
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern13(n):
    space=2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        for j in range(space-(i*2)):
            print(" ",end="")
        for j in range(i,-1,-1):
            print(j+1,end="")
        print()
# enter n:5
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
def pattern14(n):
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(f"{num} ",end="")
            num+=1
        print()
# enter n:5
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
n=int(input("enter n:"))
pattern14(n)




