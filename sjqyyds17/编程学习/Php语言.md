# 7天理解掌握php基础

## day1 （配置环境）

#### 静态网站与动态网站的区别
静态网站是web1.0时代
动态网闸是web2.0时代
##### 网站：
Website的中文名叫做网站，使用一定规则，使用html和php等代码语言制作的用于展示指定内的相关网页，可以供管理人员操作后台及用户使用前台。简单说Website是一种网络通讯工具。或者使用Websize提供某种服务。
###### 静态网站的特点：
- [ ] 网页是保存在服务器上的，每个网页都是独立的文件夹
- [ ] 静态网页相对稳定，因此==容易被搜索引擎检索==
- [ ] ==静态网页没有数据库的支持==，在网站制作的工作量大于动态网站
- [ ] 静态网页交互性差，在功能上有很大限制

==静态网站相当于只读文档==
###### 动态网站的特点
- [ ] 交互性：==可以根据用户的要求和选择而动态的改变和响应==，实现的原理就是有连接数据库。
- [ ] 自动更新：可以根据数据库自动生成不同的内容。
###### 识别网页是静态还是动态
网页后缀是：htm,html,shtml,xml是静态
网页后缀是：asp,jsp,php,perl,cgi等形式是动态
还有就是动态网站有一个标志性符号“?”
#### 网站基本概念
##### 服务器概念 
服务器(server),提供计算机服务的设备。由于服务器需要响应服务请求，进行处理，==因此需要具备承担服务并保障服务的能力==。
服务构成包括：处理器，硬盘，内存，系统总线路等和通用计算机架构类似，但是要提供可靠的服务==需要更高的硬件水平==
在网站下，根据提供服务的不同可以分为，文件服务器，数据库服务器，应用程序服务器，WEB服务器。

==ip具有唯一性，一个域名的目的是便于记忆和沟通的一组服务器地址。==
==DNS，进行域名解析，进行访问ip
端口是设备于外界通讯的出口，虚拟端口是指计算机内部不可见的端口。==在一台电脑上区分不同的软件访问的作用
==用户输入域名和端口 localhost:端口>DNS（localhost 127.0.01）>服务器电脑>服务器电脑上端口指示的软件==
下面是演示静态网页的访问流程
![[Pasted image 20231225085711.png]]
动态访问流程多了数据进行对网页的处理和更新
![[Pasted image 20231225085837.png]]
#### 安装apache

安装包名字的意思![[Pasted image 20231225090940.png]]
apache目录里面子目录代表的意思
![[Pasted image 20231227090716.png]]
PHP.exe可以把php代码解析转变为HTML代码从而让浏览器可以解析 
也可以使用php.exe 直接运行php文件 ：php.exe -f PHP文件路径
![[Pasted image 20231227093338.png]]
###### 配置apache加载php模块
- [ ] apache加载php模块：
在apache主配置文件（httpd.conf）中加载对应的php提供的模块
LoadModule php5_moudle PHP所提供的模块连接的绝对地址
![[Pasted image 20231227094209.png]]
- [ ] apache分配工作给php,如果是PHP的代码就给php处理，判断尾部文件是否为。php
![[Pasted image 20231227094732.png]]
- [ ] 将php配置文件加载到apache配置文件中
1. 加载配置文件：PHPIniDir 配置文件
![[Pasted image 20231227101044.png]]
1. php.ini是默认不存在的，以development和production格式存在的，需要改名字
==这里修改php.ini后也要重启apache才会生效。==
#### 安装Mysql
![[Pasted image 20231227104819.png]]
bin目录的几个常用软件
![[Pasted image 20231227104900.png]]
软件设计结构：C/S和B/S
C/S:client客户端和server服务端：用户需要安装客户端软件，只能访问一个软件
B/S:Browser 浏览器server服务端：用户只用安装浏览器，就可以访问所有可用的软件
##### Mysql访问流程
Mysql是一款C/S架构的软件，需要访问客户端来访问服务端。

使用本身的客户端![[Pasted image 20231227105421.png]]

mysql客户端访问服务器需要寻找匹配，连接认证
连接： mysql.exe -h 127.0.0.1 -u root -p root
![[Pasted image 20231227105711.png]]
通常是不建议明文密码输入，可以输入-p后自动再次输入密码，这时候密码是密文。安全些
![[Pasted image 20231227105917.png]]
#### php连接mysql数据库
也只能借助php的操作的扩展mysql的能力
1. php加载Mysql扩展：php.ini
取消分号![[Pasted image 20231227111227.png]]

2.php中所有的扩展都是在ext文件中，需要指定扩展路径 ![[Pasted image 20231227111843.png]]
配置成功![[Pasted image 20231227112331.png]]
现在表示php可以使用mysql
##### 增加时区
![[Pasted image 20231227112530.png]]



## day2（PHP基础）
php是一种可以运行在服务器的脚本语言，可以嵌入html中
##### php代码标记
在php中可以用多种标记来区分php脚本
 1. ASP标记 <% %>
 2. 短标记 <? ?>
 3. 脚本标记 <script language="php"> </script>
 4. 标记常用<?php ?>

##### php的编码规范
通常是以分号结尾";"
在php代码中的结束标记隐含了一个分号，所以可以不用加分号
```
<?php phpinfo();
?>

<?php 
phpinfo()?>
```
PHP对空格，回车照成的新行,Tab等空白符都忽视。合理运用空白符可以增强代码的可读性。
###### php代码注 释

```
行注释：//,#
块注释：/* */  和 C语言一样
```

#### 常量
PHP通过define()命令来声明常量：这于C语言的关键字一样
```
define("常量名",常量值);
```
例如：
```
<?php
	define("HUANY","欢迎您");
	echo HUANY;
?>
```
##### 内置常量
PHP中预定了很多系统内置的常量，随时可以被调用。
1.   `_FILE_`:这个默认常量是文件名的完整路径和文件名。如果用引用文件（include和require）则在引用文件中的该常量应该为引用文件名不是被引用它的文件名。
2. `_LINE_`:这个默认常量是PHP代码的程序行数。如果用引用文件（include和require）则在引用文件中的该常量应该为引用文件行数不是被引用它的文件行数。
3. `PHP_VERSION`:这个内置常量是PHP程序的版本。
4. `PHP_OS`:这个是指php解析的操作系统名称
5. `TRUE`：真值
6. `FALSE`:假值
7. `E_ERROR`：这个常量指向最近错误的地方
8. `E_WARNNG`:这个常量指向附近有警告的地方
9. `E_PARSE`:这个常量指向附近有语法潜在错误的地方
10. `_DIR_`:文件所在目录 PHP5.3.0新增
11. `_FUNCTION_`：这个常量为函数的名称。PHP5新增
12. `_CLASS_`：这个常量为类的名称。PHP 5新增

#### 变量
不需要声明类型：PHP不同于C或JAVA语言，因为它是弱类型所以不需要像C或java进行==声明类型==。
php中的变量一般以”$“作为前缀，然后以大小写字母或者“ _ ”开头,数字不能开头，这和C语言类似
```
$hello
$Aform1
$_forme
```
php中不需要显式地声明变量
- [ ] 传值赋值：使用"="直接将赋值表达式的的值给另一个变量。
- [ ] 引用赋值：将赋值表达式的内存空间引用给另一个变量。需要在”=“左右的变量前面加”&“,两个变量指向一个存储空间，所以改变一个就两个都改变。
```php
$a="hahaha";
$b=$a;    //将变量$a赋值给变量$b
echo "b的值为".$b.;
$a="ahahaha";
echo "a的值为".$a.;
$b=&$a;   //将变量$a的地址引用赋给$b，两个变量指向同一块内存空间
```
##### 可变变量与变量的引用
一般变量可以很容易理解，但是有两个变量表示的概念就比较容易混淆。
例题
```php
<?php
	$a="yes"; $a被赋值为字符串yes
	$$a="no"; $$a相当于$yes被赋值为字符串no
	echo $yes."<br />";
?>
```
![[Pasted image 20231228104912.png]]

==可变变量其实就是允许一个变量的值作为另一个变量的名==

==变量引用相当于给变量添加一个别名==

