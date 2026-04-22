#loops
#for,while,range,break,continue,pass
#for loop

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=(5,6,7,8,9,10)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={3,4,5,6,7,8}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"pooja","year":2026,"month":"april"}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))

for i in a.values():
    print(i)
    print(type(a))
    print(type(i))

for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''


'''a="codegnan"
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4.5,6.7,8.9]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=["apple","banana","grapes"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[5+6j,3+3j]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#Task
'''a=["codegnan","python","course"]
b=[]
for i in a:
    b.append(i.upper())
print(b)'''

'''a=["codegnan","python","course"]
b=str(a)
c=b.upper()
print(c)'''

'''a=["codegnan","python","course"]
b=[x.upper() for x in a]
print(b)'''

'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=" ")'''


'''#condition based task
#student analysis
n=int(input("enter marks:"))
if n>=91 and n<=100:
    print('Grade - A')
elif n>=81 and n<=90:
    print('Grade - B')
elif n>=71 and n<=80:
    print('Grade - c')
elif n>=50 and n<=70:
    print('Grade - D')
else:
    print('Fail')'''


#While loop
'''a=10
while a<1:
    print("true")'''


'''a=10
while a>1:
    print("true")'''

'''a=10
while a>1:
    print(a)'''


'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    a=a-1
    print(a)'''

'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=30
while a>2:
    print(a)
    a=a+1'''

#eligible for vote

'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''


#even or odd
'''while True:
    num=int(input("enter the number"))
    if num%2==0:
        print('it is even')
    else:
        print('it is odd')'''


#the range() returns a sequence of numbers, starting from zero by default and increaments by one by one and stops before a specified number
#start-stop-step

'''for i in range(5):
    print(i)'''

'''for i in range(5,15):
    print(i)'''
    
'''for i in range(2,20,2):
        print(i,end=" ")'''
        
'''for i in range(5,50,5):
        print(i,end=" ")'''

'''for i in range(0,30,3):
        print(i,end=" ")'''


'''while True:
    n=int(input())
    if n in range(91,101):
        print('Grade - A')
    elif n in range(81,91):
        print('Grade - B')
    elif n in range(71,81):
        print('Grade - c')
    elif n in range(50,71):
        print('Grade - D')
    else:
        print('Fail')'''


#Difference between break,continue,pass.
#The break statement is used to terminate the entire loop
#The continue statement is used to skips the current iteration and rest of the code will continue
#A pass is a null statement it does nothing but syntatically we need

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''for i in range(20):
    if i==12:
        break
    print(i)'''

#continue
'''a=30
while a>5:
    print(a)
    a=a-1
    if a==20:
        continue'''

'''a=30
while a>5:
    a=a-1
    if a==20:
        continue
    print(a)'''

'''for i in range(15):
    if i==9:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
        break
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
        continue
    print(i)'''

#pass

'''a=40
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass'''

'''for i in range(40):
    if i==20:
        pass
    print(i)'''


