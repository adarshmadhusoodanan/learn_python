
#swapping of two numbers

# a= 10
# b= 20
# print( a, b)
# a,b = b,a    # without using third variable
# temp = a   # using third variable
# a = b
# b = temp
# print( a, b)

#---------------------------------------------------

# WAP to find factorial of given number 

#algo

# take the input
# iterate using for loop
# till the given input

# starting from 1

# n = int(input("enter number: "))
# fact =1
# for i in range(1,n+1):
#     fact = fact*i
#     print(f"{fact} x {i}")
# print(fact)

# print("using while loop")
# i=1
# fact=1
# while i<n+1:
#     fact= fact*i
#     i+=1
# print(fact)

#-----------------------------------------------------------

# WAP to check the given number is a amstrong number or not

# take a number
# extract last digit from given numbers 
# find the cube if the numbers
# add the res to a local variable
# delete the last number from the given number

# num = int(input(" enter a number : "))
# temp = num
# res =0
# while num!=0:
#     rem = num%10
#     res = res+ rem**3
#     num = num//10

# if res ==temp:
#     print("amstrong number")
# else:
#     print("not amstrong number")


# num = int(input(" enter a number : "))
# len = len(str(num))
# temp = num
# res =0
# while num!=0:
#     rem = num%10
#     res = res+ rem**3
#     num = num//10

# if res ==temp:
#     print("amstrong number")
# else:
#     print("not amstrong number")

#---------------------------------------------------

# WAP TO CHECK the given number is strong or not

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact*i
        # print(f"{fact} x {i}")
    return fact


num = int(input(" enter number "))
temp = num
res=0
while num!=0:
    rem = num%10
    res += factorial(rem)
    num = num//10
if res == temp:
    print("strong number")
else:
    print("not strong number")


#---------------------------------------------------

# WAP to check perfect number 

# take a input value 
# run a loop besed if given numbers
# check its factor whether is completely divisible or not 
# if it is divisible make a sum of it 
# compare the result with given input value



# n= int(input("enter num: "))
# res =0
# for i in range(1,n):
#     if n%i == 0:
#         res = res+i

# if n == res:
#     print("perfect number")
# else:
#     print("not perfect number")


#---------------------------------------------------

# WAP give all the perfet number in the given range

# WAP to find sum of a given number 

# num = int(input(" enter a number : "))
# sum = 0 
# while num!=0:
#     rem = num%10
#     sum+=rem
#     num//=10
# print(sum)


#---------------------------------------------------

# WAP to reverse the given number

# num = int(input("enter a nubmer"))

# while num!=0:
#     rem = num%10
#     print(rem, end="")
#     num //= 10

# res = 0 
# while num!=0:
#     rem = num%10
#     res = res*10 + rem
#     num //= 10
# print(res)


#---------------------------------------------------

# CHECK the given number is special number or not  
# s,p = 0,1
# temp = num
# while num!=0:
#     rem = num%10
#     s = s+rem
#     p = p* rem

#     num //= 10
# if temp == s+p:
#     print("special number")
# else:
#     print("not special number")


#---------------------------------------------------

# program to check given number us a dusarium number or not
# l = len(str(num))
# temp = num
# sum = 0 
# while num!=0:

#     rem = num%10
#     sum += rem**l
#     l -= 1
#     num//=10
# print(sum)

# if temp == sum:
#     print("it is disarium number")
# else:
#     print("no it is not")


#---------------------------------------------------

# find the frequency of the number
# d={}
# while num!=0:
#     rem = num % 10
#     if rem not in d:
#         d[rem]=1
#     else:
#         d[rem]+=1
#     num//=10

# print(d)
# for k,v in d.items():
#     print(k,"->",v)


#---------------------------------------------------

# program to check automorphic number or not




#---------------------------------------------------

# program to check the given number is palindrome or not

# temp = num
# res = 0
# while num!=0:
#     rem = num%10
#     res = res * 10 +rem
#     num = num // 10

