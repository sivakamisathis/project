# class flower:
#     def flowername(self):
#         print("Name of flowers")

# flr=flower()
# flr.flowername()


# class flower:
#     def __init__(self) -> None:
#         print("Flowers")

#     def flowername(self):
#         self.name="rose"
#         print(self.name)

# flr=flower()
# flr.flowername()


# class laptop:
    
#     def __init__(self,price,processor,ram):
#         self.price=price
#         self.processor=processor
#         self.ram=ram

# hp=laptop(50000,"Intel","16GB")
# print("HP laptop details")
# print("price:",hp.price)
# print("processor:",hp.processor)
# print("Ram:",hp.ram)

# dell=laptop(60000,"Intel core","16GB")
# print("Dell laptop details")
# print("price:",dell.price)
# print("processor:",dell.processor)
# print("Ram:",dell.ram)

# lenova=laptop(60000,"Intel core","16GB")
# print("Dell laptop details")
# print("price:",lenova.price)
# print("processor:",lenova.processor)
# print("Ram:",lenova.ram)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=person("Siva",20)
# print("The name is:",p1.name)
# p1.age=30
# print("The age is:",p1.age) 


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=person("Siva",20)
# print("The name is:",p1.name)
# del p1.age
# print("The age is:",p1.age) 

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=person("Siva",20)
# del p1
# print(p1)


# class person:
#     def __init__(self):
#        print("Welcomes you")
#        pass

#     def per_name(self):
#         print("Python program")

# p1=person()
# p1.per_name()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# p1=person("siva",20)    
# p2=person("sri",10)    

# print("The Name is:", getattr(p1,'name'))
# print("The age is:", getattr(p1,'age')) 


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1=person("siva",25)

print(p1)

