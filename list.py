# defining list

# l1=[1,2,3,4,5]       [1, 2, 3, 4, 5] <class 'list'>       define
# l1=[]                [] <class 'list'>                    empty list
# l1=[0,2,4,[1,3,5]]   [0, 2, 4, [1, 3, 5]] <class 'list'>  nested list
# print(len(l1))       op: 3                                length of list

# property of list
            # list can be homogenous or heterogenous 
# l1=[1,2,3,4,5]         [1, 2, 3, 4, 5] <class 'list'>             homogenous collection
# l1=[1,3.4,"don",2+3j]  [1, 3.4, 'don', (2+3j)] <class 'list'>     heterogenous collection

            # list can have duplicate elements

# l1=[0,1,1,2,3,4]       [0, 1, 1, 2, 3, 4] <class 'list'>          have duplicate elements

            # list are ordered collection

# l1=[0,2,4,[1,3,5]]     [0, 2, 4, [1, 3, 5]] <class 'list'>        

            # list support indexing

# l1=[0,2,4,[1,3,5]]
# print(l1[0])           op: 0
# print(l1[3])           op: [1, 3, 5]
# print(l1[3][1])        op: 3
# print(l1[-1][-1])      op: 5

            # list support slicing

# print(l1[1:3])         op: [2, 4]
# print(l1[2:4])         op: [4, [1, 3, 5]]
# print(l1[0:4:2])       op: [0, 4]
# print(l1[:3])          op: [0, 2, 4]
# print(l1[::-1])        op: [[1, 3, 5], 4, 2, 0]
# print(l1[::])          op: [0, 2, 4, [1, 3, 5]]
# print(l1[4:0:-1])      op: [[1, 3, 5], 4, 2]
# print(l1[-1:-3:-1])    op: [[1, 3, 5], 4]
# print(l1[-4:-1:1])     op: [0, 2, 4]
# print(l1[3][0:2])      op: [1, 3]

            # list are mutable

# l1=[0,2,4,[1,3,5]]
# l1[1]="iron man"       op: [0, 'iron man', 4, [1, 3, 5]]
# l1[3][2]="6.7"         op: [0, 2, 4, [1, 3, '6.7']]

# list built-in functions

            # list.clear() -> None

# l1=[1,2,3,4,5]
# l1.clear()
# print(l1)              op: []
# print(l1.clear())      op: None

            # list.copy() -> list

# l1=[1,2,3,4,5]
# l2=l1.copy()
# print(l2)              op: [1, 2, 3, 4, 5]
# l2[3]=5                creates shallow copy 
# print(l2)              op: [1, 2, 3, 5, 5] 
# print(l1)              op: [1, 2, 3, 4, 5]

            # list.count() -> int

# l1=[1,2,3,4,5,1]
# print(l1.count(1))       op: 2