# if temp == res:
#     print("palindrome")
# else:
#     print("not palindrome")


#---------------------------------------------------

# program to check the given number is evil or odius number 

# res=0
# temp = 1
# count = 0
# while num != 0:
#     rem = num % 2
#     res = res + temp * rem
#     if rem == 1:
#         count+=1
#     num = num // 2
#     temp = temp * 10
# print(res)

# count = 0
# while res!=0:
#     binary = res%10
#     if binary == 1:
#         count +=1
#     res = res//10

# if count%2 == 0:
#     print("evil number")
# else:
#     print("odius number")


#---------------------------------------------------

# WAP to shift all odd number to the first place and even numbers to the last place in agiven number

# temp = 1
# res = 0 
# while num != 0: 78
#     rem = num % 10
#     if rem%2 !=0:
#         res = res + temp * rem
#         temp = temp*10
#         num = num // 10
#     else:
#         num = num * 10 + rem
#         print(num)
# print(res)


#---------------------------------------------------

# wAp TO check the number is prime or not

# if num>1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("prime number")
# else:
#     print("not prime number")


#----------------------------------------------------------------------------------

# to find a prime factors of the number

# def prime_factors(num):
    # factor = 2
    # while num!= 1:
    #     if num% factor == 0:
    #         print(factor, end=" ")
    #         num = num // factor
    #     else:
    #         factor = factor+1
    
# prime_factors(num)


# enter a nubmer12
# 2 2 3 

#---------------------------------------------------

# program to check the given number is zuker man number or not
# - it is a number which is completely divisible by its product of a given number
# - input 24
# - 2 * 4 = 8
# 24% 8 == 0



# def zuker_man(num):
#     temp = num
#     res = 1
#     while num != 0:
#         rem = num % 10
#         res = res * rem
#         num = num//10
#     if temp % res ==0:
#         print("zuker man number")
#     else: 
#         print("not zukerman number")

# zuker_man(num)


#---------------------------------------------------
    
# program to check given number is a smith number

# def digit_sum(num):
#     sum=0
#     while num !=0:
#         rem = num%10
#         sum += rem
#         num = num//10
#     print("digit sum:  ",sum)
#     return sum

# def smith(num):
#     factor = 2
#     sum1 = 0
 
#     while num!= 1:
#         if num% factor == 0:
#             sum1 += digit_sum(factor)
#             num = num // factor
#         else:
#             factor = factor+1
#     print("PRIME FACTOR SUM  ",sum1)

#     if sum == sum1:
#         print("smith number")
#     else:
#         print("not smith number")

# smith(num)
# correct code

# def sum_of_num(num):
#     res = 0
#     while num !=0:
#         rem = num%10
#         res = res + rem
#         num = num // 10
#     return res

# def prime_fators(num):
#     factors = []
#     factor = 2
#     while num != 1:
#         if num % factor == 0:
#             factors.append(factor)
#             num = num // factor
#         else:
#             factor = factor + 1
#     return factors


# res1 = sum_of_num(num)
# res2 = prime_fators(num)

# print(res1, res2)
# sum = 0 
# for i in res2:
#     sum += sum_of_num(i)

# if sum == res1:
#     print("it is smith number")
# else:
#     print("it is not smith number")


#---------------------------------------------------


# wAp to check the given number is ugly number or not

# it is a number which includes the prime factors like 2 or 3 or 5 only,  if it is getting any other prime factor then it is not an ugly number
# number which contains only the prime factors=> 2 3 5

# def prime_fators(num):
#     factors = []
#     factor = 2
#     while num != 1:
#         if num % factor == 0:
#             factors.append(factor)
#             num = num // factor
#         else:
#             factor = factor + 1
#     return factors


# res = prime_fators(num)
# print(res)
# for i in res:
#     if i == 2 and i == 3 and i == 5:
#         print("ugly number")
#         break
#     else:
#         print(" not ugly number")
#         break
    


#---------------------------------------------------