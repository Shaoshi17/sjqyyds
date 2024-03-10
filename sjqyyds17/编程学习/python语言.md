---
created: 2023-11-21T17:23
updated: 2024-03-09T18:45
---
- [x] 第二章到第三章
- [x] 第四章
- [x] 第五章
- [x] 第六章
- [x] 第七章
- [x] 第八章
- [x] 第九章
- [x] 第十章

### 变量和简单数据类型
#### 变量 
==变量就是指向一个值，使用变量相当于使用这个值，他们互相关联，变量可以描述为存储值的盒子==
在内存中的位置可以存储不同的值，如整数，实数，布尔值，字符串，或者更复杂的数据结构，列表，字典，如果我们定义一个存储整形的变量和一个存储字符串的提示消息。
==为了把两个变量连接到一个字符串中，我们必须用str（）函数==

```python
port=23

banner="FTP Server"

print(\"\[+\]\"+banner+\"on port\"+str(port)))

type（）函数可以识别变量类型

type(port)
```

#### 字符串
==字符串就是一系列字符，用引号括起来的都是字符串，其中可以是单引号和双引号==
python中字符串模块提供了一系列非常强大的字符串操作方法
###### 方法
方法：是python可对数据执行的操作。出现在变量后面。
例如：==变量.title()，解析意思就是，变量后面的句号，让python对变量执行方法title()指定操作。每个方法后面都跟着一对括号，这是因为通常需要其他额外信息来完成工作，在圆括号里面提供。函数title()不需要额外信息，因此是空的。==


###### 常用字符串的方法：

- [ ] .title() 首字母大写

- [ ] .upper() 小写字母转大写字母

- [ ] .lower() 大写字母转小写字母

- [ ] .replace(old,new)将old旧字符替换成new新字符

- [ ] .find('查询字符串')查找检测的字符有没有包含制定字符，返回这个字符串的开头

```python
banner = "FreeFloat FTP Server"
print(banner.title())
Freefloat Ftp Server

print(banner.upper())

FREEFLOAT FTP SERVER

print(banner.lower())

freefloat ftp server

print(banner.replace('FreeFloat','Ability'))

Ability FTP Server

print(banner.find('FTP'))

10
```
###### 在字符串中使用变量
==要在字符串插入变量，可以在引号前面加上字母`f`再将要插入的变量放在花括号内，当python使用这个字符串时候，会将每个变量替换成其值==
```python
banner = "FreeFloat FTP Server"  
name="root";  
banner_root=f"{banner},{name}"  
print(banner_root)

//FreeFloat FTP Server,root
```
字母f是format(设置格式的简写)，这是python3.6才引入的。如果是以下的版本就要用format()方法。
###### 使用制表符或者空白符添加空白
在编程中空白泛指任何非打印字符。

|   |   |
|---|---|
|转义字符|描述|
|\ （在行尾时）|续行符|
|\\|反斜杠符号|
|\'|单引号|
|\"|双引号|
|\a|响铃|
|\b|退格(Backspace)|
|\0 / \000|空字符(NULL)|
|\n|换行|
|\v|纵向制表符|
|\t|横向制表符|
|\r|回车|
|\f|换页|
|\oyy|八进制数 yy 代表的字符，例如， \o12 代表换行|
|\xyy|十六进制数 yy 代表的字符，例如， \x0a 代表换行|
|\other|其他字符以普通格式输出|
|\ddd|1到3位八进制数所代表的的任意字符|
###### 删除空白
删除空白的方法：
- [ ] str.rstrip([chars])  删除字符串末尾的指定字符chars指定的字符，默认为空白符
- [ ] str.lstrip([chars])  删除字符串开头的指定字符chars指定的字符，默认为空白符
- [ ] str.strip([chars])  删除字符串首尾的指定字符chars指定的字符，默认为空白符
```python
name=" root ";  
print(name.rstrip())  
print(name.lstrip())  
print(name.strip())  
print(name)
 
' root'
'root '
'root'
' root '

```
这种删除是暂时的，所以要改成name=name.strip()才是真正的删除了。
#### 数
##### 整数
在python中对整数可以进行加减乘除运算和乘方。
```python
print(1+2)  
print(4-2)  
print(4*2)  
print(4/2)  
print(2**2)

3
2
8
2.0
4
```
##### 浮点数
编程语言把所有带小数点的数都叫做==浮点数==
无论哪种运算只要有操作数是浮点数，python默认得到的总是浮点数。
###### 数中下划线
书写很大的数时候可以，使用下划线将其中的数字分组，更清晰。
这种方法适用于整数和浮点数。
```python
a=1000_0000_0000  
print(a)

//100000000000
```
但也是只有python3.6和更高的版本支持
###### 同时给多个变量赋值
用一系列数赋值给一组变量。
```python
a,b,c=1,2,3  
print(a,b,c)
//1 2 3
```
###### 常量
python没有内置常量类型。
在python中要是设置变量为常量不和C语言那样用#define而是直接把其字母全部大写就当作常量，==但是可以覆盖和修改，只是我们看作常量使用。==
###### 注释符
在python中用#号注释。C语言和php都是用//注释
##### 判断字符类型
```python

a='sssss'
if type(a)==str:
    print('yes')
else:
    print('no')

yes
```

### 列表
#### 列表是什么
列表是由于一系列特定元素组成的。
在python中列表是由方括号[]表示列表，并用逗号分隔其中元素。
```python
home=['a','b','c']  
print(home)

//['a', 'b', 'c']
```
打印出来包括方括号。
###### 访问列表元素
列表是有序集合 ，所以要访问列表的任意元素，只需要把该元素的下标或叫索引告诉python编译器就可以访问到。
```python
home=['a','b','c']  
print(home[0])

//a
```
==所有编程语言的索引是从0开始的，而不是从1开始,访问-1就是访问列表中最后一个元素==
#### 修改和删除元素
创建的列表大多数是动态的，所以需要改动
###### 修改列表元素
直接索引出要改变的元素，然后赋值改变即可
```python
home=['a','b','c']  
home[0]='A'  
print(home)

//['A', 'b', 'c']
```
###### 在列表中添加元素
- [ ] 在列表末尾添加元素，最简单方法就是附加（append）到列表。使用方法.append('str')
```python
home=['a','b','c']  
home.append('A')  
print(home)
//['a', 'b', 'c', 'A']
```
在列表尾部添加字符‘A’

- [ ] 在列表中插入元素，使用插入(insert)方法可以在列表中任意位置添加新元素。为此要指定新元素的索引和值。
```python
home=['a','b','c']  
home.insert(2,'A')  
print(home)

//['a', 'b', 'A', 'c']
```
指定的地方就是插入元素的地方原来有元素就会被排挤到后面去
- [ ] 从列表中删除元素，使用删除（del)函数，或者使用.pop()方法，弹出                                                                                                                                
```python
home=['a','b','c']  
del home[0]  
print(home)

home=['a','b','c']  
home.pop(1)  
print(home)

//['a', 'c']
```
- [ ] 根据值来删除元素，使用方法.remove()
```python
home=['a','b','c']  
home.remove('a')  
print(home)

//['b', 'c']
```
#### 组织列表
###### 使用方法sort()对列表永久排序
sort()让列表按照字母顺序排序。
```python
home=['a','c','b']  
home.sort()  
print(home)
//['a', 'b', 'c']
```
这是对列表永久的排序。
还可以按字母顺序相反的排序排列,只需要在sort()方法中传递参数`reverse=True`即可
```python
home=['a','c','b']  
home.sort(reverse=True)  
print(home)

//['c', 'b', 'a']
```
一样是永久性的
###### 使用函数sorted()对列表进行临时排序
要保留原来列表排序就要，同时要以特定顺序展示出来。
```python
home=['a','c','b']  
print(sorted(home))  
print(home)

['a', 'b', 'c']
['a', 'c', 'b']
```
###### 倒着打印列表
使用reverse()方法。
```python
home=['a','c','b']  
home.reverse()  
print(home)

//['b', 'c', 'a']
```
###### 判断列表长度
使用len()函数判断列表函数
```python
home=['a','c','b']  
print(len(home))

//3
```
### 操作列表
| Python 表达式                     | 结果                           | 描述         |
| ------------------------------ | ---------------------------- | ---------- |
| len([1, 2, 3])                 | 3                            | 长度         |
| [1, 2, 3] + [4, 5, 6]          | [1, 2, 3, 4, 5, 6]           | 组合         |
| `['Hi!']` * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复         |
| 3 in [1, 2, 3]                 | True                         | 元素是否存在于列表中 |
| for x in `[1, 2, 3]`: print x, | 1 2 3                        | 迭代         |
#### 遍历整个列表
使用循环一个一个打印出来。

