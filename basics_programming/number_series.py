n = int(input("enter the value: "))

# for i in range(1,n+1):
#     print(i, end=" ")

#---------------------------------------

# for i in range(1, n+1):
#     if i%2!=0:
#         print(i+1, end=" ")
#     else:
#         print(i-1, end=" ")

# enter the value: 5
# 2 1 4 3 6 

#------------------------------------------

# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i*2, end=" ")
#     else:
#         print(i, end=" ")

# enter the value: 6
# 1 4 3 8 5 12 

#--------------------------------------------

# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i**2, end=" ")
#     else:
#         print(i**3, end=" ")

# enter the value: 5
# 1 4 27 16 125 

#---------------------------------------------

# val = 1
# for i in range(n):
#     print(val, end=" ")
#     val +=3

# enter the value: 6
# 1 4 7 10 13 16 

#---------------------------------------------

# val = 5
# for i in range(n):
#     print(val, end=" ")
#     val *= 2

# enter the value: 6
# 5 10 20 40 80 160 

#----------------------------------------------
# val = 1
# for i in range(2,n+1):
#     print(val,end=" ")
#     val *=i

# enter the value: 6
# 1 2 6 24 120 

#----------------------------------------------
# eleven =11
# val = 1
# for i in range(1,n+1):
    
#     if i> 9:
#         print(eleven * val, end=" ")
#         val +=1
#     else:
#         print(i, end=" ")

# enter the value: 14
# 1 2 3 4 5 6 7 8 9 11 22 33 44 55 

# other method

# def palindrome(n):
#     res=0
#     while n!=0:
#         rem = n%10
#         res = res * 10 +rem
#         n = n // 10
#     return res


# for i in range(1, n+1):
#     if palindrome(i) == i:
#         print(i, end=" ")

# enter the value: 100
# 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 

#--------------------------------------------

# def binary_to_decimal(n):
#     res=0
#     temp = 1
#     count = 0
#     while n != 0:
#         rem = n % 2
#         res = res + temp * rem
#         if rem == 1:
#             count+=1
#         n = n // 2
#         temp = temp * 10
#     return res


# for i in range(1, n+1):
#     print(binary_to_decimal(i), end=" ")


#------------------------------------------------

# def is_prime(n):
#     if n>1:
#         for i in range(2, n):
#             if n%i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# without a range
# for i in range(n+1):
#     if is_prime(i):
#         print(i, end=" ")

# enter the value: 15
# 2 3 5 7 11 13

# with a range
# start = 50
# end = 100

# for i in range(start, end):
#     if is_prime(i):
#         print(i, end=" ")

# 53 59 61 67 71 73 79 83 89 97 

#------------------------------------------------

# fibinocci series

# n1 = 0
# n2 = 1

# if n<= 0:
#     print("enter a positive number: ")
# elif n == 1:
#     print(n1, end=" ")
# else:
#     print(n1, end=" ")
#     print(n2, end=" ")
#     for i in range(2, n):
#         r = n1 + n2
#         n1 = n2
#         n2 = r
#         print(r, end=" ")

# enter the value: 10
# 0 1 1 2 3 5 8 13 21 34 


#----------------------------------

# val1 = n
# val2 = 1

# for i in range(1, n*2+1):
#     if i % 2 !=0:
#         print(val1,end=" ")
#         val1 -=1
#     else:
#         print(val2,end=" ")
#         val2 +=1

# enter the value: 10
# 10 1 9 2 8 3 7 4 6 5 5 6 4 7 3 8 2 9 1 10 

# another method

# val1 = n
# val2 = 1

# for i in range(n):
#     print(val1, end=" ")
#     print(val2, end=" ")
#     val1 -=1
#     val2 +=1

# enter the value: 10
# 10 1 9 2 8 3 7 4 6 5 5 6 4 7 3 8 2 9 1 10 

#--------------------------------------------

# val1 = ord("A")
# print(1, end=" ")
# for i in range(n):
#     print(chr(val1), end=" ")
#     print("*", end=" ")
#     val1 +=2

# enter the value: 4
# 1 A * C * E * G * 


# correct way

# val = ord("A")

# for i in range(1, n+1):
#     if i == 1:
#         print(1, end=" ")
#     elif i % 2 == 0:
#         print(chr(val), end=" ")
#         val += 2
#     else:
#         print("*", end=" ")

# enter the value: 10
# 1 A * C * E * G * I 

#---------------------------------


# wap to display the series based on below condition
# - try to display all the perfect numbers from 25 to 90, print the same number if it is a perfect or display the @ character





# @ @ @ 28 @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @

#---------------------------------------

# n1 = 0
# n2 = 1
# n3 = 1
# if n<= 0:
#     print("enter a positive number: ")
# elif n == 1:
#     print(n1, end=" ")
# elif n == 2:
#     print(n1, end=" ")
#     print(n2, end=" ")
# else:
#     print(n1, end=" ")
#     print(n2, end=" ")
#     print(n3, end=" ")
#     for i in range(3, n):
#         r = n1 + n2 + n3
#         n1 = n2
#         n2 = n3
#         n3 = r
#         print(r, end=" ")

# enter the value: 1
# 0 
# enter the value: 2
# 0 1 
# enter the value: 3
# 0 1 1 
# enter the value: 6
# 0 1 1 2 4 7 

#------------------------------------------------------

