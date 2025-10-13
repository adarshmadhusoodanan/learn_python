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
# print(s1)                                             #op: hello\nworld
# print(len(s1))                                        #op: 13                               length of raw string
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
# print((s1+s2)*3)                                    op: helloworldhelloworldhelloworld <class 'str'> concatenation and repetition
# print(s1*3+s2*2)                                    op: hellohellohelloworldworld <class 'str'> repetition and concatenation
# print(s1*0)                                         op: '' <class 'str'> empty string
# print(s1*0+s2)                                      op: world <class 'str'> concatenation with empty string
# print(s1*3.5)                                       op: TypeError: can't multiply sequence by non-int of type 'float'

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

            # 1. string.lower() -> str

# s1='Hello@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>
# s1='HELLO@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>
# s1='hello@123'
# print(s1.lower())                                   op: hello@123 <class 'str'>   
# s1='ß'
# print(s1.lower())                                   op: ß <class 'str'>

            # 2. string.upper() -> str 

# s1='Hello@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>
# s1='HELLO@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>
# s1='hello@123'
# print(s1.upper())                                   op: HELLO@123 <class 'str'>

            # 3. string.swapcase() -> str

# s1='HELlo@123'
# print(s1.swapcase())                                op: helLO@123 <class 'str>

            # 4. string.capitalize() -> str

# s1='hello@o12'
# print(s1.capitalize())                              op: Hello@o12 <class 'str'>

            # 5. string.title() -> str

# s1='hello1 world@ python123program!ming '
# print(s1.title())                                   op:Hello1 World@ Python123Program!Ming 

            # 6. string.casefold()

# s1='HELlo@123'
# print(s1.casefold())                                op: hello@123 <class 'str'>
# s1='hello@123'
# print(s1.casefold())                                op: hello@o12 <class 'str'>
# s1='ß'
# print(s1.casefold())                                op: ss <class 'str'>

# difference between lower(),casefold()    

            # 7. string.islower() -> bool

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

            # 8. string.isupper() -> bool

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

            # 9. string.istitle() -> bool
# s1='Adarsh'
# print(s1.istitle())                                 op: True
# s1='Keerthana Gowd@'
# print(s1.istitle())                                 op: True
# s1='Ad@Sh M@Dhu'
# print(s1.istitle())                                 op: True
# s1='Ad@rsh M@dhu'
# print(s1.istitle())                                 op: False


            # 10. string.isalnum() -> bool  

# s1='hello123'
# print(s1.isalnum())                                  op: True
# s1='hello@123'
# print(s1.isalnum())                                  op: False
# s1='hello 123'
# print(s1.isalnum())                                  op: False

            # 11. string.isalpha() -> bool

# s1='hello'
# print(s1.isalpha())                                  op: True
# s1='hello123'
# print(s1.isalpha())                                  op: False
# s1='hello@123'
# print(s1.isalpha())                                  op: False        
# s1='hello 123'
# print(s1.isalpha())                                  op: False

            # 12. string.isdigit() -> bool  

# s1='123456'
# print(s1.isdigit())                                  op: True
# s1='hello123'
# print(s1.isdigit())                                  op: False
# s1='123.456'
# print(s1.isdigit())                                  op: False
# s1='123 456'          
# print(s1.isdigit())                                  op: False
# s1='²³¼½¾'                              
# print(s1.isdigit())                                  op: False
# s1='²³'
# print(s1.isdigit())                                  op: True
# s1='Ⅷ'
# print(s1.isdigit())                                  op: False
# s1="०१२३४५६७८९"
# print(s1.isdigit())                                  op: True

            # 13. string.isnumeric() -> bool

# s1='123456'
# print(s1.isnumeric())                                op: True
# s1='hello123'
# print(s1.isnumeric())                                op: False
# s1='123.456'
# print(s1.isnumeric())                                op: False
# s1='123 456'          
# print(s1.isnumeric())                                op: False
# s1='123*123'
# print(s1.isnumeric())                                op: AttributeError: 'int' object has no attribute 'isnumeric'
# s1='²³'
# print(s1.isnumeric())                                op: True
# s1='²³¼½¾' 
# print(s1.isnumeric())                                op: True
# s1='Ⅷ'
# print(s1.isnumeric())                                op: True
# s1="०१२३४५६७८९"
# print(s1.isnumeric())                                op: True
 
            # 14. string.isdecimal() -> bool

