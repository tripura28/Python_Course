Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
#A variable is a container which we store the data in a particular memory location it is known it as a variable.
print(3+4)
7
a=7
b=2
print(a+b)
9
b=89
print(b)
89
c=34
print(c)
34
x=56
print(y)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(y)
NameError: name 'y' is not defined
print(x)
56
z=50
print(Z)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
a01234=490
print(a01234)
490
@3=59
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
_t=45
print(_t)
45
_=50
print(_)
50
name="Tripura"
print(name)
Tripura
city="kkd"
print(city)
kkd
print("name")
name
country="India"
print(country)
India
#Don't use keywords as a variable if we use they give error like below
if=30
SyntaxError: invalid syntax
else=45
SyntaxError: invalid syntax
a,b=4,5
print(a,b)
4 5
a=6, b=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=5
print(a,b)
4 5
print(a+b)
9
a,b,c=2,3,3,1,4
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a,b,c=2,3,3,1,4
ValueError: too many values to unpack (expected 3, got 5)
first_name="pooja"
print(first_name)
pooja
firstname="sundari"
print(firstname)
sundari
a=8
print(a)
8
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> fname="Tripura"
>>> lname="B"
>>> print(fname+lname)
TripuraB
>>> print(fname+" "+lname)
Tripura B
>>> print(fname,lname)
Tripura B
>>> age=45
>>> print(age)
45
>>> Age=20
>>> print(age)
45
>>> print(Age)
20
>>> a,b=5,6
>>> print(a,b)
5 6
>>> del (a,b)
>>> print(a,b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(a,b)
NameError: name 'a' is not defined
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
