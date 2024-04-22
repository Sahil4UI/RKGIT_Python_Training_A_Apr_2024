Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Data Collection - 1.List is an ordered and mutable data collection which is non -homogeneous in nature
x = [1,2,3,4,5]
type(x)
<class 'list'>
x[-1]
5
x = [1,2,3,4,[5,6,7,[8,9,10,11]]]
x[4][3][2]
10
x[-1][-1][-2]
10
x[-1][-2]
7
#list comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [for i in range(1,11)]
SyntaxError: invalid syntax
x = [range(1,11)]
x
[range(1, 11)]
x = [ i for i in range(1,6)]
x
[1, 2, 3, 4, 5]
x.append(100)#it will store the value at the end
x
[1, 2, 3, 4, 5, 100]
x.insert(1,65)
x
[1, 65, 2, 3, 4, 5, 100]
x[-1] = "hey"
x
[1, 65, 2, 3, 4, 5, 'hey']
x.pop()#it will remove the last value
'hey'
x
[1, 65, 2, 3, 4, 5]
x.pop(0)
1
>>> x
[65, 2, 3, 4, 5]
>>> x.remove(65)# delete by value
>>> x
[2, 3, 4, 5]
>>> del x[0]
>>> x
[3, 4, 5]
>>> x.clear()
>>> x
[]
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = [23,456]
x.index(45)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.index(45)
ValueError: 45 is not in list
x.insert(45)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x.insert(45)
TypeError: insert expected 2 arguments, got 1
x.insert(1,23)
x
[23, 23, 456]