#### 变量作用域
1. 内置超全局变量
2. 常数
3. 全局变量
4. 函数中声明的全局变量
5. 函数中声明的静态变量
6. 函数中声明的局部变量
##### 内置超全局变量
所谓超全局变量就是不管在程序什么地方都能访问到。
- [ ] `$GLOBALS`：包括全含变量的数组
- [ ] `$_GET`:包含所有通过GET方法传递给代码的变量
- [ ] `$_POST`:包含所有通过POST方法传递给代码的变量
- [ ] `$_REQUEST`:包含用户所有的输入内容的数组(`$_GET`,`$_POST`,`$_COOKIE`)
- [ ] `$_FILES`：包含文件上传变量的数组
- [ ] `$_COOKIE`:包含cookie变量的数组
- [ ] `$_SERVER`：包含服务器环境变量的数组
- [ ] `$_ENF`:包含环境变量的数组
- [ ] `$_SESSION`:包含会话变量的数组
##### 全局变量
所谓全局变量就是在函数外声明的变量。在代码间可以访问，==但是在函数内是不能访问的==。
```php
<?php
$root=20;
function show(){
	echo $root;
}
show();
echo $root." 2";
?>
```
这里和C语言不一样不能在函数中引用外部全局变量，但是代码间可以访问
![[Pasted image 20231228113725.png]]
使用关键字global，可以让函数访访问到全局变量
```php
<?php
$root=20;
function show(){
	global $root;
	echo $root." 1<br />";
}
show();
echo $root." 2";
?>

```
![[Pasted image 20231228143514.png]]
还可以使用超全局变量中的”$GLOBALS“数组进行访问。
```php
<?php
$root=20;
function show(){
	$root=$GLOBALS['root'];
	echo $root." 1<br />";
}
show();
echo $root." 2";
?>
```
![[Pasted image 20231228143514.png]]
两个效果相同，就是用法不同
##### 静态变量
静态变量只存在函数内，函数外无法访问。静态变量的值可以保留下次调用函数还可以用这个值
```php
<?php
function show(){
	static $a=1;
	$a++;
	echo $a."<br \>";
}
show();
show();
show();

?>

```
![[Pasted image 20231228144204.png]]
如果不使用关键字static那这个函数的值将不会保留。
##### 变量的销毁
使用 unset()函数实现销毁，不能销毁全局变量
该函数语法是：void unset(变量)
```php
<?php
$a=10;
function show(){
	static $b=20;
	unset ($b);
	unset ($a);
	
	
}
echo $a;
echo $b;

show();
?>
```
![[Pasted image 20231228144919.png]]
#### 数据类型
- [ ] 整型（integer）：存储整数
- [ ] 浮点型（float）：存储实数
- [ ] 字符串型（string）：存储字符串
- [ ] 布尔型（boolean）：存储真（true）假（false）
- [ ] 数组型（array）：存储一组数据
- [ ] 对象型（object）：存储一个类的实例
##### 整型，浮点型，布尔型和字符串型数据
```php
<?php
$int1=2012;   //十进制
$int2=01233; //八进制
$int3=01234;//十六进制
echo $int1." ".$int2." ".$int3."\t"; //都以十进制输出
$float1=3.14;
echo $float1."\t";
echo (Boolean)($int1); //将int1整型转换为布尔变量
?>

```
![[Pasted image 20231228150850.png]]
##### 数组型
在PHP中，使用list()函数或array()函数来创建数组，也可以直接赋值。
例题：
```php
<?php
$arr=array(   //数组定义
	0=>15,
	1=>1.2,
	2=>"hello",
	
);
for($i=0;$i<3;$i++){  //循环打印数组
	echo "$arr[$i]<br \>";
}
?>

```

![[Pasted image 20231228151648.png]]
用”=>“为数组赋值，也可以一个一个赋值
```
$arr[0]=15;
..........
```
##### 资源类型
资源类型是很特殊的类型，他可以表示php扩展资源，也可以表示数据库的连接。对象型类型也算资源类型
##### 对象型
对象就是类的实例。
#### 类型转换
##### 自动类型转换
```php
<?php
	$flo1=1.23;
	echo (int)$flo1;
	
?>

```
![[Pasted image 20231228152148.png]]
使用settype函数强制转换数据类型。
```
Bool settype(var,string type)
```
==这里type的可能值不能是资源类型的数据==
```php
<?php
	$flo1=1.23;
	echo settype($flo1,"int"); //强制转换
	
?>

```
#### 标量类型的声明
默认情况所有PHP文件都处于弱类型校验模式。PHP7加了标量类型声明的特性，标量类型声明有两种情况：==强制模式（默认）和严格模式==
标量类型声明语法格式如下：
```php
declare(strict_types=1);
```
通过指定strict_types的值（1或0）来表示模式，1是严格模式，0是强制模式。

强制即使不是设置的类型也可以执行
```php
//强制模式
<?php
function test(int $param){echo($param);}
test("1");
?>
```
![[Pasted image 20231228184828.png]]
因为默认是强制

严格不是设置的类型就报错
```php
//严格模式
<?php
declare(strict_types=1);
function test(int $param){echo($param);}
test("1");
?>
```
![[Pasted image 20231228184818.png]]
## day3(运算符)
#### 运算符
##### 算术运算符
| 运算符 | 名称 | 描述 | 实例 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| x + y | 加 | x 和 y 的和 | 2 + 2 | 4 |
| x - y | 减 | x 和 y 的差 | 5 - 2 | 3 |
| x * y | 乘 | x 和 y 的积 | 5 * 2 | 10 |
| x / y | 除 | x 和 y 的商 | 15 / 5 | 3 |
| x % y | 模（除法的余数） | x 除以 y 的余数 | 5 % 2  <br>10 % 8  <br>10 % 2 | 1  <br>2  <br>0 |
| -x | 设置负数 | 取 x 的相反符号 | <?php<br>$x = 2;<br>echo -$x;<br>?> | -2 |
| ~x | 取反 | x 取反，按二进制位进行"取反"运算。运算规则：<br><br>~1=-2;   <br>~0=-1; | <?php<br>$x = 2;<br>echo ~$x;<br>?> | -3 |
| a . b | 并置 | 连接两个字符串 | "Hi" . "Ha" | HiHa |

##### PHP递增/递减运算符

|运算符|名称|描述|
|:--|:--|:--|
|++ x|预递增|x 加 1，然后返回 x|
|x ++|后递增|返回 x，然后 x 加 1|
|-- x|预递减|x 减 1，然后返回 x|
|x --|后递减|返回 x，然后 x 减 1|
##### PHP 赋值运算符

在 PHP 中，基本的赋值运算符是 =。它意味着左操作数被设置为右侧表达式的值。也就是说，$x = 5 的值是 5。

|运算符|等同于|描述|
|:--|:--|:--|
|x = y|x = y|左操作数被设置为右侧表达式的值|
|x += y|x = x + y|加|
|x -= y|x = x - y|减|
|x *= y|x = x * y|乘|
|x /= y|x = x / y|除|
|x %= y|x = x % y|模（除法的余数）|
|a .= b|a = a . b|连接两个字符串|
##### PHP 比较运算符

比较操作符可以让您比较两个值：

|运算符|名称|描述|实例|
|:--|:--|:--|:--|
|x == y|等于|如果 x 等于 y，则返回 true|5==8 返回 false|
|x === y|绝对等于|如果 x 等于 y，且它们类型相同，则返回 true|5==="5" 返回 false|
|x != y|不等于|如果 x 不等于 y，则返回 true|5!=8 返回 true|
|x <> y|不等于|如果 x 不等于 y，则返回 true|5<>8 返回 true|
|x !== y|不绝对等于|如果 x 不等于 y，或它们类型不相同，则返回 true|5!=="5" 返回 true|
|x > y|大于|如果 x 大于 y，则返回 true|5>8 返回 false|
|x < y|小于|如果 x 小于 y，则返回 true|5<8 返回 true|
|x >= y|大于等于|如果 x 大于或者等于 y，则返回 true|5>=8 返回 false|
|x <= y|小于等于|如果 x 小于或者等于 y，则返回 true|5<=8 返回 true|
`===`和`！==`需要注意一下。`$b===$c`表示`$b的值和$c`的值不仅仅是值相同==还要类型相同==,而`$b!==$c`表示`$b和$c可能是类型不同也可能是数值不同`

##### PHP 逻辑运算符

|运算符|名称|描述|实例|
|:--|:--|:--|:--|
|x and y|与|如果 x 和 y 都为 true，则返回 true|x=6  <br>y=3  <br>(x < 10 and y > 1) 返回 true|
|x or y|或|如果 x 和 y 至少有一个为 true，则返回 true|x=6  <br>y=3  <br>(`x==6 or y==5`) 返回 true |
|x xor y|异或|如果 x 和 y 有且仅有一个为 true，则返回 true|x=6  <br>y=3  <br>(`x==6 xor y==3`) 返回 false |
|x && y|与|如果 x 和 y 都为 true，则返回 true|x=6  <br>y=3  <br>(x < 10 && y > 1) 返回 true|
|x \|\| y |或|如果 x 和 y 至少有一个为 true，则返回 true|x=6  <br>y=3  <br>(x`==5 \| y==5`) 返回 false |
|! x|非|如果 x 不为 true，则返回 true|x=6  <br>y=3  <br>!(x==y) 返回 true|

