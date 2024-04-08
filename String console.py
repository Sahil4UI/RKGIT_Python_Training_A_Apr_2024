Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String
x = "Welcome to RKGIT"
x = '''
Welcome
to
RKGI'''
print(x)

Welcome
to
RKGI
x = 'Python is a "high level" lang'
print(x)
Python is a "high level" lang
x = "Python is a \"high level\" lang"
print(x)
Python is a "high level" lang
#Indexing
x[0]
'P'
x[-3]
'a'
#slicing
x[0:5]
'Pytho'
x[0:6]
'Python'
x
'Python is a "high level" lang'
x[:6]
'Python'
x[:]
'Python is a "high level" lang'
x[::-1]
'gnal "level hgih" a si nohtyP'
x
'Python is a "high level" lang'
len(x)
29
x.upper()
'PYTHON IS A "HIGH LEVEL" LANG'
#immutable
x
'Python is a "high level" lang'
x.lower()
'python is a "high level" lang'
x.capitalize()
'Python is a "high level" lang'
x.title()
'Python Is A "High Level" Lang'
x.swapcase()
'pYTHON IS A "HIGH LEVEL" LANG'
x
'Python is a "high level" lang'
x = "Hello Welcome to Python Programming"
x.find("o")
4
x.rfind("o")
26
x.find("o",5)
10
x.index("o",5)
10
x.find("X")
-1
#-1 value not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'Hello Welcome to Python Programming'
x.replace("Python","JAVA")
'Hello Welcome to JAVA Programming'
x =
SyntaxError: invalid syntax
x
'Hello Welcome to Python Programming'
x.split()
['Hello', 'Welcome', 'to', 'Python', 'Programming']
len(x)
35
len(x.split())
5
x
'Hello Welcome to Python Programming'
x.split("o")
['Hell', ' Welc', 'me t', ' Pyth', 'n Pr', 'gramming']
x = x.split()
x
['Hello', 'Welcome', 'to', 'Python', 'Programming']
str(x)
"['Hello', 'Welcome', 'to', 'Python', 'Programming']"
x
['Hello', 'Welcome', 'to', 'Python', 'Programming']
" ".join(x)
'Hello Welcome to Python Programming'
"#".join(x)
'Hello#Welcome#to#Python#Programming'
x = "RKGIT"
x.center(6)
'RKGIT '
x.center(7)
' RKGIT '
x.center(20)
'       RKGIT        '
x.center(20,"*")
'*******RKGIT********'
x
'RKGIT'
z.fill(20)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    z.fill(20)
NameError: name 'z' is not defined
x.zfill(20)
'000000000000000RKGIT'
x = x.center(20,"*")
x
'*******RKGIT********'
x.lstrip("*")
'RKGIT********'
x.rstrip("*")
'*******RKGIT'
x.strip("*")
'RKGIT'
x = "hello"
x.islower()
True
x.isalpha()
True
x = "45"
x.isdigit()
True
>>> x ="435edfdfg"
>>> x.isalnum()
True
>>> x = "Hello Welcome to RKGIT"
>>> " ".join(x.split()[::-1])
'RKGIT to Welcome Hello'
>>> 
= RESTART: /Users/sahilkumar/Desktop/RKGIT A/Chatbot.py
Enter Message :hi
Hey...
