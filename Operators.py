Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithmetic
a=5
b=4
print(a+b)
9
print(a-b)
1
print(a*b)
20
print(a/b)
1.25
print(a//b)
1
print(a%b)
1
print(a**b)
625
#Assignment [It takes updated values}
a=3
b=4
b+=4
b
8
b+=a
b
11
b-=a
b
8
b*=a
b
24
b//=a
b
8
b/=a
b
2.6666666666666665
b%=a
b
2.6666666666666665
b**=5
b
134.84773662551436
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
137.84773662551436
#Comparision [Only True and False]
a=6
b=5
a<b
False
a>b
True
a<=b
False
a>=b
True
a1=b
a!=b
True
a==b
False
a=3
b=3
a==b
True
#Logical
a=7
b=11
a<b and a>b
False
a<=b and a>=b
False
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
a<=b or a>=b
True
not True
False
not False
True
#Identify
a=5
if type(a) is int:
    print("it is int")

    
it is int
b=4.5
if type(b) is int:
    print("It is int")

    
if type(b) is not int:
    print("It is float value")

    
It is float value
#Membership
a=2,2,3,4,5,6
if 5 in a:
    print(True)

...     
True
>>> if 23 in a:
...     print(23)
... 
...     
>>> if 23 not in a :
...     print(23)
... 
...     
23
>>> #Bitwise
>>> a=4
>>> b=8
>>> bin(4)
'0b100'
>>> bin(8)
'0b1000'
>>> a &b
0
>>> a|b
12
>>> ~a
-5
>>> # [~ it is negotiation and formula is -(x+1)]
>>> a^b
12
>>> a<<2
16
>>> a>>2
1
