n = int(input("n: "))

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2*(n-i)-1):
#         print("*", end=" ")
#     print()

# char = ord("A")+ n-1
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2*(n-i)-1):
#         print(chr(char), end=" ")
#     char-=1
#     print()

# n: 4
# D D D D D D D
#   C C C C C
#     B B B
#       A


# for i in range(2*n):
#     s=i
#     if i>n:
#         s=2*n-i
#     for j in range(s):
#         print("*", end=" ")

#     print()

# n: 5

#   0  # *
#   1  # * *
#   2  # * * *
#   3  # * * * *
#   4  # * * * * *
#   5  # * * * *
#   6  # * * *
#   7  # * *
#   8  # *

# other way
for i in range(n-1,-n,-1):
    for j in range(n-abs(i)):
        print("*", end=" ")
    print()

# n: 6
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(n-1,-n,-1):
#     for k in range(abs(i)):
#         print(" ", end=" ")

#     for j in range(n-abs(i)):
#         print("*", end=" ")
#     print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# for i in range(n):
    
#     pre = 1
#     for j in range(n-i):
#         print(" ", end="")
        
#     for k in range(i+1):
#         val = pre+(i//(j+1))
     
#         print(f"{val} ",end="")
#     print()

# pascal's triangle

# for i in range(n):
#     val = 1
#     for k in range(n-i-1):
#         print(" ", end="")
    
#     for j in range(i+1):
#         print(val,end=" ")
#         val = val*(i-j)//(j+1)
#     print()

#     1 
#    1 1 
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# holow pyramid

# for i in range(n):
#     for j in range(2*n-1):
#         if i==n-1 or i+j==n-1 or j-i==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

# for i in range(n):
#     for j in range(n):
#         if i==0 or i ==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# for i in range(n):
#     for j in range(n):
#         if i==0 or i ==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * * *
# * *   * *
# *   *   *
# * *   * *
# * * * * *

# for i in range(n):
#     for j in range(n):
#         if i==0 or i ==n-1 or j==0 or j==n-1 or i==n//2 or j == n//2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * * *
# *   *   *
# * * * * *
# *   *   *
# * * * * *


# for i in range(2*n):
#     s=i
#     if i>n:
#         for j in range(2*n-i):
#             if i+j==n-1 or j-i==n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
        
#     else:
#         for k in range(i):
#             if i==k or i+k==n-1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()


for i in range(2*n):
    if i>n:
        for j in range(n):
            if i==j or i+j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
    else:
        for j in range(2*n-1):
            if i+j==n-1 or j-i==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()