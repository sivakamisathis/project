
# #Create python program add, sum, product, difference
# a=5
# b=2.5
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# print("The sum is:",c)
# print("The Difference is:",d)
# print("The product is:",e)
# print("The Quotient is:",f)

# #Boolean Operations
# is_sunny=True
# is_raining=False
# result=is_sunny or is_raining
# print("Is either sunny or raining?:",True)

# is_sunny=True
# is_raining=False
# if is_sunny or is_raining:    
#     print("Is either sunny or raining?:",True)
# else:
#     print("otherwise:",False)


# #String operations:
# x="Python Programming"
# print("The oringinal string:",x)
# print("The substring:", x[0:6])
# x1=x.upper()
# print("The uppercase :",x1)
# y=x.replace("Programming","Language!")
# print("The Replaced string:",y)

# #List Operations
# fruits=["apple","banana","cherry","orange"]
# print("The original list:", fruits)
# fruits.append("grapes")
# print("updated list after adding grapes:",fruits)
# fruits.insert(1,"kiwi")
# print("List after inserting kiwi at index 1:",fruits)
# fruits.remove("banana")
# print("List after removing banana:",fruits)
# z=fruits.index("cherry")
# print("Index of cherry:",z)
# print("First three fruits:",fruits[0:3])
# print("Last two fruits:",fruits[3:])
# print("The length of the list:",len(fruits))


# #tuple Operations
# tuple=(10,20)
# print("Original tuple:",tuple)
# #tuple[1]=30
# #print(tuple)
# tuple1=(30,40)
# result=tuple+tuple1
# print("The concatenated tuple is:",result)
# print("The first element of tuple is:",tuple[0])
# print("The last element of tuple is:",tuple[1])
# print("The length of tuple is:",len(tuple))


# #Dictionary Operations
# my_dict={"name":"Siva","age":20,"city":"New york"}
# print("Original dictionary:",my_dict)
# my_dict.update({"age":31})
# print("Updated dictionary with new age:",my_dict)
# my_dict.update({"job":"Engineer"})
# print("Dictionary after adding job:", my_dict)
# my_dict.pop("city")
# print("Dictionary after removing city:",my_dict)
# #print("Name:",my_dict.get("name"))
# print("Name:",my_dict["name"])
# '''res=True
# for ele in my_dict:
#     if not my_dict[ele]:
#         res=False
#         break'''
# print("Job exists:" "job" in my_dict)
# print(len(my_dict))

# # #Set Operations
# # set={1,2,3,4,5}
# # print("Original set is:",set)
# # set.add(6)
# # print("Set after adding 6:",set)
# # set.add(3)
# # print("Set after trying to add 3 again:",set)
# # set.remove(2)
# # print("Set after removing 2:",set)
# # set1={4,5,6,7,8}
# # set2=set.union(set1)
# # print("Union of sets:",set2)
# # set2=set.intersection(set1)
# # print("Intersection of sets:",set2)
# # print("Length of the set:",len(set))



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 2)
    print(result)
  else:
    result = 0
  return result
x=["rat","goat","cow","ant","horse"]
print("\n")
print("Recursion Example Results:")

tri_recursion(6)






