#global and local variables
#variables inside and outside the functions is called local and global variables
#A variable defined above the function and is accessible to the entire global space is called a global variable
#A variable defined inside the function is called local variable

#first case of global variable

'''
a=5
def check():
    print("inside value is",a)
check()
print("outside value is",a)
'''

#second case of global variable

'''
a=7
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)
'''

#third case of both global and variables

'''
a=2
b=8
def check2():
    a=4
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=20 #local variable
    b=b+a
    print("inside value of b is",b)
check2()
print("value of a is",a)
print("value of b is",b)
'''

#usage of global keyword

'''When user wants to access the global variable inside the function directly and carry forward the updated value
even outside the function then we need to use global keyword'''

'''
a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)
'''

#A generator is also a function which can be used as an iterator (loop) by producing group of values where we use yield keyword
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every successive iteration

'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        #yield a
print(*check(a,b))
'''

'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))
'''

#yield v/s return

'''
def mygen():
    #return "python"
    #return "java"
    #return "ds"
    return "python","java","ds"
print(*mygen())'''


'''
def mygen():
    yield "apple"
    yield "mango"
    yield "grapes"
print(*mygen())

#next
#to print line by line values
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#Stop iteration error

'''




    

