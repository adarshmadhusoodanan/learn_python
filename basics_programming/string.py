# string based program

# s1 = "python coding is awesome"

# o = 0
# c = 0

# for i in s1:
#     if i == " ":
#         continue

#     elif i in "aeiouAEIOU":
#         o += 1
#     else:
#         c += 1

# print("consonets count",c)
# print("vowels count",o)


#==========================================

# s1 = "AfghjkASSSFK"
# lower = 0
# upper = 0
# for i in s1:
#     if i>= 'a' and i<= 'z':
#         lower += 1
#     elif i>= 'A' and i<= 'Z':
#         upper += 1

# print("uppercase count: ", upper)
# print("lowercase count: ", lower)

# s1 = "Ad"
# s2 = ""
# print(s1)
# for i in s1:
#     if i>= 'a' and i<= 'z':     
#         s2 += chr(ord(i)-32)
#     elif i>= 'A' and i<= 'Z':   
#         s2 += chr(ord(i)+32)


# print(s2)

#===========================================

# wap to convert camel case character to snake case character

# s1 = "Dont Be Stupid Be An Idiot"
# s2 = ""
# print(s1)
# for i in s1:
#     if i>= 'A' and i<= 'Z':   
#         s2 += chr(ord(i)+32)
#     elif i == " ":
#         s2 += "_"
#     else:
#         s2 += i
# print(s2)

# convert the snake case to camal case

# s3 = ""
# s3 += chr(ord(s2[0]) - 32)
# for i in range(1,len(s2)):
#     if s2[i] == "_":
#         s3+= " "    
#     elif s3[i-1] == "_":
#         s3 += chr(ord(s2[i]) - 32)
#     else:
#         s3 += s2[i]
    
# print(s3)  # bug is there

#=================================================

# wap to check the given string is a palindrom string or not

# def check_palindrom(s):
#     return s==s[::-1]

# s = "malayalam"

# if check_palindrom(s):
#     print("palindrome")
# else:
#     print("not palindrome")

# another

# s = "malayalam"
# j = len(s) - 1

# for i in range(len(s)):
#     if s[i] != s[j]:
#         print("string not palindrome")
#         break
#     j -= 1
# else:
#     print(" palindrome")

#========================================
# s="rtyufghuigbik"
# d={}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# for k,v in d.items():
#     print(f"{k}-> {v}")


#=====================================

# wap to check the given string is a mirror string or not

# def mirror_string(s):
#     mirror_char = {'A','H','I','M','O','T','U','V','W','X','Y','b','d','p','q','i','o','v','w','x'}
#     for char in s:
#         if char.upper() not in mirror_char:
#             return False
        
#     return s 
#     # return s == s[::-1]  # optional to check palindromic nature

# s = "aha"
# if mirror_string(s):
#     print(f"{s} is a mirror string")
# else:
#     print(f"{s} is not a mirror string")

#===============================================================

# s = "if you always do what you always did you will always get what you always got"
# d= {}
# words = s.split(" ")
# for i in range(len(words)):
#     if words[i] not in d:
#         d[words[i]] = [i]     # we can asign like this to get the list       
#     else:      
#         d[words[i]] += [i]

# print(d)
# {'if': [0], 'you': [1, 5, 8, 13], 'always': [2, 6, 10, 14], 'do': [3], 'what': [4, 12], 'did': [7], 'will': [9], 'get': [11], 'got': [15]}

#====================================================================

#wap check the given input string can be a strong password or not
# it should contains minimum 8 characters maximum 13 character
# it should contains one up case one lower case one special case one numeric
# if it is not satisfing give output accordingly
# this string should not start with the numerical value

# password = "8asswordet"
# up,lp,nc,sc =0,0,0,0
# if len(password)>=8 and len(password)<=30:
#     if password[0] >= '0' and password[0] <='9':
#         print("first the letter shouldn't be number")
#     else:
#         for i in range(len(password)):
#             if password[i] >= 'A' and password[i]<='Z':
#                 up +=1
#             elif password[i] >= 'a' and password[i]<='z':
#                 lp +=1
#             elif password[i] >= '0' and password[i]<='9':
#                 nc +=1
#             else:
#                 sc+=1

