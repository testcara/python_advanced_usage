### python 装饰器
#### 为什么要用到装饰器
在项目中，我们会遇到过以下场景：
针对不同的组件或者函数，我们需要进行统一处理，例如希望输出相同格式的日志信息，性能相关信息等。如果没有装饰器，我们可能就需要针对所有的组件和函数进行编辑和调整，让其满足我们的功能。当文件很多时或者很久没有维护时，这还将是一件非常繁重的工作，且又增加了代码的维护成本。
装饰器就帮我们很好的解决了这个问题。简单的讲，我们只需要将这些本身和代码逻辑不太相关的装饰作用的普遍使用的功能进行封装，然后用这个封装后的函数去装饰我们已经有的功能函数或者模块就可以达到我们的目的。这样操作，不会影响到原来代码的完整性，也不会其增加额外的维护成本，且如果我们需要对这些额外功能进行修改的话，只需要修改修饰器本身就可以解决问题了，非常方便有木有。
### 闭包函数
在介绍装饰器的实现之前，我们先来了解内嵌函数和闭包函数。
* 内嵌函数
    定义在一个函数内部的函数，我们称为内嵌函数。
    ```
    def outFunc():
        print("I am the outside function!")
    
        def innerFunc():
            print("I am the inner function!")
            
    outFunc()
    ```
    则输出结果为：
    ```
    Press ENTER or type command to continue
    I am the outside function!
    
    real	0m0.051s
    user	0m0.043s
    sys	0m0.009s
    
    Press ENTER or type command to continue
    ```
* 闭包函数
    当内部函数引用了外部函数或者外部函数之外定义的对象（非全局变量），这个内部函数就是闭包函数。闭包函数所引用的外部定义的变量叫做自由变量。如下：
    ```
    def outFunc():
        num_a = 1
    
        def innerFunc():
            numb_b = 2
            return num_a + numb_b
        return innerFunc()
    
    
    print(outFunc())
    ```
    则获得输出为：
    ```
    Press ENTER or type command to continue
    3
    
    real	0m0.057s
    user	0m0.047s
    sys	0m0.010s
    
    Press ENTER or type command to continue
    ```
### python装饰器
python装饰器本质也是一个函数，它可以在其他函数不需要做任何代码变动的前提下增加额外的功能，装饰器的返回值也是一个函数对象。
装饰器装饰函数的过程为：装饰器的外部函数传入要装饰的函数名字，装饰函数对其进行装饰后，返回装饰后的函数名字。
python装饰器有很多经典的应用场景，比如：插入日志，性能测试，事务处理，权限校验等。我们将这些特定功能的代码组装称不同功能的装饰器，然后针对不同场景使用特定的装饰器，使得模块各司其职，逻辑清晰。
* 用装饰器装饰函数
    ```
    import logging
    import time
    import os
    
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    log = logging.getLogger('my-logger')
    
    
    def decorator(func):
        log.info(func.__name__)
    
        def wrappper(*args, **kargs):
            log.info(time.time())
            func()
            log.info(time.time())
        return wrappper
    
    
        @decorator
        def func():
            print("I am the main fuction")
    
    
        func()
    ```
   则执行结果为：
   ```
    Press ENTER or type command to continue
    INFO:my-logger:func
    INFO:my-logger:1559701620.1038325
    I am the main fuction
    INFO:my-logger:1559701620.1038926
    
    real	0m0.056s
    user	0m0.044s
    sys 	0m0.012s
    
    Press ENTER or type command to continue
   ```
* 用装饰器装饰类
    ```
    import logging
    import time
    import os
    
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    log = logging.getLogger('my-logger')
    
    
    def decorator(func):
        log.info(func.__name__)
    
        def wrappper(one_instance):
            log.info(time.time())
            func(one_instance)
            log.info(time.time())
        return wrappper
    
    
    class Method(object):
        @decorator
        def func(self):
            print("I am the main fuction")
    
    
    p1 = Method()
    p1.func()
    ```
无论是装饰函数还是装饰类中函数，我们都需要保证我们的装饰器函数的参数和我们要修饰的函数的参数一致。
## 装饰器链
一个函数可能同时被多个装饰器装饰，其执行顺序为由近及远。
```
def makeBold(f):
    def wrapper():
        return "<b>" + f() + "</b>"
    return wrapper


def makeItalic(f):
    def wrapper():
        return "<i>" + f() + "</i>"
    return wrapper


@makeBold
@makeItalic
def report():
    return "Hello World!"

print(report())
```
输出为：
```
Press ENTER or type command to continue
<b><i>Hello World!</i></b>

real	0m0.048s
user	0m0.040s
sys	0m0.008s

Press ENTER or type command to continue
```
## 内部装饰器
除了我们自定义的装饰器，python还有如下内部装饰器：

* @staticmethod: 类的静态方法，根成员方法的区别是没有self参数，并且可以在类不能进行实例化的情况下调用
* @classmethod: 跟成员方法的区别是接受第一个参数不是self,而是cls（当时类的具体类型）
* @property: 表示可以直接使用类实例直接访问的信息
