Marks=int(input("Enter the Marks:"))
if(Marks>90):
    print("Grade:A")
elif(Marks>80 and Marks<=90):
    print("Grade:B")
elif(Marks>=60 and Marks<=80):
    print("Grade:C")
else:
    print("Grade below 60")


cp=int(input("Enter the Cost price:"))
if(cp>100000):
    print("The tax is 15%:",cp*15/100)
elif(cp>50000 and cp<=100000):
    print("The tax is 10%:",cp*10/100)
elif(cp<=50000):
    print("The tax is 5%:",cp*5/100)


year=int(input("Enter the year:"))
if (year %4==0 and year %100!=0 or year %400==0):
    print("The year is leap year")
else:
    print("The year is not a leap year")


num=int(input("Enter the number:"))
if num==1:
    print("The day is Sunday")
elif num==2:
    print("The day is Monday")
elif num==3:
    print("The day is Tuesday")
elif num==4:
    print("The day is Wednesday")
elif num==5:
    print("The day is Thursday")
elif num==6:
    print("The day is Friday")
elif num==7:
    print("The day is saturday")




a=int(input("Enter a value:"))
if (a %2==0):
    print("The number is Even")
else:
    print("The number is odd")




num=15
factorial=1
if num < 0:
    print("Factorial does not exist for Negative")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num, "is",factorial)


a=5
b=7
if(a>b):
    print("a is greater than b")
    pass


p=10000
print("The p value is:",p)
n=5
print("The n value is:",n)
r=5
print("The r value is:",r)
SI=p*n*r/100
print("The simple interest is:",SI)
#[P (1 + r/100)n] – P
e=p*(1+r/100)**5
print(f"The e value is {e:.2f}")
CI=e-p
print(f"The compound interest is {CI:.2f}")



          

