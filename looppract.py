#concatenation of two strings:
# s1=["cat","rat",'may']
# s2=["jan","feb",'mar']
# s1.append(s2)
# s1.extend(s2)
# s3=[*s1,*s2]
# print(s1)
# print(s3)

# #If a key is already present in a dictionary:
# my_dict={"name":"siva","age":15,"city":"namakkal"}
# if "age" in my_dict:
#     print("yes,age is present in this dictionary")
# else:
#     print("It is not present in dictionary")

#check whether a person is eligible for vote
# age=int(input("Enter the age:"))
# if(age==18 or age>=18):
#     print("You can eligible for vote")
# else:
#     print("You cannot vote")


# #Even or odd number
# x=int(input("Enter the number:"))
# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")

# #Multiplication Table using while loop:
# n=int(input("Enter the value:"))
# i=1
# while(i<=10):
#     result=i*n
#     print(i,"*",n,"=",result)
#     i=i+1


# Program to display the Fibonacci sequence up to n-th term
# n = int(input("Enter the terms: "))
# a, b = 0, 1
# count = 0
# if n <= 0:
#    print("Please enter a positive integer")
# elif n == 1:
#    print("Fibonacci sequence upto",n,":")
#    print(n)
# else:
#    print("Fibonacci sequence:")
#    while count < n:
#        print(a)
#        nth = a + b
#        # update values
#        a = b
#        b = nth
#        count += 1

#sum of N natural numbers:
# n=int(input("Enter the value:"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i=i+1
# print("The sum of first",n,"natural number is:",sum)

#prime Numbers:

# num=int(input("Enter the number:"))
# if num>1:
#     for i in range(2, num):
#         if num %2 ==0:
#             print(num,"is not a prime")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")

#pyramid program
rows=int(input("Enter the number:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
# n=int(input("Enter the value:"))
# sum=0
# i=1
# for i in range(0,n):
#     sum+=i
#     i=i+1
# print("The sum of natural number is:",sum)
        


