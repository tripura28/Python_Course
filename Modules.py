#math module
'''
import math
print(math.pi)

print("pi:",math.pi*3)

print("sqrt:",math.sqrt(2))

print("log:",math.log(10))

print("sin:",math.sin(30))

print("cos:",math.cos(60))

print("pow:",math.pow(2,3))

print("acos:",math.acos(-1))

print("tan:",math.tan(45))

print("ceil:",math.ceil(3.8))

print("floor:",math.floor(5.8))
'''

'''
we need to take a interpreter or another complier and write
from math import sqrt,pi,log
then we can directly use the sqrt without giving it as the math.pi
'''

'''
#sys module
import sys
print(sys.path)

'''

'''
import sys

for i in sys.path:
    print(i)

print(sys.version)


import os
print(os.path)
'''

#Type module doc in below search and you will get all info about modules

'''
print("getcwd:\n",os.getcwd())
print("listdir:\n",os.listdir())
print("mkdir:\n",os.mkdir('may12'))
print("listdir:\n",os.listdir())
'''

#random module
#To generate random number in python, randint() is used this function is defined in random module
#python defines a set of functions that are used to generate or manipulate random numbers through the random module

#random module
#sample is a attribute , 5 is written because we want 5 numbers from range
'''
import random
a=random.sample(range(10,30),5)
print(a)

import random
a=random.randint(20,40)
print(a)

import random
b=[10,20,30,40,50]
a=random.choice(b)
print(a)

'''

#dice

'''
import random
while True:
    a=int(input("enter the roll of dice:"))
    b=random.randint(1,7)
    print(b)
    c=input("enter 1.yes 2.no")
    if c=="yes":
        continue
    elif c=="no":
        break
    else:
        print("invalid")

'''


#calender module
'''
import calendar
year=2006
month=1
print(calendar.month(year,month))'''

#import calendar
'''
year=2006
print(calendar.calendar(year))
'''

'''
year=int(input("enter year:"))
month=int(input("enter month:"))
print(calendar.month(year,month))
'''

'''
year=int(input('enter year:'))
print(calendar.calendar(year))

'''

#data & time
'''
from datetime import date
a=date.today()
print(a)
'''

'''
import datetime
a=datetime.datetime.now()
print(a)
'''
'''
import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"weekday is {b.tm_wday},year day is {b.tm_yday} and {b.tm_isdst}")
'''

'''
import time
import random

for i in random.sample(range(10),10):
    print(i)
    time.sleep(2)

'''

#or

'''
import time
import random
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)
'''


#Attendance Report

'''
a=int(input("Number of Students:"))
ab=0
pr=0
for i in range(1,a+1):
    b=input(f"student-{i}:")
    if b=="p":
        pr+=1
    else:
        ab+=1   
print("Total number of students:",a)
print("Present:",pr)
print('absent:',ab)
'''






