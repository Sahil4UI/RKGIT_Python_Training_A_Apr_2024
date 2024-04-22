Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#set - it is a mutable data collection
#it is unordered(no indexing) as like dictionary
#set cannot store duplicate values
x = (1,2,3,4)
x.add(100)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.add(100)
AttributeError: 'tuple' object has no attribute 'add'
x = {}
type(x)
<class 'dict'>
x  = {1,2,3,4,5}
type(x)
<class 'set'>
x
{1, 2, 3, 4, 5}
x[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x[0]
TypeError: 'set' object is not subscriptable
x.add(100)
x
{1, 2, 3, 4, 5, 100}
x.remove(100)
x
{1, 2, 3, 4, 5}
x = {1,1,1,1,2,2,2,2,3,3,3,4,4,4}
x
{1, 2, 3, 4}
x.clear()
x
set()
x
set()
x.add(20)
x
{20}
x.add(100)
x
{100, 20}
x.add(43)
x
{100, 43, 20}
x = {1,2,3,4}
y = x
x
{1, 2, 3, 4}
y
{1, 2, 3, 4}
id(x)
4387741184
id(y)
4387741184
x.remove(3)
x
{1, 2, 4}
y
{1, 2, 4}
from copy import deepcopy
x
{1, 2, 4}
y = deepcopy(x)
x
{1, 2, 4}
y
{1, 2, 4}
x.remove(4)
x
{1, 2}
y
{1, 2, 4}
id(x)
4387741184
id(y)
4387741632
x = {'a','b','c','d','e','f'}
x
{'a', 'f', 'd', 'b', 'c', 'e'}
x = {'a','b','c'}
x
{'c', 'b', 'a'}
x = {'a','b','c','d'}
x
{'c', 'b', 'a', 'd'}
x = {'A','B','c','d','e','H'}
x
{'A', 'B', 'd', 'H', 'c', 'e'}
#methods
x = {1,2,3,4}
y = {3,4,5,6}
x+y#union - all
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x+y#union - all
TypeError: unsupported operand type(s) for +: 'set' and 'set'
x.update(y)
x
{1, 2, 3, 4, 5, 6}
x = {1,2,3,4}
y
{3, 4, 5, 6}
x.union(y)
{1, 2, 3, 4, 5, 6}
x.intersection(y)#common
{3, 4}
x.intersection_update(y)
>>> x
{3, 4}
>>> x = {1,2,3,4}
>>> x
{1, 2, 3, 4}
>>> x
{1, 2, 3, 4}
>>> y
{3, 4, 5, 6}
>>> x - y
{1, 2}
>>> x.difference(y)
{1, 2}
