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

            # set can not have duplicate elements

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

# set built-in methods

            # set.clear() -> None

# s1={1,4,6,3,4}
# print(s1.clear())                          op: None
# print(s1)                                  op: set()

            # set.copy() -> set

# s1={1,3,5,6,4,2}
# s2=s1.copy()
# print(s1)                                  op: {1, 2, 3, 4, 5, 6}
# print(s2)                                  op: {1, 2, 3, 4, 5, 6}

            # set.add() -> None

# s1={1,3,5,6,4,2}
# print(s1.add(10))                          op: None
# print(s1)                                  op: {1, 2, 3, 4, 5, 6, 10}

            # set.remove() -> None

# s1={1,3,5,6,4,2}
# print(s1.remove(5))                        op: None
# print(s1)                                  op: {1, 2, 3, 4, 6}

# print(s1.remove(10))                       
# print(s1)                                  op: KeyError: 10

            # set.discard() -> None

# s1={1,3,5,6,4,2}
# print(s1.discard(6))                       op: None
# print(s1)                                  op: {1, 2, 3, 4, 5}

# print(s1.discard(10))                      op: None
# print(s1)                                  op: {1, 2, 3, 4, 5}

            # set.pop() -> Any

# s1={1,2,5,3,7,8}
# print(s1.pop())                            op: 1
# print(s1)                                  op: {2, 3, 5, 7, 8}

            # set.update() -> None

# s1={1,2,3,5,4,8}
# print(s1.update([7,9]))                    op: None
# print(s1)                                  op: {1, 2, 3, 4, 5, 7, 8 ,9}

# print(s1.update(7))                        
# print(s1)                                  'int' object is not iterable

# print(s1.update((7,)))                     op: None
# print(s1)                                  op: {1, 2, 3, 4, 5, 7, 8}

# print(s1.update((7,9)))                    op: None
# print(s1)                                  op: {1, 2, 3, 4, 5, 7, 8 ,9}

# print(s1.update({7,9,10}))                 op: None
# print(s1)                                  op: {1, 2, 3, 4, 5, 7, 8, 9, 10}

# s1={1,3,5,7}
# s2={2,4,6,8}
# s1.update(s2)
# print(s1)                                  op: {1, 2, 3, 4, 5, 6, 7, 8}

            # set.union(*set) -> set

# s1={1,3,5,7}
# s2={2,4,6,8}
# s3={9}
# print(s1.union(s2))                        op: {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1.union(s2,s3))                     op: {1, 2, 3, 4, 5, 6, 7, 8, 9}

            # set.intersection(*set)-> set

# s1={1,3,5,7}
# s2={1,2,3,4}
# print(s1.intersection(s2))                 op: {1, 3}
# print(s2.intersection(s1))                 op: {1, 3}

            # set.intersection-update() -> None

# s1={1,3,5,7}
# s2={1,2,3,4}
# s1.intersection_update(s2)
# print(s1)                                   op: {1, 3}
# s2.intersection_update(s1)
# print(s2)                                   op: {1, 3}

            # set.difference() -> set

# s1={1,2,3,4,5,6}
# s2={5,6,7,8,9,1}
# print(s1.difference(s2))                    op: {2, 3, 4}
# print(s2.difference(s1))                    op: {8, 9, 7}

            # set.difference_update() -> None

# s1={1,2,3,4,5,6}
# s2={5,6,7,8,9,1}
# s1.difference_update(s2)
# print(s1)                                   op: {2, 3, 4}
# s2.difference_update(s1)
# print(s2)                                   op: {7, 8, 9}

            # set.symmetric_difference() -> set

# s1={1,2,3,4,5,6}
# s2={5,6,7,8,9,1}
# print(s1.symmetric_difference(s2))          op: {2, 3, 4, 7, 8, 9}
# print(s2.symmetric_difference(s1))          op: {2, 3, 4, 7, 8, 9}

            # set.symmetric_difference_update() -> None

# s1={1,2,3,4,5,6}
# s2={5,6,7,8,9,1}
# s1.symmetric_difference_update(s2)
# print(s1)                                   op: {2, 3, 4, 7, 8, 9}
# s2.symmetric_difference_update(s1)
# print(s2)                                   op: {2, 3, 4, 7, 8, 9}

            # set.isdisjoint() -> bool

# s1={1,2,3,4,5,6,7,8}
# s2={9,10,11,12}
# print(s1.isdisjoint(s2))                    op: True
# s1={1,2,3,4,5,6}
# s2={2,4,6}
# print(s1.isdisjoint(s2))                    op: False

            # set.issuperset() -> bool

# s1={1,2,3,4,5,6}
# s2={5,6,7,8}
# print(s1.issuperset(s2))                    op: False
# s1={1,2,3,4,5,6}
# s2={5,6}
# print(s1.issuperset(s2))                    op: True

            # set.issubset() -> bool

# s1={1,2,3,4,5,6}
# s2={1,2}
# print(s1.issubset(s2))                      op: False
# print(s2.issubset(s1))                      op: True