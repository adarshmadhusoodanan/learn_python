# n= int(input("enter anumber "))
# for i in range(0,n):
#     for j in range(0,n):
#         print(chr(65+i),end=" ")
#     print()

# # A A A A 
# # B B B B
# # C C C C
# # D D D D

# for i in range(0,n):
#     for j in range(0,n):
#         print(chr(65+j),end=" ")
#     print()
# # A B C D 
# # A B C D
# # A B C D
# # A B C D

# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(chr(65+i-1),end=" ")
#     print()

# # D D D D
# # C C C C
# # B B B B
# # A A A A

# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(chr(65+j-1),end=" ")
#     print()

# # D C B A
# # D C B A
# # D C B A
# # D C B A

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         print(chr(val),end=" ")
#     val+=1
#     print()

# # A A A A 
# # B B B B
# # C C C C
# # D D D D

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         print(chr(val),end=" ")
#     val-=1
#     print()

# # D D D D
# # C C C C
# # B B B B
# # A A A A

# -------------------------------------------------------------------------------------------------------

n=int(input("enter number "))
# for i in range (n):
#     for j in range(n):
#         print(i, end="")
#         print(j, end=" ")
#     print()
# # 00 01 02 03 04 
# # 10 11 12 13 14
# # 20 21 22 23 24
# # 30 31 32 33 34
# # 40 41 42 43 44

#     for j in range(n):
#         print(i+j,end=" ")
#     print()

# # 0 1 2 3 4
# # 1 2 3 4 5
# # 2 3 4 5 6
# # 3 4 5 6 7
# # 4 5 6 7 8

# for i in range (n):
#     for j in range(n):
#         if i>=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # *       
# # * *
# # * * *
# # * * * *
# # * * * * *

# for i in range (n):
#     for j in range(n):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *

# for i in range (n):
#     for j in range(n):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # * * * * *
# #   * * * *
# #     * * *
# #       * *
# #         *

# for i in range(n):
#     for j in range (n):
#         if i+j<n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # * * * * * 
# # * * * *
# # * * *
# # * *
# # *

# ----------------------------------------------------------------------------------------------------------
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4


# for i in range(n):
#     val=1
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#             val+=1
#     print()
# # 1 
# # 1 2
# # 1 2 3
# # 1 2 3 4

# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             if len(str(val))==1:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 val=1
#                 print(val,end=" ")
#                 val+=1
#     print()
# # 1 
# # 2 3
# # 4 5 6
# # 7 8 9 1
# # 2 3 4 5 6


# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()

# # A       
# # B B
# # C C C
# # D D D D

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # A       
# # A B
# # A B C
# # A B C D

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()

# # A       
# # B C
# # D E F
# # G H I J

# val=n
# for i in range(n):
#     for j in range(n):
#         if(i>=j):
#             print(val , end=" ")
#         else:
#             print(" ",end=" ")
#     val=n-i-1
#     print()
# # 4       
# # 3 3
# # 2 2 2
# # 1 1 1 1

# for i in range(n):
#     val=n
#     for j in range(n):
#         if(i>=j):
#             print(val , end=" ")
#             val=n-1-j
#         else:
#             print(" ",end=" ")
#     print()

# # 4       
# # 4 3
# # 4 3 2
# # 4 3 2 1

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if(i>=j):
#             print(chr(val) , end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # Z       
# # Y Y
# # X X X
# # W W W W

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if(i>=j):
#             print(chr(val) , end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # D       
# # C C
# # B B B
# # A A A A

# for i in range(n):
#     val=ord("A")+n-1
#     for j in range(n):
#         if(i>=j):
#             print(chr(val) , end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # D       
# # D C
# # D C B
# # D C B A

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if(i>=j):
#             if val>=ord("A"):
#                 print(chr(val) , end=" ")
#                 val-=1
#             else:
#                 val=ord("A")+n-1
#                 print(chr(val),end=" ")
#                 val-=1
#         else:
#             print(" ",end=" ")
#     print()

# # D       
# # C B
# # A D C
# # B A D C

# -------------------------------------------------------------------------------------------------

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val), end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # A A A A 
# #   B B B
# #     C C
# #       D

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # A B C D 
# #   A B C
# #     A B
# #       A

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # A B C D 
# #   E F G
# #     H I
# #       J

# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # 1 1 1 1 
# #   2 2 2
# #     3 3
# #       4

# for i in range(n):
#     val=1
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# # 1 2 3 4 
# #   1 2 3
# #     1 2
# #       1

# for i in range(n):
#     val=n
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # 4 3 2 1 
# #   4 3 2
# #     4 3
# #       4

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # D D D D 
# #   C C C
# #     B B
# #       A

# val=ord("A")+n-1
# for i in range(n):
#     val=ord("A")+n-1
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
# # D C B A 
# #   D C B
# #     D C
# #       D

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     val=ord("Z")-1-i
#     print()
# # Z Y X W 
# #   Y X W
# #     X W
# #       W

# ------------------------------------------------------------------------------------

# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # 1       
# #   2
# #     3
# #       4
        
# val=n
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val=n-1-i
#     print()
# # 4       
# #   3
# #     2
# #       1

# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     print()
# # A       
# #   B
# #     C
# #       D

# val=ord("A")+n-1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # D       
# #   C
# #     B
# #       A

# val=ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     print()
# # Z       
# #   Y
# #     X
# #       W

# val1=1
# val2="*"
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             if i%2==0:
#                 print(val1,end=" ")
#                 val1+=1
#             else:
#                 print(val2,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # 1       
# #   *
# #     2
# #       *
