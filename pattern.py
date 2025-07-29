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
def pattern2(n):
    for i in range(n):
        for j in range (i+1):
            print("*",end='')
        print()
n=int(input("enter n:"))
pattern2(n)




