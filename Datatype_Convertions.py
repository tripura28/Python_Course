Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype convertions
>>> #int
>>> int(4)
4
>>> int(9.4)
9
>>> int("Tripura")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Tripura")
ValueError: invalid literal for int() with base 10: 'Tripura'
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(4)
4.0
>>> float(9.3)
9.3
>>> float(4+3j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(4+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float("Code")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("Code")
ValueError: could not convert string to float: 'Code'
float(True)
1.0
float(False)
0.0
#String
str(3)
'3'
str(4.5)
'4.5'
str(4+5j)
'(4+5j)'
str("Try")
'Try'
str(True)
'True'
str(False)
'False'
#Complex
complex(2)
(2+0j)
complex(34.3)
(34.3+0j)
complex("Tripura")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("Tripura")
ValueError: complex() arg is a malformed string
complex(4+7j)
(4+7j)
complex(True)
(1+0j)
complex(False)
0j
#Boolean
bool(4)
True
bool(4.1)
True
bool("Tripura")
True
bool(3+7j)
True
bool(True)
True
bool(False)
False
