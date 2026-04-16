Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
a={"name":"Tripura","year":2026,"month":4}
type(a)
<class 'dict'>
b={"name","year"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['Tripura', 2026, 4])
a.items()
dict_items([('name', 'Tripura'), ('year', 2026), ('month', 4)])
#accessing and update
a={"year":2026,"month":4,"date":16}
a["month"]
4
a[2026]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[2026]
KeyError: 2026
a.update({"time":5})
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 5}
a.update({"time":5},{"min":30})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.update({"time":5},{"min":30})
TypeError: update expected at most 1 argument, got 2
a.update({"time":5,"min":30})
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 5, 'min': 30}
a={"name":"Tripura","mail":"doraemon@gmail.com"}
a.setdefault("city","kkd")
'kkd'
a
{'name': 'Tripura', 'mail': 'doraemon@gmail.com', 'city': 'kkd'}
a={"color":"blue","food":"biryani"}
a
{'color': 'blue', 'food': 'biryani'}
a.pop("color")
'blue'
a
{'food': 'biryani'}
a.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(0)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pop(0)
KeyError: 0
a={"city":"vja","country":"India"}
a.popitem()
('country', 'India')
a
{'city': 'vja'}
a.copy()
{'city': 'vja'}
>>> a
{'city': 'vja'}
>>> a.get("city")
'vja'
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"name":"Tripura"})
>>> b
{'name': 'Tripura'}
>>> a={"year":2026,"month":"April","name":"Tripura","name":"Tripura"}
>>> a
{'year': 2026, 'month': 'April', 'name': 'Tripura'}
>>> a={"year":2026,"month":"April","name":"Tripura","name":"sundari"}
>>> print(a)
{'year': 2026, 'month': 'April', 'name': 'sundari'}
>>> a={"year":2026,"month":"April","name":"Tripura","name1":"Tripura"}
>>> print(a)
{'year': 2026, 'month': 'April', 'name': 'Tripura', 'name1': 'Tripura'}
>>> #key must be different
>>> #It doesn't allow duplicate values
>>> a={"idnos":[10,20,30],"names":["ammu","sarvani","sundari"]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['ammu', 'sarvani', 'sundari']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['ammu', 'sarvani', 'sundari'])])
