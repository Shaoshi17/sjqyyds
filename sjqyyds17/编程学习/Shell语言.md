###### **nl ./\* \>\>a 将/的文件目录的名字和文件内容**

###### tr命令

使用语法：

```shell
tr \[--c/d/s/t\] \[SET1\] \[SET2\]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SET1/SET2: 字符集

-c: complement，用SET2替换SET1中没有包含的字符

-d: delete，删除SET1中所有的字符，不转换

-s: squeeze-repeats，压缩SET1中重复的字符，即删除重复的字符

-t: truncate-set1，将SET1用SET2替换，一般缺省为-t

-c：complement，用SET2替换SET1中没有包含的字符

将字符串的小写字母全部转换成大写字母，此时，可使用如下命令：

cat \"ssss\" \|tr a-z A-Z

还可以进行凯撒加解密

tr解码rot13

echo -n \"rot13加密的字符串\"\|tr \'A-Za-z\' \'N-ZA-Mn-za-m\'
//这里n正好是26字母的第14位

```
###### **十进制转十六进制**

检查文件重复的并且删除

sort pass.txt \|uniq \> pass1.txt

-u, \--unique 配合-c，严格校验排序；不配合-c，则只输出一次排序结果

###### **文件内容替换**

sed -i \'s#0# #\' c //把所有0转换为空格

![]( Shell语言/media/image1.png){width="5.152777777777778in"
height="4.109705818022747in"}

###### **执行命令默认yes的办法**

echo yes \| 命令

![]( Shell语言/media/image2.png){width="5.760416666666667in"
height="2.7081966316710413in"}

![]( Shell语言/media/image3.png){width="2.361111111111111in"
height="1.0029494750656167in"}

###### 可以使用{}代替do done

![]( Shell语言/media/image4.png){width="4.986111111111111in"
height="0.17733048993875766in"}

zsh不适用

###### 获取用户输入

![]( Shell语言/media/image5.png){width="5.760416666666667in"
height="1.1315102799650043in"}

###### \$便捷传参

![]( Shell语言/media/image6.png){width="5.611111111111111in"
height="2.581735564304462in"}

![]( Shell语言/media/image7.png){width="2.6944444444444446in"
height="0.9362937445319335in"}

循环用" \` "符合可以写入命令执行代替 \${} ，当然可以可以使用
\$(要使用的命令)

![]( Shell语言/media/image8.png){width="2.5in"
height="2.1041666666666665in"}

###### **4. seq 的使用总结**

　　用来获取增量的区间范围，默认从1开始，且以空格分隔

```
 　   seq 尾数

　　seq  首数 尾数

　　seq  首数  增量    尾数

　　seq -s  分隔符  首数   增量      尾数
```

 　　

![]( Shell语言/media/image9.png){width="4.805555555555555in"
height="3.064714566929134in"}

###### **ascii转换**

![]( Shell语言/media/image10.png){width="3.111111111111111in"
height="2.570048118985127in"}

###### shell字符串逆转

![]( Shell语言/media/image11.png){width="2.0277777777777777in"
height="0.4991447944006999in"}

![]( Shell语言/media/image12.png){width="5.760416666666667in"
height="1.4041021434820646in"}

###### **以统计sh出现的次数**

![]( Shell语言/media/image13.png){width="4.069444444444445in"
height="0.6244674103237096in"}

**[将已执行程序暂停/运行在后台]{.mark}**

[ctrl+z快捷键可直接将当前程序暂停在后台。]{.mark}

vi t.txt

[ctrl+z后将vi暂停在后台，终端输入fg命令可直接重新调起。]{.mark}

**[打印日期]{.mark}**

date \'+%Y%m%d%H%M%S\'

![]( Shell语言/media/image14.png){width="2.361111111111111in"
height="0.5850535870516186in"}

###### **13 、MD5加密**

echo -n \"sr\" \| md5sum

不加-n的话， 会带\\n

tr -d \'\[:/\]\' \< passwd  //删除文件中 :和/ 符号

![]( Shell语言/media/image15.png){width="5.760416666666667in"
height="3.813069772528434in"}

tr \'\[0-9\]\' \'#\' \< passwd   //替换文件中0-9数字为#

![]( Shell语言/media/image16.png){width="5.760416666666667in"
height="2.810870516185477in"}

###### **去除字符串中的所有空格**

echo \$string\|tr -d \" \"

![]( Shell语言/media/image17.png){width="3.763888888888889in"
height="1.1468919510061242in"}

###### **大小写转换**

tr  'a-z'  'A-Z'  转换大小写

![]( Shell语言/media/image18.png){width="3.736111111111111in"
height="1.1655839895013123in"}

![]( Shell语言/media/image19.png){width="5.760416666666667in"
height="4.674084645669291in"}

###### **shell多线程**

![]( Shell语言/media/image20.png){width="5.760416666666667in"
height="4.294442257217848in"}
###### `>/dev/null 2>&1`这样的语句
