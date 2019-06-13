### Python enum数据类型
在python中有些数据类型，，在刚开始学习的时候，会觉得搞的不太清楚。
入enum， tuple, set等数据类型。
#### enum枚举类型
枚举类型用来定义一个有多种固定取值的一个常量，如季节，月份，性别等。
我们可以用以下两种方式获得枚举对象：
* 直接声明和定义变量
	In [1]: from enum import Enum

	In [2]: Tender = Enum('Tender', ('Male','Female'))

	In [3]: Tender.Male
	Out[3]: <Tender.Male: 1>

	In [4]: Tender(1)
	Out[4]: <Tender.Male: 1>

	In [5]: Tender.Male.name
	Out[5]: 'Male'

	In [6]: Tender.Male.value
	Out[6]: 1

	In [9]: for name, member in Tender.__members__.items():
	   ...:     print("name:{}, member_name:{}, member_value:{}".format(name,member.name,member.value))
	name:Male, member_name:Male, member_value:1
	name:Female, member_name:Female, member_value:2
我们看到枚举对象的value属性的默认值从1开始。
如果我们觉得从1开始有问题，可以使用下一种方法，用类来定义，来自己定义value属性的默认值
如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
* 自定义类
	In [1]: from enum import Enum

	In [2]: class Tender(Enum):
	...:     Female = 'Female'
	...:     Male = 'Male'
	...:     

	In [3]: Tender.Female
	Out[3]: <Tender.Female: 'Female'>

	In [4]: Tender.Female.name
	Out[4]: 'Female'

	In [5]: Tender.Female.value
	Out[5]: 'Female'

	In [6]: Tender.Male.value
	Out[6]: 'Male'
