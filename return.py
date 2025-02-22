# def add_num(a,b):
#     return a+b
# print("Addition of two numbers:",add_num(8,5))


# def largest_num(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>c and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
# print("The largest three numbers:",largest_num(10,20,15))


# def reverse_fun(x):
#     y=x[::-1]
#     return y
# print("The reverse function is:",reverse_fun("python"))


# def area_cir(r):
#     pi=3.14
#     return lambda a:pi*r**2
# doubler=area_cir(5)
# print("The area of circle:",doubler(3.14))



def vow_count(string):
    count=0
    vow_count="aeiou"
    for x in string:
        if(x in vow_count):
            count=count+1
    return count

print("The vowels counts are:",vow_count("Hello World"))



















# def sum_num(numbers):
#    return sum(numbers)
# print("The sum of number is:",sum_num([1,2,3,4,5]))


# def small_num(numbers):
#     smallest = numbers[0]
#     for x in numbers:
#         if x < smallest:
#             smallest=x
#             return smallest
# print("The smallest number is:",small_num([8,3,5,2,9]))



# def remove_num(numbers):
#     final_list=[] 
#     for val in numbers:
#         if val not in final_list:
#             final_list.append(val)
#     return final_list
        
# print(remove_num([1,2,2,3,4,4,5]))
