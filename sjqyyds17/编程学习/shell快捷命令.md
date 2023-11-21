#### tr命令

使用语法：

```shell
 tr [–c/d/s/t] [SET1] [SET2]

-------------------------------------------------

SET1/SET2: 字符集

-c: complement，用SET2替换SET1中没有包含的字符

-d: delete，删除SET1中所有的字符，不转换

-s: squeeze-repeats，压缩SET1中重复的字符，即删除重复的字符

-t: truncate-set1，将SET1用SET2替换，一般缺省为-t

-c：complement，用SET2替换SET1中没有包含的字符

```
```
将字符串的小写字母全部转换成大写字母，此时，可使用如下命令：

cat "ssss" |tr a-z A-Z

还可以进行凯撒加解密
```

##### tr解码rot13

echo -n "rot13加密的字符串"|tr 'A-Za-z' 'N-ZA-Mn-za-m' //这里n正好是26字母的第14位

#### **十进制转十六进制**

检查文件重复的并且删除

```
sort pass.txt |uniq > pass1.txt

-u, --unique 配合-c，严格校验排序；不配合-c，则只输出一次排序结果
```

#### **文件内容替换**

sed -i 's#0# #' c     //把所有0转换为空格

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps806.jpg) 

#### **执行命令默认yes的办法**

echo yes | 命令

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps807.jpg) 

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps808.jpg) 

可以使用{}代替do done

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps809.jpg) 

zsh不适用

获取用户输入

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps810.jpg) 

$便捷传参

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps811.jpg) 

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps812.jpg) 

循环用” ` “符合可以写入命令执行代替 ${} ，当然可以可以使用 $(要使用的命令)

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps813.jpg) 

#### **4. seq 的使用总结**

　　用来获取增量的区间范围，默认从1开始，且以空格分隔

```
 　 seq 尾数

　　seq  首数 尾数

　　seq  首数  增量    尾数

　　seq -s  分隔符  首数   增量      尾数
```

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps814.jpg) 

#### **ascii转换**

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps815.jpg) 

##### shell字符串逆转

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps816.jpg) 

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps817.jpg) 

#### **以统计sh出现的次数**

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps818.jpg) 

#### **将已执行程序暂停/运行在后台**

ctrl+z快捷键可直接将当前程序暂停在后台。

vi t.txt

ctrl+z后将vi暂停在后台，终端输入fg命令可直接重新调起。

#### **打印日期**

date '+%Y%m%d%H%M%S'

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps819.jpg)
#### **13 、MD5加密**

echo -n "sr" | md5sum

不加-n的话， 会带\n

tr -d '[:/]' < passwd  //删除文件中 :和/ 符号

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps820.jpg) 

tr '[0-9]' '#' < passwd   //替换文件中0-9数字为#

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps821.jpg) 

#### **去除字符串中的所有空格**

echo $string|tr -d " "

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps822.jpg) 

#### **大小写转换**

tr  ‘a-z’  ‘A-Z’  转换大小写

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps823.jpg) 

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps824.jpg) 

#### **shell多线程**

![](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml8108\wps825.jpg)