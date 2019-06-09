### yield
在后面生成器的定义和讲解中，yield是最关键的，我们来了解下yield这个关键字的用法。
yield是一种特殊的return, 一般的return，而yield return的是个生成器。让我们根据下面这个函数，来看下yield的用法
```
In [108]: def foo():
     ...:     print("Starting...")
     ...:     while True:
     ...:        res = yield 4
     ...:        print("res:", res)
```
第一次执行，结果为：
```
In [109]: g = foo()

In [110]: type(g)
Out[110]: generator

In [111]: print(g)
<generator object foo at 0x7fc0d6b50678>
```
调用next,结果为：
```
In [112]: next(g)
Starting...
Out[112]: 4
```
程序开始执行，yield变成return，直接返回其后面的值
```
In [113]: next(g)
res: None
Out[113]: 4
```
则我们可以看出程序开始重复
```
return 4
print("res:", res)
```
让我们总结下yield的整个过程：
程序正常执行至yield，返回一个generator,则每一个next都执行yield后面的代码块，知道不能迭代
