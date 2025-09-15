# Python List Datatype
# List is a collection which is ordered and changeable. Allows duplicate members.
# List are written with square brackets []
#------------------------------------------------------------------------------------------------------------------------------------------------

#                   defining list

# l1=[1,2,3,4,5]                                            [1, 2, 3, 4, 5] <class 'list'>       define
# l1=[]                                                     [] <class 'list'>                    empty list

# l1=[0,2,4,[1,3,5]]                                        #[0, 2, 4, [1, 3, 5]]<class 'list'>  nested list
# print(len(l1))                                            #op: 4                                length of list

# l1=[1,2,3]
# l2=[5,7,8,9]
# print(l1+l2)                                              #op: [1, 2, 3, 5, 7, 8, 9]            <class 'list'> concatenation of list
# print(l1*3)                                               #op: [1, 2, 3, 1, 2, 3, 1, 2, 3]      <class 'list'> repetition of list

# l1=[1, 2, 3, (1, 2, 3)]                                   
# print(type(l1[3]))                                        #<class 'tuple'>
# print(l1,type(l1))                                        #[1, 2, 3, (1, 2, 3)] <class 'list'>

# l1=[1, 2, 3, {1, 2, 3}]                                  
# print(type(l1[3]))                                        #<class 'set'>
# print(l1,type(l1))                                        #[1, 2, 3, {1, 2, 3}] <class 'list'>

# l1=[1,2.3,2+4j,'a'== 'a', {'a':"apple" , 'b':"bat"} ]
# print(type(l1[4]))                                        #<class 'dict'>
# print(l1,type(l1))                                        #[1, 2.3, (2+4j), True, {'a': 'apple', 'b': 'bat'}] <class 'list'>


# note: 
#       list comprehension is also there
# l1=[x for x in range(10)]
# print(l1,type(l1))                                        #op: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

#------------------------------------------------------------------------------------------------------------------------------------------------

# property of list

            # list can be homogenous or heterogenous 

# l1=[1,2,3,4,5]                                            [1, 2, 3, 4, 5] <class 'list'>             homogenous collection
# l1=[1,3.4,"don",2+3j]                                     [1, 3.4, 'don', (2+3j)] <class 'list'>     heterogenous collection

            # list can have duplicate elements

# l1=[0,1,1,2,3,4]                                          [0, 1, 1, 2, 3, 4] <class 'list'>          have duplicate elements

            # list are ordered collection

# l1=[0,2,4,[1,3,5]]                                        [0, 2, 4, [1, 3, 5]] <class 'list'>        

            # list support indexing

# l1=[0,2,4,[1,3,5]]
# print(l1[0])                      #op: 0
# print(l1[3])                      #op: [1, 3, 5]
# print(l1[3][1])                   #op: 3
# print(l1[-1][-1])                 #op: 5

            # list support slicing

# l1=[0,2,4,[1,3,5]]
# print(l1[1:3])                    #op: [2, 4]
# print(l1[2:4])                    #op: [4, [1, 3, 5]]
# print(l1[0:4:2])                  #op: [0, 4]
# print(l1[:3])                     #op: [0, 2, 4]
# print(l1[::-1])                   #op: [[1, 3, 5], 4, 2, 0]
# print(l1[::])                     #op: [0, 2, 4, [1, 3, 5]]
# print(l1[4:0:-1])                 #op: [[1, 3, 5], 4, 2]
# print(l1[-1:-3:-1])               #op: [[1, 3, 5], 4]
# print(l1[-4:-1:1])                #op: [0, 2, 4]
# print(l1[3][0:2])                 #op: [1, 3]

            # list are mutable

# l1=[0,2,4,[1,3,5]]
# l1[1]="iron man"     
# print(l1)                         #op: [0, 'iron man', 4, [1, 3, 5]]
# l1[3][2]="6.7"                    
# print(l1)                         #[0, 'iron man', 4, [1, 3, '6.7']]


#------------------------------------------------------------------------------------------------------------------------------------------------


# list 11 built-in functions


            # list.copy() -> list                                   returns a shallow copy of the list

# l1=[1,2,3,4,5]
# l2=l1.copy()
# print(l2)                         #op: [1, 2, 3, 4, 5]
# l2[3]=5                           #creates shallow copy 
# print(l2)                         #op: [1, 2, 3, 5, 5] 
# print(l1)                         #op: [1, 2, 3, 4, 5]  no change in original list

            # list.count(value) -> int                                  returns the count of number of occurrences of value

