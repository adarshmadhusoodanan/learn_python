# Python String Datatype
# String is a collection which is ordered and unchangeable. Allows duplicate members.
# String are written with single, double or triple quotes

#------------------------------------------------------------------------------------------------------------------------------------------------

#                   defining string

# s1='hello'                                            'hello' <class 'str'>               define with single quotes
# s1="hello"                                            'hello' <class 'str'>               define with double quotes
# s1='''hello'''                                        'hello' <class 'str'>               define with triple quotes
# s1="""hello"""                                        'hello' <class 'str'>               define with triple quotes
# s1=''                                                 '' <class 'str'>                    empty string


# s1="hello world"                                     'hello world' <class 'str'>           string with space
# print(len(s1))                                        op: 11                               length of string

# s1='''hello
# world'''
# print(s1)                                             op: hello
#                                                       world
# print(len(s1))                                        op: 12                               length of string with newline character



# note: 
#       raw string is also there
# s1=r'hello\nworld'
# print(s1)                                             op: hello\nworld
# print(len(s1))                                        op: 13                               length of raw string
#------------------------------------------------------------------------------------------------------------------------------------------------


# property of string

            # string can be homogenous or heterogenous
# s1='hello'                                            'hello' <class 'str'>               homogenous collection
# s1='hello123'                                         'hello123' <class 'str'>            heter
# s1='hello@123'                                        'hello@123' <class 'str'>           heter
# s1='hello 123'                                       'hello 123' <class 'str'>           heter

            # string can have duplicate elements    
# s1='hellohello'                                      'hellohello' <class 'str'>          have duplicate elements
# s1='hello'                                            'hello' <class 'str'>               no duplicate elements

            # string are ordered collection
# s1='hello'                                            'hello' <class 'str'>               ordered collection
# print(s1[0])                                          op: h
# print(s1[4])                                          op: o
# print(s1[-1])                                         op: o
# print(s1[-5])                                         op: h

            # string are immutable
# s1='hello'
# s1[0]='H'                                            TypeError: 'str' object does not support item assignment
# print(s1)                                            op: hello
# s1='Hello'                                           #reassigned
# print(s1)                                            op: Hello

            # string support indexing and slicing   
# s1='hello'
# print(s1[1])                                         op: e
# print(s1[-1])                                        op: o
# print(s1[1:4])                                       op: ell
# print(s1[-4:-1])                                     op: ell
# print(s1[::2])                                       op: hlo
# print(s1[::-1])                                      op: olleh
# print(s1[1::2])                                      op: el
# print(s1[-1::-2])                                    op: olh

            # string support concatenation and repetition
# s1='hello'
# s2='world'
# print(s1+s2)                                        op: helloworld <class 'str'> concatenation
# print(s1*3)                                         op: hellohellohello <class 'str'> repetition
# print((s1+s2)*3)                                   op: helloworldhelloworldhelloworld <class 'str'> concatenation and repetition
# print(s1*3+s2*2)                                   op: hellohellohelloworldworld <class 'str'> repetition and concatenation
# print(s1*0)                                        op: '' <class 'str'> empty string
# print(s1*0+s2)                                    op: world <class 'str'> concatenation with empty string
# print(s1*3.5)                                     op: TypeError: can't multiply sequence by non-int of type 'float'

# note:
#       string comprehension is also there

# s1=''.join([x for x in 'hello'])                     op: hello <class 'str'>
# print(s1,type(s1))                                   op: hello <class 'str'>
# s1=''.join([x for x in range(5)])                    op: TypeError: sequence item 0: expected str instance, int found
# print(s1,type(s1))                                   op: TypeError: sequence item 0: expected str instance, int found
# s1=''.join([str(x) for x in range(5)])               op: 01234 <class 'str'>
# print(s1,type(s1))                                   op: 01234 <class 'str'>
#------------------------------------------------------------------------------------------------------------------------------------------------

# string built-in functions

            # string.capitalize() -> str
# s1='hello'
# print(s1.capitalize())                               op: Hello <class 'str'>

            # string.count(value, start, end) -> int
# s1='hellohello'
# print(s1.count('l'))                                 op: 4
# print(s1.count('lo'))                                op: 2
# print(s1.count('lo',5))                              op: 1
# print(s1.count('lo',0,5))                            op: 1
# print(s1.count('z'))                                 op: 0

            # string.find(value, start, end) -> int

# s1='hellohello'
# print(s1.find('l'))                                  op: 2
# print(s1.find('lo'))                                 op: 3
# print(s1.find('lo',5))                               op: 8
# print(s1.find('lo',0,5))                             op: 3
# print(s1.find('z'))                                  op: -1       #if substring not found it returns -1

            # string.index(value, start, end) -> int    
