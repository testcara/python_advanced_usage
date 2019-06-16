### python switch的实现
python流程控制中没有switch，官方文档建议，简单的使用的if..elseif..else等实现，如果情况较为复杂，则使用函数，类等方法。
#### 枚举实现switch
实现如下：
```
from enum import Enum
SEASONS = Enum('SEASONS', ('Spring', 'Summer', 'Autumn', 'Winner'))
def switch(season_name):
    print(SEASONS[season_name].value)
switch('Autumn'
```
则可获得输出：
```
Press ENTER or type command to continue
3
```
#### 字典实现switch
```
dict_season = { 
    "spring": "It is Spring!",
    "autumn": "It is Autumn!",                                  
    "summer": "It is Summer!",
    "winner": "It is Winner!"
  }
def switch(seanson_name):
    print(dict_season.get(seanson_name, None))

switch('spring')
```
#### 字典和函数实现switch
```
def hello():
  print("hello!")

def bye():
  print("bye!")

dict_types = { 
  "h": hello,
  "b": bye,
}

def switch(type):
  method = dict_types.get(type, None)
  if method:
      method()

switch('h')
```
#### 类实现switch
```
class switch(object):
  def __init__(self, moden):
      self.li = { 
          'a': self.__a,
          'b': self.__b
      }   
      function = self.li.get(moden, self.__other)
      function()                                                                                                                                         

  def __a(self):
      print("This is function a!")

  def __b(self):
      print("This is function b!")

  def __other(self):
      print("This is other function!")


switch('a')
```
输出为：
```
Press ENTER or type command to continue
This is function a!
```
