# def fun_name(fname,lname="sathis"):
#     print(fname,"","sathis")
# fun_name("siva")
# fun_name("sri")
# fun_name("mahi")

# #Positional Arguments:
# def pos_args(fname,lname):
#     print(fname,"",lname)

# pos_args("sri","siva")
# pos_args("mahi","sri")
# pos_args("siva","sathi")

# #Keyword Arguments:
# def sum(a,b,c):
#     print("The sum of three values:",a+b+c)

# sum(b=5,c=3,a=4)

# #Default Arguments:
# def def_val(a,b=5,c=3):
#     print("The sum of three values:",a+b+c)

# def_val(3,6,2)

# #Arbitrary positional Arguments:
# def sum_all(*numbers):
#     return sum(numbers)

# x=sum_all(2,3,4,5,3)
# print("The sum of all numbers:",x)

# #Arbitrary keyword arguments:
# def fun_name(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)

# fun_name(name="siva",age=20,city="Namakkal")

# def fun_name(**kwargs):
#     for i in kwargs.keys():
#         print(i)

# fun_name(name="siva",age=20,city="Namakkal")

# def fun_name(**kwargs):
#     for j in kwargs.values():
#         print(j)

# fun_name(name="siva",age=20,city="Namakkal")

# def fru_name(fruits="pomegranate"):
#     print("I need",fruits)

# fru_name("apple")
# fru_name()
# fru_name("banana")
# fru_name()
# #passing a list an Arguments:
# def fun_name(fruits):
#     for i in fruits:
#         print (i)
        
# x= ["apple","kiwi","orange"]
# fun_name(x)

# def fun_name(fruits):
#     for i in fruits:
#         print (i)
        
# x= ["apple","kiwi","orange"]
# fun_name([x])

#Recursion 
# def rec_fun(k):
#     if(k>0):
#         result=k+rec_fun(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# print("Recursion Example Results:")
# rec_fun(6)

# #Lambda function:
# def fun_name(n):
#     return lambda a:a*n

# x=fun_name(5)
# y=fun_name(6)
# print(x(10))
# print(y(3))

#Declaring variables:
x="Python program"
def myvar_fun():
    print(x)

myvar_fun()

x="Language"
def fun_name():
    x="fantastic"
    print("python is a ",x)

fun_name()
print("python is a progrmming",x)
#Declaring variable using global keyword
x="Language"
def fun_name():
    global x
    x="fantastic"
    print("python is a ",x)

fun_name()
print("python is a progrmming",x)




# a=5
# b=3
# def add(a,b):
#     a=6
#     b=4
#     c=a+b
#     print(c)
# add(6,4)

