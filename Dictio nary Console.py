Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#for , for each , while
x =
SyntaxError: invalid syntax
x = "Welcome to RKGIT"
for i in range(len(x)):
    print(x[i],end=",")

W,e,l,c,o,m,e, ,t,o, ,R,K,G,I,T,
for i in x:
    print(i,end=",")

W,e,l,c,o,m,e, ,t,o, ,R,K,G,I,T,
x = [1,2,3,4,56,678,689]
for i in x:
    print(i,end=" ")

1 2 3 4 56 678 689 
#Tuple - python's immutable and ordered data collection
x = (1,2,3,4,5)
type(x)
<class 'tuple'>
x[0]=100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x[0]=100
TypeError: 'tuple' object does not support item assignment
x = (1,1,1,2,2,3,4,5,6)
x.index(1)
0
x.count(1)
3
min(x)
1
max(x)
6
sum(x)
25
for i in x:
    print(i)

1
1
1
2
2
3
4
5
6
x= [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = (i for i in range(1,11))
#generator object
x
<generator object <genexpr> at 0x105607e80>
for i in x:
    print(i)

1
2
3
4
5
6
7
8
9
10
#Dictionary
x = {"id":101,"name":"ravi","marks":90}
type(x)
<class 'dict'>
#dictionary is mutable and unordered
x[0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x[0]
KeyError: 0
x
{'id': 101, 'name': 'ravi', 'marks': 90}
x['id']
101
x.get('id')
101
x
{'id': 101, 'name': 'ravi', 'marks': 90}
x.keys()
dict_keys(['id', 'name', 'marks'])
x.values()
dict_values([101, 'ravi', 90])
x.items()
dict_items([('id', 101), ('name', 'ravi'), ('marks', 90)])
x
{'id': 101, 'name': 'ravi', 'marks': 90}
for i in x:
    print(i,x[i])

id 101
name ravi
marks 90
x
{'id': 101, 'name': 'ravi', 'marks': 90}
len(x)
3
x
{'id': 101, 'name': 'ravi', 'marks': 90}
#keys cannot be duplicate
x['contact'] = 9876543210
x
{'id': 101, 'name': 'ravi', 'marks': 90, 'contact': 9876543210}
>>> x['contact'] = 0#update
>>> x
{'id': 101, 'name': 'ravi', 'marks': 90, 'contact': 0}
>>> x.pop('contact')
0
>>> x
{'id': 101, 'name': 'ravi', 'marks': 90}
>>> x.popitem()#it will remove last key value pair
('marks', 90)
>>> x
{'id': 101, 'name': 'ravi'}
>>> del x['name']
>>> x
{'id': 101}
x.clear()
x
{}
del x
x
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x
NameError: name 'x' is not defined