# s1='123456'
# print(s1.isdecimal())                                op: True
# s1='hello123'
# print(s1.isdecimal())                                op: False    
# s1='123.456'
# print(s1.isdecimal())                                op: False
# s1='123 456'          
# print(s1.isdecimal())                                op: False
# s1='²³¼½¾'                              
# print(s1.isdecimal())                                op: False
# s1='²³'
# print(s1.isdecimal())                                op: False
# s1='Ⅷ'
# print(s1.isdecimal())                                op: False
# s1="०१२३४५६७८९"
# print(s1.isdecimal())                                op: True

# `isdecimal()` accepts only standard decimal digits (including non-Latin ones), `isdigit()` also accepts superscripts and subscripts, and `isnumeric()` is the most inclusive, additionally recognizing fractions, Roman numerals, and other numeric characters.

            # 15. string.isidentifier() -> bool

# s1='hello123'
# print(s1.isidentifier())                             op: True
# s1='123hello'
# print(s1.isidentifier())                             op: False
# s1='else'
# print(s1.isidentifier())                             op: True  <it is reserved identifier in python>
# s1='$hello'
# print(s1.isidentifier())                             op: False
# s1='_hello'
# print(s1.isidentifier())                             op: True

            # 16. string.isspace() -> bool

# s1=" "
# print(s1.isspace())                                  op: True
# s1=""
# print(s1.isspace())                                  op: False
# s1=" hello "
# print(s1.isspace())                                  op: False

            # 17. string.isascii() -> bool

# s1='hello'
# print(s1.isascii())                                  op: True
# s1='$@#123a'
# print(s1.isascii())                                  op: True
# s1='₹'
# print(s1.isascii())                                  op: False
# s1='🤗🫠'
# print(s1.isascii())                                  op: False

            # 18. string.isprintable() -> bool


# print(s1.isupper())                                  op: True
# s1='HELLO 123'
# print(s1.isupper())                                  op: True
# s1='HELLO WORLD'
# print(s1.isupper())                                  op: True
# s1='HELLO World'
# print(s1.isupper())                                  op: False
                 
                
            # 19. string.count(value, start, end) -> int

# s1='hellohello'
# print(s1.count('l'))                                 op: 4
# print(s1.count('lo'))                                op: 2
# print(s1.count('lo',5))                              op: 1
# print(s1.count('lo',0,5))                            op: 1
# print(s1.count('z'))                                 op: 0

            # 20. string.find(value, start, end) -> int

# s1='hellohello'
# print(s1.find('l'))                                  op: 2
# print(s1.find('lo'))                                 op: 3
# print(s1.find('lo',5))                               op: 8
# print(s1.find('lo',0,5))                             op: 3
# print(s1.find('z'))                                  op: -1

            # 21. string.index(value, start, end) -> int    

# s1='hellohello'
# print(s1.index('l'))                                 op: 2    
# print(s1.index('lo'))                                op: 3
# print(s1.index('lo',5))                              op: 8
# print(s1.index('lo',0,5))                            op: 3
# print(s1.index('z'))                                 op: ValueError: substring not found

# difference between find() and index() method is that find() method returns -1 if the value is not found where as index() method raises ValueError if the value is not found
            
            # 22. string.rfind(value, start, end) -> int

# s1='adarsh madhu'
# print(s1.rfind('a'))                                 op: 8
# print(s1.rfind('a',0,8))                             op: 2
# print(s1.rfind('z'))                                 op: -1

            # 23. string.rindex(value, start, end) -> int

# s1='adarsh madhu'
# print(s1.rindex('a'))                                op:8
# print(s1.rindex('a',0,8))                            op:2
# print(s1.rindex('k'))                                op:ValueError: substring not found

            # 24. string.center(width,fillchar:space(default)) -> str

# s1='Keerthi'
# print(s1.center(9))                                  op:  Keerthi 
# print(s1.center(10,'*'))                             op:*Keerthi**   
# s1='adarsh'
# print(s1.center(10,'-'))                             op:--adarsh-- 
# print(s1.center(9,'*'))                              op: **adarsh*

            # 25. string.ljust(width,fillchar:space(default)) -> str
# s1="Keerthi"
# print(s1.ljust(10))                                  op: Keerthi   .
# print(s1.ljust(9,'*'))                               op: Keerthi**
# s1='Adarsh'
# print(s1.ljust(10,'-'))                              op: Adarsh----

            # 26. string.rjust(width,fillchar:space(default)) -> str

