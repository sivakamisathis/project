# for num in range(25, 51):
#     if num > 1:
#         for i in range(2, num):  
#             if num % i == 0:
#                 break  
#         else:
#             print(num) 



# list1 = [30, 50, 60]
# list2 = [40, 30, 10]

# for num1 in list1:  
#     for num2 in list2:  
#         if num1 == num2:  
#             print(f"Match found: {num1}")
#             break  
#         elif num1 > num2:  
#             print(f"Skipping {num1} > {num2}")
#             continue  
# print(f"Processing break and continue")



# x=[1,2,4,6,88,125]
# for i in x:
#     print(i,end=" ")





# num = 153
# num_str = str(num)
# num_length = len(num_str)  
# sum_of_powers = 0
# for digit in num_str:
#     sum_of_powers += int(digit) ** num_length  
# if sum_of_powers == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")






numbers = [10, 15, 22, 35, 40, 53, 60, 75]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        even_count += 1
    else:  # If the number is odd
        odd_count += 1
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")