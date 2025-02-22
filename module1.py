# def fun_name():
#     print("Hello")
# def fun_name1():
#     print("python")
# def fun_name2():
#     print("programming")


# def fun_name():
#     print("Welcome to python")
# def fun_name1():
#     print("Programming")
# def fun_name2():
#     print("Language")


# def add(a,b):
#     x=a+b
#     print("The addition of two numbers:",x)

# def sub(a,b):
#     y=a-b
#     print("The subtraction of two numbers:",y)

# def mul(a,b):
#     z=a*b
#     print("The Multiplication of two numbers:",z)


# from datetime import date
# tdate=date.today()
# print("Today date:",tdate)
# print("Current year:",tdate.year)
# print("Current month:",tdate.month)


# from datetime import datetime
# day_name=datetime.now()
# print("Today is:",day_name.strftime("%A"))


# import math
# print(math.sqrt(64))
# print(math.factorial(5))
# print(math.pow(5,2))


# from datetime import datetime,date,timedelta
# day_name=datetime.now()
# print("Today is:",day_name.strftime("%A"))

# from datetime import datetime,date,timedelta
# def add_days(n,d=datetime.today()):
#    return d+timedelta(n)
# x=add_days(25,date(2024, 11, 21))
# print("The 25 day is added:",x)



# from datetime import datetime,timedelta
# print("Current date:",datetime.now().date())
# print("date after 25 days:",(datetime.now()+timedelta(days=25)).date())

# print("Current date:",datetime.now().date())
# print("date before 5 days:",(datetime.now()-timedelta(days=5)).date())

import datetime
x=datetime.datetime.now()
print(x)

# 2. Get current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# 3. Get current time
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# 5. Creating a specific datetime object
specific_datetime = datetime.datetime(2024, 11, 28, 15, 30, 0)
print("Specific Date and Time:", specific_datetime)

# 4. Format the date and time
formatted_datetime = x.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# 6. Parse a string into a datetime object
date_string = "2024-11-28 15:30:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

# 7. Timedelta example (difference between two dates)
time_difference = x - specific_datetime
print("Time Difference:", time_difference)

# 8. Adding/subtracting time using timedelta
one_week = datetime.timedelta(weeks=-1)
new_date = x + one_week
print("One week from now:", new_date)