# s1="Keerthi"
# print(s1.rjust(10))                                  op:    Keerthi
# print(s1.rjust(9,'*'))                               op: **Keerthi
# s1='Adarsh'
# print(s1.rjust(10,'-'))                              op: ----Adarsh

            # 27. string.endswith(suffix,start:0,end:len(str)) -> bool

# s1='adarsh'
# print(s1.endswith('h'))                             op: True
# print(s1.endswith('a',0,3))                         op: True
# print(s1.endswith('H'))                             op: False
# print(s1.endswith('sh'))                            op: True
# print(s1.endswith('ar',0,4))                        op: True

            # 28. string.startswith(prefix,start:0,end:len(str))

# s1='keerthi'
# print(s1.startswith('k'))                           op: True
# print(s1.startswith('e',2))                         op: True
# print(s1.startswith('ee',1,7))                      op: True
# print(s1.startswith('a'))                           op: False

            # 29. string.maketrans(x,y) -> dict

# s1='adarsh'
# print(s1.maketrans('ar','AR'))                       op: {97: 65, 114: 82}
# print(s1.maketrans('ar','dar'))                      op: ValueError: the first two maketrans arguments must have equal length
# print(s1.maketrans('a','A'))                         op: {97: 65}
# print(s1.maketrans('ki','ad'))                       op: {107: 97, 105: 100}

            # 30. string.translate(translation_table) -> str

# s1='keerthi'
# s2=s1.maketrans('ki','ad')
# res=s1.translate(s2)
# print(res)                                           op: aeerthd
# s2=s1.maketrans('kd','AD')
# res=s1.translate(s2)
# print(res)                                           op: keerthi
# s2=s1.maketrans('e','i')
# res=s1.translate(s2)
# print(res)                                           op: kiirthi

            # 31. string.replace(old, new, count) -> str    

# s1='hellohello'
# print(s1.replace('ll','L'))                         op: heLoheLo <class 'str'>
# print(s1.replace('l','L',1))                        op: heLlohello <class 'str'>
# print(s1.replace('lo','LO'))                        op: helLOhelLO <class 'str'>
# print(s1.replace('lo','LO',2))                      op: helLOhelLO <class 'str'>
# print(s1.replace('z','Z'))                          op: hellohello <class 'str'>
 
            # 32. string.split(sep=None, maxsplit=-1) -> list   

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
# print(s1.split('@',2))                              op: ['hello', 'world', 'python@programming']
# s1='hello@world@python@programming'   
# print(s1.split('#'))                                op: ['hello@world@python@programming']

            # 33. string.rsplit(sep,maxsplit)

# s1='hello world welcome to python'
# print(s1.rsplit('l'))                               op: ['he', '', 'o wor', 'd ']
# print(s1.rsplit(' ',2))                             op: ['hello world welcome', 'to', 'python']  
# print(s1.rsplit())                                  op: ['hello', 'world', 'welcome', 'to', 'python']
# print(s1.rsplit('rl'))                              op: ['hello wo', 'd welcome to python']
# print(s1.rsplit(' ',2))                             op: ['hello world welcome', 'to', 'python']
# print(s1.rsplit(2))                                 op: TypeError: must be str or None, not int
# print(s1.rsplit(' ',0))                             op: ['hello world welcome to python']
# s1='hello@world@python@programming'
# print(s1.rsplit('@',2))                             op: ['hello@world', 'python', 'programming'] 

            # 34. string.splitlines(keepends=False) -> list

# s1="hello\n welocome\n to\n programming\n world"
# print(s1.splitlines())                              op: ['hello', ' welocome', ' to', ' programming', ' world']
# print(s1.splitlines(keepends='True'))               op: ['hello\n', ' welocome\n', ' to\n', ' programming\n', ' world']
# print(s1.split("\n"))                               op: ['hello', ' welocome', ' to', ' programming', ' world']
# print(s1.splitlines('\n'))                          op: ['hello\n', ' welocome\n', ' to\n', ' programming\n', ' world']

            # 35. string.partition(separator) -> tuple

# s1="welcome to python world"
# print(s1.partition('to'))                           op: ('welcome ', 'to', ' python world')
# print(s1.partition('python'))                       op: ('welcome to ', 'python', ' world')
# print(s1.partition("I"))                            op: ('welcome to python world', '', '')
# print(s1.partition("welcome"))                      op: ('', 'welcome', ' to python world')
# print(s1.partition('world'))                        op: ('welcome to python ', 'world', '')
# print(s1.partition(" "))                            op: ('welcome', ' ', 'to python world')
# print(s1.partition())                               op: TypeError: str.partition() takes exactly one argument (0 given)

            # 36. string.rpartition(separator) -> tuple

