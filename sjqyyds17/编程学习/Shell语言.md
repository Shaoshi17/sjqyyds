---
created: 2023-11-21T17:24
updated: 2024-03-10T11:58
---
##### sed
它是文本处理中非常中的工具，能够完美的配合正则表达式使用，功能不同凡响.
==处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”（pattern space），接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。==

###### nl ./\* \>\>a 将/的文件目录的名字和文件内容

###### tr命令

使用语法：

```shell
tr [--c/d/s/t] [SET1] [SET2]

-------------------------------------------------

SET1/SET2: 字符集

-c: complement，用SET2替换SET1中没有包含的字符

-d: delete，删除SET1中所有的字符，不转换

-s: squeeze-repeats，压缩SET1中重复的字符，即删除重复的字符

-t: truncate-set1，将SET1用SET2替换，一般缺省为-t

-c：complement，用SET2替换SET1中没有包含的字符

将字符串的小写字母全部转换成大写字母，此时，可使用如下命令：

cat "ssss" \|tr a-z A-Z

还可以进行凯撒加解密

tr解码rot13

echo -n "rot13加密的字符串"\|tr 'A-Za-z' 'N-ZA-Mn-za-m'
//这里n正好是26字母的第14位

```
###### 十进制转十六进制

检查文件重复的并且删除

sort pass.txt \|uniq \> pass1.txt

-u, --unique 配合-c，严格校验排序；不配合-c，则只输出一次排序结果

###### 文件内容替换

sed -i 's#0# #' c //把所有0转换为空格

![]( Shell语言/media/image1.png)


###### 执行命令默认yes的办法

echo yes \| 命令

![]( Shell语言/media/image2.png)


![]( Shell语言/media/image3.png)


###### 可以使用{}代替do done

![]( Shell语言/media/image4.png)


zsh不适用

###### 获取用户输入

![]( Shell语言/media/image5.png)


###### \$便捷传参

![]( Shell语言/media/image6.png)


![]( Shell语言/media/image7.png)


循环用" \` "符合可以写入命令执行代替 \${} ，当然可以可以使用
\$(要使用的命令)

![]( Shell语言/media/image8.png)


###### 4. seq 的使用总结

　　用来获取增量的区间范围，默认从1开始，且以空格分隔

```
 　   seq 尾数

　　seq  首数 尾数

　　seq  首数  增量    尾数

　　seq -s  分隔符  首数   增量      尾数
```

 　　

![]( Shell语言/media/image9.png)


###### ascii转换

![]( Shell语言/media/image10.png)


###### shell字符串逆转

![]( Shell语言/media/image11.png)


![]( Shell语言/media/image12.png)


###### 以统计sh出现的次数

![]( Shell语言/media/image13.png)


[将已执行程序暂停/运行在后台]{.mark}

[ctrl+z快捷键可直接将当前程序暂停在后台。]{.mark}

vi t.txt

[ctrl+z后将vi暂停在后台，终端输入fg命令可直接重新调起。]{.mark}

[打印日期]{.mark}

date '+%Y%m%d%H%M%S'

![]( Shell语言/media/image14.png)


###### 13 、MD5加密

echo -n "sr" \| md5sum

不加-n的话， 会带\\n

tr -d '[:/]' \< passwd  //删除文件中 :和/ 符号

![]( Shell语言/media/image15.png)


tr '[0-9]' '#' \< passwd   //替换文件中0-9数字为#

![]( Shell语言/media/image16.png)


###### 去除字符串中的所有空格

echo \$string\|tr -d " "

![]( Shell语言/media/image17.png)


###### 大小写转换

tr  'a-z'  'A-Z'  转换大小写

![]( Shell语言/media/image18.png)


![]( Shell语言/media/image19.png)


###### shell多线程

![]( Shell语言/media/image20.png)

##### shell重定向
###### 文件描述符
当执行shell命令时，会默认打开3个文件，每个文件有对应的文件描述符来方便我们使用：

|类型|文件描述符|默认情况|对应文件句柄位置|
|---|---|---|---|
|标准输入（standard input）|0|从键盘获得输入|/proc/self/fd/0|
|标准输出（standard output）|1|输出到屏幕（即控制台）|/proc/self/fd/1|
|错误输出（error output）|2|输出到屏幕（即控制台）|/proc/self/fd/2|

输出重定向
输出重定向的使用方式很简单，基本的一些命令如下：

|命令|介绍|
|---|---|
|command >filename|把标准输出重定向到新文件中|
|command 1>filename|同上|
|command >>filename|把标准输出追加到文件中|
|command 1>>filename|同上|
|command 2>filename|把标准错误重定向到新文件中|
|command 2>>filename|把标准错误追加到新文件中|
![[Pasted image 20240121120311.png]]
把错误信息保存到b.txt

输入重定向
在理解了输出重定向之后，理解输入重定向就会容易得多。对输入重定向的基本命令如下：

|命令|介绍|
|---|---|
|command <filename|以filename文件作为标准输入|
|command 0<filename|同上|
|command <<delimiter|从标准输入中读入，直到遇到delimiter分隔符|

###### `>/dev/null 2>&1`这样的语句 
这条命令其实分为两命令，一个是`>/dev/null`，另一个是`2>&1`
1. >/dev/null
这条命令的作用是将标准输出1重定向到`/dev/null`中。 `/dev/null`代表linux的空设备文件，所有往这个文件里面写入的内容都会丢失，俗称“黑洞”。==那么执行了`>/dev/null`之后，标准输出就会不再存在，没有任何地方能够找到输出的内容。==
 2. 2>&1
这条命令用到了重定向绑定，采用&可以将两个输出绑定在一起。这条命令的作用是错误输出将和标准输出同用一个文件描述符，==说人话就是错误输出将会和标准输出输出到同一个地方。==

linux在执行shell命令之前，就会确定好所有的输入输出位置，并且从左到右依次执行重定向的命令，所以`>/dev/null 2>&1`的作用就是让标准输出重定向到`/dev/null`中（丢弃标准输出），然后错误输出由于重用了标准输出的描述符，所以错误输出也被定向到了`/dev/null`中，错误输出同样也被丢弃了。执行了这条命令之后，==该条shell命令将不会输出任何信息到控制台，也不会有任何信息输出到文件中。==

|命令|标准输出|错误输出|
|---|---|---|
|>/dev/null 2>&1|丢弃|丢弃|
|2>&1 >/dev/null|丢弃|屏幕|
##### 小知识
```
>创建很短的文件名
ls-t 按时间列出文件名按行存储
\连接换行命令
dir 类似cat把所有内容输出在一行
$(dir *) 把文件名当作命令执行,如果第一个文件是命令就执行命令，后续文件名作为参数传入
```
 相关命令:
- [ ] sleep:
休息指令
```
sleep 5:   5秒后返回结果
```
- [ ] awk NR:
逐行获取数据
```
cat /etc/passwd|awk NR ==1  只查看/etc/passwd的第一行内容
```
- [ ] cut -c:
命令逐列获取单个字符
```
cat /etc/passwd|awk NR ==1 |cut -c 1 只查看/etc/passwd的第一行第一个的字符
```
- [ ] if语句 
判断命令是否执行
```
[]:包含条件体语句
then：成功就执行后面的内容
fi:结束
if[$(cat flag|awk NR==2|cut -c 1)==a];then echo "yes";fi 判断flag文件的第一行第一列的单词是不是a
```