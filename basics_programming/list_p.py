# list based program

# l1 = [2,11,6,8,1,4,13,10]

# for i in l1:
#     print(i, end=" ")
# #2 11 6 8 1 4 13 10 
# for i in range(len(l1)):
#     print(l1[i], end=" ")

#------------------------------------------------------

# max and min value without using built in functions

# max_val = l1[0]
# min_val = l1[0]
# idx = 0
# idy = 0
# count = 0
# for i in range(len(l1)):
#     if max_val<l1[i]:
#         max_val = l1[i]
#         idx = i
#     if min_val>l1[i]:
#         min_val = l1[i]
#         idy = i

#     count+=1

# print("maximum value: ", max_val ," present at ", idx)
# print("total number or element: ", count)
# print("minmum value: ", min_val ," present at ", idy)

# # maximum value:  13  present at  6
# # total number or element:  8
# # minmum value:  1  present at  4

#----------------------------------------------

# l2  = [2, 10, 18, 36, 49, 51]

# for i in range(len(l2)-1):
#     val1 = l2[i] +1   #it will start from 3
#     val2 = l2[i+1]
#     for j in range(val1, val2):
#         print(j, end=" ")

# 3 4 5 6 7 8 9 11 12 13 14 15 16 17 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 37 38 39 40 41 42 43 44 45 46 47 48 50 

#----------------------------------------------------------------------

# wap to check given list is palindrome or not

# l2 = [1,2,3,4,4,3,2,1]
# wrong

# pal = True
# for i in range(len(l2)):
#     for j in range(len(l2)-1,0,-1):
#         print("i   ",l2[i])
#         print("j   ",l2[j])
#         if l2[i] == l2[j]:
#             pal = True
#         else:
#             pal = False

# if pal:
#     print("palindrome")
# else:
#     print("not palindrome")

# correct

# j = len(l2) - 1

# for i in range(len(l2)):
#     if l2[i] != l2[j]:
#         print("list is not palindrome")
#         break
#     j -=1
# else:
#     print("list is a palindrome")

# program to find sum even and odd numbers present in a list and print its difference

# l1 = [10,7,1,14,18,23,6]

# even = 0 
# odd = 0
# for i in range(len(l1)):
#     if l1[i]%2 == 0:
#         even += l1[i]
#     else:
#         odd += l1[i]
# print("even sum: ", even)
# print("odd sum: ", odd)
# print("difference ",abs(even-odd))

#------------------------------------------------

# # program to display first two max element present in the list
# l2 = [100,7,1,14,18,23,66]
# max_val = l2[0] #- 100
# sec_val = l2[1] #- 7/100

# for i in range(len(l2)):
#     if max_val<l2[i]:
#         sec_val = max_val
#         max_val = l2[i]
    
#     elif sec_val<l2[i]:
#         sec_val = l2[i]

# print(max_val,sec_val)

#100 100   -bug need to change
#--------------------------------------

# sort the given list in the asencding order without using any in built function

# bubble sort/ sinking sort

# l1 = [2,11,6,8,1,4,13,10]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# print(l1)

#---------------------------------------------------

# selection sort

# it is used to sort the given list in a ascending order
# in this need to find minimum element present in a list and then swap with the i th element

# algorithm
# - use two pointer technique in such a way that when the first variable is pointing to 0 th index and second variable need to point second index
#steps: 

# consider the first element as min element
# compare min value with all the remaning elements 
# once we get the min value while comming out of inner for loop swap with the i th element in a list

#solustion

#        | 7 | 8 | 2 | 5 | 1 |
    #      i   j                initial
 

# value = [7, 8, 2, 5, 1,1]

# for i in range(len(value)):
#     min_ele = i      # initaily the min index is = 0
#     for j in range(i+1, len(value)):
#         if value[min_ele] > value[j]:   # here 7 > 8 => j+1 => check 7> 2 then condition true
#             min_ele = j                 # min_ele index will be the index of 2 that is 2       => this will repeat until the smallest element, last the min_ele = index of 1 that is 4
    
#     # swap i th and current min_ele

#     value[i], value[min_ele] = value[min_ele], value[i]    # now it will swap 7, and 1
#      now the first elemenet is 1
#       i will increse 1  => repeat



# print(value)


#------------------------------------------------------------------------------
# ahifting all the zero to the left side
# l1 = [1,1,1,0,0,0,1,1,0,1,1]
# zc = 0

# for i in range(len(l1)):
#     if l1[i] == 0:
#         zc+=1

# for i in range(len(l1)):
#     if i< zc:
#         l1[i] = 0
#     else:
#         l1[i] = 1

# print(l1)


# wap to display all the prime numbers present in the list along with its sum using sum

