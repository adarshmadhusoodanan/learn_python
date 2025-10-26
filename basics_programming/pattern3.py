n=int(input ("enter the number "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
#     print()
# #       * 
# #     * * *
# #   * * * * *
# # * * * * * * *

# for i in range(n):
#     print("  "*(n-1-i)+"* "*(2*i+1))
# #       * 
# #     * * *
# #   * * * * *
# # * * * * * * *

# str=1
# spc=n-1
# for i in range(n):
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(str):
#         print("*",end=" ")
#     print()
#     spc-=1
#     str+=2
# #       * 
# #     * * *
# #   * * * * *
# # * * * * * * *

# val=1
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#     val+=1
#     print()
# #       1 
# #     2 2 2
# #   3 3 3 3 3
# # 4 4 4 4 4 4 4

# for i in range(n):
#     val=1
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#         val+=1
#     print()
# #       1 
# #     1 2 3
# #   1 2 3 4 5
# # 1 2 3 4 5 6 7

# val=n
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#     val-=1
#     print()
# #       4 
# #     3 3 3
# #   2 2 2 2 2
# # 1 1 1 1 1 1 1

# for i in range(n):
#     val=n
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         if val>=0:
#             print(val,end=" ")
#             val-=1
#         else:
#             val=n
#             print(val,end=" ")
#             val-=1
#     print()
# #       4 
# #     4 3 2
# #   4 3 2 1 0
# # 4 3 2 1 0 4 3

# val=ord("A")
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
#     val+=1
#     print()
# #       A 
# #     B B B
# #   C C C C C
# # D D D D D D D

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
#     val-=1
#     print()
# #       D 
# #     C C C
# #   B B B B B
# # A A A A A A A