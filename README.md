### 函数式编程
#### 编程范式
所谓编程范式，指的是计算机编程的基本风格和典范模式。编程是为了解决问题，而解决问题有多种视角和思路，其中普遍适用且行之有效的模式称之为范式。面向对象编程，面向过程编程等都是编程范式。每种范式都引导人们带着某种倾向去分析问题，解决问题。如果把一门编程语言比作一门武功，它的语法，工具和技巧等是招法，它采用的编程范式则是心法。
一种范式可以在不同的语言中实现，一种语言也可以支持多种范式。比如php可以通过面向对象编程，也可以面向过程编程。任何语言在设计时都会倾向于某种范式，而回避某些范式，由此形同不同的语法特征和语言风格。
#### python多范式编程
python支持面向对象编程和函数式编程
* 面向对象编程
将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性，灵活性和扩展性，核心概念有多态，集成和封装。
* 函数式编程
一种以数学函数为编程语言建模为核心的编程范式，其将计算机运算视为数学函数运算，并且避免使用程序状态以及可变对象。函数是函数式编程的基石，函数式编程语言的代码就是由一个个的函数组合而成的。函数作为参数传入另一个函数，返回一个函数在函数编程中都是基本功能。
### python高阶函数
高阶函数（函数作为参数）是函数式编程的核心。python支持的高阶函数有：
* map
    map函数对每一个元素调用func
    ```
    map(func, iteratable objects)
    ```
    示例如下：
    ```
    In [16]: def dou(x): 
        ...:     return x*x 
        ...:                                                        
    In [17]: list(map(dou, [1,2,3]))                                    
    Out[17]: [1, 4, 9]
    ```
* reduce
    reduce函数每次拿一个元素和之前func返回的值作为参数传递给func
    ```
    reduce(func, iterable objects)
    例如：
    reduce(func, [x1,x2,x3,x4])=
    func((func(x1,x2),x3),x4)
    ```
    示例如下：
    ```
    In [6]: from functools import reduce                              
    In [7]: def sum(x,y): 
       ...:     return x+y 
    In [8]: reduce(sum, [1,2,3])                                                                                 
    Out[8]: 6
    ```
    python 3之后，reduce已经不是内置函数，需要从functools倒入。
    reduce函数返回的是一个终值。
* filter
    将func作用域每个元素，根据func返回true或者false来决定是否保留该元素。
    ```
    filter(func, iterable objects)
    ```
    示例如下：
    ```
    In [18]: def get_odd(x): 
        ...:     if x%2==0: 
        ...:         return True 
        ...:     else: 
        ...:         return False
    In [19]: list(filter(get_odd, [1,2,3,4,5,6,7]))                     
    Out[19]: [2, 4, 6]
    ```
* sorted
    依据func对整个列表或者其他可遍历数据进行排序
    ```
    sorted(iterable_objects, key=lambda x: )
    ```
    示例如下：
    ```
    In [26]: sorted([-1,3,2, -2, -5, 5, 1],key=lambda x: abs(x))
    Out[26]: [-1, 1, 2, -2, 3, -5, 5]
    ```
#### lambda函数
我们在上例中用到了lambda函数，即匿名函数。
匿名函数也是函数，只是由于特别简单，不需要显示定义成函数。
如在高阶函数示例中，我们都可以使用lambda来代替简单的用法。
```
In [27]:  list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7])) 
Out[27]: [2, 4, 6]
In [29]:  reduce(lambda x,y:  x+y, [1,2,3])          
Out[29]: 6
In [37]: list(map(lambda x:x*x, [1,2,3]))
Out[37]: [1, 4, 9]
In [38]: reduce(lambda x,y:x+y, map(lambda x:x*x, [1,2,3]))         Out[38]: 14
```