#         if up>=1 and lp>=1 and nc>=1 and sc>=1:
#             print("correct password")
#         else:
#             print("password should contain atleast one uppercase,lowercase,number,special characters")
# else:
#     print("it should contain minimum 8 and maximum 13 character")

#===============================================================================

# s = "pneumonuttramicroscopicsilicvolcanoconoria it refers to the lungs details caure by silica dust"


# n = int(input("enter a number: "))

# new_S = s.replace(" ","")
# for i in range(0,len(new_S),n):
#     print(new_S[:i+n-1], end="\n")


#===========================================



# wap to convert the given string into modified string based on given condition
# check len of string if it is even check ascii value of each character
# if it is even then add 4 to it and again  to respective ascii character
# if characters ascii id odd add 3 to it and convert it into respective ascii character
# if len is odd add +6 to even ascii value and +5 to odd ascii value

# s = "hello world"
# n = len(s)
# new_s = ""

# if n % 2 ==0:
#     for i in s:
#         if ord(i) % 2 == 0:
#             new_s += chr(ord(i)+4)
#         else:
#             new_s += chr(ord(i)+3)
# else:
#     for i in s:
#         if ord(i) % 2 == 0:
#             new_s += chr(ord(i)+6)
#         else:
#             new_s += chr(ord(i)+5)

# print(new_s)

#=================================================
# s1='pneumonultramicroscopicsiliconvalcanic it refers to disease'
# # n=int(input("enter a number "))
# # for i in range(0,len(s1)-1,n):
# #     for i in range(i,i+6):
# #         print(s1[i],end="")
# #     print()

# s3=''
# div=math.ceil(math.sqrt(len(s2)))
# cnt=0
# for i in s2:
#     if cnt==div:
#         s3+='\n'
#         cnt=0
#     s3+=i
#     cnt+=i
# print(i)

# # ----------------------------------------------------------------------------------
# # convert given string into modified string based on given condition 
# # check len of string if it is even check ascii value of each character if ascii is even 
# # add +4 to it and again to respective ascii character 
# # if characters ascii is odd add +3 to it and convert it into respective ascii character 
# # if len is odd add +6 to even ascii value and add +5 to odd ascii value

# s='Python$ Coding@ is Awesome#'
# s2=''

# if len(s)%2==0:
#     for i in s:
#         if ord(i)%2==0:
#             i1=ord(i)+4
#         else:
#             i1=ord(i)+3
#         s2+=chr(i1)
# else:
#     for i in s:
#         if ord(i)%2==0:
#             i1=ord(i)+6
#         else:
#             i1=ord(i)+5
#         s2+=chr(i1)

# print(s2)
# V~zntt*&HtjntlF&nx&F|jxtrj(

# ---------------------------------------------------------

# # compress given string to get desired output
# s1='aaaabbbccccddddeeeefggggg'
# # s2=''
# # d={}
# # for i in s1:
# #     if i not in d:
# #         d[i]=1
# #     else:
# #         d[i]+=1
# # for k,v in d.items():
# #     s2+=str(k)+str(v)
# # print(s2)
# s1='aaaabbbccccddddeeeefggggg'
# s3=''
# c=1
# for i in range(0,len(s1)-1):
#     if s1[i]==s1[i+1]:
#         c+=1
#     else:
#         s3+=s1[i]+str(c)
#         c=1
# s3+=s1[-1] +str(c)    
# print(s3)
# # a4b3c4d4e4f1g5

# ----------------------------------------------

# s1='Pyspiders'
# if len(s1)%2!=0:
#     for i in range(len(s1)):
#         for j in range(len(s1)):
#             if i==len(s1)//2:
#                 print(s1[j],end=" ")
#             elif j==len(s1)//2:
#                 print(s1[i],end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# -------------------------------------------------------
# wap to print the pattern using the given string
# s1='Pyspiders'
# n=int(input('enter number'))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(s1[k],end=" ")
#     print()

