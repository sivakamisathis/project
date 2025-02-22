#Creation of set
numbers={10,15,23,7,25,12,21}
print(numbers)
strings={'c','o','m','p','u','t','e','r'}
print(strings)
mix={100,'siva',-5,'good'}
print(mix)
#Accessing set
set={"apple","banana","cherry"}
print("banana" not in set)
print('banana' in set)
set.add("kiwi")
print(set)
print("kiwi" in set)
#Add sets
A={3,8,6}
B={2,3,5}
A.update(B)
print(A)

#data type of set
empty_set=set()
empty_dict={}
print("Data type of empty_set:",type(empty_set))
print("Data type of empty_dict:",type(empty_dict))
print()

#Duplicate item in a set
numbers1={10,15,23,7,25,12,21,15,10}
print(numbers1)



#Adding item to a set
print("Initial set:",numbers)
numbers.add(56)
print("After Adding an element:",numbers)
#update of an item to a set
str={"Apple","banana","mango"}
str1={"car","bike","cycle"}
str.update(str1)
print(str)
#Remove an item from a set
str={"Apple","banana","mango"}
print("The original set:",str)
str.remove("banana")
print(str)
#Length of the numnbers
numbers={10,15,23,7,25,12,21}
print("The length of numbers:",len(numbers))
#Union of two sets using |
A={3,8,6}
B={2,3,5}
print("union using |:",A|B)
print("union using union():",A.union(B))
#intersection using &
print("Intersection using &:",A&B)
print("Intersection using intersection():",A.intersection(B))
#Difference between of two sets
print("Difference using &:",A-B)
print("difference using difference():",A.difference(B))
#symmetric_difference of set
print("using symmetric difference ^:",A^B)
print("using symmetric difference using:",A.symmetric_difference(B))
#Copy of set
A={3,8,6}
A1=A.copy()
print(A1)
A1.add(5)
print(A1)
A1.add(2)
print(A1)
#Difference_update
A={3,8,6}
B={2,3,5}
print("A before (A-B)=",A)
A.difference_update(B)
print("A after (A-B)=",A)
#Set discard
numbers={10,15,23,7,25,12,21}
print("The original set is:",numbers)
numbers.discard(15)
print(numbers)
#clear set
numbers={10,15,23,7,25,12,21}
print("The original set is:",numbers)
numbers.clear()
print("After clearing the set is:",numbers)
#set pop
X={'a','b','c','d'}
print("pop() remove:",X.pop())
print("Updated setX:",X)

