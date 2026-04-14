Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#Count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("little")
1
a.count("k")
2
a.count(" ")
3
a.count("star")
1
#find a string
a="code"
a.find("d")
2
a.find("c")
0
b="codegnan"
b.find("n")
5
b[5]+b[7]
'nn'
b.find("4")
-1
#escape sequences
#\n-> new line
#\t-> tab space
a="name\nmobileno\tmailid\naddress"
a
'name\nmobileno\tmailid\naddress'
print(a)
name
mobileno	mailid
address
b="name:Tripura\nmobileno:8328524298\tmailid:sundaritripura44@gmail.com\nKakinada"
print(b)
name:Tripura
mobileno:8328524298	mailid:sundaritripura44@gmail.com
Kakinada
#t -> The tab space between 4 to 8
#replace
a="Wait until you succeed"
a.replace("Wait","Work")
'Work until you succeed'
#upper() and lower()
a="programming"
a.upper()
'PROGRAMMING'
b="institution"
b.lower()
'institution'
c="work hard"
c.title()
'Work Hard'
c.capitalize()
'Work hard'
d="i am in class"
d.title()
'I Am In Class'
x="hello"
x.isupper()
False
x.islower()
True
x.startswith()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.startswith()
TypeError: startswith expected at least 1 argument, got 0
x.startswith("h")
True
x.endswith("o")
True
x.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d="python123"
d.isalnum()
True
e="python@123"
e.isalnum()
False
y=1234
y.isdigit()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    y.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
x="1234"
x.isdigit()
True
#Split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="I am learning python full stack"
b.split()
['I', 'am', 'learning', 'python', 'full', 'stack']
#Join()
a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'
#strip()-> removing of white spaces
#lstrip(),rstrip()
a="     Tripura   "
a.strip()
'Tripura'
a.lstrip()
'Tripura   '
a.rstrip()
'     Tripura'
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="tripura"
lname="bojja"
print(fname+lname)
tripurabojja
print(fname+" "+lname)
tripura bojja
print((fname+" "+lname).title())
Tripura Bojja
print(fname.title()+lname.title())
TripuraBojja
#formatting-> we had to add one additional string
a=2
>>> b=5
>>> print("The product of numbers is",a*b)
The product of numbers is 10
>>> print("The square of a is",a**2)
The square of a is 4
>>> #format()
>>> a="motu"
>>> b="patlu"
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {}\nhello {}.format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {}\nhello {}".format(a,b))
...       
hello motu
hello patlu
>>> #fstring
...       
>>> a="chota"
...       
>>> b="bheem"
...       
>>> print(f"hello {a}{b}")
...       
hello chotabheem
>>> print(f"hello {a} hello {b}")
...       
hello chota hello bheem
