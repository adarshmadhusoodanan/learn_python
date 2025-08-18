# defining set
# s1={1,2,3,4,5}
# print(s1,type(s1))                        {1, 2, 3, 4, 5} <class 'set'>

# print(len(s1))                            op: 5

# s1=set()                                  empty set
# print(s1,type(s1))                        set() <class 'set'>

# property of sets

            # set can be homogenous or heterogenous

# s1={1,2,4,6,1,4}
# print(s1)                                 op: {1, 2, 4, 6}                    homo

# s2={1,2.3,"don",4+5j}                     
# print(s2)                                 op: {1, 2.3, (4+5j), 'don'}         hetro

            # set can have duplicate elements

# s1={1,2,4,6,1,4}
# print(s1)                                 op: {1, 2, 4, 6}

            # set are unordered collection 

# s1={9,5,1,3,7,4,0}
# print(s1)                                 op: {0, 1, 3, 4, 5, 7, 9}

            # set support only int, float, str, complex, boolean, tuple as element

# s1={1,2.5,"don",2+3j,(1,2,3),'a'==2}
# print(s1,type(s1))                        op: {False, 1, 2.5, 'don', (2+3j), (1, 2, 3)} <class 'set'>

# s1={1,2,3,{1,2,3}}                        TypeError: unhashable type: 'set'

# s1={1,2,3,[1,2,3]}                        TypeError: unhashable type: 'list'

# s1={1,5,3,3,{'a':'apple','b':'bat'},2}    TypeError: unhashable type: 'dict'
# print(s1,type(s1))

            # set doesnt support indexing and slicing

# s1={1,2,4,6,1,4}
# print(s1[1])                              TypeError: 'set' object is not subscriptable

# s1={3,5,7,2,3,4}
# print(s1[1:4])                            TypeError: 'set' object is not subscriptable

            # set are mutable collection (insertion and deletion)

# s1={1,3,5,2,4,6}
# s1.add(7)
# print(s1)                                  op: {1, 2, 3, 4, 5, 6, 7}

# s1.remove(5)
# print(s1)                                  op: {1, 2, 3, 4, 6}


