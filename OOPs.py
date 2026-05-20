#OOPs
'''
A class contains attributes or variables and methods or functions that can manipulate the data.
A class is the blueprint of an object.
An object is an initiation of a class.
Methods are functions defined inside the body of the class.
'''

#Four pillars of OOPs
'''
1)Polymorphism
In polymorphism we have four type that are:-
-Operator overloading
-Operator overriding
-Method overloading
-Method overriding


2)Inheritence
In inheritence we have 3types:
-single inheritence
-multiple inheritence
-multi level inheritence


3)Encapsulation
In encapsulation combine multiple units into single unit
we have 3types:
 ->  Public data
 ->  _protected data
 ->  __Private data
   

4)Abstraction
Hiding unnecessary information from the user is known it as a abstraction.
-> Abstract class
If a class contains one or more than one abstract method is known it as a abstract class
-> Abstract Method
If the method is declared without implimentation is called abstract method
'''

#oops syntax
'''
class classname:
    name="codegnan"
    place="vja"
    year=2026
    def fname(method_name):
        print("statements.....")
a=classname()
a.fname()
'''

#class declaration

'''
class details():
    name="Tripura"
    age=20
    year=2006
    def display(self):
        print(self.name,self.age,self.year)
a=details()
print(dir(a))
a.display()
'''

#object instantiation

'''
class details:
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.Data("Tripura",20,"kkd")
a.display()
b=details()
b.Data("Reddy",21,"rjy")
b.display()
c=details()
c.Data("Sundari",21,"vjy")
c.display()'''


#object Initialization
'''
class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("sundari",20,"vja")
print(dir(a))
a.display()

a=input("enter name:")
b=int(input("enter age:"))
c=input("enter place:")
d=details(a,b,c)
d.display()


x=details(input("enter name:"),int(input("enter age:")),input("enter place:"))
x.display()
'''


'''
class details():
    #creating a constructor
    def __init__(self):
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
        self.place=input("enter place:")
    def display(self):
        print(self.name,self.age,self.place)
a=details()
a.display()

'''

#diff b\w _ and __
'''
we generally use it for private variables that means whenever we use "__" for a variable our python interpreter treats it
it as a special variable to avoid name conflicts with methods and inner classes''' 

'''
class Employee():
    def __init__(self):
        self.name="sundari"
        self._mailid="sundari12@gmail.com"  #protected
        self.__salary=40000 #private
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)

'''

'''
class Employee():
    def __init__(self):
        self.name="sundari"
        self._mailid="sundari12@gmail.com"
        self.__salary=40000
        
class Employee1():
    def __init__(self):
        self.name="tripura"
        self._mailid="sundari12@gmail.com"
        self.__salary=80000

class Employee2():
    def __init__(self):
        self.name="jnana"
        self._mailid="jnana12@gmail.com"
        self.__salary=90000
a=Employee()
b=Employee1()
c=Employee2()
print(dir(a))
print(a.name)
print(b.name)
print("employee2 salary:",c._Employee2__salary)
print("employee salary:",a._Employee__salary)
'''

#Polymorphism
#operator overloading [same operator with different properties]

'''
a=2; b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(3))
print(a.__le__(5)) #less than
print(a.__ge__(2)) #greater than


a=[1,2,3,4]; b=[5,6,7,8]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(2))


a="code"; b="gnan"
print(a.__add__(b))


a="python"; b="course"
print(a.__add__(" "+b).title())
print("tripura".__add__(" "+"bojja").title())

'''

#operator overriding

'''
class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(3)
#x=5
#y=2
print(x+y)
'''

#Method Overloading

'''
class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is",a+b+c)
        elif a!=None and b!=None:
            print("The product is",a*b)
        else:
            print("Program Ends")
x=New()
x.sum()
x.sum(2,3,4)
x.sum(5,6)
'''

#Method Overriding

'''
class Animal():
    def speak(self):
        print("Animal can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()

'''
#another example

'''
class vehicle():
    def sound(self):
        print("No vehicle No sound")
class Auto():
    def sound(self):
        print("Auto sound! watch and walk")
class Lorry():
    def sound(self):
        print("Lorry sound! go away")
class car():
    def sound(self):
        print("car sound! Take a look at the car")
        
a=vehicle()
b=Auto()
c=Lorry()
d=car()
a.sound()
d.sound()
c.sound()

'''

#Single Inheritance

'''
class RBI(): #parent class
    cash=100000
    def available_cash(cls):
        print("Available cash is",cls.cash)
        print("Availbale cash is",RBI.cash)
class SBI(RBI): #child-1
    pass
class HDFC(RBI): #child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()

'''

#multiple Inheritance

'''
class Father():
    height=165
    def length(self):
        print("height of father is",self.height)
class Mother():
    weight=56
    def weig(self):
        print("weight of mother is",self.weight)
class kid(Father,Mother):
    dob="28-1-2006"
    def date(self):
        print("Date of birth is",self.dob)
a=kid()
a.date()
a.weig()
a.length()
'''

'''
class Father():
    height=float(input("enter height"))
    def length(self):
        print("height of father is",self.height)
class Mother():
    weight=int(input("enter weight:"))
    def weig(self):
        print("weight of mother is",self.weight)
class kid(Father,Mother):
    dob=input("enter dob:")
    def date(self):
        print("Date of birth is",self.dob)
a=kid()
a.date()
a.weig()
a.length()

'''

#multi-level

'''
class grandparent():
    def given(self):
        print("Grand parent had 10acers")
class parent(grandparent):
    def taken(self):
        print("Parents had house")
class child(parent):
    def received(self):
        print("child had debts")
b=child()
b.given()
b.taken()
b.received()
'''

#Encapsulation
#public data

'''
class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()
        
'''

#_protecteddata()

'''
class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
        
'''

#__privateddata()

'''
class parent():
    __privatedata="sundari"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()
'''

#Abstraction
'''
class parent():
    def method1(self):
        pass
obj1=parent()
obj1.method1()'''


'''
class parent():
    def method1(self):
        print("python full stack")
obj1=parent()
obj1.method1()'''


'''
from abc import ABC,abstractmethod
class parent():
    #@abstractmethod
    def method1(self):
        print("data")
obj1=parent()
obj1.method1()

'''

'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''#ERROR


'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj=B()
obj.method1()
obj.method2()
obj.method3()
'''













