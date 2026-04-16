Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(3,4.5,'python',5+4j,True,False)
>>> print(a)
(3, 4.5, 'python', (5+4j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count("python")
1
>>> len(a)
6
>>> a.index(True)
4
