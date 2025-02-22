#sum of list
v=[5,10,20,25]
a=sum(v)
print(a)

#Multiplication of list
res=1
for val in v:
    res=res*val
print(res)
print('\n')

#find the largest and smallest number of list
small=min(v)
print(small)
large=max(v)
print(large)

#Join the strings
s= ['w','e','l','c','o','m','e',' ','p','y','t','h','o','n']
s1=''.join(s)
print(s1)
#Adding an elements in tuple
t=("Python",50,2.3)
print(t)
z=(2,4,7)
print("The elements of tuple are:",z)
z += (3,)
print("The new element is add in tuple",z)
print('\n')
#Multiplication of elements in tuple

#Removing an element from tuple
st=(5,3,9,26,15,24)
print("Original value :",st)
st1=list(st)
st1.remove(26)
st=tuple(st1)
print("After Removing 26:",st)
print('\n')
#Index of element in tuple
a=('p','r','o','g','r','a','m')
index=a.index('o')
print("Index of o:",index)
index=a.index('a')
print("Index of a:",index)
s=(5,3,9,26,15,24)
print("The length of Tuple is:",len(s))