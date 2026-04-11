Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing [It means accessing an element]
a="Kakinada"
a[0]
'K'
a[1]
'a'
a[2]
'k'
a[3]
'i'
a[4]
'n'
a[5]
'a'
a[6]
'd'
a[7]
'a'
a[8]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[8]
IndexError: string index out of range
a[0]+a[1]+a[2]+a[3]+a[4]
'Kakin'
b="I am in Heaven"
b[0]
'I'
b[4]
' '
b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
'Heaven'
c="I am learning python"
a[2]+a[3]
'ki'
c[2]+c[3]
'am'
c[5]+c[6]+c[7]+c[8}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
c[5]+c[6]+c[7]+c[8]
'lear'
c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
d="I am in work"
d[5]+d[6]
'in'
d[8]+d[9]+d[10]+d[11]
'work'
d[2]+d[3]
'am'
d[2]+" "+d[3]
'a m'
a="simple is better than complex"
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
x="codegnan it solutions"
x[-21]+x[-20]+x[-19]+x[-18]+x[-17]+x[-16]+x[-15]+x[-14]
'codegnan'
x[-9]+x[-8]+x[-7]+x[-6]+x[-5]+x[-4]+x[-3]+x[-2]+x[-1]
'solutions'
x[-12]+x[-11]
'it'
#Slicing
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
b="work hard until you succeed"
b[17:20]
'ou '
b[16:19]
'you'
b[21:]
'ucceed'
b[20:]
'succeed'
b[10:15]
'until'
b[5:9]
'hard'
b[0:4]
'work'
y="Beautiful is better than ugly"
y[13]
'b'
y[13:19]
'better'
y[25:]
'ugly'
y[0:9]
'Beautiful'
x="Patience is strength"
x[-8:-1]
'strengt'
x[-1]
'h'
x[-0]
'P'
x[-8:]
'strength'
x[:-14]
'Patien'
x[:-16]
'Pati'
x[-20:-12]
'Patience'
b="sun rises in the east"
b[-8:-5]
'the'
b[-4:]
'east'
b[-17:-12]
'rises'
>>> b[-21:-18]
'sun'
>>> #Striding
>>> a="Cloud computing"
>>> a[::5]
'C u'
>>> a[::3]
'Cucpi'
>>> a[3:]
'ud computing'
>>> a[:9]
'Cloud com'
>>> a[::7]
'Cog'
>>> a[5:11]
' compu'
>>> a[::2]
'Codcmuig'
>>> # In negative striding lowest to highest is not possible
>>> # In postive striding highest to lowest is not possible
>>> a="python course"
>>> a[8:4:2]
''
>>> a[-7:-6:-4]
''
>>> a[-1:]
'e'
>>> a[::-1]
'esruoc nohtyp'
>>> a[::1]
'python course'