# s1='hellohello'
# print(s1.index('l'))                                 op: 2    
# print(s1.index('lo'))                                op: 3
# print(s1.index('lo',5))                              op: 8
# print(s1.index('lo',0,5))                            op: 3
# print(s1.index('z'))                                 op: ValueError: substring not found

            # string.isalnum() -> bool  
# s1='hello123'
# print(s1.isalnum())                                  op: True
# s1='hello@123'
# print(s1.isalnum())                                  op: False
# s1='hello 123'
# print(s1.isalnum())                                  op: False

            # string.isalpha() -> bool
# s1='hello'
# print(s1.isalpha())                                  op: True
# s1='hello123'
# print(s1.isalpha())                                  op: False
# s1='hello@123'
# print(s1.isalpha())                                  op: False        
# s1='hello 123'
# print(s1.isalpha())                                  op: False

            # string.isdigit() -> bool  
# s1='123456'
# print(s1.isdigit())                                  op: True
# s1='hello123'
# print(s1.isdigit())                                  #op: False
# s1='123.456'
# print(s1.isdigit())                                  #op: False
# s1='123 456'          
# print(s1.isdigit())                                  #op: False

            # string.islower() -> bool
# s1='hello'
# print(s1.islower())                                  op: True

# s1='Hello'
# print(s1.islower())                                  op: False

# s1='hello123'
# print(s1.islower())                                  op: True

# s1='hello@123'
# print(s1.islower())                                  op: True

# s1='hello 123'
# print(s1.islower())                                  op: True
# s1='hello world'
# print(s1.islower())                                  op: True
# s1='hello World'
# print(s1.islower())                                  op: False

            # string.isupper() -> bool

# s1='HELLO'
# print(s1.isupper())                                  op: True
# s1='Hello'

# print(s1.isupper())                                  op: False
# s1='HELLO123'
# print(s1.isupper())                                  op: True
# s1='HELLO@123'


# print(s1.isupper())                                  op: True
# s1='HELLO 123'
# print(s1.isupper())                                  op: True
# s1='HELLO WORLD'
# print(s1.isupper())                                  op: True
# s1='HELLO World'
# print(s1.isupper())                                  op: False

            # string.lower() -> str

# s1='Hello@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>
# s1='HELLO@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>
# s1='hello@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>   
# s1='hello@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>

            # string.upper() -> str 

# s1='Hello@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>
# s1='HELLO@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>
# s1='hello@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>
# s1='hello@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>

            # string.replace(old, new, count) -> str    

# s1='hellohello'
# print(s1.replace('l','L'))                          op: heLLoheLLo <class 'str'>
# print(s1.replace('l','L',1))                        op: heLlohello <class 'str'>
# print(s1.replace('lo','LO'))                        op: helLOhelLO <class 'str'>
# print(s1.replace('lo','LO',1))                      op: helLOhello <class 'str'>
# print(s1.replace('z','Z'))                          op: hellohello <class 'str'>

            # string.split(sep=None, maxsplit=-1) -> list   

# s1='hello world'
# print(s1.split())                                   op: ['hello', 'world'] <class 'list'>
# s1='hello,world,python'
# print(s1.split(','))                                op: ['hello', 'world', 'python']
# s1='hello world python programming'
# print(s1.split(' ',2))                              op: ['hello', 'world', 'python programming']
# s1='hello'        
# print(s1.split())                                   op: ['hello']
# s1=''
# print(s1.split())                                   op: []
# s1='hello@world@python@programming'
# print(s1.split('@',2))                              op: ['hello', 'world', '  python@programming']
# s1='hello@world@python@programming'   
# print(s1.split('#'))                               op: ['hello@world@python@programming']

           # string.partition(sep) -> tuple

# partition() method searches for a specified string and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.


# s1='hello world python programming'
# print(s1.partition(' '))                            op: ('hello', ' ', 'world python programming') <class 'tuple'>
# s1='hello@world@python@programming'
# print(s1.partition('@'))                            op: ('hello', '@', 'world@python@programming') <class 'tuple'>

# s1='hello world python programming'
# print(s1.partition('#'))                            #   op: ('hello world python programming', '', '') <class 'tuple'>

# s1='hello'
# print(s1.partition(' '))                            op: ('hello', '', '') <class 'tuple'>

# s1=''
# print(s1.partition(' '))                            op: ('', '', '') <class 'tuple

# s1 = 'hello@world@python@programming'
# print(s1.partition('rl'))                           # op: ('hello@wo', 'rl', 'd@python@programming') <class 'tuple'>                 

# s1 = 'hello@world@python@programming'
# print(s1.partition('pt'))                             # op: ('hello@world@python@programming', '', '') <class 'tuple'>


#                       

#------------------------------------------------------------------------------------------------------------------------------------------------



