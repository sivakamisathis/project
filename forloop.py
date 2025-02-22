# i=1
# while(i<=10):
#     print(i)
#     i+=1
# else:
#     print("The number is exceed")



# rows= 7
# for i in range(1, rows +1 ):
#     for j in range(1,i-1):
#         print(j, end=" ")
#     print()




a=[5,2,7,4,8,3,9] 
x=[]
for i in a[::-1]:
    x.append(i)
print(x)



x=[1,2,4,6,88,125]
for i in x:
    print(i,end=" ")

for num in range(25, 51):
    if num > 1:
        for i in range(2, num):  # Check divisors from 2 to num-1
            if num % i == 0:
                break  # Skip to the next number if divisible
        else:
            print(num)  # Print if no divisor is found


list1 = [30, 50, 60]
list2 = [40, 30, 10]

for num1 in list1:  # Outer loop
    for num2 in list2:  # Inner loop
        if num1 == num2:  # If numbers are equal
            print(f"Match found: {num1}")
            break  # Exit the inner loop immediately
        elif num1 > num2:  # If num1 is greater
            print(f"Skipping {num1} > {num2}")
            continue  # Skip the rest of the inner loop and go to the next num2
print(f"Processing break and continue")


# Input number
num = 153
# Convert number to string to process each digit
num_str = str(num)
num_length = len(num_str)  # Get the number of digits

# Initialize sum
sum_of_powers = 0

# Loop through each digit
for digit in num_str:
    sum_of_powers += int(digit) ** num_length  # Raise each digit to the power of the number's length and add to sum

# Check if the sum equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# Series of numbers
numbers = [10, 15, 22, 35, 40, 53, 60, 75]

# Initialize counters
even_count = 0
odd_count = 0

# Loop through each number in the series
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        even_count += 1
    else:  # If the number is odd
        odd_count += 1

# Output the results
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")





