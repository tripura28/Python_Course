#conditions
#if condition by using comparision operators
#<,>,<=,>=,==,!=

'''a=2
b=4
if a<b:
    print("it is less")'''

'''a=2
b=4
if a>b:
    print("it is less")'''


'''a=5
b=10
if a<=b:
    print("true")'''


'''a=7
b=11
if b>=a:
    print("greater")'''


'''a=2
b=4
if a!=b:
    print("it is less")'''


'''a=10
b=10
if a==b:
    print("it is equal")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''


'''a=int(input("a value"))
if a<15:
    print("less")'''

'''a="python"
if a!="java":
    print("true")'''

'''a="python"
if a=="python":
    print("true)'''

'''a=input("name")
if a=="Tripura":
    print("true")'''
    

#if condition by using logical operators
#and, or, not

'''a=9
b=12
if a<b and b>a:
    print("true")'''

'''a=9
b=12
if a<=b and b>=a:
    print("true")'''


'''a=20
b=30
if a!=b and b==a:
    print("true")'''


'''a=4
b=8
if a<b or b>a:
    print("true")'''


'''a=5
b=10
if a<=b or b>=a:
    print("true")'''


'''a=9
b=12
if a!=b or b==a:
    print("true")'''


'''a=6
b=9
if not a<b:
    print("it is less")'''


'''a=6
b=9
if not a>b:
    print("it is less")'''
    

'''a=int(input("enter age:"))
if a>=18:
    print("major, you can vote!")'''

#identity operator
#is,isnot

'''a=8
if type(a) is int:
    print("it is int")'''


'''a=8
if type(a) is not int:
    print("it is not int")'''

'''a=int(input("enter the value"))
if type(a) is int:
    print("true")'''

    
'''a=3.4
if type(a) is float:
    print("float")'''


'''a=input("enter value:")
if type(a) is float:
    print("it is a float")'''

#membership operator
#in, not in

'''a=[2,3,4,5,5]
if 7 in a:
    print("true")'''


'''a=[3,4,5,5,2,6]
if 5 not in a:
    print("true")'''


'''a=[3,4,5,6,2]
if 10 not in a:
    print("true")'''


'''a=[3,4,5,6,7,3,8,9]
b=int(input("enter a value:"))
if b in a:
    print("true")'''


#if-else conditions by using comparision

'''a=5
b=10
if a<b:
    print("a is less")
else:
    print("b is big")'''


'''a=5
b=10
if a>b:
    print("a is small")
else:
    print("b is big")'''


'''a=10
b=10
if a==b:
    print("Equal")
else:
    print("not equal")'''


'''a=5
b=10
if a!=b:
    print("a is not equal to b")
else:
    print("equal")'''


#if-else conditions by using logical

'''a=9
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''


'''a=9
b=12
if a!=b or b==a:
    print("true")
else:
    print("false")'''


'''a=20
b=14
if not (a<b and b>a):
    print("true")
else:
    print("false")'''


#if-else conditions by using identity operators

'''a=9
if type(a) is int:
    print("it is int")
else:
    print("false")'''


'''a=45.3
if type(a) is not int:
    print("it is not int")
else:
    print("false")'''


#if-else conditions by using membership operators

'''a=[10,20,30,40,50]
if 10 in a:
    print("true")
else:
    print("false")'''


'''a=[10,20,30,40,50]
if 10 not in a:
    print(" no 10")
else:
    print("10")'''

#if-elif conditions by using comparision

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")'''
    

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")'''

'''a=2
b=2
if a<b:
    print("less")
elif b>a:
    print("greater")
elif b==a:
    print("equal")'''


#if-elif conditions by using logical

'''a=2
b=4
if a<b and b<a:
    print("less")
elif b<a or a>b:
    print("greater")
elif not a==b or a<b:
    print("true")'''

#if-elif conditions by using identity

'''a="kfjd"
if type(a) is int:
    print("int")
elif type(a) is float:
    print("float")
elif type(a) is not (float and int):
    print("string")'''

#if-elif conditions by using membership

'''a=[21,23,24,25,28,22]
if 20 in a:
    print("20")
elif 20 not in a:
    print("add 20")'''


#if-elif conditions by using comparision

'''a=8
b=9
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''


#if-elif-else conditions by using logical

'''a=5
b=5
if a<b and b>a:
    print("true")
elif a==b or a!=b:
    print("equal or not")
elif not a<b:
    print("false")
else:
    print("no condition satisfied")'''

#if-elif-else conditions by using identity

'''a="2"
if type(a) is int:
    print("int")
elif type(a) is float:
    print('float')
else:
    print("string")'''

#if-elif-else conditions by using membership

'''a=[10,20,30,34,23,21]
if 11 in a:
    print("11")
elif 20 not in a:
    print("add 20")
else:
    print(a)'''

#multiple-if conditions

'''a=3
b=9
if a<b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''

'''a=3
b=9
if a>b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''


#multiple-if conditions by using logical

'''a=4
b=5
c=3
if a<b and a<c:
    print("a is small")
if a>b and a>c:
    print("a is big")
if b>c and b>a:
    print("b is big")'''


'''a=4
b=5
c=3
if a!=b and a!=c:
    print("a is small")
if a>b and a>c:
    print("a is big")
if b>c and b>a:
    print("b is big")'''

#multiple-if conditions by using identity

'''a=3
b=4
c=a
if a is b:
    print("a is b")
if a is not b:
    print("a is not b")
if a is c:
    print("a is c")'''
    

'''a=3
b="4"
c=a
if type(a) is type(b):
    print("a is b")
if type(a) is not type(b):
    print("a is not b")
if type(a) is not type(c):
    print("a is c")'''

#multiple-if conditions by using membership

'''a=[1,2,3,4]
b=4
if b in a:
    print("yes")
if b not in a:
    print("no")'''

'''a=[1,2,3,4]
b=10
if b in a:
    print("yes")
if b not in a:
    print("no")'''


#nested-if conditions

'''a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")'''


'''a=10
b=15
if a>b:
    print("less")
    if b>a:
        print("greater")'''


'''a=5
b=10
if a>b:
    print("less")
    if b==a:
        print("greater")'''


'''a=5
b=10
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")'''


'''a=5
b=10
if a>b:
    print("less")
    if b>a:
        print("greater")
else:
    print("true")'''           


'''a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''


'''a=7
b=12
if a<b:
    print("less")
    if a==b:
        print("equal")
    elif a>=b:
        print("not equal")
    else:
        print("true")
else:
    print("false")'''
    