# s1="welcome to python welcome to coding"
# print(s1.rpartition("welcome"))                     op: ('welcome to python ', 'welcome', ' to coding')            
# print(s1.rpartition(" "))                           op: ('welcome to python welcome to', ' ', 'coding')
# print(s1.partition("I"))                            op: ('welcome to python welcome to coding', '', '')
# print(s1.rpartition())                              op: TypeError: str.rpartition() takes exactly one argument (0 given)

            # 37. strinf.zfill(width) -> str
# s1='8153'
# print(s1.zfill(7))                                  op: 0008153
# print(s1.zfill(4))                                  op: 8153
# print(s1.zfill(2))                                  op: 8153
# s1='aba'
# print(s1.zfill(5))                                  op: 00aba

            # 38. string.strip(chars) -> str

# s1="   hello   "
# print(s1.strip())                                    op: hello
# s1="****hell*o***"
# print(s1.strip("*"))                                 op: hell*o
# print(s1.strip("*o"))                                op: hell
# s1="*h*o*ell*o**"
# print(s1.strip('*o'))                                op: h*o*ell
# print(s1.strip('o'))                                 op: *h*o*ell*o**

            # 39. string.lstrip(chars) -> str

# s1="  hello  "
# print(s1.lstrip())                                   op: hello  .
# s1="***hello***"
# print(s1.lstrip('*'))                                op: hello***
# s1="h*hello*"
# print(s1.lstrip("*"))                                op: h*hello*
# print(s1.lstrip('h'))                                op: *hello*
# s1="welcomewelocme to python world"
# print(s1.lstrip('welcome'))                          op: to python world

            # 40. string.rstrip(chars) -> str

# s1="  hello  "
# print(s1.rstrip(" "))                                op:   hello
# s1="***hello***"
# print(s1.rstrip("*"))                                op: ***hello
# s1="h*hello*"
# print(s1.rstrip("*"))                                op: h*hello
# print(s1.rstrip('o'))                                op: h*hello*
# s1="welcome to python worldworld"
# print(s1.rstrip('world'))                            op: welcome to python

            # 41. string.removeprefix(prefix) -> str

# s1="hello"
# print(s1.removeprefix('h'))                          op: ello
# print(s1.removeprefix('hello'))                      op: 
# s1="welcomewelcome to python world"
# print(s1.removeprefix('welcome'))                    op: welcome to python world
# print(s1.removeprefix('to'))                         op: welcomewelcome to python world 

            # 42. string.removesuffix(suffix) -> str

# s1="hello"
# print(s1.removesuffix("o"))                          op: hell
# s1="welcome to python worldworld"
# print(s1.removesuffix('world'))                      op: welcome to python world

            # 43. string.join(iterable(str)) -> str

# s1=['adarsh','madhu']
# print(" ".join(s1))                                  #op: adarsh madhu
# s1=('keerthi','gowda')
# print(" ".join(s1))                                  #op: keerthi gowda
# s1={'adarsh','madhu','keerthi','gowda'}              #op: keerthi adarsh gowda madhu
# print(" ".join(s1))                                 
# s1={'adarsh':'A','madhu':'M'}
# print(" ".join(s1.values()))                         #op: A M 
# print(" ".join(s1.keys()))                           #op: adarsh madhu
# print(" ".join(s1))                                  #op: adarsh madhu
# s1=[1,2,'keerthi','adarsh']                          #op: TypeError: sequence item 0: expected str instance, int found
# print(" ".join(s1))
# s1='adarsh'
# s2='madhu'
# print(" ".join(s1,s2))                               #op: TypeError: str.join() takes exactly one argument (2 given)
# s1='adarsh'
# print(" ".join(s1))                                  #op: a d a r s h

            # string.format(value1,value2,..) -> str

# s1='adarsh'
# s2='keerthi'
# print("This is format method:{},{}".format(s1,s2))                              #op: This is format method:adarsh,keerthi
# print("This is format method:{},{}".format(s2,s1))                              #op: This is format method:keerthi,adarsh
# print("This is positional indexing: {1},{0}".format('keerthi','adarsh'))        #op: This is format: adarsh,keerthi
# print("This is placeholder: {name},{age}".format(name='Keerthana',age=21))      #op: This is placeholder: Keerthana,21

            # string.encode()

s1='Keerthi'
print(s1.encode())                                  #op: b'Keerthi'

# s1.format_map


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



