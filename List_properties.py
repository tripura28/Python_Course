Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"KKD",4+6j,True,False]
type(a)
<class 'list'>
print(a)
[3, 4.5, 'KKD', (4+6j), True, False]
b=9.0
type(b)
<class 'float'>
b=[4.5]
type(b)
<class 'list'>
a=["vjy","rjy","kkd"]
a.append(1)
a
['vjy', 'rjy', 'kkd', 1]
a.extend([3,4,5])
a
['vjy', 'rjy', 'kkd', 1, 3, 4, 5]
a.insert(3,2)
a
['vjy', 'rjy', 'kkd', 2, 1, 3, 4, 5]
a.append(2,3,4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append(2,3,4)
TypeError: list.append() takes exactly one argument (3 given)
a=["python","java","c"]
a.index("java")
1
a.copy()
['python', 'java', 'c']
a.clear()
a
[]
b=[]
b.append("html")
b
['html']
a=["dora","doraemon","nobitha","shizukha"]
a.sort()
a
['dora', 'doraemon', 'nobitha', 'shizukha']
a.reverse()
a.sort(reverse=False)
a
['dora', 'doraemon', 'nobitha', 'shizukha']
b=[1,4,5,3,5,3]
b.sort()
b
[1, 3, 3, 4, 5, 5]
b.reverse()
b
[5, 5, 4, 3, 3, 1]
b.sort()
b
[1, 3, 3, 4, 5, 5]
b.sort(reverse=False)
b
[1, 3, 3, 4, 5, 5]
>>> b.sort(reverse=True)
>>> b
[5, 5, 4, 3, 3, 1]
>>> #pop -> removes last value
>>> a=["black","blue","white"]
>>> a.pop()
'white'
>>> a.pop("blue")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop("blue")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(1)
'blue'
>>> a
['black']
>>> #pop -> it totally removes the value
>>> #remove
>>> a=["sweet","spicy","bitter"]
>>> a.remove("bitter")
>>> a
['sweet', 'spicy']
>>> a.count("sweet")
1
>>> b='python'
>>> len(b)
6
>>> b=["python"]
>>> len(b)
1
