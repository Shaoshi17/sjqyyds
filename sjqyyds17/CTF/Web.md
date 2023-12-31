### SQL注入漏洞：[[SQL]]
SQL注入往往需要选手具有发现手工注入与绕过各种Web应用防护系统（WAF）的能力
#### 关键字绕过：
在注入过程中，往往有些关键字被禁用，如“select”，“union”，“and","or","="还有空格等。可以采取以下手段：
##### 编码绕过：
原理：==每次输入URL浏览器都自动进行一次URL解码，这样就绕过了。==
==select URL编码==：%73%65%6c%65%63%74
```
sqlmap脚本：charencode.py
```
![[Pasted image 20231211091334.png]]
原理：双重编码就是在每个前面加一个%25，而%25url解码就是%。
==select 双重编码==：%25%73%25%65%25%6c%25%65%25%63%25%74
原理：把代码的ascii码用CHAR()转换成字符绕过。
```
sqlmap脚本：chardoubleencode.py
```
==ANSCII HEX编码==：admin=CHAR(97)+CHAR(100)+CHAR(109)....
原理：对大小写不敏感
```
sqlmap脚本：versionedkeywords.py
```
==字母大小写绕过==：SElect,UNioN,And,or
原理：干扰编码和转义的判断。
```
sqlmap脚本:randomcase.py
```
==在关键字中添加无效字符==：SEL%00ECT,Sel%0bECT ,%00-%0b及其他的空字符
```
sqlmap脚本：space2randomblank.py
```
原理：
```
在mysql的语法中，有三种注释方法：`--空格、--+和#（单行注释）和 /* */（多行注释）`如果在`/*`后加惊叹号 ! 意为`/* */`里的语句将被执行。(*!内容*/这种方法只适用于mysql数据库）
```
![[Pasted image 20231211095407.png]]
==内联注释绕过==:
```
/* !UNion */,/*!Select*/

sqlmap脚本：versionedkeywords.py
```
==利用被删除的关键字绕过==：假如删除了SELECT，我们就构建SEL+SELECT+ECT就可以构建一个SELECT关键字。俗称==双写绕过==
```
sqlmap脚本：nonrecursivereplacement,没用的话就用level 5 risk 3
```
==等价函数与命令绕过==：
```
 ;  //分号
  |  //只执行后面那条命令
  ||  //只执行前面那条命令
  &  //两条命令都会执行
  &&  //两条命令都会执行
  %0a      //换行符
  %0d     //回车符号
  ...
