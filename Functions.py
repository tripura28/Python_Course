#Function
'''
1)A function is a block of organised,reusable code and that is used to perform a single or multiple tasks
2)Python gives in built function like print(),you can make your own function also and these are called user defined functions.
3)A function block begin with the keyword "def" followed by a function name and paranthesis (())
'''

#basic form
'''
a=10
b=20
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is ",a*b)

a=100
b=200
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is ",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is ",a*b)'''

#using function

'''
def calculate(a,b):
    print("the sum is",a+b)
    print("the difference is",a-b)
    print("the product is ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)
        
'''

'''
def calculate(a,b):
    print("the Integer division is",a//b)
    print("the power is",a**b)
    print("the modulus is",a%b)
calculate(10,20)
calculate(100,200)
calculate(1,2)
'''

'''
def add(a,b):
    print(a+b)
add(4,5)
'''

'''
while True:
    def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    add()
'''

'''
def fullname():
    fname=input("first name:")
    lname=input("last name:")
    print((fname+" "+lname).title())
fullname()

'''

#print vs return
#print just shows the human user output in a console
#return is a keyword and return is used to terminate the function and gives back the value from the function

'''
def sub(a,b):
    print(a-b)
sub(3,8)
'''

'''
def sub(a,b):
    return a-b
print(sub(2,9))

'''
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(10,20)

'''

'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,6))
'''

#split bill

'''
def bill():
    n=int(input("enter amount:"))
    a=int(input("Total members:"))
    print(f"spliting of  bill for total {a} members is {n//a}")
bill()

'''

'''
def bill():
    n=int(input("enter amount:"))
    a=int(input("Total members:"))
    print("spliting of  bill for total {} members is {}".format(a,n//a))
bill()
'''

'''
def bill():
    n=int(input("enter amount:"))
    a=int(input("Total members:"))
    b=n//a
    print("spliting of  bill for total members is",b)
bill()
'''

'''
def bill(a,b):
    print("The bill is",b//a)
a=int(input("Total members"))
b=int(input("Total bill"))
bill(a,b)
'''

'''
def cal():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    c=int(input("choose a option 1.add 2.sub 3.mul"))
    if c==1:
          print('The sum is',a+b)
    elif c==2:
        print('The difference is ',a-b)
    elif c==3:
        print('The product is',a*b)
    else:
        print('Wrong option')
cal()

'''

'''
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    option=int(input("choose a option 1.add 2.sub 3.mul"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
    else:
        print('Invalid choice')
    
'''


#Railway Ticket

#passing parameter

'''
def senior_citizen_m(Ticket):
    a=(30/100)*Ticket
    print(round(Ticket-a))
def nrml_citizen_m(Ticket):
    print(Ticket)
def senior_citizen_f(Ticket):
    b=(50/100)*Ticket
    print(round(Ticket-b))
def nrml_citizen_f(Ticket):
    c=(30/100)*Ticket
    print(round(Ticket-c))
while True:
    def ticket_cal():
        name=input("enter name:")
        gender=input("Enter Gender M/F:")
        Age=int(input("Enter your Age:"))
        Ticket=1000
        if gender=="M":
                if Age>60:
                    senior_citizen_m(Ticket)
                else:
                    nrml_citizen_m(Ticket)
        elif gender=="F":
                if Age>60:
                    senior_citizen_f(Ticket)
                else:
                    nrml_citizen_f(Ticket)
        else:
            print("invalid choice")
    ticket_cal()

 '''       

#without parameter

'''
def senior_citizen_m():
    a=(30/100)*1000
    print(round(1000-a))
def nrml_citizen_m():
    print(1000)
def senior_citizen_f():
    b=(50/100)*1000
    print(round(1000-b))
def nrml_citizen_f():
    c=(30/100)*1000
    print(round(1000-c))

def ticket_cal():
    name=input("enter name:")
    gender=input("Enter Gender M/F:")
    Age=int(input("Enter your Age:"))
    if gender=="M":
        if Age>60:
            senior_citizen_m()
        else:
            nrml_citizen_m()
    elif gender=="F":
        if Age>60:
            senior_citizen_f()
        else:
            nrml_citizen_f()
    else:
        print("Invalid Choice")
ticket_cal()

'''


while True:
    def tick_calc():
        gender=input("Enter Gender M/F:").upper()
        Age=int(input("Enter your Age:"))
        tick=1000
        if gender=="F":
            if Age>60:
                a=tick-((50/100)*tick)
                print(round(a))
            else:
                b=tick-((30/100)*tick)
                print(round(b))
        elif gender=="M":
            if Age>60:
                b=tick-((30/100)*tick)
                print(round(b))
            else:
                print(tick)
        else:
            print("Invalid Gender!")
    tick_calc()
















    
    
    














    