# l1=[1,2,3,4,5,1]
# print(l1.count(1))                #op: 2

            # l1.index(value,start:0,stop:size of list)-> int          returns the index of first occurrence of value (optionally restrict to start, stop)

# l1=[3,2,3,[4,"don",8.5,3],3]
# print(l1.index(3))                #op: 0

# print(l1.index(8.5))              #op: ValueError: 8.5 is not in list

# print(l1[3].index(8.5))           #op: 2

# print(l1.index(3,1,5))            #op: 2

            # list.clear() -> None

# l1=[1,2,3,4,5]
# l1.clear()
# print(l1)                         #op: []
# print(l1.clear())                 #op: None

            # list.sort() -> None

# l1=[1,4,7,8,4,3,2]
# l1.sort()
# print(l1)                         #op: [1, 2, 3, 4, 4, 7, 8]
# print(l1.sort())                  #op: None

# l1=["list","tuple","set","dic"]
# l1.sort()
# print(l1)                         #op: ['dic', 'list', 'set', 'tuple']

# l1.sort(reverse=True)
# print(l1)                         #op: [8, 7, 4, 4, 3, 2, 1]

# l1=[1,4,6,7,3.4]
# l1.sort()
# print(l1)                         #op: [1, 3.4, 4, 6, 7]

# l1=[10,2,9,4,[0,9,7,3]]
# l1.sort()
# print(l1)                         #op: TypeError: '<' not supported between instances of 'list' and 'int'

# l1=[1,4,6,7,3.4,"sort","dice"]
# l1.sort()
# print(l1)                         #op: TypeError: '<' not supported between instances of 'str' and 'int'

# l1 =[1,2,3+4j]
# l1.sort()
# print(l1)                         #op: TypeError: '<' not supported between instances of 'complex' and 'int'

            # list.reverse() -> None

# l1=[1,4,7,8,4,3,2]
# l1.reverse()
# print(l1)                         #op: [2, 3, 4, 8, 7, 4, 1]
# print(l1.reverse())               #op: None

# l1=["list","tuple","set","dic"]
# l1.reverse()
# print(l1)                         op: ['dic', 'set', 'tuple', 'list']

# l1=[1,3,3.4,3+4j,"list"]
# l1.reverse()
# print(l1)                         op: ['list', (3+4j), 3.4, 3, 1]



            # list.append(value/object) -> None

# l1=[1,2,3,4,5]
# l1.append(6)
# print(l1)                         op: [1, 2, 3, 4, 5, 6]

# print(l1.append(6))               op: None

# l1.append([5,6,7])       
# print(l1)                         op: [1, 2, 3, 4, 5, [5, 6, 7]]

# l1.append("don")
# print(l1)                         op: [1, 2, 3, 4, 5, 'don']

# l1.append(1,2)
# print(l1)                         op: TypeError: list.append() takes exactly one argument (2 given)

            # list.extend(iterable) -> None

# l1=[1,2,3,4]
# l1.extend([5,6,7])
# print(l1)                         op:[1, 2, 3, 4, 5, 6, 7]

# print(l1.extend([1,3,5]))         op: None

# l1.extend("list")
# print(l1)                         op: [1, 2, 3, 4, 'l', 'i', 's', 't']

# l1.extend([5])
# print(l1)                         op: [1, 2, 3, 4, 5]

# l1.extend(1)
# print(l1)                         op: TypeError: 'int' object is not iterable

            # list.insert(index,value) -> None

# l1=[1,2,3,4,5]
# l1.insert(3,5)                  
# print(l1)                         op: [1, 2, 3, 5, 4, 5]

# print(l1.insert(3,5))             op: None

            # list.pop(index:-1)-> Any          - removes and returns item at index (default last). Raises IndexError if list is empty or index is out of range.

# l1=[1,2,3,4,5]
# print(l1.pop(1))                  op: 2
# print(l1)                         op: [1, 3, 4, 5]

# print(l1.pop())                   op: 5
# print(l1)                         op: [1, 2, 3, 4]
            
# print(l1.pop(-2))                 op: 4
# print(l1)                         op: [1, 2, 3, 5]

# print(l1.pop(5))                  op: IndexError: pop index out of range

            # list.remove(value) -> None         - removes first occurrence of value. Raises ValueError if the value is not present.

# l1=[1,5,2,3,4,5]
# l1.remove(5)
# print(l1)                         op: [1, 2, 3, 4, 5]

# print(l1.remove(5))               op: None
# l1.remove()                       op: list.remove() takes exactly one argument
# l1.remove(10)                     op: ValueError: list.remove(x): x not in list