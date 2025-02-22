country_code={"india":10,"Aus":11,"canada":12}
print(country_code)
x=country_code["india"]
y=country_code["canada"]
print(x)
print(y)
country_code["Italy"]=14
print(country_code)
del country_code["Aus"]
print(country_code)
country_code["india"]=20
print(country_code)
for country in country_code:
    print(country)
print()
for country in country_code:
    code=country_code[country]
    print(code)
print(len(country_code))
element=country_code.pop("india")
print('popped country_code:',element)
print("The dictionary is:",country_code)
#elment=country_code.pop("japan")
element=country_code.pop("dubai","china")
print("The popped element is:",element)
print("The dictionary is:",country_code)
