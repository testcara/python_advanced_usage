## 容器与collections模块

### python中的对象类型
* 基本数据类型：Numbers, String, bool, None
* 复合数据类型：类，函数, enum
* 容器：list, set, tuple, dict

### 容器和collections模块

在python中，在某些对象中包含了对其他对象的引用，这样的对象被称为容器。
除了以上我们列出的四种标准容器外，我们还可以使用collections使用特定目标容器，
作为标准容器对象的替代方案。我们来对collections模块提供的几个数据类型来进行学习。

* namedtuple

	生成一个类似于字典的有键值对组成的不可变的对象。

	```
	In [1]: from collections import namedtuple

	In [2]: Animal=namedtuple('Animal','name age type')

	In [5]: type(Animal('xiaoming',18,'dog'))
	Out[5]: __main__.Animal

	In [6]: a=Animal('xiaoming',18,'dog')

	In [7]: print(a)
	Animal(name='xiaoming', age=18, type='dog')

	In [8]: a.name
	Out[8]: 'xiaoming'

	In [9]: a.age
	Out[9]: 18

	In [10]: a.type
	Out[10]: 'dog
	```
	Line 2生成了一个不可辨的类似于字典的对象。

* double-ended queue

	双端队列，可以从两端实现插入和移除。我们在处理列表时，其时间复杂度为o(n)，也就时说随着元素的增加，其时间复杂度也是直线上升的。而实现双向队列，时间
	复杂度为o(1)，当你的代码有这样的性能需求时，记得使用双端队列。现在让我们来
	举例双端队列的应用。

	```
	In [1]: from collections import deque

	In [2]: a_list = deque([1,2,3])

	In [3]: a_list.append(4)

	In [4]: a_list
	Out[4]: deque([1, 2, 3, 4])

	In [5]: a_list.appendleft(0)

	In [6]: a_list
	Out[6]: deque([0, 1, 2, 3, 4])

	In [7]: print(a_list)
	deque([0, 1, 2, 3, 4])

	In [8]: type(a_list)
	Out[8]: collections.deque

	In [9]: a_list.rotate(-1)

	In [10]: a_list
	Out[10]: deque([1, 2, 3, 4, 0])

	In [11]: a_list.rotate(1)

	In [12]: a_list
	Out[12]: deque([0, 1, 2, 3, 4])

	In [13]: a_list.popleft()
	Out[13]: 0

	In [14]: a_list
	Out[14]: deque([1, 2, 3, 4])
	```

* OrderedDict

	创建字典，并支持调整顺序。

	```
	In [99]: a = OrderedDict.fromkeys('cdea')

	In [100]: a.move_to_end('d')

	In [101]: a
	Out[101]: OrderedDict([('c', None), ('e', None), ('a', None), ('d', None)])

	In [102]: a.move_to_end('d', last=False)

	In [103]: a
	Out[103]: OrderedDict([('d', None), ('c', None), ('e', None), ('a', None)])

	In [104]: a = OrderedDict.fromkeys({'d':'1','a':'2'})

	In [105]: a
	Out[105]: OrderedDict([('d', None), ('a', None)])

	In [106]: a = OrderedDict({'d':'1','a':'2'})

	In [107]: a.move_to_end('d')

	In [108]: a
	Out[108]: OrderedDict([('a', '2'), ('d', '1')])
	```

* defaultDic

	当我们用dict[]这种方式获取字典元素时，字典不存在该元素，则会报错。使用defaultDic定义该字典，则不会报错，而会返回我们默认值。

	```
	In [46]: from collections import defaultdict

	In [47]: a=defaultdict(int)

	In [48]: a['name']='cara'

	In [49]: a
	Out[49]: defaultdict(int, {'name': 'cara'})

	In [50]: a['name']
	Out[50]: 'cara'

	In [51]: a['testing']
	Out[51]: 0

	In [52]: a.setdefault('default value')

	In [53]: a
	Out[53]: defaultdict(int, {'name': 'cara', 'testing': 0, 'default value': None})

	```
* Counter

	用来统计字符串所有出现的字符的个数。

	```
	In [54]: from collections import Counter
	    ...: 
	    ...: s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and th
	    ...: eir counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is simil
	    ...: ar to bags or multisets in other languages.'''.lower()
	    ...: 
	    ...: c = Counter(s)
	    ...: 
	    ...: 

	In [55]: c
	Out[55]: 
	Counter({'a': 24,
	         ' ': 54,
	         'c': 15,
	         'o': 22,
	         'u': 13,
	         'n': 21,
	         't': 24,
	         'e': 32,
	         'r': 20,
	         'i': 20,
	         's': 25,
	         'd': 10,
	         'b': 5,
	         'l': 14,
	         'f': 1,
	         'g': 7,
	         'h': 6,
	         'j': 1,
	         '.': 4,
	         'w': 2,
	         'm': 3,
	         'y': 4,
	         'k': 1,
	         'v': 3,
	         'z': 1})
	In [62]: Counter(s)['a']
	Out[62]: 24
	```
* Chainmap

	用来合并多个字典并输出，并不会影响到原有字典。

	```
	In [81]: maps = ChainMap(baseline, adjustments)

	In [82]: type(maps)
	Out[82]: collections.ChainMap

	In [83]: maps.keys()
	Out[83]: KeysView(ChainMap({'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'}))

	In [84]: maps.values()
	Out[84]: ValuesView(ChainMap({'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'}))

	In [85]: maps['music']
	Out[85]: 'bach'

	In [86]: maps['art']
	Out[86]: 'rembrandt'

	In [87]: maps['opera']
	Out[87]: 'carmen'

	In [90]: len(baseline)
	Out[90]: 2

	In [91]: len(adjustments)
	Out[91]: 2

	In [92]: len(a)
	Out[92]: 1

	In [93]: d = ChainMap({'music': 'bach', 'art': 'rembrandt'}, {'name': 'cara'}, {'art': 'van gogh', 'opera': 'carmen'})

	In [94]: len(d)
	Out[94]: 4
	```
	
还有UserList, UserDict, UserString这些对象，我们不在此讨论。