```
```
sqlmap脚本：
```
==宽字节注入==：当数据库编码为GBK,PHP开启了GPC等，==并且在单引号前面添加一个反斜杠=="\\"，输入”%df%27“，程序会在%27前面添加"\"，构成“%df%5c%27”。
在GBK编码中，"%df%5c"是一个宽字节，而后面的%27不会被处理相当于插入了单引号，形成注入。
```
sqlmap脚本：chardoubleencode.py
```


##### 题目1：简单编码绕过
面对==两次urldecode()函数==，就可以使用双重url编码绕过。
知识点：
```
urldecode()函数：url解码
htmlspecialchars()函数：字符转html
addslashes()函数：字符转添加反斜杠的字符
```
sqlmap:chardoubleencode.py
##### 题目2：截断绕过
原理：URL中的"%00"在ASCII中表示0，而ASCII码中的0表示字符串的结束。所以url中出现%00，服务器就认为结束，就不会检测后面内容，就引发绕过验证。
在关键字添加%00，即可绕过某些WAF检测。
sqlmap:apostrophennullencode.py
##### 题目3： 二次注入
原理：二次注入指在数据库内的数据再次被调用时导致的注入攻击。
如：先向服务器写入数据，然后读取出来，在写入的时候动手脚，到达绕过效果。
[【技术分享】如何借助Burp和SQLMap Tamper利用二次注入-安全客 - 安全资讯平台 (anquanke.com)](https://www.anquanke.com/post/id/86551)

容易的可以直接使用admin '#然后直接访问得到admin的密码
这个难的就比较难要自己学python写tamper脚本跑sqlmap
### 命令执行漏洞：[[命令执行绕过]]
命令执行漏洞就是通过浏览器发送==bash/shell命令==到服务器程序，攻击者一般使用“&”,"|",";"等符号来绕过原有的命令，在执行完命令后，紧接着拼接命令，对系统造成伤害。
无论是在CTF比赛中还是真实网络环境，在ping，和文件长短判断，图片编辑处理等操作都会存在命令执行漏洞。

##### 题目1：上传图片
一些应用在接收到图片时候，会取图片的名字来拼接形成一条命令，以执行的方式重命名或者移动，但是如果没有严格的检查，可以被使用命令执行漏洞攻击。
##### 题目2：ping命令工具
典型的送分题，如果网站对输入内容验证的不严格就会出现命令执行。

### 文件上传漏洞[[文件上传漏洞]]
正常情况下，服务器会对上传文件的格式或内容进行校验，不可能直接运行上传文件，攻击者需要对不同的防御方式进行绕过，才能上传文件 。
常见绕过方法：
1. 客户端：抓包改包
2. 服务端：文件类型，文件名，文件后缀
3. 配合文件包含漏洞解析
4. 配合服务器漏洞解析
5. CMS,编译器漏洞绕过
6. 配合操作系统文件命名规则绕过
7. 配合其他规则绕过
8. WAF桡过
##### 题目1 MIME
在解题的时候要知道题目是在哪里建立了验证，前端，后端，前端只有一种方法就是javascript验证，后端方法比较多：MIME验证，文件目录验证，文件扩展名验证，文件内容验证。
MIME:就是修改bp抓包的Content-Type:image/jpeg文件格式。
##### 题目2：PHP标签
既然是文件上传就要先上传一个照片试试，上传功能是否正常。然后在慢慢测试，
然后直接上传非法文件php,如果不行，

上传照片改后缀，==看看有没有对php后缀进行验证==

对于==文件内容的检测判断==就将文件内容全部删除，如果是白名单就会上传失败，如果是黑名单就上传成功





























### 信息泄露漏洞[[信息泄露漏洞]]
信息泄露漏洞通常有以下情况：
- [ ] 开发工作完成没删除的编译器缓存文件
- [ ] 备份的.1，.bak等文件
- [ ] 开发工作未删除的phpinof,探针,robots等文件
- [ ] 安装文件
- [ ] SVN信息
- [ ] GItHub源码中的默认账号密码
- [ ] 服务器配置不当的目录遍历
- [ ] 默认名称的可下载数据库等文件
- [ ] 可猜测目录地址
攻击者可以从中获得关键信息数据库密码，网页源代码，网站框架等各种攻击行为。
 


### 代码审计[[代码审计]]
代码审计就是源代码中的缺点和错误，分析可能发生的安全漏洞。需要选手有一定的代码读写能力，读懂代码做什么。


##### 散列值： 
md5,sha1函数缺陷（hash缺陷绕过）
弱比较和强比较的区别：== 比较值，=== 比较值和类型
如果是== 弱比较在MD5中如果是"== ",==可以构造出MD5值为0e开头的字符串，这样的话弱类型比较时就会认为是科学技术法==，因此可以绕过
![[Pasted image 20231219105649.png]]
```php
<?php
	if(MD5('QNKCDZO')==Md5('240610708'))
		echo 'yes';
	else 
		echo 'no';
	echo "\n";
	if(MD5('QNKCDZO')===Md5('240610708'))
		echo 'yes';
	else 
		echo 'no';
?>

```
如果是"=== ",PHP自身的特性使得可以提交一个数组，而md5函数传入数组的返回值都是NULL，这样就可以绕过强类型比较，这样可以进行数组绕过。 //name[]=1&password[]=2

##### 对象注入：
反序列化漏洞



##### JavaScript代码审计：
从js代码中获取flag
![[Pasted image 20231220151337.png]]
将alert()函数放到控制台中弹出flag![[Pasted image 20231220151410.png]]
### 暴力破解[[暴力破解]]



### 反序列化[[反序列化]]

###### 题目：messagecenter
发现cookie是一个序列化的数据，尝试反序列化绕过，php特性比较方式，’== ‘和’=== ‘如果是== 那么可以用True绕过密码之类的。




### 综合渗透[[sjqyyds17/高职/vulnhub靶机综合渗透]]

综合渗透是一种接近实战的题目，包括多种漏洞组合，重点考察选手实战能力

### 其他Web类赛题
###### 文件包含（FIL）[[文件包含和Php伪协议]]









