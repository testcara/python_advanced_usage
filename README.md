### 迭代器和生成器
#### 可迭代对象
在python中最直接的判断一个对象是否是可迭代对象的最简单的方法如下：
```
In [5]: from collections import Iterable

In [6]: isinstance([], Iterable)
Out[6]: True

In [7]: isinstance('', Iterable)
Out[7]: True

In [8]: isinstance('{}', Iterable)
Out[8]: True

In [9]: isinstance('()', Iterable)
Out[9]: True
```
以上可知，我们常见的元组，列表，字典，字符串都是可迭代对象。但是他们是迭代器吗？不是。
#### 迭代器
在python中判断一个对象是否是迭代器的最直接的方法如下：
```
In [10]: from collections import Iterator

In [11]: isinstance('',Iterator)
Out[11]: False

In [12]: isinstance([],Iterator)
Out[12]: False

In [13]: isinstance({},Iterator)
Out[13]: False

In [14]: isinstance((),Iterator)
Out[14]: False
```
由上可知，我们常见的列表，字典，元组和字符串都不是迭代器。
但是，我们可以把通过以下手段变成迭代器：
```
In [15]: isinstance(iter(''),Iterator)
Out[15]: True

In [16]: isinstance(iter([]),Iterator)
Out[16]: True

In [17]: isinstance(iter({}),Iterator)
Out[17]: True

In [18]: isinstance(iter(()),Iterator)
Out[18]: True
```
对，我们可以通过iter()函数生成iterator对象。
Iterator对象表示的是一个数据流，其必须含有两个函数（__iter__和__next__, __iter__返回迭代器自己，__next__定义next()执行的操作)， iterator对象可以通过被next()函数调用并不断返回下一个值，直到没有数据抛出stopIteration。如下我们定义我们自己的迭代器：
```
In [84]: class OwnerIterator(object):
    ...:     def __iter__(self):
    ...:         return self
    ...:     def __next__(self):
    ...:         self.count += 1
    ...:         return self.count
    ...:     def __init__(self):
    ...:         self.count = 1
    ...:         
    ...:         

In [85]: isinstance(OwnerIterator(), Iterator)
Out[85]: True
In [87]: next(OwnerIterator())
Out[87]: 2
```
#### 生成器
迭代器的功能虽然强大，但是很多时候使用并不方便。我们可以理解为生成器是一个简单的可生成可迭代对象的函数，或者就理解为简单的迭代器。
在一个简单的函数里使用yield的关键字，可以实现一个最简单的生成器，此时这个函数变成了一个生成器函数，如下：
```
In [89]: def foo():
    ...:     yield
    ...:     

In [90]: g=foo()

In [91]: isinstance(g, Iterator)
Out[91]: True

In [92]: type(g)
Out[92]: generator
```
如上，我们获得一个生成器且我们还可以看出生成器是迭代器的子类。
让我们利用生成器做更多的实验。
我们都知道列表生成式：
···
In [138]: [x*x for x in range(10)]
Out[138]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
···
如我们在开头所说，让我们让生成器来实现并获取这些值。
方法1:
```
In [141]: g=(x*x for x in range(10))

In [142]: g
Out[142]: <generator object <genexpr> at 0x7fc0d6a93570>
In [159]: for n in g:
     ...:     print(n)
0
1
4
9
16
25
36
49
64
81
```
方法2:我们也可以使用如下yield函数来实现：
```
In [160]: def foo():
     ...:     i=0
     ...:     while i < 10:
     ...:         yield i * i
     ...:         i=i+1
     ...:         

In [161]: g=foo()

In [162]: for n in g:
     ...:     print(n)
     ...:     
0
1
4
9
16
25
36
49
64
81
```
