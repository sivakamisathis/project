# x=0
# y=1
# while y<50:
#     print(y)
#     x,y=y,x+y

# def sum(x,y):
#     sum=x+y
#     if sum in range(15,20):
#         return 20
#     else:
#         return sum
# print(sum(10,6))
# print(sum(10,2))
# print(sum(10,12))

# a=int(input("Enter the first no:"))
# b=int(input("Enter the second no:"))
# a=a+b
# b=a-b
# a=a-b
# print("After swappling")
# print("First no:",a)
# print("second no:",b)

num=int(input("Enter the first no:"))
sum_of_digit=0
while num>0:
    digit=num%10
    sum_of_digit+=digit
    num=num//10
    print("sum of digits:",sum_of_digit)