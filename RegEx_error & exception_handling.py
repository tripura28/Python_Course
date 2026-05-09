#Regular Expressions
'''
Regular expressions are powerful tools [module] embedded in python which is mainly used to find a pattern
within a given string or statements or files and we mainly used for text manipulation
'''

'''
a="codegnan is in vja"
print(a)

b="codegnan\nis\tin\nvja"
print(b)
'''

#rstring[raw string-> no modifications]
'''
a=r"codegnan\nis\tin\nvja"
print(a)
'''

#compile(),search(),findall(),split(),sub()
#sequence characters

'''
\w-> it matches alphanumeric
\W-> it matches non-alphanumeric
\d-> it matches any digit
\D-> it matches non-digit
\s-> it represents white spaces
\S-> it represents non-white spaces
'''

#import re
#a="cap cash map money mat maths cat dog donkey cup"
'''
b=re.compile(r"m\w\w\w")
print(b)
c=b.search(a)
print(c)
'''
'''
b=re.search(r"m\w+",a)
print(b)
'''

#findall
'''
c=re.findall(r"m\w+",a)
print(c)

#to unpack
print(*c)

'''

#split()
'''
d=re.split(r"m",a)
print(d)

d=re.split(r"\s",a)
print(d)
'''

#sub()
'''
e=re.sub(r"maths","science",a)
print(e)
'''

#digit
'''
import re
b="cat doll 1monkey 2mat 24 45 89 222 333 444 888"
x=re.findall(r"\d+",b)
print(x)

y=re.findall(r"\D+",b)
print(y)
'''

#error handling
'''
1) syntax error-> complie error
2) runtime error-> during execution time it will happens
3) logical error-> error in logic(it can't visible)
'''

#syntax error
'''
for i in range(10)
print(i)

'''

#runtime error
'''
a=int(input("a value"))
b=int(input("b value"))
print(a//b)
'''

#logical error
'''
a=10
b=20
print(a-b)
'''

'''
a=3
b=7
if a>b:
    print('less')

'''


#Exception handling
#try
'''
Instructions from which we are expecting the exceptions'''
#except
'''
Exceptions are raised in try block it will be handle by this block'''
#else
'''
optional(no-exceptions)'''
#finally
'''
always'''

'''
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends....")

'''

