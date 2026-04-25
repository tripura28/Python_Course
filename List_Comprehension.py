#List Comprehension
#Every list comprehension can be rewritten as a for loop but every for loop cannot be rewritten in list comprehension.

a=["python","java","dsa"]
#["PYTHON","JAVA","DSA"]

'''
b=str(a)
c=b.upper()
print(c)

'''
'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]

'''
a=[i.upper() for i in a]
print(a)
'''

'''
b=["hyd","vzg","vja"]
c=[i.capitalize() for i in b]
print(c)
'''

'''
a=[1,2,4,5,6,8,12,13]
b=[i**2 for i in a]
c=[pow(i,2) for i in a]
d=[i*i for i in a]
print(b)
print(c)
print(d)

'''

#if-usage in list comprehension
'''
a=[i for i in range(16) if i%2==0]
print(a)
'''

'''fruits=["apple","banana","mango","grapes","kiwi","berry"]
b=[i for i in fruits if "a" in i]
print(b)'''

#no-elif usage in list comprehension

#if-else usage in list comprehension

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)
'''














