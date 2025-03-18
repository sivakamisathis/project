# x=["rat","goat","cow","ant","horse"]
# print(x)
# x[2]="cat"
# print(x)
# print(x[1])
# print(x[-4:-1])
# x.insert(2,"lamp")
# print(x)
# x.append("elephant")
# print(x)
# x1=["red","green"]
# print(x1)
# x.extend(x1)
# print(x)
# #Remove() Method)
# x=["rat","goat","cow","ant","horse"]
# x.remove("ant")
# print(x)
# #pop() Method
# x=["rat","goat","cow","ant","horse"]
# x.pop(1)
# print(x)
# #Delete particulat item
# x=["rat","goat","cow","ant","horse"]
# del x[2]
# print(x)
# #Delete full list
# x=["rat","goat","cow","ant","horse"]
# del x
# #Clear() Method
# x=["rat","goat","cow","ant","horse"]
# x.clear()
# #Iteration method using loop
# x=["rat","goat","cow","ant","horse"]
# for i in x:
#     print(i)
# #while loop
# x=["rat","goat","cow","ant","horse"]
# i=0
# while i < len(x):
#     print(x[i])
#     i=i+1

# x=["rat","goat","cow","ant","horse"]
# [print(i) for i in x]

# List comprehension:
x=["rat","goat","cow","ant","horse"]
x1=[]
for i in x:
    if "a" in i:
        x1.append(i)
print(x1)
print("")

# #List comprehension:
# x=["rat","goat","cow","ant","horse"]
# x1=[i for i in x if "a" in i]
# print(x1)

# x=["rat","goat","cow","ant","horse"]
# x1=[i for i in x if i!="goat"]
# print(x1)

# #Iterable
# x1=[i for i in range(10)]
# print(x1)

# x1=[i for i in range(10) if i < 5]
# print(x1)

# x=["rat","goat","cow","ant","horse"]
# x1=[i.upper() for i in x]
# print(x1)
# x=["rat","goat","cow","ant","horse"]
# x1=["hello" for i in x]
# print(x1)

# x=["rat","goat","cow","ant","horse"]
# x1=[i if i != "goat" else "sheep" for i in x]
# print(x1)

# x=["rat","goat","cow","ant","horse"]
# x.sort()
# print(x)

# #Sort descending order
# x=["rat","goat","cow","ant","horse"]
# x.sort(reverse=True)
# print(x)

# #copy() Method
# x=["rat","goat","cow","ant","horse"]
# x1=x.copy()
# print(x1)

# #Join Methods
# l1=["a","b","c"]
# l2=[1,2,3]
# l3=l1+l2
# print(l3)
# for x in l2:
#     l1.append(x)
# print(l1)

# #count Method:
# x=["rat","goat","cow","ant","horse","cow"]
# y=x.count("cow")
# print(y)



#SET
#CREATION OF SET
# set={"car","bike","cycle","train"}
# print(set)
# print(len(set))
# # x=set(("car","bike","cycle","train")) 
# # print(x) 
# for x in set:
#     print(x)
# print("cycle" in set)
# print("aeroplane" not in set)
# print(set.add("aeroplane"))
# print(set)
# set={"car","bike","cycle","train"}
# set1={"red","green","blue"}
# set.update(set1)
# print(set)
# set.remove("bike")
# print(set)
# set.discard("car")
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
# del set
# print(set)
# set={"car","bike","cycle","train"}
#Iteration
# for x in set:
#     print(x)
#Union
# set1={"car","bike","cycle","train"}
# set2={"red","green","blue"}
# set3=set1.union(set2)
# print(set3)
# x=set1|set2|set3
# print(x)
# x=set1.union(set2,set3)
# print(x)
# y=(1,2,3)
# z=set.union(y)
# print(z)
#Intersection
set1={"red","green","orange","blue"}
set2={"yellow","orange","pink","green"}
set3=set1 & set2
print(set3)
set1.update(set2)
print(set1)
set1={"red","green","orange","blue"}
set2={"yellow","orange","pink","green"}
set1.intersection_update(set2)
print(set1)
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)