##### PHP 数组运算符

|运算符|名称|描述|
|:--|:--|:--|
|x + y|集合|x 和 y 的集合|
|x == y|相等|如果 x 和 y 具有相同的键/值对，则返回 true|
|x === y|恒等|如果 x 和 y 具有相同的键/值对，且顺序相同类型相同，则返回 true|
|x != y|不相等|如果 x 不等于 y，则返回 true|
|x <> y|不相等| 如果 x 不等于 y，则返回 true |
|x !== y|不恒等|如果 x 不等于 y，则返回 true|
##### 位运算符
| 例子 | 名称 | 结果 |
| ---- | ---- | ---- |
| `$a & $b` | And（按位与） | 将把 $a 和 $b 中都为 1 的位设为 1。 |
| $a \| $b | Or（按位或） | 将把 $a 和 $b 中任何一个为 1 的位设为 1。 |
| `$a ^ $b` | Xor（按位异或） | 将把 $a 和 $b 中一个为 1 另一个为 0 的位设为 1。 |
| `~ $a` | Not（按位取反） | 将 $a 中为 0 的位设为 1，反之亦然。 |
| `$a << $b` | Shift left（左移） | 将 $a 中的位向左移动 $b 次（每一次移动都表示“乘以 2”）。 |
| `$a >> $b` | Shift right（右移） | 将 $a 中的位向右移动 $b 次（每一次移动都表示“除以 2”）。 |

位移在 PHP 中是数学运算。向任何方向移出去的位都被丢弃。左移时右侧以零填充，符号位被移走意味着正负号不被保留。右移时左侧以符号位填充，意味着正负号被保留。

##### 否定控制运算符 
| 否定控制符 | 含义 |
| ---- | ---- |
| ！ | 逻辑否 |
| ~ | 按位否 |
##### 错误控制运算符
PHP 支持一个错误控制运算符：`@`。当将其放置在一个 PHP 表达式之前，==该表达式可能产生的任何错误诊断都被抑制==。
##### 三元运算符
```
(exp1)?(exp2):(exp3)
```
如果exp1成立,执行exp2，否则执行exp3;
##### 运算符的优先级和结合规则
- [ ] 加减乘除的先后运算顺序和数学中的一样
- [ ] 对于括号，这先括号内后括号外
- [ ] 对于赋值，由右向左，依次赋值
#### 多维数组
```php
<?php
	$arr[0][0]=10;
	$arr[0][1]=10;
	$arr[0][2]=10;
	
?>
```
和C语言的差不多。

## day4（流程控制）
顺序结构：代码最基础的结构
分支结构：if
循环结构：for
##### php的if结构和C语言相似：
```php
<?php
if (expr)
  statement
?>
```

```php
<?php
if (expr)
  statement
else
  statement
?>
```

```php
<?php
if (expr)
  statement
elseif(expr)
  statement
else 
  statement
?>
```

##### 流程控制的代替语法：
替代语法就把左花括号（{）换成冒号（:），把右花括号（}）分别换成 _endif;_，_endwhile;_，_endfor;_，_endforeach;_ 以及 _endswitch;_。
```php
<?php
if($a==5):
	 echo '1';
 elseif($a==6):
	 echo '2';
 else:
	 echo '3';
endif; 
?>
```
##### while 循环是 PHP 中最简单的循环类型。它和 C 语言中的 _while_ 表现地一样。_while_ 语句的基本格式是：

```php
while (expr)
    statement
```
替代语法：
```php
while (expr):
    statement
    ...
endwhile;
```
##### do-while 循环只有一种语法：（没有替代语法）

```php
<?php   
$i = 0;   
do {      
	echo $i;   
} while ($i > 0); 
?>
```
do-while和while区别在于表达式的值是在每次循环结束时检查而不是开始时.
##### for 循环是 PHP 中最复杂的循环结构。它的行为和 C 语言的相似。 _for_ 循环的语法是：

```php
for (expr1; expr2; expr3)
    statement
```

替代语法：
```php
for (expr1; expr2; expr3):
    statement;
    ...
endfor;
```

##### foreach_ 语法结构提供了遍历数组的简单方式。_foreach_ 仅能够应用于数组和对象
```php
foreach (array_expression as $value)
    statement
foreach (array_expression as $key => $value)
    statement

```
> **Note**:
> 
> 当 _foreach_ 开始执行时，数组内部的指针会自动指向第一个单元。这意味着不需要在 _foreach_ 循环之前调用 [reset()](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/function.reset.html)。
> 
> 由于 _foreach_ 依赖内部数组指针，在循环中修改其值将可能导致意外的行为。
可以在$value前面加&这样就是以引用的方式去赋值而不是拷贝一个值。
```php
<?php
$arr=array(1,2,3,4);
foreach($arr as &$value){
	$value=$value*2;
}
foreach($arr as $values){
	echo $values." ";
}
?>
```
![[Pasted image 20240105100223.png]]
可以看见改变了原来的值。
==foreach_ 不支持用"@"来抑制错误信息的能力。==

##### list()给嵌套的数组解包
遍历一个数组的数组的功能并且把嵌套的数组解包到循环变量中，只需将 [list()](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/function.list.html) 作为值提供。
```php
<?php
$array = [
    [1, 2],
    [3, 4],
];

foreach ($array as list($a, $b)) {
    echo "A: $a; B: $b\n";
}
?> 
```
![[Pasted image 20240105103504.png]]

[list()](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/function.list.html) 中的单元可以少于嵌套数组的，此时多出来的数组单元将被忽略：
```php
<?php
$array = [
    [1, 2],
    [3, 4],
];

foreach ($array as list($a)) {
    echo "A: $a\n";
}
?> 

```
![[Pasted image 20240105110028.png]]
如果 [list()](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/function.list.html) 中列出的单元多于嵌套数组则会发出一条消息级别的错误信息：
```php
<?php
$array = [
    [1, 2],
    [3, 4],
];

foreach ($array as list($a, $b, $c)) {
    echo "A: $a; B: $b; C: $c\n";
}
?> 


```
![[Pasted image 20240105110436.png]]
##### break
_break_ 结束当前 _for_，_foreach_，_while_，_do-while_ 或者 _switch_ 结构的执行。
==_break_ 可以接受一个可选的数字参数来决定跳出几重循环。==这里是C语言没有的。
```php
<?php
$a=10;
$b=10;
for($i=0;$i<$a;$i++):
        for($j=0;$j<$b;$j++):
                if ($j>$i){
                        echo "$j";
                        break 2;
                }
        endfor;
endfor;
?>

```
![[Pasted image 20240105113008.png]]
直接跳出两个for循环
##### continue
continu 在循环结构用用来跳过本次循环中剩余的代码并在条件求值为真时开始执行下一次循环

continue 也可以接受一个可选的数字参数来决定==跳过几重循环到循环结尾==。默认值是 _1_，即跳到当前循环末尾。
```php
<?php
$a=10;
$b=10;
for($i=0;$i<$a;$i++):
        for($j=0;$j<$b;$j++):
                if ($j>$i){
                        echo "$j\n";
                        continue 2;
                }
        endfor;
endfor;
?>

```
![[Pasted image 20240105114832.png]]
##### switch
> **Note**: 注意和其它语言不同，[continue](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/control-structures.continue.html) 语句作用到 switch 上的作用类似于 _break_。如果在循环中有一个 switch 并希望 continue 到外层循环中的下一轮循环，用 _continue 2_。
==这里和C语言不一样==