#================================================
# wap to print the pattern using user inputs string and the integer

# s = input("enter a string: ")
# n = int(input("enter number"))
# val = 0
# if n> 2:
#     for i in range(n):
#         for j in range(n):
#             print(s[val], end=" ")
#             val += 1
#             if val == len(s):
#                 val = 0 
#         print()
# else:
#     print("enter value greater than 2")

#=================================================

# check the given substring is present in the given string and give the count

# s1 = 'aadcdaaaabcdadadbcdaabcdabcd'

# sub_s = 'bcd'
# check_s =''
# count = 0

# for char in s1:
#     if char in sub_s:
#         check_s += char
#         if check_s == sub_s:
#             count += 1
#             print(count)
#             check_s = ''
#     else:
#         check_s = ''

# print(sub_s, "is present", count, "times")

# count = 0
# for i in range(len(s1)):
#     if s1[i:i+len(sub_s)] == sub_s:
#         count += 1

# print(count)

#=============================================
# def get_vowel_and_consonet_count(word):
#     vowels = 0
#     consonets = 0

#     for char in word:
#         if char in "aeiouAEIOU":
#             vowels += 1
#         else:
#             consonets += 1

#     return [vowels,consonets]

# s1 = "the most voilent man called one man the most voilent"
# words = s1.split(" ")
# d={}
# for word in words:
#     d[word] = get_vowel_and_consonet_count(word)

# for k,v in d.items():
#     print(f"{k} : {v}")


#op:
# the : [1, 2]
# most : [1, 3]
# voilent : [3, 4]
# man : [1, 2]
# called : [2, 4]
# one : [2, 1]

#=================================


# wap to print all possible substrings of the given string

# s1 ="a"
# sub_s = ""

# for i in range(len(s1)):
#     sub_s += s1[i]
#     print(sub_s)
#     for j in range(i+1, len(s1)):
#         sub_s += s1[j]
#         print(sub_s)   
#     sub_s = ""

#--------------------------------

# wap program to all the anagram string to an individual list

# s1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

# d = {}
# for word in s1:
#     sorted_word = ''.join(sorted(word))
#     if sorted_word not in d:
#         d[sorted_word] = [word]
#     else:
#         d[sorted_word].append(word)

# list_s = []
# for k,v in d.items():
#     list_s.append(v)
# print(list_s)

#------------------------------------------------------

# wap to make the sum of only integer values present in a dictionary

# d= {
#     "a": "one",
#     2 : 100,
#     3 : "python"
# }

# sum =0
# for k,v in d.items():
#     if type(k) == int:
#         sum +=k
#     if type(v) == int:
#         sum += v
# print(sum)

#=====================================

# wap to encode and decode the numeric string based on the morse code
# when program is executed it should ask two options

# 1. encode 
# 1. decode

# if it is encode it should accept numeric string convert to morse code values 
# if it is decode need to accept morse code as an input and convert to numeric string

# morse_code = {
#     "0" : "-----",
#     "1" : ".----",
#     "2" : "..---",
#     "3" : "...--",
#     "4" : "....-",
#     "5" : ".....",
#     "6" : "-....",
#     "7" : "--...",
#     "8" : "---..",
#     "9" : "----."
# }

# def encode_morse_code(msg):
#     for i in msg:
#         if ord(i)>=48 and ord(i)<=57:
#             print(morse_code[i], end="")


# def decode_morse_code(user_msg):
#     if len(user_msg)%5 != 0:
#         print("enter proper morse code")
#         return
#     value = []
#     n = 0
#     for i in range(len(user_msg)):
#         value.append(user_msg[n:n+5])
#         n = n+5
#         if n == len(user_msg):
#             break
#     for i in value:
#         for k,v in morse_code.items():
#             if i == v:
#                 print(k, end="")


