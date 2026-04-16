Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set
>>> #It is unordered,doesn't consider duplicate values
>>> a={3,4,4.5,"hi",6+9j,True,False}
>>> print(a)
{False, True, (6+9j), 3, 4.5, 4, 'hi'}
>>> type(a)
<class 'set'>
>>> b={7,9,6,5,4,34,7,9}
>>> type(b)
<class 'set'>
>>> print(b)
{34, 4, 5, 6, 7, 9}
>>> a={5,6,7,8}
>>> a.add(4)
>>> a
{4, 5, 6, 7, 8}
>>> #issubset()
>>> a={1,2,3,4,5,6}
>>> b={4,5,6}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
>>> #issuperset()
>>> a.issuperset(b)
True
>>> b.isuperset(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.isuperset(a)
AttributeError: 'set' object has no attribute 'isuperset'. Did you mean: 'issuperset'?
b.issuperset(a)
False
#union-> merging of two sets
a={3,4,5,6}
b={6,7,8,9}
a.union(b)
{3, 4, 5, 6, 7, 8, 9}
#intersection-> common elements
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.intersection(b)
{4, 5, 6}
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.difference(b)
{1, 2, 3}
b.difference(a)
{8, 7}
#update
a={1,2,3,4,5,6}
b={4,5,6,7}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7}
b
{4, 5, 6, 7}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7}
#symmetric_difference
a={3,4,5,6,7}
b={5,6,7,11,8}
a.symmetric_difference(b)
{3, 4, 8, 11}
b.symmetric_differencee(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b.symmetric_differencee(a)
AttributeError: 'set' object has no attribute 'symmetric_differencee'. Did you mean: 'symmetric_difference'?
b.symmetric_difference(a)
{3, 4, 8, 11}
a={11,12,13,14,15,16]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a={11,12,13,14,15,16}
b={7,8,9,10,11,12,13}
a.difference_update(b)
a
{16, 14, 15}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12, 13}
#intersection_update
a={2,3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.intersection_update(b)
a
{4, 5, 6, 7, 8}
b.intersection_update(a)
b
{4, 5, 6, 7, 8}
#symmetric_difference_update
a={1,2,3,4,5,6,7}
b={4,5,6,7,34,23,22,12}
a.symmetric_difference_update(b)
a
{1, 2, 3, 34, 12, 22, 23}
b.symmetric_difference_update(a)
b
{1, 2, 4, 5, 6, 7, 3}
#pop
a={1,2,3,4,5,6}
a.pop()
1
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a.remove(3)
a
{2, 4, 5, 6}
a={5,6,7,8}
a.discard(6)
a
{8, 5, 7}
a.copy()
{8, 5, 7}
b=a.copy()
b
{8, 5, 7}
a={7,8,9,0{
    
SyntaxError: '{' was never closed
a={7,8,9,0}
a.clear()
a
set()
b=set()
b.add(20)
b
{20}
c=a.copy()
c
set()
#isdisjoint
a={5,6,7,8}
b={1,2,3,4,5}
a.isdisjoint(b)
False
a={3,4,5,6}
b={8,9,0,1,2}
a.isdisjoint(b)
True
