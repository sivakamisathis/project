def fun_name(fno,sno):
    print("The output is:",+fno+sno)

fun_name(8,5)



def largest(a,b,c):
    if(a>b and a>c):
        print("largest no is:",+a)
    elif(b>c and b>a):
        print("The largest no is:",+b)
    elif(c>a and c>b):
        print("The largest no is:"+c)

largest(10,20,15)


def area_cir(r):
    pi=float(3.14)
    a=pi*r**2
    print("The area of circle is:", +a)

area_cir(5)


def vow_count(string):
    count=0
    vow_count="aeiou"
    for x in string:
        if(x in vow_count):
            count=count+1
    print("The count is:",+count)

vow_count("Hello World")


def sum_num(numbers):
   print("The sum of five nos:",sum(numbers))
sum_num([1,2,3,4,5])


def calculate_sum(numbers):
    total=0
    for x in numbers:
        total+=x
    print("The sum of numbers:",total)

calculate_sum([1,2,3,4,5])



def small_num(numbers):
    smallest = numbers[0]
    for x in numbers:
        if x < smallest:
            smallest=x
    print("The smallest element is:",smallest)
small_num([8,3,5,2,9])


def remove_num(numbers):
    final_list=[] 
    for val in numbers:
        if val not in final_list:
            final_list.append(val)

    print("The final list is:",final_list)
remove_num([1,2,2,3,4,4,5])


def rev_str(x):
    y=x[::-1]
    print("The reversed string is:",y)

rev_str("python")    




