## Day-1: 生成器
一边循环一边计算的机制，就是生成器
生成器保存的是算法，每调用next(g)就计算出下一个元素的值，直到计算到最后一个元素，没有更多元素时，则抛出StopInteration的错误。
通常不会调用next(),因为会报异常。生成器也是可迭代对象，我们通常用for来控制输出。
```
g = (x * x for x in range(10))
for n in g:
    print(n)
```
普通函数遇到return返回，生成器遇到yield返回，遇到next时，继续执行yield处的语句。没有yield可执行时，则抛出StopInteration的错误。
```
In [1]: def odd():
   ...:     print('step 1')
   ...:     yield 1
   ...:     print('step 2')
   ...:     yield 3
   ...:     print('step 3')
   ...:     yield 5

In [2]: g = odd()
In [3]: next(g)
step 1
Out[3]: 1
In [4]: next(g)
step 2
Out[4]: 3
In [5]: next(g)
step 3
Out[5]: 5
In [6]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-e734f8aca5ac> in <module>()
----> 1 next(g)
StopIteration:
```
让我们来实现斐波拉契数列（Fibonacci), 普通函数的实现如下：
```
In [3]: def fib(max):
   ...:     n, a, b = 0, 0, 1
   ...:     while n < max:
   ...:         print(b)
   ...:         a, b = b, a + b
   ...:         n = n + 1
   ...:     return 'done'

In [4]: fib(6)
1
1
2
3
5
8
Out[4]: 'done'
```
则生成器函数的实现如下：
```
In [5]: def fib(max):
   ...:     n, a, b = 0, 0, 1
   ...:     while n < max:
   ...:         yield b
   ...:         a, b = b, a + b
   ...:         n = n + 1
   ...:     return 'done'
   ...: 
   ...: 

In [6]: fib(6)
Out[6]: <generator object fib at 0x7fca29f42c50>

In [7]: g=fib(6)

In [8]: for n in g:
   ...:     print(n)
   ...:     
1
1
2
3
5
8
```
若想获得返回值，则需要必须StopInteration异常，返回值包含在StopInteration的value中。如下：
```
g_return = fib_g(6)                                                                                                                                                                                              
while True:
  try:
      print(next(g_return))
  except StopIteration as e:
      print(e.value)
      break
```
则输出为：
```
1
1
2
3
5
8
done
```
在如上fib生成器，我们必须给循环设置一个条件，才能退出循环，不然就会产生一个无限序列出来。
所以，我们在编写生成器的时候，我们必须清楚终止条件。
