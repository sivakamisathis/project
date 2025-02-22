# #Area of rectangle
# def area_rec(l,b):
#     return l*b

# x=area_rec(5,3)
# print("The area of rectangle is:",x)



# #Keyword Arguments
# def sample(name,age):
#     txt=f"{name} is {age} years old"
#     return txt
    
# x=sample(name="john",age=30)
# print(x)

#Arbitrary arguments using sum
# def arbit(*args):
#     return sum(args)

# x=arbit(5,6,7)
# print("The sum of value is:",x)


# #The final price after applying the discount
# def pri_dis(price,discount=10):
#     x=price*(discount/100)
#     final=price-x
#     return final

# x=pri_dis(150)
# print("The final price after applying the discount:",x)



# def vowels(strings):
#     count=0
#     vowel_count="aeiou"
#     for i in strings:
#         if(i in vowel_count):
#             count=count+1
#     return count
    
# x=vowels("python program")
# print("The vowel count is:",x)


# def sum_list(list):
#     sum=0
#     for x in list:
#         sum+=x
#     return sum
        
    
# a=sum_list([5,3,6,2])
# print("The sum of list value is:",a)




def area_cir(r):
    pi=float(3.14)
    area=pi*r**2
    return area

x=area_cir(5)
print("The area of circle:",x)
















# def rev_str(strings):
#     x=strings[::-1]
#     return x

# a=rev_str("program")
# print("The reversed strings are:",a)