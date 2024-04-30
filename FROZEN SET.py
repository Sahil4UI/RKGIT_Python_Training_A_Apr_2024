Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #frozenset
>>> x = {1,2,3,45}
>>> y = frozenset(x)
>>> x
{1, 2, 3, 45}
>>> y
frozenset({1, 2, 3, 45})
>>> x.remove(45)
>>> x
{1, 2, 3}
>>> y.remove()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    y.remove()
AttributeError: 'frozenset' object has no attribute 'remove'
#frozen set is a immutable version of set