# def is_prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# prime = [2, 3, 5, 7, 9,11]
# sum = 0
# for i in range(len(prime)):
#     if is_prime(prime[i]):
#         sum += prime[i]

# print(sum)


#---------------------------------------------

# wap to display the list after nth left rotation

# l1 = [11,22,33,44,55,66]
# rot = int(input("enter the number of rotation"))
# for _ in range(rot):
#     last = l1[0]
#     for i in range(len(l1)-1):
#         l1[i]= l1[i+1]
        
#     l1[len(l1)-1] = last
#     print(l1)  #[22, 33, 44, 55, 66, 11]
#------------------------------------------------------

## wap to display the list after nth right rotation
# l1 = [11,22,33,44,55,66]
# # rot = int(input("enter the number of rotation"))
# # for _ in range(rot):



# last = l1[0]
# for i in range(len(l1)-1):
#     l1[i]= l1[i+1]
    
# l1[len(l1)-1] = last
# print(l1)  #[22, 33, 44, 55, 66, 11]

#-------------------------------------

#10#program to display average of sum of given values using following condition.
# l1 = [2, 4, 6, 8, 10]
# l2=[]
# for i in l1:
#     prod=1
#     for j in l1:
#         if i != j:
#             prod = prod * j
#     l2.append(prod//i)
# print(l2) # [960, 240, 106, 60, 38]  

#11#
# l1=['1','l','$','u','2','h','a','#','r','3','r','4']
# print(l1)
# # count the characters and numbers in l1
# count = 0
# for i in range(len(l1)):
#     if ord(l1[i]) >= 48 and ord(l1[i]) <= 57 or ord(l1[i]) >= 97 and ord(l1[i]) <= 122:
#         count+=1
# print(count)

# # #create a new list based the count
# l2 = [None]*count
# print(l2)   #[None, None, None, None, None, None, None, None, None, None]

# # #add only characters and numbers to new list
# j=0
# for i in range(len(l1)):
#     if ord(l1[i]) >= 48 and ord(l1[i]) <=57 or ord(l1[i])>=97 and ord(l1[i]) <= 122:
#         l2[j] = l1[i]
#         j = j + 1
# print(l2)   #['1', 'l', 'u', '2', 'h', 'a', 'r', '3', 'r', '4']

# # #reverse the list
# l2 = l2[::-1]
# # print(l2) #['4', 'r', '3', 'r', 'a', 'h', '2', 'u', 'l', '1']

# j=0
# for i in range(len(l1)):
#     if ord(l1[i]) >= 48 and ord(l1[i]) <=57 or ord(l1[i])>=97 and ord(l1[i]) <= 122: 
#          l1[i] = l2[j]
#          j = j + 1
# print(l1)  #['4', 'r', '$', '3', 'r', 'a', 'h', '#', '2', 'u', 'l', '1']
#output:
# ['1', 'l', '$', 'u', '2', 'h', 'a', '#', 'r', '3', 'r', '4']
# ['4', 'r', '$', '3', 'r', 'a', 'h', '#', '2', 'u', 'l', '1']

#create a function to check the value is num or char and print True or False
# l1=['1', 'l', '$', 'u', '2', 'h', 'a', '#', 'r', '3', 'r', '4']
# def is_num_or_char(val):

#     j=len(l1)-1
#     for i in range(len(l1)):
#         if is_num_or_char(l1[i]) and is_num_or_char(l1[j]):

#             swap 1st and last e

#-------------------------------------------------

# flatterned the nested list

# l1 = [[1,2,3], 5,6, [7,8,9,3],8,[5]]

# res = []

# for i in l1:
#     if type(i) == list:
#         for j in i:
#             res.append(j)
#     else:
#         res.append(i)

# print(l1)   #[[1, 2, 3], 5, 6, [7, 8, 9, 3], 8, [5]]
# print(res)  #[1, 2, 3, 5, 6, 7, 8, 9, 3, 8, 5]
#------------------------------------------


#l1 = [2,1,89,70,3,10,90,23,5]

# we have a list we need to find the mid element and sort the first half in ascennding order
# and second half in descending order

# def sort_asc(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 l[i], l[j] = l[j], l[i]
#     return l 

# def sort_desc(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]<l[j]:
#                 l[i], l[j] = l[j], l[i]
#     return l 

# l1 = [2,1,89,70,3,10,90,23,5]

# first=[]
# second=[]
# for i in range(len(l1)//2):
#     first.append(l1[i])
# for j in range(len(l1)//2, len(l1)):
#     second.append(l1[j])


# print(first)
# print(second)
# print(sort_asc(first)+sort_desc(second))

# another method

# def sort_list(l1):
#     mid= len(l1)//2
#     # print(mid)

