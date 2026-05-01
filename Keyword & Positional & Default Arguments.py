#keyword and positional arguments

'''
def details(id,name,mailid):
    id=10
    name='Tripura'
    mailid='s@gmail.com'
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
'''

'''
def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="uday",mailid="u@gmail.com")
details(id=30,name="surya",mailid="s@gmail.com")
details(40,"jnana","j@gmail.com")
details(name='sundari',mailid='s@gmail.com',id=50)
'''

#default arguments

'''
def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",200)'''

'''
def Grocery(item="rice",price=1000):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''
def Grocery(item,price=500):
    print("item is %s" %item)
    print("price is %d" %price)
Grocey("ghee")
'''

'''
def Grocery(item="dhal",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(200)

 #correct form is

def Grocery(price,item="dhal"):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(200)

'''

#cake,price,quantity

'''
def bakery(cake="blackforest",price=300,quantity="2kg"):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %s" %quantity)
bakery()
'''

'''
def bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %s" %quantity)
bakery(cake="strawberry",quantity="2kg",price=400)

'''
'''
def bakery(cake,price=300,quantity="2kg"):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %s" %quantity)
bakery("chocolate")
'''

#error raises

'''
def bakery(cake="blackforest",price,quantity="2kg"):
    print("cake is %s" %cake)
    print("price is %d" %price)
    print("quantity is %s" %quantity)
bakery(200)
'''

# *arguments-> * is used to unpack the elements
'''
a=[2,3,4,5,5,6]
print(a)
print(*a)

'''

'''
b=(6,7,8,9)
print(b)
print(*b)'''

'''
c={5,6,7,8,9}
print(c)
print(*c)
'''

'''
d={"year":2026,"month":4}
print(d)
print(*d) #Returns only keys
'''

'''a="codegnan"
print(a)
print(*a)'''

'''
a,b,c=2,3,4,5,5,6,7,8,10
print(a)
print(b)
print(c)''' #value error

'''
a,b,c=5,6,7
print(a)
print(b)
print(c)

'''

'''
a,*b,c=2,3,4,5,5,6,7,8,10
print(a)
print(*b)
print(c)

'''

'''
a,b,c="codegnan"
print(a)
print(b)
print(c)
''' #value error

'''
a,b,c="cod"
print(a)
print(b)
print(c)
'''

#bmi calculator
'''
weight=float(input("enter weight:"))
height=float(input("enter height in meter:"))
Bmi=weight/height**2
print("BMI is %.f" %Bmi)
if Bmi<18.5:
    print("Under Weight")
elif 18.5<=Bmi<24.5:
    print("Healthy weight")
elif 24.5<=Bmi<=29.5:
    print("Over weight")
else:
    print("Obesity")
    

 '''

#variable length arguments
#It automatically stores in tuple and we use *arguments
#In real world examples are aadhar,pan,etc..,[storing standard information]
'''
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,4,5)
b=[1,2,3,4,5,6]
check(*b)
c={5,6,7,6,8,9}
check(*c)
d={"name":"sundari","year":2026}
check(*d)
'''

'''
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5.6,4.7)
check1(1,3,5,4.5,2.5,"tripura")'''


'''
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in [int,float]:
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5.6,4.7)
check1(1,3,5,4.5,2.5,"tripura")

'''

#kwargs(**)


'''
def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)
'''


'''
def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)
'''

'''
def multiple(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d+=i
        print(d)
    for i in b:
        print(i,b[i])
    
a=[3,24,2]
b={"name":"kdfj","age":34}
multiple(*a,**b)
data=(2,3,4.1,5.2)
multiple(*data)
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
multiple(**details)
multiple(*data,**details)

'''


