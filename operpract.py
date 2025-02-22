# # Arithmetic Operators
# x=7
# y=5
# print("The Addition of two numbers:",x+y)
# print("The Subtraction of two numbers:",x-y)
# print("The Multiplication of two numbers:",x*y)
# print("The Division of two numbers:",x/y)
# print("The Modulo division of two numbers:",x%y)
# print("The Exponentiation of two numbers:",x**y)
# print("The floor division of two numbers:",x//y)

#Assignment Operators:
# x=7
# print(x)
# x+=3
# print(x)
# x=7
# x-=3
# print(x)
# x=7
# x*=3
# print(x)
# x=7
# x/=3
# print(x)
# x=7
# x%=3
# print(x)
# x=7
# x//=3
# print(x)
# x=7
# x**=3
# print(x)
# x=7
# x&=3
# print(x)
# x=7
# x|=3
# print(x)
# x=7
# x^=3
# print(x)
# x=7
# x>>=3
# print(x)
# x=7
# x<<=3
# print(x)
# x=7
# print(x)

#Comparision operator
# x=10
# y=15
# print(x==y)
# print(x!=y)
# print(x<y)
# print(x>y)
# print(x<=y)
# print(x>=y)
# print('\n')
# x1="siva"
# y1="srisiva"
# print(x1==y1)
# print(x1!=y1)
# print(x1<y1)
# print(x1>y1)
# print(x1<=y1)
# print(x1>=y1)

#Logical Operators(and,or,not)
# x=10
# print(x>6 and x>45)
# print(x<6 and x<45)
# print('\n')
# # #(or)
# print(x>6 or x<45)
# print(x<6 or x>45)
# #not
# print(not(x>6 and x<45))

#Bitwise Operator(and,or,xor,NOT,Zero fill left shift,signed right shift)
# a=-5
# b=5
# print(a & b)
# print(a | b)
# print(a ^ b) 
# print(~a)
# a=3
# b=2
# print(3<<2)
# a=8
# b=2
# print(8>>2)

# #Identity Operator(is,is not)
# x=["siva","sri","mahi","abi"]
# y=["siva","sri","mahi","abi"]
# z=x
# print(x is z)
# print(y is x)
# print(x == y)
# print(x is not y)
# print(x is not z)

# # #Membership Operator(in,notin)
# list=["kiwi","orange","grapes","cherry"]
# print("grapes" in list)
# print("banana" in list)
# print("cherry" not in list)
# print("apple" not in list)

m1=int(input("Enter tamil mark:"))
m2=int(input("Enter tamil mark:"))
m3=int(input("Enter tamil mark:"))
m4=int(input("Enter tamil mark:"))
m5=int(input("Enter tamil mark:"))
total=m1+m2+m3+m4+m5
print("The total is:",total)
avg=total/5
print("The average is:",avg)
if(avg>90):
    print("grade is:O")
elif(avg>80):
    print("grade is:A")
elif(avg>60):
    print("grade is:B")
else:
    print("grade is:Fail")




       

