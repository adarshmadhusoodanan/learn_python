n=int(input("enter number"))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# #       1 
# #     2
# #   3
# # 4

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# #       A 
# #     B
# #   C
# # D

# val=n
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       4 
# #     3
# #   2
# # 1

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       Z 
# #     Y
# #   X
# # W

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       D 
# #     C
# #   B
# # A

# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             if i%2==0:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #       1 
# #     *
# #   2
# # *

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# #       A 
# #     B B
# #   C C C
# # D D D D

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# #       A 
# #     A B
# #   A B C
# # A B C D

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       D 
# #     C C
# #   B B B
# # A A A A

# for i in range(n):
#     val=ord("A")+n-1
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# #       D 
# #     D C
# #   D C B
# # D C B A

# for i in range(n):
#     val=ord("Z")
#     for j in range(n):
#         if(i+j>=n-1):
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# #       Z 
# #     Z Y
# #   Z Y X
# # Z Y X W