> 注意 switch/case 作的是[松散比较](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/types.comparisons.html#types.comparisions-loose)。

switch ==结构可以用字符串==
```php
<?php
$i="apple";
switch ($i) {
case "apple":
    echo "i is apple";
    break;
case "bar":
    echo "i is bar";
    break;
case "cake":
    echo "i is cake";
    break;
}
?> 

```
![[Pasted image 20240105115840.png]]


允许使用分号代替 case 语句后的冒号，例如：

```php
<?php
$beer="heineken";
switch($beer)
{
    case 'tuborg';
    case 'carlsberg';
    case 'heineken';
        echo 'Good choice';
    break;
    default;
        echo 'Please make a new selection...';
    break;
}
?>

```
![[Pasted image 20240105115922.png]]
## day5(函数)
#### 文件加载原理
在使用include,require的时候，系统会自动将被包含的文件自动加载到对应代码位置。和C语言的预处理一样。
php中被包含的文件是单独进行编译的。

##### include和require的区别
include和include_once区别：
include系统碰到一次执行一次，而include_once系统只会执行一次
include和require区别就是包含不到文件，报错的形式不一样。
```php
<?php
include 's.zip';
echo '123123';
?>

```

![[Pasted image 20240106145521.png]]
include包含错误只是警告，后面还能用。
```php
<?php
require's.zip';
echo '123123';
?>
    
```
![[Pasted image 20240106145626.png]]
require报错直接退出。
#### 文件加载
绝对路径和相对路径

#### 文件嵌套包含
一个文件包含了另外一个文件，同时被包含的文件也包含另外一个文件
==嵌套包含文件很容易出现相对路径的问题。==例如（./和../）
![[Pasted image 20240106151411.png]]
包含的相对路径会出问题。
#### 函数定义
function 关键字，函数名，参数，函数体和返回值.
```php
function 函数体([参数]){  //中括号是可选的输入参数这里C语言并没有
	//函数体
	//返回值
}

```
函数调用可以在函数定义前这里和C不一样。(原因是编译和执行是分开的，==先编译后执行==)，函数只要在内存中存在，系统就去执行
```php
<?php
ah();

function ah(){
        echo 'hello world';
}
?>

```
![[Pasted image 20240106192418.png]]
#### 参数详解
###### 形参
函数定义时使用的参数
###### 实参
函数调用时使用的参数
形参是实参的载体
###### 函数默认值
```php
<?php
function jian($num1=0,$num2=1){
        echo $num1+$num2;
}
jian();
?>


```
![[Pasted image 20240106193516.png]]
函数内部定义变量和外部变量是不一样的，同一个名字也不一样
##### 引用传递
在函数内部改变函数外部的变量
基本定义语法：
```php
function 函数体(形参1,&形参2){
	//函数体
}

```
在调用的时候，必须传递
##### 静态变量
静态变量的作用就是跨函数共享数据（同一个函数多次使用）
static定义静态变量
```php
<?php
function jian(){
        $name=1;
        static $age=1;
        echo $age++."\n";
}
jian();
jian();
?>

```
![[Pasted image 20240106201857.png]]
用处：
1. 统计函数被调用的次数
2. 统计多次调用得到的不同结果（递归思想）
##### 可变函数
可变函数：当前有一个变量所保存的值，刚好是一个函数的名字，那么就可以使用变量充当函数名使用。
```php
$变量='display';
function display(){
	echo 'yes';
}
$变量();
```
```php
<?php
$fun='display';
function display(){
        echo 'yes';
}
$fun();

?>
```
![[Pasted image 20240107092701.png]]
可变函数的魅力![[Pasted image 20240107092821.png]]
传入的过程叫做回调过程，传入的函数叫回调函数
##### 匿名函数
没有名字的函数：
基本语法：
```
变量名=function(){
 //函数体
};
```
![[Pasted image 20240107094738.png]]
变量保存匿名函数本质上是得到一个对象

##### 闭包函数
函数内部有一些局部变量没有被释放因为函数内部还有对应的函数在引用（匿名函数）
```php
<?php
function display(){
        $name =__FUNCTION__;
        $inc=function(){
                echo $name;
        };
        $inc();
}
display();

?>

```
![[Pasted image 20240107102339.png]]
这里就是$name和匿名函数不是同一个地方所以不能引用。
```php
<?php
function display(){
        $name =__FUNCTION__;
        
        $inc=function() use($name){ //将外部局部变量保留给内部使用
                echo $name;
        }; //函数内部函数
        $inc();
}
display();

?>

```
![[Pasted image 20240107102407.png]]
##### 伪类型
假类型，实际上在PHP中不存在的类型。但是通过伪类型可以帮助程序员去更好的查看操作手册从而更方便学习。

伪类型主要有两种：在三大类八小类之外

Mixed：混合的，可以是多种PHP中的数据类型
Number：数值的，可以是任意数值类型（整形和浮点型）
 
![[Pasted image 20240107103416.png]]

## day6
#### 常用函数
###### 输出
print():类似于echo ，不是一个真正的函数，而是一个结构，所以可以不用括号包裹
print_r()：类似于var_dump
![[Pasted image 20240106101623.png]]
###### 时间
data():按照指定格式对应时间戳（从1970年格林威治时间开始计算秒数）
string **date** ( string `$format` [, int `$timestamp` ] )

返回将整数 `timestamp` 按照给定的格式字串而产生的字符串。如果没有给出时间戳则使用本地当前时间。换句话说，`timestamp` 是可选的，默认值为 [time()](mk:@MSITStore:C:\Users\ADMINI~1\AppData\Local\Temp\Rar$DIa10924.45350\php手册2015.chm::/res/function.time.html)。

time():获取当前时间对应的时间戳


microtime():获取微秒级时间戳

```php
<?php
echo date('Y m d H:i:s',12345678)."\n";
echo time();
?>
```
![[Pasted image 20240106103903.png]]
strtotime():按照规定格式的字符串转换成时间戳
```php
<?php
echo date('Y m d H:i:s',12345678)."\n";
echo time()."\n";
echo strtotime('10 hours');
?>
```

![[Pasted image 20240106104323.png]]
###### 数学
max():最大值
min()：最小值
rand()：随机数
mt_rand()：和rand一样但是更好
round：四舍五入
ceil():向上取整
floor():向下取整
pow():求指定数字指定指数的结果
abs()：绝对值
sqrt():求平方根
###### 关于函数的函数
![[Pasted image 20240108093437.png]]
##### php字符串定义
###### 引号定义：
$str1='hellow';
适合比较短的不超过一行的，没有结构要求的字符串
如果有结构要求可以使用以下两种结构定义
###### nowdoc字符串
没有单引号字符串的单引号字符串
```
$str=<<<'边界符'
	字符串内容
边界符;
```
也可以定义常量
###### heredoc字符串
没有双引号字符串双引号字符串
```
$str=<<<边界符
	字符串内容
边界符;
```
```php
<?php
$str1=<<<EOD
        hello
EOD;
$str2=<<<'EOD'
        hello
EOD;
var_dump($str1,$str2);
?>

```
![[Pasted image 20240108105349.png]]
结构化定义字符串还是比较保持结构的样子。
##### 字符串转义
```
\r\n：回车换行
php在识别转义字符的时候也是使用一样的模式反斜杠+字母
\'在单引号中显示单引号
\"在双引号中显示双引号
\r表示回车
\n表示新建一行
\ttab键
\$显示$
```
双引号可以识别$符号,解析变量而单引号不可以解析变量
```php
<?php
$str1=<<<EOD
        hello
EOD;
$str2=<<<'EOD'
        hello
EOD;
echo '$str1';
echo "$str2";
?>

```
![[Pasted image 20240108105824.png]]
```
echo "sabc{$a}sdf"; //规则的变量符
```
###### 结构化定义字符串变量规则
结构化定义字符串对应边界符有条件
1. 上边界符后面帮你跟任何内容
2. 下边界符必须定格：最左边
3. 下边界符只能跟分号，不能跟内容
4. 结构化定义字符串的内部的所有内容都是字符串本身。
##### 字符串长度
strlen()得到字符串的长度，以字节为单位。默认是ascii字符集
```php
<?php
$a="shan";
echo strlen($a);
?>

```
![[Pasted image 20240108112434.png]]
mb_strlen()要开启扩展，可以指定字符集，默认是ascii字符集
![[Pasted image 20240108112823.png]]
#### 字符串相关函数：
###### 转换函数：implode(),explode(),str_split()
implode(连接方式,数组)：将数组中元素按照某个规则连接成字符串

explode(分割字符,目标字符串)：将字符串按某种格式分割，变成数组

str_split(字符串，字符串长度)：按照字符串长度拆分字符串得到数组

```php
<?php
$arr=array('shan','ji','qiang');
var_dump(implode("",$arr));
$str="shan,ji,qiang";
var_dump(explode(',',$str));
$str1="hahahahahaha";
var_dump(str_split($str1,4));
?>
```
![[Pasted image 20240108144825.png]]
###### 截取函数：trim(),ltrim(),rtrim()
trim(字符串[,指定字符])：默认去除两边空格（中间不行）但是可以指定要去除的内容，按照指定内容循环去除两边有的内容
ltrim(字符串[,指定字符])：去除左边的
rtrim(字符串[,指定字符])：去除右边的
```php
<?php
$str="shan,ji,qiang";
var_dump(trim($str,"g"));
?>
```
![[Pasted image 20240108145536.png]]
substr(字符串,起始位置[,指定长度])：指定位置开始截取字符串，可以指定截取长度，不指定就到字符串尾部
strstr(字符串,匹配字符)：从指定位置截取到字符串尾部和C语言一样,取文件后缀。
```php
<?php
$str="shan,ji,qiang";
var_dump(substr($str,1,3));
var_dump(strstr($str,"ji"));
?>
```
![[Pasted image 20240108150648.png]]
###### 大小转换函数:strtolower(),strtoupper(),ucfirst()
strtolower(字符串):全部小写
strtoupper(字符串)：全部大写
ucfirst(字符串):首字母大写
```php
<?php
$str="shan";
$str1="SHAN";
echo strtoupper($str)."\n";
echo strtolower($str1)."\n";
echo ucfirst($str)."\n";
?>
```
![[Pasted image 20240108152504.png]]
###### 查找函数：strpos(),strrpos()
strpos(字符串,判断字符):判断字符在字符串的首次出现的地方
strrpos(字符串,判断字符):判断字符在字符串的最后出现的地方
```php
<?php
$str="shanjiqiang";
echo strpos($str,'n')."\n";
echo strrpos($str,'n');
?>
```
![[Pasted image 20240108153909.png]]
###### 替换函数：str_reploace()
str_replace(匹配目标,替换内容,字符串本身)：将目标字符串中包含匹配的字符串进行替换成字符本身
```php
<?php
$str="shanjiqiang";
echo str_replace('n','e',$str)."\n";
?>
```
![[Pasted image 20240108154425.png]]
###### 格式化函数：printf(),sprintf()
printf/sprintf(输出字符串有占位符,顺序占位内容。。。):格式化输出数据和==C语言一样==
使用方法
```php
<?php
$str="123";
echo sprintf("%d",$str);
?>

```
![[Pasted image 20240108155205.png]]
###### 其他：str_repeat(),str_shuffle()
str_repeat(字符串,次数)：重复某个字符串N次
str_shuffle(字符串):随机打乱字符串
```php
<?php
$str="shan";
echo str_repeat($str,5)."\n";
echo str_shuffle($str);
?>

```
![[Pasted image 20240108160423.png]]
#### 数组
数组：array,数据的组合
##### 数组定义语法
使用array关键字：最常用
$变量=array(元素1,元素2,元素3...);
用中括号包裹数据
$变量=[元素1,元素2];
隐形数组，给变量增加中括号，系统自动变成数组
$变量[]=元素1;
$变量[下标]=值,中括号的内容可以是下标key,该下标可以是字母（单纯）或数字，于变量命名规则相似,这里和C语言不一样，可以用字母来定义。
```php
<?php
//定义数组：array
$arr1=array('1',123,'hello');
//定义数组：[]
$arr2=['1',123,'hello'];
//隐形数组：
$arr3[10]=1;
$arr3[1]=2;
$arr3['key']='root';
var_dump($arr1,$arr2,$arr3)
?>```
![[Pasted image 20240109100656.png]]

##### php数组特点：
1. 可以整数下标或者字符串下标
2. 不同下标可以混合在一起
3. 数组元素的顺序是以放入顺序为准，跟下标无关
4. 数字下标的自增长性
5. 特殊值下标的自动转换
6. 数组元素没有类型限制
7. 数组元素没有长度限制
注意：php数组是很大的数据，所存储位置是堆区，为当前数组分配一块连续的数组。
#### 多维数组
数组里面的元素又是数组
##### 二维数组
数组所有的元素都是一维数组
![[Pasted image 20240109101618.png]]
##### 多维数组
在第二维数组元素中可以继续是数组，在php中没有维度限制
不建议三维以上，会增加访问复杂度
##### 异性数组（不规则数组）
数组中元素不规则，有普通基本变量也有数组
#### 数组遍历
```php
<?php
$arr=array(0=>array('name'=>'tom'),1=>array('age'=>'18'));
//访问一维数组元素
var_dump($arr[0]);//
//访问二维数组元素
var_dump($arr[0]['name']);
?>
```
![[Pasted image 20240109105655.png]]
###### 数组遍历foreach()
基本语法如下：
```
foreach($数组变量 as [$下标=>] $值){
	//通过$下标访问元素的下标；通过$值访问数组的每个值
}
```
```php
<?php
$arr=array(1,2,3,4,5,6);
foreach($arr as $k => $vul){
        echo $k.":".$vul."\n";
}
?>

```
![[Pasted image 20240109110515.png]]
二维
```php
<?php
$arr=array(0=>array('name'=>'tom'),1=>array('name'=>'shan'));
foreach($arr as  $vul){
        echo $vul['name']."\n";
}
?>


```
![[Pasted image 20240109111336.png]]
###### foreach()遍历原理
1. foreach()会重置指针：让指针指向第一个元素：
2. 进入foreach()循环：通过指针取得当前第一个元素，任何将下标取得变量$k（如果存在）中，将值取出来放到对应值变量$$v中（指针移动）
3. 进入循环内部（循环体），开始执行
4. 重复2和3步骤，直到2取不到内容
###### for循环遍历
和C语言一样
```php
<?php
$arr=array(0=>array('name'=>'tom'),1=>array('name'=>'shan'));
for($a=0;$a<count($arr);$a++){
       var_dump($arr[$a])."\n";
}
?>

```
![[Pasted image 20240109114008.png]]
###### while配合each和list遍历数组
本身就可以和for一样遍历数组
	each函数使用：能够从一个数组中获取当前数组指针所指向的元素的下标和值，拿到之后将数组指针下移，同时将这些值 
	以四个元素的数组返回
	![[Pasted image 20240109120302.png]]

7.2版本已经弃用
list()必须从数组中获取数据，而且从0开始
```php
<?php
$arr=array(0,'name'=>'ahg',3,'name1'=>'shan');
var_dump(list($ar)=$arr)."\n";
var_dump($ar);
?>
```
![[Pasted image 20240109141700.png]]
each搭配list![[Pasted image 20240109144543.png]]
#### 数组的相关函数
###### 排序函数都是按照ASCII码首字母比较
sort():顺序排序（下标重排）
![[Pasted image 20240110084506.png]]
rsort():逆向排序
![[Pasted image 20240110084545.png]]
asort():顺序排序（下标保留）
![[Pasted image 20240110084532.png]]
arsort():逆向排序（下标保留）
![[Pasted image 20240110084557.png]]
ksort():顺序排序（按照键值排序）
![[Pasted image 20240110082339.png]]
shuffle()：随机打乱
![[Pasted image 20240110083115.png]]
###### 指针函数
reset()：重置指针，将数组指针回到首位。
end(): 重置指针，将数组指针重置到最后一位。
next()：指针下移，取得下一个元素的值
prev(): 指针上移，取得上一个元素的值
current():获取当前指针对应的元素值
key():获取当前指针对应的下标值 
![[Pasted image 20240110090028.png]]
#### 其他函数
count():统计数组中元素的数量
![[Pasted image 20240111085420.png]]
array_push()：在数组后追加一个元素
array_pop()：从数组后取走一个元素
array_shift(): 从数组前面取走一个元素
array_unshift():从数组前面压进去一个元素
###### PHP模拟数据结构：
栈：先进后出
队列：先进先出
###### 栈模拟
array_push()和array_pop()在后面模拟栈
array_shift()和array_unshift()在前面模拟栈
![[Pasted image 20240111084610.png]]
从后面压进去
![[Pasted image 20240111084811.png]]
出栈就也从后面取出
###### 队列模拟
array_push()和array_shift()从后进前出
array_unshift()和array_pop()从前进后出
![[Pasted image 20240111085153.png]]
array_reverse():数组元素反转
![[Pasted image 20240111085622.png]]
in_array():判断元素在数组中是否存在
![[Pasted image 20240111085800.png]]
array_keys():获取数组的所有下标，索引数组

array_values():获取数组所有值，索引数组



##### 选择排序算法
```php
<?php
$arr=array(3,2,1,4,5,7,9);
for($i=0,$len=count($arr);$i<$len;$i++){
	$min=$i;
	for($j=$i+1;$j<$len;$j++){
		if($arr[$min]<$arr[$j])
			$min=$j;
	}
	if($min!=$i){
		$tmp;
		$tmp=$arr[$min];
		$arr[$min]=$arr[$i];
		$arr[$i]=$tmp;
	}
}
var_dump($arr);
?>

```
![[Pasted image 20240111162223.png]]



## day7
### 类与对象
###### 面向对象编程优点
封装性
继承性
多态性
##### 类的声明
声明关键字是class，格式
```PHP
<?php
	权限修饰符 class 类名{
		类的内容;
	}
?>

```
权限修饰符是可选项
一般情况是默认public，这意味着属性和方法的各个项从类内部和外部都能访问。相当于公开
==private声明属性和方法则只能从类内部访问。protected声明的属性和方法也是只能从类内部访问，但是可以通过继承的子类访问。==
###### 成员属性
	指的是类中声明的变量
每个变量将存储不同的对象属性信息。
其中成员属性必须用关键词修饰，public,protected private。
声明成员属性可以不进行赋值操作。
```
public class student{
	 public $name; 类成员属性
}
```
###### 成员方法 
指的是类中的函数，当然也能声明多个函数，类的成员方法可以通过关键字修饰,从而控制成员方法使用
```
public class student{
	 public $name; //类成员属性
	 function s(){
	 } //类成员方法
}
```
###### 类的实例化
总而言之类的实例化就成对象了
实例化格式：
```
$变量名=new 类名称([参数]);
```
new为创建对象的关键字
一个类可以实例化多个对象
###### 访问类中的成员属性和方法
通过对象的引用可以访问类中的成员属性和方法，这里需要特殊字符“->”具体语法
```
$变量名=new 类名称();   //类的实例化
$变量名->成员属性=值;   //为成员属性赋值
$变量名->成员属性;   //直接获取成员的属性值
$变量名->成员方法   //访问对象中指定的方法
```
和普通的调用对象和方法一样，只不过要加$变量名->成员属性或成员方法这里不用加 $
另外用户还可以使用一些特殊的访问方法。
###### $this
$this存在于类的每一个成员方法中，是一个特殊的对象引用方式。主要作用是完成对象内部成员的访问
给类属性去赋值
```php
<?php
//定义类
class guests{
	public $name;//成员属性
	function set($ame){
		$this->name=$ame; //将这个set的成员方法里面的参数来改变类成员属性
	}
}
$nam=new guests();
$nam->set("shanjiqiang");
var_dump($nam->name);
?>
```
![[Pasted image 20240112095501.png]]
###### 操作符"::"
操作符”::“可以没有任何声明实例的情况下访问类中的成员。访问静态的，访问动态的会报错
```
关键字::变量名/常量名/方法名
```
通过parent::来访问被覆盖的方法或静态属性
关键字主要包括parent，self和类名三种，parent可以调用父类中的成员变量常量和成员方法。self可以调用当前类中的常量和静态成员。
```php
<?php
//定义类
class guests{
	public $name="shan";//成员属性
	public $age=12;
	function pepnle(){
		echo "shan";
	}
}
guests::pepnle();
?>
```
![[Pasted image 20240112100843.png]]
::class
获取类名
```php
<?php
//定义类
class guests{
	public $name="shan";//成员属性
	public $age=12;
	function pepnle(){
		echo guests::class;
	}
}
guests::pepnle();
?>
```
![[Pasted image 20240112102038.png]]
###### extends关键字 子类
继承另一个类的方法和属性

```php
<?php
	//定义类
	class gute{
		public $haha="jicheng";
	}
	class guests extends gute{
		public $name="shan";//成员属性
		public $age=12;
		function pepnle(){
			echo guests::class."\n";
			echo $this->haha;
		}
	}
$A=new guests();
echo $A->pepnle();
?>
```
![[Pasted image 20240112102540.png]]
###### final关键字
父类方法声明final，不能覆盖;类声明final，不能继承.属性不能定义为final
```php
<?php
	//定义类
	class gute{
		function key(){
			echo "qiang";
		}
	}
	class guests extends gute{
		public $name="shan";//成员属性
		public $age=12;
		final function key(){
			echo "jicheng";
		}
		function pepnle(){
			return self::key()."\n";
			return parent::key()."\n";
		}
	}
$A=new guests();
echo $A->pepnle();
?>
```
![[Pasted image 20240112104517.png]]
###### 常量
定义
```
const 常量名=值 名不加$,值必须定值，不能是变量
```
调用
```
名不加$，和调用静态变量一直
```
```php
<?php
	//定义类
	class gute{
		const shan ="shan";
		function key(){
			echo "qiang";
		}
	}

echo gute::shan;
?>
```
![[Pasted image 20240112115504.png]]
  在类中的常量和静态变量实例化为对象是不会显示的，==因为常量和静态变量是属于类的，不是属于对象的==
  ![[Pasted image 20240112145421.png]]
由于静态方法不需要通过对象即可调用，所以伪变量 $this 在静态方法中不可用。

静态属性不可以由对象通过 -> 操作符来访问。
###### 类的自动加载
![[Pasted image 20240112150422.png]]
感觉一般般没啥用
###### 构造函数和析构函数
`__construct`：在实例化到时候一定会第一个调用这个，就像C语言的main()一样
还可以给他加参数
```php
<?php
//定义类
class guests{
	public $name;//成员属性
	public $age;
	public function __construct($n,$a){
			$this->name=$n;
			$this->age=$a;
			$this->set();
				
	}
	public function set(){
		echo $this->name; //将这个set的成员方法里面的参数来改变类成员属性
		echo $this->age;
	}
}
$nam=new guests("shan",12); //传递的值给到__construct
?>
```
![[Pasted image 20240112100049.png]]
`__destruct`:调用完毕，做清理工作，就是最后执行的工作
```php
<?php
//定义类
class guests{
	public $name;//成员属性
	public $age;
	public function __construct($n,$a){
			$this->name=$n;
			$this->age=$a;
			$this->set();
				
	}
	public function set(){
		echo $this->name; //将这个set的成员方法里面的参数来改变类成员属性
		echo $this->age;
	}
	public function __destruct(){
		echo "收工";
	}
}
$nam=new guests("shan",12); //传递的值给到__construct
?>
```
![[Pasted image 20240112153403.png]]
###### 抽象类
定义为抽象的类不能被实例化。任何一个类，==如果它里面至少有一个方法是被声明为抽象==的，那么这个类就必须被声明为抽象的。被定义为抽象的方法只是声明了其调用方式（参数），不能定义其具体的功能实现。




























------------------------------------------------------------------------
# 杂



\_FILE\_ 文件路径和文件名

PHP_VERSION php版本

**[strcmp]{.mark}**

```
int strcmp ( string $str1 , string $str2 )1
```

参数 str1 第一个字符串。str2 第二个字符串。如果 str1 小于 str2 返回
\<0； 如果 str1 大于 str2 返回\> 0；如果两者相等，返回 0。区分大小写

绕过的漏洞就是[数组或者一个 object
即可，就可以让比较直接变成0,就是相当于两个都相等，从而绕过验证。]{.mark}

**empty判断字符是否为空**

bool empty ( mixed \$var )

**is_numeric**

**PHP 提供了 is_numeric
函数，用来变量判断是否为数字。但是函数的范围比较广泛，不仅仅是十进制的数字。**

bool is_numeric ( mixed \$var )

[如果指定的变量是数字和数字字符串则返回 TRUE，否则返回
FALSE，注意浮点型返回 1，即 TRUE。]{.mark}

[is_numeric 函数对于空字符 %00，无论是 %00
放在前后都可以判断为非数值，而 %20 空格字符只能放在数值后。]{.mark}

**PHP preg_match_all() 函数**

1,方括号 \[n\] 在目标寻找字符n

2,连字符\[A-Za-z\] 匹配全部任意字符

2，点字符在正则表达式中是一个通配符，\".er\"
匹配所有三个字符中结尾是er的字符

'''''''''''''''''''''''''

[认证email的正则表达]{.mark}

[\^\[a-zA-Z0-9\_-\]+@\[a-zA-Z0-9\_-\]+(\\.\[a-zA-Z0-9\_-\]+)+\$]{.mark}

[PHP 正则表达式(PCRE)](https://www.runoob.com/php/php-pcre.html)

preg_match_all 函数用于执行一个全局正则表达式匹配

```php
<?php

show_source("test.php");

?>
```

原理: flag_1234.php=\*\_1234.php (绕过)

![截图.png](    Php语言/media/image1.png){width="4.291666666666667in"
height="2.3755096237970252in"}

[正则分析 /key.\*key.{4,7}key:/./(.\*key)\[a-z\]\[\[:punct:\]\]/]{.mark}

key就是普通的字符

.是除了换行的任意字符，假设就是a \*匹配0或多个正则表达式，假设有2个

key又是一个普通字符

.{4,7}就是匹配4-7个任意字符(包括4，不包括7)，假设有5个a

key普通字符

:又是普通字符

\\反斜杠进行转义，此处取/的原意

.任意字符，假设取a

/同上，取/原意

()改变逻辑顺序，此处不影响，按.\*key顺序正则匹配

假设两个a和key

\[a-z\]取a-z中任意一个字符，假设取a

\[:punct:\]就是特殊字符的意思，\[\[:punct:\]\]就是在特殊字符里取一个，假设是;(当然也可以是@#等等)

**json_encode()函数**

**格式转换**

**echo 输出不了数组用 json_encode()转换**

**如 echo json_encode($data);**

**serialize序列化函数**

**对象转序列化**

**如 echo serialize($data);**

**unserialize反序列化**

**序列化转对象**

**在序列化转对象时候如果没过滤并且有执行函数就可以传php代码**

**如**

![截图.png](    Php语言/media/image2.png){width="5.760416666666667in"
height="3.2402351268591425in"}

**[有@eval()函数和\$\_GET变量利用]{.mark}**

![截图.png](    Php语言/media/image3.png){width="5.760416666666667in"
height="3.2402351268591425in"}

**[注意长度也要符合]{.mark}**

![截图.png](    Php语言/media/image4.png){width="5.760416666666667in"
height="2.033589238845144in"}

2 要绕过正则表达式

(preg_match('/\[oc\]:\\d+:/i', \$var))

而正则匹配的规则是: 在不区分大小写的情况下 ， 若字符串出现 "o:数字" 或者
\"c:数字' 这样的格式 ， 那么就被过滤 .很明显 ， 因为 serialize()
的参数为 object ，因此参数类型肯定为对象 \" O \" ，
又因为序列化字符串的格式为 参数格式:参数名长度 ， 因此 \" O:4 \"
这样的字符串肯定无法通过正则匹配

绕过

而O:+4没被过滤说明绕过了过滤而且最后的值不变。

//wakeup绕过 在原来的1个元素加一个数

```php
<?php

class Demo {

private $file = 'index.php';

public function __construct($file) {

$this->file = $file;

}

function __destruct() {

echo @highlight_file($this->file, true);

}

function __wakeup() {

if ($this->file != 'index.php') {

//the secret is in the fl4g.php

$this->file = 'index.php';

}

}

}

$A = new Demo ('fl4g.php');//创建对象

$C = serialize($A);                     //对对象A进行序列化

$C = str_replace('O:4','O:+4',$C);      //绕过正则表达式过滤 #将O:4 替换O:+4

$C = str_replace(':1:',':2:',$C); //wakeup绕过

var_dump($C);

var_dump(base64_encode($C));            //base64加密

?>
```
**getimagesize检查文件大小，一般用于文件上传**

**preg_replace()函数**

替换函数

例如：

```php
<?php

$str=preg_replace('/a/,'b',"aaaaaaaaa'')

echo $str

?>
```

会将aaaaaaaaa里面包含a的全部替换成b

一般用于过滤非法字符

如：

```php
<?php

if(isset($_GET['code'])){

     $code=$_GET['code'];

     preg_replace("\/[(.*)\}/e",'\\1',$code) #正则匹配将中括号的值转换成1

}

?>
```

[trim函数：去除首尾空格]{.mark}

[file_get_contents函数：读取文件内容]{.mark}

![stickPicture.png](    Php语言/media/image5.png){width="5.760416666666667in"
height="2.576596675415573in"}

**[PHP内置过滤函数]{.mark}**

php.ini 魔术引号：

magic_quotes_gpc = On

magic_quotes_runtime =Off

[本特性已自 PHP 5.3.0 起废弃并将自 PHP 5.4.0 起移除。]{.mark}

[当打开时，所有的 \'（单引号），\"（双引号），\\（反斜线）和 NULL
字符都会被自动加上一个反斜线进行转义。这和 addslashes()
作用完全相同]{.mark}

**[addslashes()]{.mark}**

[将单引号，双引号，反斜杠，NULL进行加反斜杠转义]{.mark}

[用法：addslashes(\$x)
#就可以将\$x之前不管是使用什么传入方式发现可以转义就在前面添加反斜杠转义]{.mark}

```php
<?php

    header("content-type:text/html;charset=utf-8");

    $x = $_GET['cmd'];

    $y=addslashes($x);

    print_r($y);

?>
```

![截图.png](    Php语言/media/image6.png){width="5.760416666666667in"
height="4.345704286964129in"}

** stripslashes（）**

该方法会删除所有的反斜杠

防止文件包含的绝技

stripslashes使用方法：

![截图.png](    Php语言/media/image7.png){width="4.138888888888889in"
height="1.7931714785651793in"}

![截图.png](    Php语言/media/image8.png){width="5.760416666666667in"
height="1.5382327209098863in"}

![截图.png](    Php语言/media/image9.png){width="4.986111111111111in"
height="2.217205818022747in"}

![截图.png](    Php语言/media/image10.png){width="5.760416666666667in"
height="1.0523840769903763in"}

**[htmlspecialchars()函数]{.mark}**

**[防止xss注入的绝招]{.mark}**

![截图.png](    Php语言/media/image11.png){width="5.760416666666667in"
height="1.6954068241469815in"}

将危险字符进行html实体化使用方法,无效编码就返回空：

htmlspecialchars(\$x);

```php
<?php

    header("content-type:text/html;charset=utf-8");

    $x = $_GET['cmd'];

    $y=htmlspecialchars($x);

    print_r($y);

?>
```

![截图.png](    Php语言/media/image12.png){width="5.760416666666667in"
height="1.1708748906386701in"}

![截图.png](    Php语言/media/image13.png){width="5.760416666666667in"
height="0.85793416447944in"}

**strip_tags()函数**

**防止xss好办法**

**去除空字符串，html和php标记**

**用法也是：strip_tags(\$x);**

```php
<?php

    header("content-type:text/html;charset=utf-8");

    $x = $_GET['cmd'];

    $y=strip_tags($x);

    print_r($y);

?>
```

![截图.png](    Php语言/media/image14.png){width="5.760416666666667in"
height="0.8960651793525809in"}

**escapeshellcmd()函数**

**对字符串中可能会欺骗shell命令执行任意的字符进行转义，保证用户输入数据是安全的**

**用法：escapeshellcmd(\$x);**
```php
<?php

    header("content-type:text/html;charset=utf-8");

    $x = $_GET['cmd'];

    $y=escapeshellcmd($x);

    print_r($y);

?>
```

![截图.png](    Php语言/media/image15.png){width="5.760416666666667in"
height="1.03920384951881in"}

**intval函数**

[函数用于获取变量的整数值。]{.mark}

**使用方法：**

**\$id=intval(\$\_GET\[\'id\'\]);**

```php
<?php

    header("content-type:text/html;charset=utf-8");

    $x = intval($_GET['cmd']);

    print_r($x);

?>
```

![截图.png](    Php语言/media/image16.png){width="5.760416666666667in"
height="1.0942443132108486in"}

**http-only防御那么js脚本将无法读取cookie信息。**

![截图.png](    Php语言/media/image17.png){width="5.760416666666667in"
height="0.6598862642169728in"}

**sprintf函数漏洞**

<https://www.ctf.show/challenges#%E7%BB%99%E5%A5%B9-119>**靶场**

sprintf函数使用switch
case对15种类型做了匹配，包括%s、%d、%u...但如果在15种类型之外就会直接break。

当我们输入%\\或%1\$\\时，sprintf会把反斜杠当做格式化字符串的类型，但他们并不在15种类型之中，就会未经任何处理而被替换为空

具体漏洞可见 php sprintf 漏洞

![截图.png](    Php语言/media/image18.png){width="5.760416666666667in"
height="0.718853893263342in"}

![截图.png](    Php语言/media/image19.png){width="5.760416666666667in"
height="0.7285520559930009in"}

**[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{.mark}**

**[文件上传笔记]{.mark}**

**[上传页面设置.上传方式是POST还是GET，还有enctype类型，和上传到文件的页面,加入上传的文件类型，和名字定义，]{.mark}**然后加入\<buttor\>提交\</buttor\>按钮

```html
    <form action="update.php" method="post" enctype="multipart/form-data">

        <input type="file" name="up">

        <button>提交</button>

    </form>
```

**[并且设置好php.ini的]{.mark}** upload_tmp_dir =
\"D:/phpstudy_pro/WWW/update\" （windows格式，默认在前面有；要去掉）

**[然后创建update.php文件]{.mark}**

[**用print_r(**\$\_FILES**)#**通过\$\_FILES超级全局变量进行读取]{.mark}

[然后文件就回上传到临时文件夹中不过一瞬间就
回消失可以设置sleep(10)这样就可以停留10秒，然后在保存到永久的文件夹中]{.mark}

[将临时文件转移到永久目录里要写的函数：]{.mark}

```php
function uploader() #定义函数

{

    if(is_uploaded_file($_FILES['up']['tmp_name'])) #判断是否合法，如果没成功就false

    {

        $to ='upload/' . $_FILES['up']['name']; #将保存文件地址为源文件名赋值到$to,可以使用time时间戳添加以防有相同

        if(move_uploaded_file($_FILES['up']['tmp_name'],$to))#将文件转移到$to的地方去

        {

            return $to; #成功打印地址

        }

    }

    return false; #错误打印false

}

var_dump(uploader());
```

**[通过前台表单的形式过滤字节大小：]{.mark}**

**[字节大小过滤要放在\<form\>\</form\>里面的最前面]{.mark}**

```php
<input type="hidden" name="MAX_FILE_SIZE" value="2000">#字节为单位

    <form action="update.php" method="post" enctype="multipart/form-data">

        <input type="hidden" name="MAX_FILE_SIZE" value="2000">

        <input type="file" name="up">

        <button>提交</button>

    </form>
```

**[加固设置文件上传目录无执行权限（简单粗暴）]{.mark}**

**[文件上传设置白名单jpg/png/gif]{.mark}**

```php
<?php

function uploader(){

    if(($_FILES['up']['type'] == 'image/jpeg') || ($_FILES['up']['type'] == 'image/png') || ($_FILES['up']['type'] == 'image/gif'))

    {

        $to ='upload/' . $_FILES['up']['name'];

        if(move_uploaded_file($_FILES['up']['tmp_name'],$to))

        {

            return $to;

        }

    }

    return $_FILES['up']['name'];#失败返回上传名字

}

var_dump(uploader());
?>
```

![截图.png](    Php语言/media/image20.png){width="4.861111111111111in"
height="1.0513320209973753in"}

![截图.png](    Php语言/media/image21.png){width="4.430555555555555in"
height="1.0633333333333332in"}

文件上传加固

![截图.png](    Php语言/media/image22.png){width="3.6527777777777777in"
height="0.5531353893263342in"}

设置目录内禁止解析php后缀文件

**[文件上传利用的常见函数]{.mark}**

**deldot函数（）**

**去除字符串尾部的点**

**使用方法：echo deldot(\"hell.world\...);**

**输出为:hell.world**

**strrchr**

strrchr(string \$haystack, mixed \$needle): string

strrchr函数在字符串\$haystack中查找\$needle，并将最后一次查找到的\$needle及其后面的字符串返回。如果没有在该字符串中查找到\$needle，则返回false。

注：

如果第二个参数不是不是单个字符，则只使用该字符串的第一个字符进行查找匹配。

如果第二个参数是一个数值，则将该数值转换为对应的ASCII码进行匹配。

\<?php\$s=\"1.phP\";\$k=strtolower(\$s);echo \$e=strrchr(\$k,\".\");?\>

![截图.png](    Php语言/media/image23.png){width="4.013888888888889in"
height="1.084271653543307in"}

**5. strtolower**

strtolower(string \$string): string

将字符串\$string中的**各个英文字符转换为小写并返回**。

当然也可以是数组集体转换

```php
<?php

$s="1.phP,2.pHTml,3.PHp3";

$k=strtolower($s);

echo str_ireplace("php","",$k)."\n";

?>
```

![截图.png](    Php语言/media/image24.png){width="3.263888888888889in"
height="1.3973195538057743in"}

**[str_ireplace函数]{.mark}**

**[用于对数组中的元素或字符串中的子串进行替换。（不区分大小写，只会过滤一次绕过双写绕过就没办法了）]{.mark}**

[**用法：**echo
str_ireplace(\"php\",\"\",\"hello.php\").\"\\n\";]{.mark}

```php
<?php

$s="1.php,2.phtml,3.php3";

echo str_ireplace("php","",$s)."\n";

?>
```

![截图.png](    Php语言/media/image25.png){width="3.736111111111111in"
height="0.978257874015748in"}

**strstr**

**strchr :也是返回第一次出现的地方和strstr用法一样**

strstr(string \$haystack, mixed \$needle, bool \$before_needle = false):
string

查找字符串\$needle在\$haystack中首次出现的位置，并将\$needle及其之后的字符串返回。

PHP5起新增第三个参数\$before_needle，如果\$before_needle取值为true，则返回\$needle前面的部分。

```php
<?php

$s="hahahphpinfo.php";

echo strstr($s,"php");

?>
```

![截图.png](    Php语言/media/image26.png){width="4.083333333333333in"
height="1.0in"}

**substr函数**

**语法**

substr(**string,start,length**)

```php
<?php

echo substr("Hello world",0,10)."<br>";

echo substr("Hello world",1,8)."<br>";

echo substr("Hello world",0,5)."<br>";

echo substr("Hello world",6,6)."<br>";

echo substr("Hello world",0,-1)."<br>";

echo substr("Hello world",-10,-2)."<br>";

echo substr("Hello world",0,-6)."<br>";

echo substr("Hello world",-2-3)."<br>";

?>
```

![截图.png](    Php语言/media/image27.png){width="4.916666666666667in"
height="2.6041666666666665in"}

[**strrpos()**]{.mark}

[函数查找字符串在另一字符串中最后一次出现的位置（区分大小写）]{.mark}

![截图.png](    Php语言/media/image28.png){width="5.760416666666667in"
height="1.1846281714785651in"}

[将两个组合在一起就是strrchr函数一样的作用（文件上传第11题就是用这个方法代替想借此误导我们分析）]{.mark}

```php
<?php

$s="phpinfo.php";

var_dump(strrpos($s,"."));

var_dump(substr($s,strrpos($s,".")));

var_dump(strrchr($s,"."));

?>
```

![截图.png](    Php语言/media/image29.png){width="4.694444444444445in"
height="1.7317279090113735in"}

[in_array函数]{.mark}

**[in_array() 函数搜索数组中是否存在指定的值。]{.mark}**

[in_array(mixed \$needle, array \$haystack, bool \$strict = false):
bool]{.mark}

其中第一个参数\$needle为待搜索的值，\$haystack为被搜索的数组，第三个参数决定是否进行类型比较。

第三个类型默认为false，即不考虑类型是否相同。

```php
<?php

$sites = array("Google", "Runoob", "Taobao", "Facebook");#创建$sites数值 

if (in_array("Runoob", $sites))#判断$sites数值中是否有Runoob

{

    echo "找到匹配项！";

}

else

{

    echo "没有找到匹配项！";

}

?>

利用这些写的加固代码
```
```php
//2022.9.14

<?php

function uploader(){

    $suffis = array('.jpg','.gif','.png'); //定义白名单后缀的数组

    $file_name = trim($_FILES['up']['name']); //文件名字去空

    $file_suffis = strrchr($file_name,'.'); //查找点出现最后出现的位置.也就是后缀名赋值

    $file_suffis = strtolower($file_suffis);//防止大写绕过，后缀名全部转为小写

    $file_suffis = str_ireplace('::$DATA','',$file_suffis); //将::$DATA转换为空，防止::$DATA,因为这个还是替换是不管大小写所以小写也可以使用

    $file_suffis = trim($file_suffis);//再去空

    if(in_array($file_suffis,$suffis)) //判断白名单

    {

        $to ='upload/' .rand(1000,9999).$file_suffis; //自定义文件名字,及时你成功绕过，但是文件名后缀是我的白名单赋值的名字是时间戳。

        if(move_uploaded_file($_FILES['up']['tmp_name'],$to))

        {

            return $to;

        }

    }

    return $_FILES['up']['name'];

}

var_dump(uploader());
```

其实7,8,9行都没必要因为只要后缀是.jpg,.png,.gif，就保存，并且保存时会重新添加这三个白名单的后缀。

**最简最强白名单**

```php
<?php

function uploader(){

    $suffis = array('.jpg','.gif','.png');

    $file_name = trim($_FILES['up']['name']);

    $file_suffis = strrchr($file_name,'.');

    var_dump($file_suffis);

    if(in_array($file_suffis,$suffis))

    {

        $to ='upload/'.time().rand(100,999).$file_suffis;

        if(move_uploaded_file($_FILES['up']['tmp_name'],$to))

        {

            return $to;

        }

    }

    return $_FILES['up']['name'];

}

var_dump(uploader());
```

**2.trim函数仅仅是去掉空格，不能去掉空白字符。因此本关可以通过在sh.php文件名末尾加十六进制81\~99（比如下图中加的是0x88）来绕过后缀黑名单限制
对这个码也是无解**

**\<?php include(\'文件名\');?\>包含查看文件内容**

**弱类型绕过**

![截图.png](    Php语言/media/image30.png){width="5.760416666666667in"
height="2.8830522747156606in"}