# yes =True
# while yes:
#     choice = int(input("\n*****************\nselect one\n1. encode\n2. decode\n for exit type 0\n -> "))
#     if choice == 1:
#         msg = input(" enter message : ")
#         encode_morse_code(msg)
#     elif choice == 2:
#         msg = input(" enter message : ")
#         decode_morse_code(msg)
#     elif choice == 0:
#         yes= False
#     else:
#         print("enter number 1,2")
        

#==============================

# wap to build a vending machine
# it should contain the dictionary of product along with its price


# create a class for vending machine during the object creation it should accept the dictionary of products
# it should contains a methods like add card, display card, update card and the bill summary.



# class Vending_Machine:

#     def __init__(self,**products):
#         self.products = products
#         self.cart = {}
#         self.bill = {}

#     def add_cart(self,product,qty):
#         if product in self.products.keys():

#             self.cart[product] = qty

#     def display_cart(self):

#         # print("product details")
#         # for k,v in self.products.items():
#         #     print(k, " : ",v)
#         if len(self.cart) == 0:
#             print("cart is empty")
#         else:
#             print("cart items")
#             for k,v in self.cart.items():
#                 print(k," : ",v)

            
#     def update_crat(self,product,qty):
#         choice = int(input("select options\n 1. update item \n 2. delete item\n"))
#         if choice == 1:

#             if product in self.cart.keys():
#                 self.cart[product] = qty
#             else:
#                 print("item is not in cart")
#         elif choice == 2:
#             if product in self.cart.keys():
#                 del self.cart[product]
#         else:
#             print("enter a valid options")

#     def bill_summary(self):
        
#         print("********************* bill summary *****************\n")
#         print("product\t:\tprice\t*\tqty\t=\ttotal")
#         print("----------------------------------------------------")
#         for product,qty in self.cart.items():
#             self.bill[product] = qty* self.products[product]
#         for product,total in self.bill.items():
#             print(f"{product}\t:\t{self.products[product]}\t*\t{qty}\t=\t{total}")
        

# vm = Vending_Machine(chikki=5,kitkat=20,cupcake=10,oreo=30)

# vm.add_cart("chikki",3 )
# vm.add_cart("kitkat",10 )
# vm.add_cart("oreo",10 )

# vm.display_cart()

# print()

# # vm.update_crat("chikki",6789)

# vm.display_cart()
# print()
# vm.bill_summary()

#===============================================

# create a class trian check list and it should contains then methods
# get_train_name
# get_total_price
# get_days_of_run
# 
# take the train details like each train details should be in the form of dict 
# and all the train all the train should be in the form of list 

class Train:
    global train_list
                     
    def get_train_name(self, train_no):
        for train in train_list:
            if train['train_no'] == train_no:
                return train['train_name']
        return "Train not found"
    
    def get_total_price(self, train_no, general_seat, sleeper_seat, ac_seat):
        for train in train_list:
            if train['train_no'] == train_no:
                total_price = (general_seat * train['general_seat_price']+ sleeper_seat * train['sleeper_seat_price'] + ac_seat * train['ac_seat_price'])
                return total_price
        return "no train found"

    def get_day_of_run(self,day):
        for train in train_list:
            # print(train['days_of_run'])
            if day in train['days_of_run']:
                print( f"{train['train_name']} runs on {day}\n")
        
        else:
            print(f"no train run on {day}\n")

train_list = [{'train_no': '12345', 'train_name': 'Express Train', 'general_seat_price': 100, 'sleeper_seat_price': 300, 'ac_seat_price': 500, 'days_of_run': ['Monday', 'Wednesday', 'Friday']},
                           {'train_no': '67890', 'train_name': 'Superfast Train', 'general_seat_price': 150, 'sleeper_seat_price': 400, 'ac_seat_price': 600, 'days_of_run': ['Monday','Tuesday', 'Thursday', 'Saturday']},
        ]

t = Train()

print("train name\t",t.get_train_name('12345'))
print("total price\t",t.get_total_price('12345', 2, 1, 0))
t.get_day_of_run("sunday")