
#Largest of three numbers:
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if(a>b and a>c):
#     print("The largest number is:",a)
# elif(b>c and b>a):
#     print("The largest number is:",b)
# else:
#     print("The largest number is:",c)


#Even  or odd numbers:
# x=int(input("Enter the number:"))
# if x %2==0:
#     print(f"{x}is even")
# else:
#     print(f"{x}is odd")


#Find the vowels or not
# x=str(input("enter the character:"))  
# if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#     print(f"{x} is a vowel")
# else:
#     print(f"{x} is a consonant")


#Multiplication Table
# x=int(input("enter the number:"))
# for i in range(1,11):
#     result=x*i
#     print(x,"*",i,"=",result)


#Reverse number using while loop
# x=int(input("Enter the number:"))
# rev_num=0
# while x!=0:
#     remainder=x % 10
#     rev_num=(rev_num*10)+remainder
#     x=x//10
# print("The reverse number is:",rev_num)


#odd,even,positive,negative,zero
# x=int(input("Enter the number:"))
# if x%2==0 and x<0:
#     print("x is even and negative")
# elif x%2 ==0 and x>0:
#     print("x is even and positive")
# elif x%2 !=0 and x<0:
#     print("x is odd and negative")
# elif x%2 !=0 and x>0:
#     print("x is odd and positive")
# elif x==0:
#     print("x is zero")


#Reverse a string
# text=str(input("Enter the string:"))
# for x in reversed(text):
#     print(x,end="")


#basic arithmetic operations
# a=10
# b=5
# print("Addition is:",a+b)
# print("Subtration is:",a-b)
# print("Multiplication is:",a*b)
# print("Division is;",a/b)
# print("Floor division is:",a//b)
# print("Modulo division is:",a%b)


#Using pass in a loop
# i=0
# for i in range(0,5):
#     print("processing number:",i)
#     i=i+1
#     if(i>5):
#         pass

#To find the first number divisible by 7 between 1 and 100 using break.
# for i in range(1,100):
#     while i%7==0:
#         if i==7 and i<8:
#             print(f"The first number is divisible by 7 is {i}")
#             break
#         i=i+1


#To print numbers from 1 to 10, skipping 5 using continue.
# i=0
# while i<10:
#     i=i+1
#     if i==5:
#         continue
#     print(i,end=" ")

#Write a program to sort a list of numbers in ascending order.
# x=input("enter  the number separated by space:")
# y=x.split()
# for i in range(len(y)):
#     y[i] = int(y[i])
# y.sort()
# print("The sorted list:",y)



# y=['a','e','i','o','u']
# x=str(input("Enter the character:"))
# for x in y:
#     print("x is vowel")
# else:
#     print("x is not vowel")


# i=0
# while i<5:
#     print("Processing number:",i)
#     i=i+1
# else:
#     pass




# for i in range(1,100):
#        if i%7==0:
#             print(f"The first number is divisible by 7 is {i}")
#             break
        





# x=input("enter  the number separated by space:")
# y=[int(num) for num in x.split()]
# y.sort()
# print("Sorted list:",y)    




        




