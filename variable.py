global a,b,c
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
def max_num(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c
    
x=max_num(a,b,c)
print("The maximum of three numbers:",x)



# total=0
# def sum_num(list):
#     global total
#     for i in list:
#         total+=i
#     return total
    
# sum_num([8,2,3,0,7])
# print("The sum of numbers:",total)



# total=1
# def mul_num(list):
#     global total
#     for i in list:
#         total*=i
#     return total
# x=mul_num([8,2,3,-1,7])
# print("The Multiplication of all numbers:",x)



# # global Even_numbers
# def even_num(list):
#     Even_numbers=[]
#     for i in list:
#         if i % 2 == 0:
#            Even_numbers.append(i)
#     print("The even numbers are:",Even_numbers)
       
     
# even_num([1,2,3,4,5,6,7,8,9])



# x="welcome"
# def print_fun(text):
#     global x
#     x+= " " +"to python"
#     return x

# y=print_fun("Welcome to python")
# print("The string is:",y)
