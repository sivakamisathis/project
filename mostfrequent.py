def most_frequent(numbers):
    return max(set(numbers),key=numbers.count)
x=input("Enter the list:")
numbers=list(x.split())
print("Original list")
print(numbers)
print("Items with maximum frequency of numbers in a list:")
print(most_frequent(numbers))