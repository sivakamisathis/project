# def most_frequent(numbers):
#     return max(set(numbers),key=numbers.count)
# numbers=[1,2,2,3,3,3,4]
# print("Original list")
# print(numbers)
# print("Items with maximum frequency of numbers in a list:")
# print(most_frequent(numbers))


# def most_frequent(numbers):
#     return max(set(numbers),key=numbers.count)
# x=input("Enter the list:")
# numbers=list(map(int,x.split()))
# print("Original list")
# print(numbers)
# print("Items with maximum frequency of numbers in a list:")
# print(most_frequent(numbers))



def most_frequent(numbers):
    return max(set(numbers),key=numbers.count)
x=input("Enter the list:")
numbers=list(x.split())
print("Original list")
print(numbers)
print("Items with maximum frequency of numbers in a list:")
print(most_frequent(numbers))
