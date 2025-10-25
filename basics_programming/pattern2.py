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

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       Z 
# #     Y Y
# #   X X X
# # W W W W

# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(val,end=' ')
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# #       1 
# #     2 2
# #   3 3 3
# # 4 4 4 4

# for i in range(n):
#     val=1
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# #       1 
# #     1 2
# #   1 2 3
# # 1 2 3 4

# val=n
# for i in range(n):
#     for j in range(n):
#         if(i+j>=n-1):
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# #       4 
# #     3 3
# #   2 2 2
# # 1 1 1 1

# for i in range (n):
#     val=n
#     for j in range(n):
#         if(i+j>=n-1):
#             print(val,end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# #       4 
# #     4 3
# #   4 3 2
# # 4 3 2 1

# val=1
# for i in range(n):
#     for j in range(n):
#         if(i+j<=n-1):
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # 1 1 1 1 
# # 2 2 2
# # 3 3
# # 4

# for i in range(n):
#     val=1
#     for j in range(n):
#         if(i+j<=n-1):
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # 1 2 3 4 
# # 1 2 3
# # 1 2
# # 1

# for i in range(n):
#     val=n
#     for j in range(n):
#         if i+j<=n-1:
#             print(val,end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # 4 3 2 1 
# # 4 3 2
# # 4 3
# # 4

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # A B C D 
# # A B C
# # A B
# # A

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # A A A A
# # B B B
# # C C
# # D

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # Z Z Z Z 
# # Y Y Y
# # X X
# # W

# for i in range(n):
#     val=ord("Z")
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # Z Y X W 
# # Z Y X
# # Z Y
# # Z

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # D D D D 
# # C C C
# # B B
# # A

# for i in range(n):
#     val=ord("A")+n-1
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # D C B A 
# # D C B
# # D C
# # D

# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             if j%2==0:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # 1 * 2 * 
# # 3 * 4
# # 5 *
# # 6

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # A B C D 
# # E F G
# # H I
# # J