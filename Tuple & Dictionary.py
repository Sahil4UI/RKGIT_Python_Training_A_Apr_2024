Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Tuple->Python's immutable data type
x = []
type(x)
<class 'list'>
x = (1,2,3,4)#tuple
type(x)
<class 'tuple'>
#tuple is a Python's Immutable Data Collection
x
(1, 2, 3, 4)
x[3]
4
x[0:3]
(1, 2, 3)
x[0]=100
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[0]=100
TypeError: 'tuple' object does not support item assignment
x = (1,2,3,4,5,1,1,1,1,1)
x.index(2)
1
x.count(1)
6
#Dictionary - key value pair separated by commas enclosed inside {}
x = {"id":101,"name":"Ravi"}
x.keys()
dict_keys(['id', 'name'])
x.values()
dict_values([101, 'Ravi'])
x.items()
dict_items([('id', 101), ('name', 'Ravi')])
x
{'id': 101, 'name': 'Ravi'}
x["contact"] = 9876543221
x
{'id': 101, 'name': 'Ravi', 'contact': 9876543221}
x["contact"] = 981234567
x
{'id': 101, 'name': 'Ravi', 'contact': 981234567}
x.popitem()#it will remove last key value pair
('contact', 981234567)
x
{'id': 101, 'name': 'Ravi'}
x.pop("name")
'Ravi'
x
{'id': 101}
>>> del x['id']
>>> x
{}
>>> x = {'id': 101, 'name': 'Ravi'}
>>> x.clear()
>>> x = {'id': 101, 'name': 'Ravi'}
>>> for i in x:
...     print(i)
... 
id
name
>>> for i in x:
...     print(i,x[i])
... 
id 101
name Ravi
>>> x["name"]
'Ravi'
