# a=5
# b=7
# c=a+b
# print("The addition of two numbers:",c)
# square root
# import math
# x=16
# y=math.sqrt(x)
# print(y)
#Area of triangle
# a=5
# b=6
# c=7
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print("The area of triangle is %0.2f" %area)


# swap two variables
a=5
b=6
x=a
a=b
b=x
# print("After swapping the value of a is :{}" .format(a))
# print("After swapping the values of b is :{}" .format(b))
print(f"After swapping the value of a is:{a}")
print(f"After swapping the values of b is:{b}")

#without using temporary variabls:
# a=5
# b=6
# a=a+b
# b=a-b
# a=a-b
# print("After swapping:")
# print("After swapping a value:",a)
# print("After swapping b value:",b)




# #swap case:
# name="SiVaKAmI"
# print(name.swapcase())
# s1="THIS IS A PROGRAM"
# print(s1.swapcase())
# s2="python language"
# print(s2.swapcase())
# s3="ThiS iS a pYthON prOGRAMming laNGUage"
# print(s3.swapcase())
















#fibonacci series between 0 and 50
# x,y=0,1
# while y<50:
#     print(y)
#     x,y=y,x+y

#sum of two integers.If the sum is between 15 and 20 it will return 20
# def add_sum(x,y):
#     sum=x+y
#     if sum in range(15,20):
#         return 20
#     else:
#         return sum
    
# print(add_sum(10,12))
# print(add_sum(10,7))
# print(add_sum(10,15))

# #sum of digits of a number
# num=int(input("Enter the number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
#     print("The sum of digits are:",sum)
'''def count_words(siva1.txt):
    with open(siva1.txt, 'r') as file:  # Open the file in read mode
        text = file.read()  # Read the entire content of the file
        words = text.split()  # Split the text into words using whitespace
        word_count = len(words)  # Count the number of words
        return word_count

# Specify the file path
filename = 'siva1.txt'  # Replace with the actual file name you want to read

# Count words in the file and print the result
count = count_words(siva1.txt)
print(f"The number of words in the file '{filename}' is: {count}")
'''