#     # first half for ascending order
#     for i in range(mid):
#         for j in range(i+1, mid):
#             if l1[i]>l1[j]:
#                 l1[i], l1[j] = l1[j], l1[i]
    
#     #print(l1)

#     # second half for the descending order

#     for i in range(mid,len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i]<l1[j]:
#                 l1[i], l1[j] = l1[j], l1[i]

#     return l1

# l1 = [2,1,89,70,3,10,90,23,5]
# print(sort_list(l1))



#----------------------------------------------------------

# display the index of first and last of the given input number

# l1 = [2,3,1,10,3,4,6,3,18,20]
# num = int(input("n: "))
# for i in range(len(l1)):
#     if num == l1[i]:
#         findex = i
#         # print(l1[i])
#         break
# for i in range(len(l1)-1,0,-1):
#     if num == l1[i]:
#         lindex = i
#         break


# print("first index: ", findex)
# print("last index: ", lindex)

# another way

# def first_and_last(l1, val):
#     first_idx = -1
#     last_idx = -1

#     for i in range(len(l1)):
#         if val == l1[i]:
#             if first_idx == -1:
#                 first_idx = i
#             last_idx = i
#     return first_idx, last_idx

# l1 = [2,3,1,10,3,4,6,3,18,20]
# num = int(input("n: "))

# f, l = first_and_last(l1, num)

# print("first index: ", f)
# print("last index: ", l)

#-------------------------------------------------

# display all the possible pairs of a target value

# l1 = [2, 3, 1, 10, 3, 4, 6, 3, 5, 2]
# target = 6
# def target_sum(l1,target):
#     result = []
#     for i in range(len(l1)):
        
#         val = target-l1[i]
#         # print(val)
#         for j in range(i+1, len(l1)):
#             if val == l1[j]:
#                 result.append((l1[i],l1[j]))
#     return result

# print(target_sum(l1,target))

#--------------------------------------------------------

# output should be true or false

# l1 = [5,5]

# def check_last_digit_is_5(l1):
#     result = True
#     if l1 == []:
#         result = False
#         return result
#     else:
#         for val in l1:
#             last_num = val% 10
#             if last_num != 5:
#                 result = False
#                 break
#     return result

# print(check_last_digit_is_5(l1))


# anil wants to purchase a stock. after purchasing we need to sell in another day.
#  to get the maximum profit. write a code to help anil when to purchase and when to sell to get a maximum profit.

# l1 = [12,11,10,1,2,3,9]
# l1 = [1,1]
# l1=[1,2]
# l1 = [2,1]
# l1 = [3,2,1]

# max_profit = 0
# if len(l1)<2:
#     print("buy and sell price is not there")
# else:
#     for i in range(len(l1)):
#         for j in range(i+1,len(l1)):
#             current_profit = abs(l1[i] - l1[j])
#             if max_profit<=current_profit:
#                 max_profit = current_profit
#                 if l1[i]>l1[j]:
#                     buy_index= j
#                     sell_index= i
#                 else:
#                     buy_index= i
#                     sell_index= j

#     print(f"buy at {buy_index} and sell at {sell_index} then profit will be {max_profit}")

#--------------------------------

# display the majority element present in the list 

# using dictionary

# def check_majority_element(l1):
#     d={}
#     for i in l1:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i]+=1
#     return d

# l1 = [1]
# print(check_majority_element(l1))

# for k,v in check_majority_element(l1).items():
#     if v > len(l1)//2:
#         print("majority element-> ", k)
#         print("count: ", v)
#         break
# else:
#     print(-1)

# using two pointer

# l1 = [1,2,3,5]
# def majority_element(l1):
#     for i in range(len(l1)):
#         count = 0
#         for j in range(len(l1)):
#             if l1[i] == l1[j]:
#                 count += 1
#             if count > len(l1) // 2:
#                 return l1[i]
#     return -1

# print(majority_element(l1))

#---------------------------------------


# wap to display the list leaders present in a given list
# two pointer method

# l1 = [16,17,2,3,5,2]
# def find_leader(l1):
#     leader = []
#     for i in range(len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i]<l1[j]:
#                 break
#         else:
#             leader.append(l1[i])               
#     return leader
# print(find_leader(l1))

#-------------------------------------------

# wap to increase and decrease height of a given element based on the k th value 
# and then display the difference of maximum and minimum element.


l1 = [1,4,6,2,5,7,3]
k = 3
result = []
for i in l1:
    if i<k:
        result.append(i+k)
    elif i>k:
        result.append(i-k)
    else:
        result.append(i)
print(result)
# for i in range(len(result)-1):
#     if result[i]<result[i+1]:
#         maxval = result[i+1]
#     else:
#         minval = result[i]
print(max(result) - min(result))

#----------------------------------------------

# wap to display the maximum sub list based on the k th value

