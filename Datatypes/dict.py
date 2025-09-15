# defining dictionary: Group of key value pairs separated by coma and enclosed within curly braces{}
# syntax: {key:value,key:value,....}

# d1={1:10,2:20,3:30,4:40}
# print(d1,len(d1),type(d1))                          op: {1: 10, 2: 20, 3: 30, 4: 40} 4 <class 'dict'>

# d1={}
# print(d1,len(d1),type(d1))                          op: {} 0 <class 'dict'> Empty dict

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# d2={1:10,2:20,3:30,4:40}
# print(d1+d2)                                        op: TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(d1*3)                                         op: TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# property of dict

            # dict can be homogenous or heterogenous

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}      homogenous
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

# d1={'A':"apple",1:10,2.1:[1,2],2+3j:{1,2,3}}        heterogenous 
# print(d1)                                           op:  {'A': 'apple', 1: 10, 2.1: [1, 2], (2+3j): {1, 2, 3}}

            # dict support duplicate values but not duplicate keys if key is duplicate last assigned value will be considered

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog','A':"ant"}
# print(d1)                                           op: {'A': 'ant', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

            # dict are ordered coolection

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}      
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

            # dict doesnt support indexing and slicing keys are used to fetch values

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1[1])                                        op: KeyError: 1

# print(d1['A'])                                      op: apple
# print(d1['a'])                                      op: KeyError: 'a'

            # dict keys are immutable and values are mutable

# d1={1:10,2:20,3:30,4:40}
# d1[1]=100
# print(d1)                                           op: {1: 100, 2: 20, 3: 30, 4: 40}

            # dict key can be int, float, str, complex, boolean, tuple values can be any data type

# d1={1:10,2.5:"don",3+4j:[1,2,3],True:{1,2,3},(1,2):"het"}
# print(d1,type(d1))                                 op: {1: 10, 2.5: 'don', (3+4j): [1, 2, 3], True: {1, 2, 3}, (1, 2): 'het'} <class 'dict'>

# d2={1:10,2.5:"don",3+4j:[1,2,3],True:{1,2,3},(1,2):"het",[1,2,3]:"list"}
# print(d2,type(d2))                                 op: TypeError: unhashable type: 'list'

            # looping in dict

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}

            # fetching only keys:

# for i in d1:
#     print(i,end=" ")                                op: A B C D

# res1=d1.keys()
# print(res1,type(res1))                              op: dict_keys(['A', 'B', 'C', 'D']) <class 'dict_keys'>

# for i in d1.keys():
#     print(i,end=" ")                                op: A B C D

            # fetching only values:

# for i in d1.values():
#     print(i,end=" ")                                op: apple bat cat dog

# res2=d1.values()
# print(res2,type(res2))                              op: dict_values(['apple', 'bat', 'cat', 'dog']) <class 'dict_values'>

            # fetching key and values both:

# for i in d1.items():
#     print(i,end=" ")                                op: ('A', 'apple') ('B', 'bat') ('C', 'cat') ('D', 'dog') 

# res3=d1.items()
# print(res3,type(res3))                              op: dict_items([('A', 'apple'), ('B', 'bat'), ('C', 'cat'), ('D', 'dog')]) <class 'dict_items'>

# dict built-in methods 

            # dict.clear() -> None

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.clear())                                   op: None

            # dict.copy() -> dict

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# d2=d1.copy()  
# print(d2)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

# print(d1 is d2)                                     op: False

# print(d1==d2)                                       op: True

            # dict.get(key,default=None) -> value of key if key is not present returns default value

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.get('B'))                                  op: bat

# print(d1.get('b'))                                  op: None

# print(d1.get('b',"not found"))                      op: not found

            # dict.update({key:value}) -> None, used to add key value pair or update value of existing key

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.update({'E':"elephant"}))                  op: None  
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog', 'E': 'elephant'}

# print(d1.update({'B':"ball"}))                      op: None
# print(d1)                                           op: {'A': 'apple', 'B': 'ball', 'C': 'cat', 'D': 'dog', 'E': 'elephant'}

            # dict.setdefaults(key,default_value) -> value of key if key is not present adds key with default_value and returns default_value

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.setdefault('B'))                           op: bat
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

# print(d1.setdefault('b',"not found"))               op: not found
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog', 'b': 'not found'}

# print(d1.setdefault('E'))                           op: None
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog', 'b': 'not found', 'E': None}

# print(d1.setdefault('C',"cow"))                     op: cat
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog', 'b': 'not found', 'E': None}

            # dict.pop(key,default=None) -> value of key if key is not present returns default value and removes the key value pair

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.pop('C'))                                  op: cat
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'D': 'dog'}

# print(d1.pop('c'))                                  op: KeyError: 'c'

# print(d1.pop('c',"not found"))                      op: not found
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'D': 'dog'}

# print(d1.pop('D',"not found"))                      op: dog
# print(d1)                                           op: {'A': 'apple', 'B': 'bat'}

# print(dict.pop())                                   op: TypeError: pop expected at least 1 argument, got 0

            # dict.popitem() -> (key,value) removes and returns last inserted key value pair

# d1={'A':"apple",'B':"bat",'C':"cat",'D':'dog'}
# print(d1.popitem())                                 op: ('D', 'dog')
# print(d1)                                           op: {'A': 'apple', 'B': 'bat', 'C': 'cat'}

            #  dict.fromkeys(iterable,default_value=None) -> dict, used to create dict with keys from iterable and values as default_value

# l1=['A','B','C','D']
# print(dict.fromkeys(l1))                            op: {'A': None, 'B': None, 'C': None, 'D': None}

# print(dict.fromkeys(l1,10))                         op: {'A': 10, 'B': 10, 'C': 10, 'D': 10}

# d1={}.fromkeys(l1,100)
# print(d1)                                           op: {'A': 100, 'B': 100, 'C': 100, 'D': 100}

# d1.fromkeys(l1,[1,2,3]))                            op: {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3], 'D': [1, 2, 3]}
# d1['A'].append(4)
# print(d1)                                           op: {'A': [1, 2, 3, 4], 'B': [1, 2, 3, 4], 'C': [1, 2, 3, 4], 'D': [1, 2, 3, 4]}

# dict comprehension

# d1={i:i*10 for i in range(1,6)}
# print(d1)                                           op: {1: 10, 2: 20, 3: 30, 4:40, 5:50 }