for循环语法：
```python
for iterating_var in sequence:  
   statements(s)
```
###### 深入研究循环
```python 
homes=['a','c','b']  
for home in homes:  
    print(home)


a
c
b
```
###### for循环结束执行操作
```python
homes=['a','c','b']  
for home in homes:  
    print(home)  
print("aaa")


a
c
b
aaa
```
这里python不像C语言或者php语言一样用什么{}包裹复合语句，==而是用换行来判断，所以在python中不用滥用换行。==

###### 忘记缩进
```python
homes=['a','c','b']  
for home in homes:  
print(home)
```
![[Pasted image 20240228084759.png]]

在for循环中每个元素执行都需要代码缩进。
###### 遗漏冒号
```python
homes=['a','c','b']  
for home in homes  
    print(home)
```
![[Pasted image 20240228085136.png]]
原来for循环的冒号是告诉python，下一行是循环的第一行。报错只能说语法无效。invalid syntax

##### 创建数值列表
###### 使用函数range()
python函数能轻松生成一系列数。
```python
for home in range(1,5):  
    print(home)

1
2
3
4
```
range(1,5),只打印了1~4，这是编程语言常见的差一行行为。函数range()让python从指定的第一个数值开始到，第二个值时结束。==因为在第二个值停止所以不包括该值==。
###### 使用range()创建数字列表
可以使用函数list将range()结果直接转换为列表。
```python
number=list(range(1,7))  
print(number)

[1, 2, 3, 4, 5, 6]
```
使用range()函数还有升级操作，叫指定步长。可以给这个函数赋值三个参数。
```
函数语法：range(start, stop[, step])
```
参数说明：

- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，**但不包括 stop**。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
例题：打印2到10的偶数
```python
number=list(range(2,11,2))  
print(number)

[2, 4, 6, 8，10]

```
解析：函数从2开始然后不断加2，直到达到或超过最终值。
###### 对数字列表执行简单的统计计算
在python中有一下出来数字列表的函数，轻松找出最大值和最小值或总和。
```python
number=list(range(2,10,2))  
print(min(number))  
print(max(number))  
print(sum(number))

2
8
20
```
当然都是英文单词的缩写，比较良心。
###### 列表解析
前面学的生成列表的方式包含三到四行代码，而列表解析只需要写==一行代码==，就可以完成。
列表解析式是将一个列表（实际上适用于任何[可迭代对象（iterable）](https://docs.python.org/3/glossary.html#term-iterable)）转换成另一个列表的工具。在转换过程中，可以指定元素必须符合一定的条件，才能添加至新的列表中，这样每个元素都可以按需要进行转换。
##### python有内置好几种解析
- [ ] []:列表解析
- [ ] {}:集合解析
- [ ] {key:value}:列表解析
- [ ] ():生成器表达式，而不是解析
```python
# 集合解析
>>> { i*2 for i in "abcd"}
{'aa', 'cc', 'dd', 'bb'}

# 字典解析
>>> { k:v for k,v in zip(("one","two","three"),(1,2,3)) }
{'one': 1, 'two': 2, 'three': 3}
>>> { k: k*2 for k in "abcd" }
{'a': 'aa', 'b': 'bb', 'c': 'cc', 'd': 'dd'}

```
![[Pasted image 20240228183139.png]]
==解析操作的外部表达式部分在for关键字的前面，而普通for循环的表达式则是在for关键字后面。==
```python
//普通
nums=[]  
for num in range(1,10):  
    nums.append(num)  
print(nums)

[1, 2, 3, 4, 5, 6, 7, 8, 9]
//列表解析
nums=[num for num in range(1,10)]  
print(nums)

[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

##### 使用列表的一部分
处理列表的部分元素，需要用到python的切片
###### 切片
切片表达式：
```
切片操作基本表达式：object[start_index : end_index : step]
```
step：正负数均可，==其绝对值大小决定了切取数据时的“步长”==，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以增量1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！

start_index：==表示起始索引==(包含该索引本身)；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。

end_index：==表示终止索引==(不包含该索引本身)；该参数省略时，表示一直取到数据”端点“，至于是到”起点“还是到”终点“，同样由step参数的正负决定，step为正时直到”终点“，为负时直到”起点“。
==要创建切片就要指出第一个元素和最后一个元素的索引，就想range()函数一样。python会到达第二个元素之前停下。==
```python
nums=[num for num in range(1,20,2)]  
print(nums[0:3])

//[1, 3, 5]
```
如果没有指定第一个元素，python自动从头开始
```python
nums=[num for num in range(1,20,2)]  
print(nums[:3])

//[1, 3, 5]
```
如果没指定第二个元素就，python会到结尾结束
```python
nums=[num for num in range(1,20,2)]  
print(nums[3:])

//[7, 9, 11, 13, 15, 17, 19]
```
==负数索引返回离列表尾部相应距离的元素。==
```python
nums=[num for num in range(1,20,2)]  
print(nums[-3:])

//[15, 17, 19]
```
###### 遍历切片
比如说遍历列表前三的内容，for循环配上切片出的内容打印出就可以。
```python
nums=[num for num in range(1,20,2)]  
for a in nums[-3:]:  
    print(a)
15
17
19
```
#### 元组
列表适合存储在程序运行期间可以便哈的数据集。列表是可以修改的。有时候需要不可修改的元素，元组就可以满足这种需求，python把不可变的值成为不可变的，而不可变的列表就是==元组==。
###### 定义元组
元组看起来很像列表，使用()不是和列表一样用[]来表示。定义元组后可以用索引来访问，就像访问列表元素一样。
```python
a=(1,2,3)  
print(a[0])

//1
```
如果修改就会报错
```python
a=(1,2,3)  
a[0]=2  
print(a[0])
```
![[Pasted image 20240228193837.png]]
元组是由逗号标识的，圆括号只是让它看起来更美观，如果把一个数存入元组就在数字后面加上逗号才行
a=(1,)不然识别不出。
###### 遍历元组中所有的值
像列表一样可以用for循环来遍历元组的所有值。
```python
a=(1,2,3)  
for b in a:  
    print(b)
    
1
2
3

```
###### 修改元组变量
虽然不能修改元组的元素，但是能重新给元组进行赋值，相当于变相的修改。 
```python
a=(1,2,3)  
print(a)  
a=(3,)  
print(a)


(1, 2, 3)
(3,)
```
相对于列表，元组是更简单的数据结构，如果要存储  一组值在程序中整个生命周期都不变，就可以使用元组。




### if语句

每条if语句的核心就是true或者false的表达式，这种表达式称为条件测试。
```
if 要判断的条件(True)：
      条件成立的时候，要做的事情 
else:
      条件不成立的时候要做的事

```
###### 布尔表达式
编程语言的布尔表达式的值都是要么为True要么为false。
```python
a=True
b=False
```
###### 连接语句只能是使用or、and、elif，不能使用&&和||



###### 简单的if语句

```python
if conditional_test:
	do something
if age>19:
	print("age>19")
```
###### if-elif-else结构
```
if 要判断的条件(True)：
      条件成立的时候，要做的事情 
elif 要判断的条件(True)：
	条件成立的时候，要做的事情 
else:
      条件不成立的时候要做的事

```
==python并不要求使用if-elif结构后面必须有else代码块。可以省略==

### 字典
字典是一系列==键值对==，每个键都有与一个值相关联。可以使用键访问相关联的值。
键值对是两个相关联的值，键值对用逗号分隔，键值是用分号分隔。
在python中字典放在{}中一系列键值对表示。
```
alione={'color':'green','points':5}
```
color是一个键，与之关联的值是green
###### 访问字典中的值
要获取与键相关联的值，可以依次指定字典名和在字典的键，就可以访问到这个值
```python
online={'shan':22222,'xie':22222}  
print(online['shan'])

//22222
```
###### 添加键值对
字典是一个动态的结构，可以随时在其中添加键值对。
添加是只要指定字典和中括号括起来的键和相关联的值。
```python
online={'shan':22222,'xie':22222}  
online['huang']=222  
print(online)

//{'shan': 22222, 'xie': 22222, 'huang': 222}
```
###### 创建一个空字典
使用花括号创建一个空字典。
```python
online={}
```
###### 修改字典中的值
修改字典的值，指定字典名，还有中括号的键，以及新值。
```python
online={'shan':22222,'xie':22222}  
online['xie']=1111  
print(online)

//{'shan': 22222, 'xie': 1111}
```
###### 删除键值对
使用del语句经相应的键值对删除,就和列表中使用差不多。
```python
online={'shan':22222,'xie':22222}  
del online['xie']  
print(online)

//{'shan': 22222}
```
删除的键值对会永远消失

==由类似对象组成的字典==
###### 使用get()来访问值
方法get()的第一个参数是用来指定键是，必要的，第二个是指定当键不存在时返回的值，可选。
```python
online={'shan':22222,'xie':22222}  
a=online.get('sss',"不存在")  
print(a)

//不存在
```
##### 遍历字典
python支持对字典的遍历
###### 遍历所有键值对
遍历所有的键值对就要写for循环声明两个变量，用于存储键值对中的键和值。
方法items()他返回一个键值对列表。然后就依次赋值个两个变量。
```python
online={'shan':22222,'xie':22222,'hua':22222,'yuan':123222}  
for key,value in online.items():  
    print(f"key: {key},\nvalue: {value}")
    
key: shan,
value: 22222
key: xie,
value: 22222
key: hua,
value: 22222
key: yuan,
value: 123222
```
###### 遍历所有的键
可以使用.key方法来放在for循环的online中，但是默认也可以遍历键
```python
online={'shan':22222,'xie':22222,'hua':22222,'yuan':123222}  
for key in online:  
    print(f"key：{key}")

key：shan
key：xie
key：hua
key：yuan
```
还可以按特定顺序排序,使用sorted函数
```python
online={'shan':22222,'xie':22222,'hua':22222,'yuan':123222}  
for key in sorted(online):  
    print(f"key：{key}")

key：hua
key：shan
key：xie
key：yuan
```
###### 遍历字典中的所有值
使用方法values()来返回一个值列表，不包含任何键
```python
online={'shan':22222,'xie':22222,'hua':22222,'yuan':123222}  
for key in sorted(online.values()):  
    print(f"key：{key}")
```
###### 集合
可以用{}创建集合用逗号分隔元素：
```python
online={'python','python2','python3'}  
print(online)

//{'python2', 'python', 'python3'}
```
==字典和集合比较容易搞混==
##### 嵌套
###### 列表存储字典
可以将一系列字典嵌套到列表中，或将列表作为值存储在字典中，这叫嵌套。
```python
alines=[]  
for alines_number in range(10):  
    new_aline={'colo':'red','nombre':2}  
    alines.append(new_aline)  
for alien in alines[0:]:  
    print(alien)  
print(f"一共{len(alines)}怪")

{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
{'colo': 'red', 'nombre': 2}
一共10怪
```
###### 字典存储列表
```python
pizza={'crust':'thick','toppings':['pepperoni','extra cheese'],}  
print(f"名字：{pizza['crust']}")  
for top in pizza['toppings']:  
    print(f"配料：{top}")

名字：thick
配料：pepperoni
配料：extra cheese
```
这里打印配料要使用for循环才好提取配料列表。
###### 字典中存储字典
把每位用户信息都存储在一个字典中去。
可以在字典中嵌套字典，可以使用两个中括号调出里面的值，==相当于C语言的多维数组。==
```python
use={'ID':'神','Name':'xieyi','Age':18,'CTF':{'web':18,'misc':12}}  
print(f"ID: {use['ID']}\nName: {use['Name']}\nAge: {use['Age']}\nCTF_web: {use['CTF']['web']}\nCTF_misc: {use['CTF']['misc']}")

ID: 神
Name: xieyi
Age: 18
CTF_web: 18
CTF_misc: 12
```

### 用户输入和while循环
##### 函数input()工作原理
函数input()让程序暂停运行，等待用户输入一些文本，获取这些输入python将其赋值给一个变量
```python
s=input("输入你的方向：")  
print(s)


输入你的方向：CTF
CTF
```
input()函数接受一个参数 ，要向用户显示提示或说明。
###### Python一次性输入多个值
```python
a,b,c = input('enter a b c: ').split()
```
###### 使用int()获取整数
使用input()时，python将用户的输入解读为字符串。
```python
s=input("输入你的年龄：")  
b=int(input("输入你的长度："))  
print(type(s),type(b))

输入你的年龄：18
输入你的长度：18
<class 'str'> <class 'int'>
```
###### 求模运算
求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数。
```python
print(4%3)

//1
```
判断奇数偶数,如果某个数能被2整除，余数为零那么这个数就是偶数。
```python
print(4%2==0)  
print(1%2==0)

True
False
```
##### while循环
for循环是针对集合中的每个元素都执行一个代码块，而while循环则是不断运行，直到不满足条件为止。
###### while计数
```python
a=0  
while a<10:  
    a=a+1  
    print(a)

1
2
3
4
5
6
7
8
9
10
```
###### 让用户选择退出
```python
a=('insert1')  
while a!='quit':  
    a=input("输入quit退出循环")  
    print(a)

输入quit退出循环2
2
输入quit退出循环quit
quit
```
###### 使用break退出循环

###### 循环中使用continue,执行成功跳过后面的代码回到前面
##### 使用while循环处理列表和字典
 for循环是一种遍历列表的有效方式，但不应该在for循环中修改列表。否则难以导致python跟踪其元素
 要对遍历列表进行修改，就可以使用while循环。
###### 在列表之间移动元素
```python
uncon_suser=['user','root','kali']  
in_user=[]  
while uncon_suser:  
    shan=uncon_suser.pop()  
    print(shan)  
    in_user.append(shan)  
print(in_user)

kali
root
user
['kali', 'root', 'user']

```
###### 删除特定值
```python
uncon_suser=['user','root','kali']  
while 'root' in uncon_suser:  
    uncon_suser.remove('root')  
print(uncon_suser)  
for i in uncon_suser:  
    if i =='user':  
        uncon_suser.remove(i)  
print(uncon_suser)

['user', 'kali']
['kali']
```
###### 使用用户来填充字典

```python
pepole={}  
flag=True  
while flag:  
    name=input("输入你的姓名：")  
    age=int(input("输入你的年龄："))  
    pepole[name]=age  
    flag=input("退出：(yes/ho)")  
    if flag=='yes':  
        flag=False  
    else:  
        flag=True  
for key,value in pepole.items():  
    print(f"key:{key}\nvalue:{value}")
    
输入你的姓名：dsfa
输入你的年龄：12
退出：(yes/ho)
输入你的姓名：sdjfan
输入你的年龄：123
退出：(yes/ho)
输入你的姓名：dnnd
输入你的年龄：123
退出：(yes/ho)
输入你的姓名：ddd
输入你的年龄：92
退出：(yes/ho)yes
key:dsfa
value:12
key:sdjfan
value:123
key:dnnd
value:123
key:ddd
value:92

```
### 函数
##### 定义函数
```python
def greet_user():  
    print("Hello World!")  
greet_user()

#Hello World!
```
函数调用依次输入函数名以及圆括号即可
###### 向函数传递信息
```python
def greet_user(huser):  
    """打印hello"""  
    print(f"Hello World! {huser}")  
greet_user('shan')

#Hello World! shan
```
 
###### 实参和形参
在上面这个代码里'shan'是实参，而huser是形参
###### 传递位置实参
简单的方法就是顺序传递。但是如果顺序搞反就得不偿失。
```python
def greet_user(huser,nuser):  
    """打印hello"""  
    print(f"Hello World! {huser} and {nuser}")  
greet_user('shan','xie')

#Hello World! shan and xie
```
###### 关键字实参
直接在实参中将名称和值关联起来，即使顺序错误也没问题。
```python
def greet_user(huser,nuser):  
    """打印hello"""  
    print(f"Hello World! {huser} and {nuser}")  
greet_user(nuser='shan',huser='xie')

#Hello World! xie and shan
```
###### 默认值
编写函数可以给每个形参指定默认值，在函数能给形参提供实参就使用指定值，没有就使用默认值。

使用默认值
```python
def greet_user(huser,nuser='xie'):  
    """打印hello"""  
    print(f"Hello World! {huser} and {nuser}")  
greet_user(huser='shan')
```
 不使用默认值
```python
 def greet_user(huser,nuser='xie'):  
    """打印hello"""  
    print(f"Hello World! {huser} and {nuser}")  
greet_user(huser='shan',nuser='xian')

#Hello World! shan and xian
```
当然这里如果你传一个值但是没按顺序还是回报错，不会说自动补全给没默认值的形参。
```python
def greet_user(nuser='xie',huser,):  
    """打印hello"""  
    print(f"Hello World! {huser} and {nuser}")  
greet_user('xian')

```
![[Pasted image 20240306085558.png]]
###### 返回值
```python
def sum(a,b):  
    return a+b  
print(sum(1,2))

#3
```

###### 让实参变成可选
```python
def sc(a,b,c=''):  
    if c:  
        full=a+b+c  
    else:  
        full=a+b  
    return full  
  
print(sc(1,2,3))  
print(sc(1,2))

6
3
```
输入两个就执行两个，输入三个就执行三个
###### 传递列表
```python
username=['admin','admin','admin']  
def gree_user(names):  
    for name in names:  
        print(f"Hello{name}")  
gree_user(username)

Helloadmin
Helloadmin
Helloadmin

```
函数中可以修改外面的实参因为传递的是这个列表的源数据。
```python
username=['admin','admin','admin']  
def gree_user(names):  
    names[0] = names[0] + 'wxhn'  
    for name in names:  
        print(f"Hello{name}")  
gree_user(username)  
print(username)

Helloadminwxhn
Helloadmin
Helloadmin
['adminwxhn', 'admin', 'admin']
```
###### 禁止函数修改列表
切片表示法[:]创建列表的副本。
```python
username=['admin','admin','admin']  
def gree_user(names):  
    names[0] = names[0] + 'wxhn'  
    for name in names:  
        print(f"Hello{name}")  
gree_user(username[:])  
print(username)

Helloadminwxhn
Helloadmin
Helloadmin
['admin', 'admin', 'admin']

```
###### 函数创建空元组，接收任意实参
有时候不知道要接受多少实参，python运行函数从调用语句中收集任意数量的实参。
```python
  
def gree_user(*names):  
        print(f"Hello{names}")  
gree_user('shan','shan','shan','shan')

Hello('shan', 'shan', 'shan', 'shan')
```
`*names`中的星号让python创建一个名为names的空元组。
写一个循环使用值，这样不管是传递一个值还是两个值都可以轻松解决
```python
  
def gree_user(*names):  
    for name in names:  
        print(f"Hello{name}")  
gree_user('shan','sshan','sdhan','dn')

Helloshan
Hellosshan
Hellosdhan
Hellodn
```
###### 函数创建字典，接收任意关键字实参
```python
def gree_user(first,last,**names):  
    names['first'] = first  
    names['last'] = last  
    return names  
print(gree_user('shan','sshan',fa='sdhan',ddd='dn'))

{'fa': 'sdhan', 'ddd': 'dn', 'first': 'shan', 'last': 'sshan'}
```
形参`**names`中的两个星号让python创建一个空字典名字为names

##### 将函数存储在模块中
将函数到文件中然后在同目录可以调用名字即可。
###### 导入整个模块
模块：
```python
sum.py

def sum1(a,b,c=''):  
    if c:  
        full=a+b+c  
    else:  
        full=a+b  
    return full
```
执行：
```python
import sum  
print(sum.sum1(1,2,3))

6
```
###### 导入模块中特定函数
使用form 模块 import 函数
用逗号隔开多个函数
```python
from sum1 import sum  
print(sum1(1,2,3))

6

```
###### 使用as给函数指定别名
form 模块 import 函数 as 函数别名
为了防止函数名冲突所以使用函数别名这个操作
```python
from sum import sum1 as sm  
print(sm(1,2,3))

6
```
###### 导入模块中的所有函数
form 模块 import *
```python
from sum import *  
print(sum1(1,2,3))

6

```
### 类
根据类来创建对象称为==实例化==。
#### 创建和使用类
使用类可以模拟任何东西。
##### 创建一个普通类
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sit(self):
        print('cccccccc')

```
###### 方法
- [ ] 类中的函数叫做==方法==,前面学习的函数都适用于方法，唯一的区别就在==调用方式==。
- [ ] 类中的变量叫做属性，和php中的类似
- [ ] `__init__()`是一个特殊方法。==每当这个match类创建一个新实例，python都会自动调用`__init__()`方法。相对于实例化后的初始化方法。类似PHP的`__construct()`魔术方法。==
- [ ] 在这个方法定义中，形参self必不可少，而且必须位于其他形参前面。
- [ ] 为什么要定义self呢？因为创建在这个实例时，将自动传入实参self， 它是一个指向实例本身（对象）的引用。（==相对于php的$this==）方法`__init__()`接受这些形参的值并赋值给根据这个类创建的实例属性。
- [ ] 以self为前缀的变量可供类中的所有方法使用，self.name=name获取与形参name想关联的值，并将其赋值给变量name。就可以被实例化访问这个属性了。

##### 根据类来创建实例
```python
my=match('sss','aaa')
```
###### 访问属性
要访问实例的属性，可以使用句点表示法。
```python
print(my.a,my.b)

('sss', 'aaa')

```
###### 调用方法
先指定实例名称和调用的方法，用句点分隔，遇到my.sit()，python在类match中找方法sit()并允许其代码。
```python
my.sit()

cccccccc
```
###### 创建多个实例化
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sit(self):
        print('cccccccc')

my=match('sss','aaa')
mm=match('zzzz','eeeee')
print(my.a,my.b)
print(mm.a,mm.b)
my.sit()

('sss', 'aaa')
('zzzz', 'eeeee')
cccccccc
```
###### 给属性指定默认值
就是在添加属性，设置值就行,不根据`__init__()`提供的值也行。
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c='cc'
```
###### 修改属性的值
- [ ] 直接修改属性的值
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sit(self):
        print('cccccccc')

my=match('zzz','aaa')
my.a='bbb'
print(my.a)


bbb
```

- [ ] 通过方法修改属性的值
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sit(self,a):
        self.a=a

my=match('zzz','aaa')
my.sit('bbb')
print(my.a)


bbb
```
- [ ] 通过方法给属性的值进行递增
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=0

    def sit(self,a):
        self.c+=a
    def print_f(self):
        print(self.a,self.b,self.c)

my=match('zzz','aaa')
my.sit(12)
my.print_f()


('zzz', 'aaa', 12)
```
###### pass语句
类定义不能为空，但是要无内容的类或方法，使用pass语句来避免错误。
```python
class per:
	pass
```
#### 继承
![[Pasted image 20240307173254.png]]
==一个类继承另一个类时，将自动获得另一个类的所有方法和属性==,原有的类称为父类，而新类称为子类。子类继承了父类的所有方法和属性，同时可以定义自己的属性和方法。
###### 子类的方法`___init__()`
既然要在原有的父类中编写子类，通常要掉用父类的方法`__init__()`。
```python
class match:  
    def __init__(self,a,b):  
        self.a=a  
        self.b=b  
    def print_f(self):  
        print(self.a,self.b)  
  
class match_pro(match):  
    def __init__(self,a,b):  
        super().__init__(a,b)  
  
  
my=match_pro('aaa','bbb')  
my.print_f()


aaa bbb
```
创建子类是，父类必须包含在当前文件中，且位于子类的前面。
1. 定义子类match_pro,必须在圆括号内指定父类的名称。==class 子类名称(父类):==
2. 方法`__init__()`接收创建match原来父类的实例需要的信息。
3. super()是一个特殊函数，让你能够调用父类的方法。这行代码让python调用match类的`__init__()`，让子类包含父类中定义的所有属性。==父类也称为超类（超累）==
###### 给子类定义属性和方法
让一个类继承领用类后，就可以添加==区分子类和父类==所需的新属性和新方法。
- [ ] 给子类新属性设置默认值
```python

class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print_f(self):
        print(self.a,self.b)

class match_pro(match):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.c='cccc'


my=match_pro('aaa','bbb')
my.print_f()
print(my.c)


aaa bbb
cccc
```
- [ ] 传递形参值给子类
```python

class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print_f(self):
        print(self.a,self.b)

class match_pro(match):
    def __init__(self,a,b,d):
        super().__init__(a,b)
        self.c='ccc'
        self.d=d


my=match_pro('aaa','bbb','ddd')
my.print_f()
print(my.c,my.d)



aaa bbb
ccc ddd

```
###### 重写父类的方法
对于父类方法，只要想改都可以重写，原理是在子类创建和父类那个要需要重写的方法一样名字，这样子类的方法优先级高于父类那个，所以相对于重写了父类的方法用途。
```python
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print_f(self):
        print(self.a,self.b)

class match_pro(match):
    def __init__(self,a,b,d):
        super().__init__(a,b)
        self.c='ccc'
        self.d=d
    def print_f(self):
        print(self.a,self.b,self.c,self.d)


my=match_pro('aaa','bbb','ddd')
my.print_f()


aaa bbb ccc ddd
```
###### 将实例用做属性
这个功能可以拓展出很多类更加具体，系统，鲜明化。
将一个复杂的大类拆分成各个小类。
```python
class sum:
    def __init__(self):
        self.z=12
        self.k=22
    def sum_f(self):
        print(self.z+self.k)
class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.sum=sum()
    def print_f(self):
        print(self.a,self.b)


my=match('aaa','bbb')
my.print_f()
my.sum.sum_f()


aaa bbb
34
```
#### 导入类
和上章的直接导入函数差不多，只是类和函数的本身有区别而已。
模块文件：
```python
match.py

class match:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print_f(self):
        print(self.a,self.b)



```
测试文件：
```python

my=match('aaa','bbb')
my.print_f()

aaa bbb
```
##### 从一个模块中导入多个类
```python
from module_name import calss_name1,calss_name2,calss_name3,calss_name4
#实例化
my.class_name()
```
###### 导入整个模块
```python
import module_name
#实例化
my.module_name.class_name()
```
###### 导入模块中的所有类
```python
from module_name import *
#实例化
my.class_name()
```
###### 使用别名 
```python
from module_name import class_name as alias

my.alias()
```
#### python标准库
python标准库是一组模块，我们安装python都包含他。

- os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
    
- sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
    
- time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
    
- datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
    
- random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
    
- math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
    
- re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
    
- json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。
    
- urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。
### 文件和异常

#### 从文件中读取数据
文件中可以存储数据多的难以置信。读取文件非常必要。
不同模式打开文件的完全列表：

#### 常见的IO操作的类型如下：

|模式|描述|
|---|---|
|t|文本模式 (默认)。|
|x|写模式，新建一个文件，如果该文件已存在则会报错。|
|b|二进制模式。|
|+|打开一个文件进行更新(可读可写)。|
|U|通用换行模式（不推荐）。|
|r|以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。|
|rb|以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。|
|r+|打开一个文件用于读写。文件指针将会放在文件的开头。|
|rb+|以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。|
|w|打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。|
|wb|以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。|
|w+|打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。|
|wb+|以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。|
|a|打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|ab|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|a+|打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。|
|ab+|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。|
#### file 对象方法

- **file.read([size])**：size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
    
- **file.readline()**：返回一行。
    
- **file.readlines([size])** ：返回包含size行的列表, size 未指定则返回全部行。
    
- **for line in f: print line** ：通过迭代器访问。
    
- **f.write("hello\n")**：如果要写入字符串以外的数据,先将他转换为字符串。
    
- **f.tell()**：返回一个整数,表示当前文件指针的位置(就是到文件头的字节数)。
    
- **f.seek(偏移量,[起始位置])**：用来移动文件指针。
    
    - 偏移量: 单位为字节，可正可负
    - 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
- **f.close()** 关闭文件

##### 读取整个文件
被读取的源文件：
```txt
aaaaaaaaaaaaa
bbbbbbbbbbbbb
ccccccccccccc
ddddddddddddd
```
###### 程序读取文件两种方法
```python
#第一种
f=open()
#第二种
whit open() as f:
```
这两个方法的区别：==第一个需要自己写f.close()关闭文件，而第二种不需要，自己自动关闭文件。==
第一种方法读取文件：
```python
str=open('list.txt','r')
print(str.read())
str.close()

aaaaaaaaaaaaa
bbbbbbbbbbbbb
ccccccccccccc
ddddddddddddd
```
第二种方法读取文件
```python

with open('list.txt') as file_list:
    str=file_list.read()
print(str)

aaaaaaaaaaaaa
bbbbbbbbbbbbb
ccccccccccccc
ddddddddddddd
```
书上基本上是用第二种使用with的方法。
##### 文件路径
把简单的文件名传递给函数open()时，python将在当前执行的文件目录下寻找。
###### 相对路径
相对路径于当前执行程序的目录路径，下面的目录就直接加上目录名和/找文件
```python
with open('text_files/filename.txt') as file_object:
```
###### 绝对路径
将文件在计算机中的准确位置告诉python就可以准确的找到文件，这就是绝对路径。在windows是使用反斜杠(`\`)而不是斜杠(`/`)在python中必须使用斜杠不能使用反斜杠会报错。因为在python中`\`是用来转义的。
```python
with open(/home/kali/Desktop/filename.txt) as file_object:
```
如果一定要使用反斜杠就要双写，因为这代表的就是转义反斜杠本身(`\\`)
```python
with open('C:\\Users\\Administrator\\Desktop') as file_object:
```
##### 逐行读取
就是在with里面加入for循环打印出来。
```python

with  open('list.txt') as file_object:
    for list in file_object:
        print(list)

aaaaaaaaaaaaa

bbbbbbbbbbbbb

ccccccccccccc

ddddddddddddd


```
使用rstrip(),删除尾部空白行。
```python
with  open('list.txt') as file_object:
    for list in file_object:
        print(list.rstrip())


aaaaaaaaaaaaa
bbbbbbbbbbbbb
ccccccccccccc
ddddddddddddd
```
###### 创建一个包含文件夹的各行内容的列表
readliens()方法
```python

with  open('list.txt') as file_object:
    constr=file_object.readlines()
print(constr)

['aaaaaaaaaaaaa\n', 'bbbbbbbbbbbbb\n', 'ccccccccccccc\n', 'ddddddddddddd\n']
```
##### 使用文件内容
创建一个字符串包含文件的所有内容不包含空格。
```python
with  open('list.txt') as file_object:
    constr=file_object.readlines()
str=''
for list in constr:
    str+=list.strip()
print(str)

aaaaaaaaaaaaabbbbbbbbbbbbbcccccccccccccddddddddddddd
```
###### 注意：python读取文件时候都解读为字符串，要什么类型就自己用函数就转换，比如int()整形，float()浮点型。
##### 判断文件内容
其实没啥必要，因为都把文件内容到导入到一个变量里面了就可以当做变量来处理套个if也是一样普通。
```python

with  open('list.txt') as file_object:
    constr=file_object.readlines()
for i in constr:
    if "aaaa" in i:
        print("YES")
    else:
        print("NO")


YES
NO
NO
NO
```
#### 写入文件
保存数据的最简单方法技术写入文件中。
##### 写入空文件
将不是打印在屏幕上而是输出在文件里
```python

def wir(str):
    with open('list.txt','a+') as file_object:
        file_object.write(str)


def pri_file():
    with  open('list.txt') as file_object:
        print(file_object.read())

pri_file()
wir('aaaaa')
pri_file()



aaaaaaaaaaaaaa
bbbbbbbbbbbbbb
cccccccccccccc
dddddddddddddd


aaaaaaaaaaaaaa
bbbbbbbbbbbbbb
cccccccccccccc
dddddddddddddd

aaaaa
```
#### 异常
python使用成为异常的特殊对象来管理程序执行期间发生错误，每当发生让python错误它就会创建一个异常对象，如果你编写了处理异常的代码，程序将继续运行。
- [ ] 异常是使用try-except代码块来处理的
##### 处理除零报错， 使用try-excep代码块处理
这个是异常处理，python不能把0当除数。
```python
try:
    print(122/0)
except Exception,e:
    print("Eorr:"+str(e))

```
![[Pasted image 20240229153046.png]]
如果try代码块中的代码运行起来没有问题，python将跳过except代码块，如果try代码块出现问题就会执行与之匹配的except代码块并运行里面的代码。
try-except后面的代码程序也会接着运行。
##### 使用异常避免崩溃
发生错误时候还有工作尚未完成，妥善处理尤为重要。
###### 写一个计算器
```python

print('Exit input q')
while True:
    a=input("num1=")
    b=input("num2=")
    if a=='q'or b=='q':
        print('out....')
        break
    print(int(a)/int(b))

```
![[Pasted image 20240308103612.png]]
###### 使用上try-except 
```python
print('Exit input q')
while True:
    a=input("num1=")
    b=input("num2=")
    if a=='q'or b=='q':
        print('out....')
        break
    try:
        print(int(a)/int(b))
    except:
        print('sum2 != zero')




Exit input q
num1=1
num2=0
sum2 != zero
num1=2
num2=1
2.0
num1=2
num2=p
sum2 != zero
num1=p
num2=p
sum2 != zero
num1=q
num2=q
out....
```
##### else代码块
在try-except执行成功的代码可以执行else的代码。
```python
try:
	#代码''''''''''''
except:
	#失败执行''''''''
else:
	#成功执行''''''''
```
##### 处理文件读取失败
```python
with open('a.txt') as file_a:
    print(file_a.read())

```
![[Pasted image 20240308110145.png]]


```python
print('Enter character q to exit')
while True:
    file_name=input("Input file name:")
    if file_name=='q':break
    try:
        with open(file_name) as file_a:
            print(file_a.read())
    except:
        print(f'File {file_name} read failure')
    else:
        break


Enter character q to exit
Input file name:a.txt
File a.txt read failure
Input file name:q
```
##### 静默失败
有时候不不需要告诉用户读取文件失败了。使用pass语句，可以让except什么都不做。
```python
try:

except:
	pass

```
#### 存储数据
模块json让我们能简单的将python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
json数据格式并非python专用，还有==可以以json格式存储时间于其他编程语言分享。==
###### json格式最初是javascript开发的，随后成为了常见格式，被众多语言采用
##### 使用json.dump()和json.load()
写入和读取
###### 函数json.dump()
函数json.dump()接收两个实参：要存储的数据，已经用于存储数据的文件对象
```python
import json  
  
numbers=[1,2,3,4,5,6]  
file_name='number.json'  
with open(file_name,'w') as str:  
    json.dump(numbers,str)
	
```
成功写入
```txt
number.json
[1, 2, 3, 4, 5, 6]
```
###### 注意：文件名不能和模块一样不然会出现大问题，还可能产生pyc
###### 函数json.load()
```python
import json

file_name='number.json'
with open(file_name,'r') as str:
    number=json.load(str)
print(number)

[1, 2, 3, 4, 5, 6]

```

##### 保持和读取用户生成的数据
```python
import json
class player_message:
    def __init__(player,names,gender,age,email,phone_number):
        player.names=names
        player.gender=gender
        player.age=age
        player.email=email
        player.phone_number=phone_number
        str=(names,gender,age,email,phone_number)
        with open('player.json','w') as f:
            json.dump(str,f)
#将内容输入到playerjson保存起来
    def print_player(player):
        with open('player.json') as f:
            str=json.load(f)
            #读取文件内容并打印出来
            print(f'player names:{str[0]}\nplayer gender:{str[1]}\nplayer email:{str[2]}\nplayer phone number:{str[3]}')

name=input("input name:")
gender=input("input gender:")
age=int(input("input age:"))
email=input("input email:")
phone=int(input("input phone:"))

player1=player_message(name,gender,age,email,phone)
player1.print_player()



input name:sjqyyds
input gender:male
input age:18
input email:2968483331@qq.com
input phone:110
player names:sjqyyds
player gender:male
player email:18
player phone number:2968483331@qq.com

```
成功保存到player.json
```txt
["sjqyyds", "male", 18, "2968483331@qq.com", 110]                                                 
```




















### 网络
socket模块提供一个用Python进行网络连接的库。
Python requests 是一个常用的 HTTP z请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果
#### socket模块
###### 抓取banner的脚本
```python
import socket  #引入socket模块
s=socket.socket()  #使用socket类实例化一个对象，用于连接
s.connect(('172.16.123.1',22))  #调用connect方法来连接22端口的ssh服务，建立连接 
ans=s.recv(1024)     #调用recv方法，接收信息，读取接下来的1024B数据。
print(ans)         #打印信息
s.close()       #关闭链接
```
![[Pasted image 20240229120238.png]]
###### 条件选择语句
```python
import socket  #引入socket模块
s=socket.socket()  #使用socket类实例化一个对象，用于连接
s.connect(('172.16.123.114',21))  #调用connect方法来连接22端口的ssh服务
ans=s.recv(1024)
if("2.3.4" in str(ans)):
    print("-_-")
else:
    print("NO")
s.close()

```
![[Pasted image 20240229144828.png]]
###### 异常操作
```python
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码

```
这个是异常处理，python不能把0当除数。
```python
try:
    print(122/0)
except Exception,e:
    print("Eorr:"+str(e))

```
![[Pasted image 20240229153046.png]]
###### 使用列表来进行批量操作
```python
import socket  
socket.setdefaulttimeout(2)  
ip=['172.16.123.112','172.16.123.1','172.16.123.114']  
for i in range(0,3):  
    try:  
        s = socket.socket()  
        s.connect((ip[i],21))  
        ans=s.recv(1024)  
        print(ip[i],ans)  
    except:  
        continue
```
批量找到21端口的banner
```python
import socket  
socket.setdefaulttimeout(2)  
ip=[f'172.16.123.{i}' for i in range(100,125)]  
for i in range(0,25):  
    try:  
        s = socket.socket()  
        s.connect((ip[i],21))  
        ans=s.recv(1024)  
        print(ip[i],ans)  
    except:  
        continue

```
###### 函数
在python中函数提供了高效的可重复利用的代码块。


###### 文件输入/输出
假如我们有一个文本bug_banner.txt写着一些有漏洞的版本banner内容，我们怎么使用if来判断我们读取过来的满足这个漏洞
#### requests模块
使用 requests 发送 HTTP 请求需要先导入 requests 模块：
```python
import requests   #导入模块
x=requests.get('http://www.baidu.com')   #发送请求
print(x.text)     #返回网页内容
```
###### 更多响应信息如下：
|属性或方法|说明|
|---|---|
|apparent_encoding|编码方式|
|close()|关闭与服务器的连接|
|content|返回响应的内容，以字节为单位|
|cookies|返回一个 CookieJar 对象，包含了从服务器发回的 cookie|
|elapsed|返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。|
|encoding|解码 r.text 的编码方式|
|headers|返回响应头，字典格式|
|history|返回包含请求历史的响应对象列表（url）|
|is_permanent_redirect|如果响应是永久重定向的 url，则返回 True，否则返回 False|
|is_redirect|如果响应被重定向，则返回 True，否则返回 False|
|iter_content()|迭代响应|
|iter_lines()|迭代响应的行|
|json()|返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)|
|links|返回响应的解析头链接|
|next|返回重定向链中下一个请求的 PreparedRequest 对象|
|ok|检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False|
|raise_for_status()|如果发生错误，方法返回一个 HTTPError 对象|
|reason|响应状态的描述，比如 "Not Found" 或 "OK"|
|request|返回请求此响应的请求对象|
|status_code|返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）|
|text|返回响应的内容，unicode 类型数据|
|url|返回响应的 URL|
###### requests 方法如下表：
|方法|描述|
|---|---|
|delete(_url_, _args_)|发送 DELETE 请求到指定 url|
|get(_url_, _params, args_)|发送 GET 请求到指定 url|
|head(_url_, _args_)|发送 HEAD 请求到指定 url|
|patch(_url_, _data, args_)|发送 PATCH 请求到指定 url|
|post(_url_, _data, json, args_)|发送 POST 请求到指定 url|
|put(_url_, _data, args_)|发送 PUT 请求到指定 url|
|request(_method_, _url_, _args_)|向指定的 url 发送指定的请求方法|


#### sys模块
sys是system的缩写，系统的意思，改模块提供了一些接口，用于访问python解析器自身使用和维护的变量。可以与解释器进行比较深度的交互。
##### sys.argv
“argv”即“argument value”的简写，是一个列表对象，==其中存储的是在命令行调用 Python 脚本时提供的“命令行参数”。==
```python
import sys  
  
print(sys.argv[0])

#C:\Users\Administrator\PycharmProjects\pythonProject\.venv\Scripts\s.py
```
如果还在后面加参数就会在sys.argv[]列表里，就像C语言的main(int argc,char `*argv[]`)

```python
import sys  
  
print(sys.argv)



$ python sys_argv_example.py arg1 arg2 arg3
 The list of command line arguments:
  ['example.py', 'arg1', 'arg2', 'arg3']
 z​
```
利用好这个属性，可以极大增强 Python 脚本的交互性。






#### OS模块






##### UNIX口令破解机
为了实现目标，自己写出其他的文件
###### 制作密码本
```python
import crypt

passd=['abc','age','kali','agg']
saltd=['HX','HE','ZG']

for i in passd:
    for a in saltd:
        print(crypt.crypt(i,a))
        
HXPrziBd8EyBs
HErGS5d1ZKWdY
ZG8QQUdiBgtLU
HX5JpyMPQNXSA
HE6Y4DJqRiE/E
ZGXzKM7.jEHPA
HXngjDTOm7nNg
HE3W0pa4eW1Cw
ZGKsnzaUC0/w6
HXB4f/unASGFI
HEnI0.d1ddnKA
ZGmz9Hr/8jRtA
```
我们假设我们得到的是“ZG8QQUdiBgtLU”密文，好接着写破解脚本
user.txt
```
root:ZG8QQUdiBgtLU
```


###### 破解脚本



### 杂
###### 内置方法
python列表，提供了一种存储一组数据的方式。程序员可以构建任何数据的列表，另外有一些内置操作列表的方法，例如添加，删除，插入，弹出，获取索引，排序，计时，排序反转。

.append()函数添加元素建立列表。

.remove()删除莫元素

.sort()从从小排到大

```python
protlist=[]

protilst.append(21)

protilst.append(80)

protilst.append(433)

protilst.append(25)

print(protilst)

[21,80,433,25]

portilst.sort() #从小到大排序

print(protilst)

[21,25,80,433]

portilst.remove(433)#删除其中某元素

print(protilst)

[21,25,80]

print(len(protilst)) #列出长度

3
```

字典

python数据结构字典，可以存储任何数量的python对象的哈系表，字典的元素由键和值组成。

当我们建立一个字典时，每个键和值用冒号隔开，同时我们用逗号分割元素。.keys()这个方法将返回字典中所有键的列表，.items()将返回字典的元素的一系列列表。

```python
service={'ftp':21,'ssh':22,'http':80}

service.keys()

['ftp','ssh','http']

services.items()

[('ftp', 21), ('ssh', 22), ('http', 80)]

services.has_key('ftp')

True

services['ftp']

21
```

两种字符串截断匹配

```python
import binascii,re

s='466C6167317B63404E745F35655F6D457D'

flag=""

for i in range(len(s)):

    flag= flag + str(binascii.a2b_hex(s[4*i:4*i+4]))

print(flag)

s='466C6167317B63404E745F35655F6D457D'

result1 = re.findall('.{2}',s)

flag=""for i in result1:

    flag= flag+ (chr(int(i,16)))

print(flag)
```
zfill函数

①语法说明：

str.zfill(width)

其中，str表示这里要对一个字符串类型string进行操作，如果是整型、浮点型这样的数字类型，要先通过str()函数转化为字符串，才可以进行相关的操作；

width表示进行补零之后的字符串的长度，如果补零后的长度小于或等于原字符串的长度，那么字符串将不会产生任何的变化（该长的短不了）

就是不够就在前面补0的一个函数

![截图.png](    Python语言/media/image1.png)


进制字符转换：

![截图.png](    Python语言/media/image2.png)


chr函数：

就是把10进制也可以是16进制的形式的数字，转换成整数

chr() 用一个范围在
range（256）内的（就是0～255）整数作参数，返回一个对应的字符。]

以下是 chr() 方法的语法:

chr(i)

切片：

```
#object [start_index:end_index:step]
```

#start_index：表示起始索引（包含索引本身）,如果为空就取端点位置

#end_index:表示终止索引（不包含索引本身）,如果为空就为终点位置

#step：可以表示切片的步长，当为1时表示顺序存取

![截图.png](    Python语言/media/image3.png)


```
if __name__=='__main__':  
```

    main()  #如果是直接执行就相当于

main()
代码的意思，如果是被import调用哪\_\_name\_\_就不等于\_\_main\_\_就不执行main()函数就达到保密的
效果

```python
try:

    x = input("ssss:")

    y = input("kkkk:")

    print(x/y)

except :

    print("报错信息") #自定义报错信息
```

```
import os

os.system("ipconfig")#调用命令

with open('1.txt','w') as file:

 file.write('ssssssssssssssssssssss')

 file.close() #with写入字符到文件1.txt

 ------------------------------------

 f = open('1.txt','r')

 f.close   #将文件内容读取并赋值到f
```

```python
import time      #线程睡眠指定时间

def a():

    for x in range(6):

        print("等六秒")

        time.sleep(1)

def b():

    for x in range(7):

        print("再等七秒")

        time.sleep(1)

def main():

    a()

    b()

if __name__ == '__main__':

    main()
```

```python
import time                  

import threading

#单线程

def a():

    for x in range(6):

        print("等六秒")

        time.sleep(1)

def b():

    for x in range(7):

        print("再等七秒")

        time.sleep(1)

def main():

    a()

    b()

if __name__ == '__main__':

    main()
```

#多线程
```python
def a():

    for x in range(6):

        print("等六秒")

        time.sleep(1)

def b():

    for x in range(7):                            #threading多线程使用方法

        print("再等七秒")

        time.sleep(1)

def main():

    t1 = threading.Thread(target=a)

    t2 = threading.Thread(target=b)

    t1.start()

    t2.start()

if __name__ == '__main__':

    main()
```

该函数执行一个命令并返回命令的结果，可用以替代os.system()。

pexpect.run('ls-la')#该函数执行一个命令并返回命令的结果，可用以替代os.system()。

将字符串的值匹配长度8的值赋值给k字符串（可以实现二进制转换进制的操作）

```python
import re

s="01010101010101010101100101011100101010101010101001111001110"

k=re.findall(r'.{8}',s) #匹配长度为8的值赋给k
```

按7个一组的分割字符串

![截图.png](    Python语言/media/image4.png)


python模拟键盘鼠标基本操作

```python
import time

from pymouse import *

from pykeyboard import *

import pyperclip

from pykeyboard import PyKeyboard

m = PyMouse()

a = m.position()    #获取当前坐标的位置(这个东西到时候可以新建个py 获取坐标)#

m.move(1510, 10)   #鼠标移动到(x,y)位置#

a = m.position()m.click(1510, 10)  #移动并且在(x,y)位置左击

time.sleep(1)

m.click(598, 51)  #移动并且在(x,y)位置左击

m.click(598, 51)  #移动并且在(x,y)位置左击

m.click(598, 51)  #移动并且在(x,y)位置左击#

m.click(300, 300, 2) #(300,300)位置右击

pyperclip.copy('中文')

keyboard = PyKeyboard()

keyboard.press_key(keyboard.control_key)    # 按下Ctrl键

keyboard.tap_key('V')                  # 点击V键

keyboard.release_key(keyboard.control_key)  # 松开Ctrl键

keyboard.press_key(keyboard.enter_key)      #ent回车键

keyboard.press_key(keyboard.function_keys[12])   #按F12键

keyboard.press_key(keyboard.alt_key)    # 按下Alt键

keyboard.press_key(keyboard.function_keys[4])   #按F4键

keyboard.release_key(keyboard.alt_key)      #松开Alt键

keyboard.press_key(keyboard.enter_key)      #ent回车键

print(dir(keyboard))                        #查看按键所以属性

m.click(1510, 10)  #移动并且在(x,y)位置左击

time.sleep(1)

m.click(598, 51)  #移动并且在(x,y)位置左击

m.click(598, 51)  #移动并且在(x,y)位置左击

m.click(598, 51)  #移动并且在(x,y)位置左击#

m.click(300, 300, 2) #(300,300)位置右击

pyperclip.copy('中文')

keyboard = PyKeyboard()

keyboard.press_key(keyboard.control_key)    # 按下Ctrl键

keyboard.tap_key('V')                  # 点击V键

keyboard.release_key(keyboard.control_key)  # 松开Ctrl键

keyboard.press_key(keyboard.enter_key)      #ent回车键

keyboard.press_key(keyboard.function_keys[12])   #按F12键

keyboard.press_key(keyboard.alt_key)    # 按下Alt键

keyboard.press_key(keyboard.function_keys[4])   #按F4键

keyboard.release_key(keyboard.alt_key)      #松开Alt键

keyboard.press_key(keyboard.enter_key)      #ent回车键

print(dir(keyboard))                        #查看按键所以属性
```

python图像识别

```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#在同个目录里放zan.png就会找zan.png图标然后点击

import time

def zan():

    time.sleep(0.5)    # 等待 0.5 秒    

    left, top, width, height = pyautogui.locateOnScreen('zan.png')   # 寻找 点赞图片；    

    center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心    

    pyautogui.click(center)    # 点击    print('点赞成功！')

while True:

    if pyautogui.locateOnScreen('zan.png'):

        zan()   # 调用点赞函数        

        break  #只执行一次    

    else:

        pyautogui.scroll(-500)    # 本页没有图片后，滚动鼠标；        

        print('没有找到目标，屏幕下滚~')
```

python网站爬虫

学习链接：[selenium-python中文文档](https://python-selenium-zh.readthedocs.io/zh_CN/latest/)

控制浏览器操作

控制浏览器窗口大小

driver.set_window_size(480, 800)

浏览器后退，前进

\# 后退 driver.back()

\# 前进 driver.forward()

刷新

driver.refresh() \# 刷新

find_element()

早期的selenium提供了针对id、name、xpath等多种方式的具体方法来定位到具体的元素，比如find_element_by_id()、find_element_by_name()等，在后续的升级中，这些方法被弃用了，现在统一使用find_element(by=By.ID,
value=None)方法，该方法包含了id、name、xpath等定位方式

find_element(by=By.ID,
value=None)是WebDriver对象用于定位元素的方法，返回对应元素对象（WebElement），我们的点击、拖拽等操作都是在元素对象的基础上进行的

参数说明

by：指定按照对应的方式来定位元素

By.ID，根据查找标签中的id属性来定位元素

By.NAME，根据查找标签中的name属性来定位元素

By.CLASS_NAME，根据class属性指定的值来查找元素

By.CSS_SELECTOR，根据css选择器的方式来查找元素

By.XPATH，根据XPath语法来查找元素

By.LINK_TEXT，查找文本精确匹配的a标签元素

By.PARTIAL_LINK_TEXT，查找文本模糊匹配的a标签元素

By.TAG_NAME，根据标签名称来查找元素，不太好用，不常用

value：元素位置，字符串类型

![截图.png](    Python语言/media/image5.png)


```python
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

---------------百度搜索-------------------

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.find_element(By.ID, "kw").send_keys("单基强最帅") #打开百度的输入框输入time.sleep(5)

driver.find_element(By.ID, "su").click() #点击搜索按钮time.sleep(5)

---------------哔哩哔哩搜索-------------------

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com/")

time.sleep(5)

driver.find_element(By.CLASS_NAME,"nav-search-input").send_keys("shan")

time.sleep(5)

driver.find_element(By.CLASS_NAME,"nav-search-btn").click()

time.sleep(5)

打开默认浏览器这样就有那些登录信息了

from selenium import webdriver

option = webdriver.ChromeOptions()

# 添加保持登录的数据路径：安装目录一般在C:\Users\\AppData\Local\Google\Chrome\User Data

option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")

如果找不到可以直接搜索Google一个一个试目录

driver = webdriver.Chrome(options=option)

driver.get("https://www.csdn.net/")

driver.maximize_window()
```