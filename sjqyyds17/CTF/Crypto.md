![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image1.png){width="5.760416666666667in"
height="2.6918996062992124in"}

**编码种类：**

**普莱费尔密码**

解密网站：http://www.hiencode.com/playfair.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image2.png){width="5.760416666666667in"
height="2.7543252405949255in"}

**埃特巴什码Atbash Cipher**

**简单替换密码**

原理

简单替换密码（Simple Substitution
Cipher）加密时，将每个明文字母替换为与之唯一对应且不同的字母。它与恺撒密码之间的区别是其密码字母表的字母不是简单的移位，而是完全是混乱的，这也使得其破解难度要高于凯撒密码。
比如：

明文字母 : abcdefghijklmnopqrstuvwxyz

密钥字母 : phqgiumeaylnofdxjkrcvstzwb

a 对应 p，d 对应 h，以此类推。

**曲路密码**

原理

曲路密码（Curve
Cipher）是一种换位密码，需要事先双方约定密钥（也就是曲路路径）。下面给出一个例子：

明文：The quick brown fox jumps over the lazy dog

填入 5 行 7 列表（事先约定填充的行列数）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image3.png){width="5.736111111111111in"
height="1.1680807086614173in"}

加密的回路线（事先约定填充的行列数）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image4.png){width="5.736111111111111in"
height="1.1680807086614173in"}

密文：gesfc inpho dtmwu qoury zejre hbxva lookT

**Polybius密码**

Polybius(波利比奥斯密码)棋盘密码

原理：把字母在密码表里面用两个数字定位后代替，解码查个表就可以了，这个加密的密码表比较混乱。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image5.png){width="5.760416666666667in"
height="2.523509405074366in"}

**ADFGX密码**

棋盘密码的升级版

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image6.png){width="5.760416666666667in"
height="2.3228379265091865in"}

**ADFGVX密码**

ADFGX的升级版，加了数字进去

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image7.png){width="5.760416666666667in"
height="4.550903324584427in"}

**列置换加密（列位移密码）**

原理：把明文按顺序从左到右，从上到下写再矩阵中如果在矩阵中明文不足以填满就用@填，然后按预定的顺序读取得到密文。

密钥通常就是用一个单词代替

nice 相当于 4312
为什么是4312呢？因为c在这个四个字母内按照字母表排序是最前面就是1，其他的以此类推就可以得到4321.

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image8.png){width="5.760416666666667in"
height="2.7730807086614173in"}

解密：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image9.png){width="5.760416666666667in"
height="2.487055993000875in"}

这个比较混乱的是有些人喜欢用行读取，有的喜欢列读取。

下面这个是不一样的一种

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image10.png){width="5.760416666666667in"
height="3.747066929133858in"}

python库

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image11.png){width="5.760416666666667in"
height="1.419902668416448in"}

**杰斐逊转轮加密**

原理：把要加密的密文注意不能超过36个字，把明文在转轮上排列出来，密文就是其他25行的任意取一行，解密就把密文按照秘钥的顺序转好后看上面有意义的行就是明文。

典型的多表替换加密方式

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image12.png){width="5.760416666666667in"
height="2.774717847769029in"}

**费纳姆密码**

历史：德军二中使用的加密方式

原理:就是用一段二进制的秘钥对明文的二进制进行异或

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image13.png){width="5.760416666666667in"
height="2.519776902887139in"}

特点是密文和秘钥是一样长，注意解密的时候要七位一组

**仿射密码**

这里要注意这个地方，A是0，不是1，下面是范围表

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image14.png){width="5.760416666666667in"
height="0.680320428696413in"}

mod
26的原因是26个字母，就和凯撒密码差不多，凯撒是加，仿射是乘完后再加，位移密码和乘数密码的结合。

加密公式：E(x)=(ax+b) mod 26

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image15.png){width="3.375in"
height="2.4791666666666665in"}

解密公式：D(x)=a\^-1(x-b) mod 26

模运算不能用除法运算，要转换成乘法逆元运算

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image16.png){width="5.760416666666667in"
height="3.16337489063867in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image17.png){width="5.760416666666667in"
height="3.2177887139107613in"}

解码方式：CTF在线工具-在线仿射密码加密\|在线仿射密码解密\|仿射密码算法\|Affine
Cipher (hiencode.com)或解密脚本

mi=\'dikxourxd\'

m =1

while True:

    if 11\*m%26==1:

        print(m)

        break

    m =m+1

for i in mi:

    print(chr(97+(ord(i)-97-7)\*m%26),end=\'\')
#-97是为了转换成ascii形式进行计算，加回去就是为了转回去、

\'\'\'\'\'\'

output

ctfsdnisc

\'\'\'\'\'\'\'

**关键密码解密：**

CTF在线工具-在线关键字加密\|在线关键字解密\|关键字密码算法\|Keyword
Cipher (hiencode.com)

**维基尼亚密码：[Vigenere]{.mark}**

又称维热纳尔加密算法

例如：

明文是shan

密钥是x

那么对应这个图就是：PEXK

如果是这种密钥是字符串就要一个一个填充完之后对应找密文

明文：come greatwall

密钥：crypto

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image18.png){width="5.760416666666667in"
height="1.0018121172353456in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image19.png){width="4.972222222222222in"
height="4.096610892388451in"}

从而得到密文

明文：come greatwall

密钥：crypto

密文：efkt zferrltzn

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image20.png){width="5.760416666666667in"
height="4.264924540682415in"}

解码方式：维吉尼亚密码在线加密解密 - 千千秀字 (qqxiuzi.cn)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image21.png){width="5.760416666666667in"
height="2.1976815398075242in"}

**云隐密码（01248密码）**

此密码运用了1248代码,因为本人才疏学法,问未发现有过使用的先例,因此暂归为原创密码。由于这个密码,我和片风云影初识,为了纪念,将其命名为"云影密码"。

有了1,2,4,8这四个苘单的数字,你可以以加法表示出0\~9任何个数字,例如0=28,7=124,9=18这样,再用1-26来表示A-Z,就可以用作密码了。为了不至于混乱,我个人引入了第五个数字0,来用作间隔,以遍免翻译错误,所以还可以称"01248密码"

注意(3个及以上数字时)：

虽然是相加，但是可以在数字内不按顺序相加，如124可写成(12)4和1(24)结果分别是7和16，只要保证不大于26即可

题目(总不超过26)：

12401011801180212011401804

第一步分割：

即124 、1、118、118、212、114、18、4

第二步基本翻译：

例如124可以表示7,也可以表示16(但不可能是34,因为不会超过26),所以可以放弃来翻译其他没有异议的,可得:124、a、s、s、w、o、18、d

第三步推测得出明文：

可以推测后面的18表示r,前面的为p最合适。

所以最后明文:

password(密码)

**培根密码：**

大小写的ABab，而且必须是5个一组

第一种方式：

A aaaaa B aaaab C aaaba D aaabb E aabaa F aabab G aabba H aabbb I abaaa
J abaab

K ababa L ababb M abbaa N abbab O abbba P abbbb Q baaaa R baaab S baaba
T baabb

U babaa V babab W babba X babbb Y bbaaa Z bbaab

第二种方式:

a AAAAA g AABBA n ABBAA t BAABA

b AAAAB h AABBB o ABBAB u-v BAABB

c AAABA i-j ABAAA p ABBBA w BABAA

d AAABB k ABAAB q ABBBB x BABAB

e AABAA l ABABA r BAAAA y BABBA

f AABAB m ABABB s BAAAB z BABBB

**键盘密码：**

例如：

[r5yG lp9I BjM tFhB T6uh y7iJ QsZ bhM]{.mark}

[原理就是这些字符在键盘的位置然后围成个圈，圈中的就是加密的明文]{.mark}

[或者是这些字符形成的图像类似什么字母就是什么字母]{.mark}

**词频分析：**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image22.png){width="5.208333333333333in"
height="1.0729166666666667in"}

解决方式：quipqiup - cryptoquip and cryptogram solver然后再找关键字

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image23.png){width="5.611111111111111in"
height="2.8708016185476817in"}

**Rabbit加密**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image24.png){width="5.760416666666667in"
height="2.418124453193351in"}

特征没什么，主要看提示吧，算是个骚加密，一般提示兔子就是这个加密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image25.png){width="5.760416666666667in"
height="0.662405949256343in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image26.png){width="5.760416666666667in"
height="2.791129702537183in"}

**关键词加密：**

原理

随机选择一个词组或短语作为密钥，如果该关键词中有重复字母，则去掉除第一次出现外的所有重复字母。例如选取关键词"nextlegend"，则处理后为"nextlgd"。将处理后的关键词依次排列在字母表的下方，并将除去这些关键词后字母表中剩余的字母依次填入剩余空间。如下图:

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image27.png){width="5.760416666666667in"
height="0.4298818897637795in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image28.png){width="4.402777777777778in"
height="0.9285476815398075in"}

解密网站：http://www.hiencode.com/keyword.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image29.png){width="5.760416666666667in"
height="3.0432392825896764in"}

**猪圈编码：**

原理：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image30.png){width="2.4027777777777777in"
height="2.4027777777777777in"}

我们举一个例子，如明文为 X marks the spot ，那么密文如下

![stickPicture.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image31.png){width="4.486111111111111in"
height="0.4892049431321085in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image32.png){width="3.1527777777777777in"
height="0.6368197725284339in"}

解密方式：http://mmoersima.00cha.net/zhuquan.asp

**手机键盘密码**

手机键盘加密方式，是每个数字键上有 3-4
个字母，用两位数字来表示字母，例如：ru
用手机键盘表示就是：7382，那么这里就可以知道了，手机键盘加密方式不可能用
1 开头，第二位数字不可能超过 4，解密的时候参考此

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image33.png){width="5.166666666666667in"
height="2.34375in"}

关于手机键盘加密还有另一种方式，就是「音的」式（这一点可能根据手机的不同会有所不同），具体参照手机键盘来打，例如：「数字」表示出来就是：748
94。在手机键盘上面按下这几个数，就会出：「数字」的拼音。

956049

**摩斯编码：**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image34.png){width="5.760416666666667in"
height="0.3696522309711286in"}

解密方式：http://www.jsons.cn/morse/

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image35.png){width="5.760416666666667in"
height="1.7067902449693788in"}

**[Morse编码]{.mark}**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image36.png){width="4.694444444444445in"
height="6.050617891513561in"}

特点 ¶

0.  只有 

    最多 6 位；

    也可以使用 

**[福尔摩斯小人密码]{.mark}**

解密图纸：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image37.png){width="4.597222222222222in"
height="9.246567147856519in"}

**[brainfuck加密]{.mark}**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image38.png){width="5.486111111111111in"
height="1.6166294838145232in"}

解密方式：https://www.splitbrain.org/services/ook

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image39.png){width="5.180555555555555in"
height="2.3036275153105863in"}

**Ook!加密**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image40.png){width="4.0in"
height="1.5in"}

解密方式：https://www.splitbrain.org/services/ook

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image39.png){width="5.180555555555555in"
height="2.3036275153105863in"}

**short Ook!加密**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image41.png){width="5.486111111111111in"
height="5.7984142607174105in"}

解密方式：https://www.splitbrain.org/services/ook

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image42.png){width="4.027777777777778in"
height="1.5715616797900263in"}

**Bubble密码加密/解密**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image43.png){width="5.760416666666667in"
height="0.5021412948381452in"}

解密方式：http://www.hiencode.com/bubble.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image44.png){width="5.760416666666667in"
height="5.251055336832896in"}

**Unicode编码**

**特点 **¶

0.  大量的\\u

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image45.png){width="5.760416666666667in"
height="0.20194225721784778in"}

解码方式：http://www.jsons.cn/unicode/

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image46.png){width="5.760416666666667in"
height="1.8083847331583551in"}

python

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image47.png){width="3.0972222222222223in"
height="0.7091283902012249in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image48.png){width="3.9027777777777777in"
height="0.5530675853018373in"}

**Rabbit加密：**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image49.png){width="5.611111111111111in"
height="0.9681430446194226in"}

解码网站：在线Rabbit加密 \| Rabbit解密- 在线工具 (sojson.com)

**jother编码**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image50.png){width="5.![[Pasted image 20231121182939.png]]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image51.png){width="5.760416666666667in"
height="1.9092082239720034in"}

解密方法：浏览器F12找到console复制回车就flag出来了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image52.png){width="5.760416666666667in"
height="7.483351924759405in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image53.png){width="5.388888888888889in"
height="5.336772747156606in"}

\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]\]()+\[\])\[!+\[\]+!+\[\]\]+(\[\]\[(\![\]+\[\])\[+\[\]\]+(\[\![\]\]+\[\]\[\[\]\])\[+!+\[\]+\[+\[\]\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]\]\]+\[\])\[(\![\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]\]+(\[\![\]\]+\[\]\[\[\]\])\[+!+\[\]+\[+\[\]\]\]+(\[\]\[(\![\]+\[\])\[+\[\]\]+(\[\![\]\]+\[\]\[\[\]\])\[+!+\[\]+\[+\[\]\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]\]+(\![\]+\[\])\[!+\[\]+!+\[\]\]\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]+(!\![\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]\]((+((+(+!+\[\]+\[+!+\[\]\]+(!\![\]+\[\])\[!+\[\]+!+\[\]+!+\[\]\]+\[!+\[\]+!+\[\]\]+\[+\[\]\])+\[\])\[+!+\[\]\]+\[+\[\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+\[\]\]+\[+!+\[\]\]\])+\[\])\[!+\[\]+!+\[\]\]+\[+!+\[\]\])

丢到控制台直接run \[\]()+!等符号就足以实现几乎任意Javascript代码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image54.png){width="5.760416666666667in"
height="1.0121336395450569in"}

**社会主义核心价值观算法**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image55.png){width="5.760416666666667in"
height="0.9214227909011373in"}

解密网站:http://z.duoluosb.com/或http://www.atoolbox.net/Tool.php?Id=850

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image56.png){width="5.760416666666667in"
height="3.169161198600175in"}

**uuencode算法**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image57.png){width="3.513888888888889in"
height="1.1573939195100613in"}

解密网站：https://www.qqxiuzi.cn/bianma/uuencode.php

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image58.png){width="3.9444444444444446in"
height="3.5270428696412948in"}

**base91**

编码字符："[!#\$%&\'()\*+,-./0123456789:;\<=\>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\\\]\^\_abcdefghijklmnopqrstuvwxyz{\|}]{.mark}"

**base92**

想比base91多了个\~

编码字符："[〜!#\$%&\'()\*+,-./0123456789:;\<=\>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\\\]\^\_abcdefghijklmnopqrstuvwxyz{\|}]{.mark}"

**base64**

密文由**64**个字符(A-Z,a-z,0-9,+,/)组成

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image59.png){width="1.3194444444444444in"
height="0.12566163604549432in"}

**base62**

密文由62个字符(A-Z,a-z,0-9)组成

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image60.png){width="3.763888888888889in"
height="0.42747812773403326in"}

**base32**

密文由**32**个字符（A-Z,2-7)组成

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image61.png){width="1.3472222222222223in"
height="0.1775404636920385in"}

**base16**

密文由**16**个字符（0-9,A-F）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image62.png){width="1.6527777777777777in"
height="0.12473753280839894in"}

**base85**

特点是奇怪的字符比较多，但是很难出现等号

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image63.png){width="1.1527777777777777in"
height="0.16767716535433072in"}

**base58：**

**特征**相比Base64，Base58不使用数字\"0\"，字母大写\"O\"，字母大写\"I\"，和字母小写\"l\"，以及\"+"和"/\"符号，最主要的是后面不会出现'=\'。

**Hex编码**

1-9,a-f

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image64.png){width="3.1944444444444446in"
height="0.5514840332458443in"}

解密方式：网站https://www.sojson.com/hexadecimal.html或者用winhex，编码转ascii

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image65.png){width="5.760416666666667in"
height="1.3364555993000875in"}

**凯撒编码家族（Casear）：**

这里要注意这个地方，A是0，不是1，下面是范围表

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image66.png){width="5.760416666666667in"
height="0.680320428696413in"}

凯撒密码是位移密码

原理：加密时会将明文密码的每个字符都按照其他字母表中的顺序，移动固定数目作为密文

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image67.png){width="4.486111111111111in"
height="0.5633716097987752in"}

代码实现解密：

mi=\'dikxourxd\'

    for p in mi:

        if \"a\" \<= p \<= \"z\":

            print(chr(ord(\"a\")+(ord(p)-ord(\"a\")-13)%26), end=\'\')

        elif \"A\" \<= p \<= \"Z\":

            print(chr(ord(\"A\")+(ord(p)-ord(\"A\")-13)%26), end=\'\')

        else:

            print(p, end=\'\')

\'\'\'

qvxkbhekq

\'\'\'

和网站的一样

以下的分支的密码

**Avocat (A-K) 偏移量为10：**

**ROT13 偏移量为13：**

特点是两次加密会变成明文，所以就可以直接写一个加密脚本就可以做到加解密。

用凯撒偏移量13加密：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image68.png){width="3.2916666666666665in"
height="3.0625in"}

用ROT13解密成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image69.png){width="2.9027777777777777in"
height="5.335681321084865in"}

**Cassis (K-6) 偏移量为-5：**

**Cassette（K-7） 偏移量为-7：**

**栅栏密码：**

原理：把加密明文排列如果是3，就明文排成一个一个分别排成三列，然后分别取出里面的第一排三个拼接第二排三个前面

明文：

123456789

划分：

147

258

36

密文：

14725836

解密方式网站：https://www.qqxiuzi.cn/bianma/zhalanmima.php

加密脚本

mi=\"flag{7sp3lmtu209ev5ikjdqa}\"

lan=2 #设置栏数

for m in range(0,lan):

    for n in range(m,len(mi),lan):

        print(mi\[n\],end=\'\')

解密脚本

\# 栅栏解密

def zhalan():

    s=input(\"输入密文：\")

    l=int(input(\"输入栏数：\"))

    print(pycipher.Railfence(l).decipher(s))# 调用python自带的模块解密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image70.png){width="4.361111111111111in"
height="2.216984908136483in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image71.png){width="2.4722222222222223in"
height="3.5779418197725286in"}

**二进制转字符串**

解密网站：http://xiaoniutxt.com/binaryToString.html

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image72.png){width="5.760416666666667in"
height="2.9636001749781276in"}

**Rot47编码**

位移密码

原理就凯撒的位移密码的47次

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image73.png){width="2.9166666666666665in"
height="0.4270833333333333in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image74.png){width="5.760416666666667in"
height="3.2370483377077863in"}

**对称加密**

加解密用同一个密钥

双向的机密性保证都可以加解密

**DES加密算法**

密钥加密的块算法

将64位比特（8个字节）加密成另外8个字节的对称加密算法，64比特一组，分组后再加密

密钥长度位也是64比特位

(不安全)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image75.png){width="5.760416666666667in"
height="3.3492333770778653in"}

**3DES加密算法**

三重DES加密，由于需要加密三次所以密文长度是明文的三倍。

加密过程：加密------》解密------》加密------》密文

解密过程：解密------》加密------》解密------》明文

（安全但是效率低）

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image76.png){width="5.347222222222222in"
height="4.065139982502187in"}

**AES算法加密算法**

数据流加密（安全）

分组长度是128比特，密钥长度是128比特，192比特，256比特，与DES不一样，这是一直SPN结构算法，加密解密流程不一样

**非对称加密**

加解密用不同密钥，分公钥和私钥

单向的机密性保证，有私钥才能解密，没有就干楞着

列题：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image77.png){width="5.760416666666667in"
height="3.6069181977252844in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image78.png){width="5.760416666666667in"
height="2.6842760279965003in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image79.png){width="5.638888888888889in"
height="3.533426290463692in"}

使用python的gmpy2模块可以解密d和m

import gmpy2

e = 13

p = 7

q = 11

c = 15 \# 密文

n = p \* q

phi = (p-1)\*(q-1) \# 求φ(n)

d = gmpy2.invert(e, phi) \# 解密指数d

m = pow(c, d, n) \# m = c\^d mod n

print(m) \# 71

**简单列题：phi = pq\*qp // n (整除不会报错)**

from Crypto.Util.number import bytes_to_long,inverse,getPrime

from flag import flag

m = bytes_to_long(flag)

p = getPrime(1024)

q = getPrime(1024)

n = p\*q

print(n)

e = 65537

c = pow(m,e,n)

pq = p\*(q-1)

qp = q\*(p-1)

print(\"c=\",c)

print(\"n=\",n)

print(\"pq=\",pq)

print(\"qp=\",qp)

\'\'\'

c=
8722269075970644434253339592758512788160408912707387632591552130175707843950684315083250494010055435391879036285103810263591951437829414438640307561645721347859659807138051841516634704123100270651976676182059252251162982609391666023674158274992400910869692389001622774140191223807887675081808561012755545464977015973615407965906513878979919700065923364884766974187303774330319143647840846354404070430118235352622445115153298578370521811697710289716188726587743282814946239856766713516166990341116198180068191759095913957606379780234116317390622824096667107736103270907349927467971817639795094030622157581511033950777

n=
10466186506773626671397261081802640650185744558208505628349249045496105597268556020207175016523119333667851114848452038431498926527983706092607207796937431312520131882751891731564121558651246025754915145600686076505962750195353958781726515647847167067621799990588328894365930423844435964506372428647802381074584935050067254029262890188260006596141011807724688556673520261743199388391094490191001701011230322653422314758778116196105077883955436582364267530633358016652912054880813710531145973799193443828969535902856467548523653920307742364119002349899553478815101092655897400295925170383678499125295006364960124859003

pq=
10466186506773626671397261081802640650185744558208505628349249045496105597268556020207175016523119333667851114848452038431498926527983706092607207796937431312520131882751891731564121558651246025754915145600686076505962750195353958781726515647847167067621799990588328894365930423844435964506372428647802381074488896197029704465200125337817646702009123916866455067019234171839614862660036737875747177391796376553159880972782837853473250804807544086701088829096838316550146794766718580877976153967582795248676367265069623900208276878140709691073369415161936376086988069213820933152601453587292943483693378833664901178324

qp=
10466186506773626671397261081802640650185744558208505628349249045496105597268556020207175016523119333667851114848452038431498926527983706092607207796937431312520131882751891731564121558651246025754915145600686076505962750195353958781726515647847167067621799990588328894365930423844435964506372428647802381074475956379708898904933143429835002718457573266164923043251954374464149976302585916538814746811455883837138715445492053610047383292461097590195481556557381952895539341802954749542143253491617052100969586396996063822508764438280468492894012685918249843558593322831683872737943676955669923498182824352081785243246

\'\'\'

Crypto的python基础

模块：

import gmpy2

import libnum

phi=(p-1)\*(q-1)

d=libnum.invmod(e,phi)

s=gmpy2.invert(e,phi)

这两个方法都可以求d

libnum.n2s(m)

iroot() #开根

import Crypto.Util.number

bytes_to_long() & long_to_long #整数和对应字节的转换

getPrime() & getStrongPrime #生成素数，加Strong就是强素数

inverse() & pow() \#

from binascii import a2b_hex,b2a_hex \#
b2a_hex是字符串转十六进制,a2b_hex是十六进制转字符串

**异或**

按位异或即为对应的二进制位相异时，数值为1，相同则为0

10 = 1010

3 = 0011

10\^3 = 1001 = 9

**幂数加密**

[二进制幂数加密法，由于英文字母只有26个字母。只要2的0、1、2、3、4、5次幂就可以表示31个单元。通过用二进制幂数表示字母序号数来加密]{.mark}

**哈希函数**

**哈希函数的特征**

第一个特征是输出的哈希值数据长度不变。

第二个特征是如果输入的数据相同，那么输出的哈希值也必定相同。

第三个特征是即使输入的数据相似，但哪怕它们只有一比特的差别，那么输出的哈希值也会有很大的差异。输入相似的数据并不会导致输出的哈希值也相似。

哈希函数的算法哈希函数的算法中具有代表性的是

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image80.png){width="5.760416666666667in"
height="2.266091426071741in"}

爆破例题

**分组密码的模式**

分组密码又称快密码，是对称算法，分组密码在加密的时候，会把明文拆分成固定长度的分组（一般是8，64，128，256位），然后通过加密模式将这些分组链接起来，形成密文。如果不够它会在后面用特定的字符或者数字例如:0填充

对称算法的解密和加密的密钥是同一个

一般CTF比赛是给一个密文和密钥(key)然后让你去解出明文

还有一种是残的密文要自己使用某些方法恢复才能再去解密

**ECB分组模式（电子密码本模式）**

明文分组的时候如果最后一组没有满字节长度就要自己填充

ECM模式加密存在严重安全问题，原因是相同的数据块加密以后密文快也是一样的。

就比如这个照片最顶上这个粉色的块是数据块一样的，密文的块也加密出来的也差不多。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image81.png){width="4.819444444444445in"
height="2.0133180227471565in"}

原理图

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image82.jpeg){width="5.760416666666667in"
height="5.217834645669291in"}

**CBC分组模式（密码块链模式）**

明文分组的时候如果最后一组没有满字节长度就要自己填充

原理：每一个分组要和前一个分组进行异或操作，然后再进行加密，由于后一个分组要依赖前一个分组，所以第一个分组要定义一个长度和分组一样的初始向量IV。

这样加密就可以解决ECB的加密的安全隐患

XOR：叫做异或 符合为\^

a \^ b =c ; c \^ b =a

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image83.png){width="5.760416666666667in"
height="4.8892913385826775in"}

**CFB分组模式（密文反馈模式）**

原理：每一个分组要和前一个分组进行加密操作，然后再
进行异或，由于后一个分组要依赖前一个分组，所以第一个分组要定义一个长度和分组一样的初始向量IV，先加密后异或和CBC反着来的。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image84.png){width="5.760416666666667in"
height="2.422836832895888in"}

**OFB分组模式（输出反馈模式）**

原理图：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image85.png){width="5.760416666666667in"
height="3.3725798337707786in"}

**CTR分组模式（计算器模式）**

原理：

1.该算法会自动生成一个随机数

2.该算法内部有一个计数器,从0开始

3.会自动将随机数和计数器当前的值组成一个初始化向量

4.利用个密钥对初始化向量进行机容

5.用当前分组和加密后的初始化向量进行异或

6.随机数不变，但是计数器+1

7.会自动将随机数和计数器当前的值组成一个初始化向量

8.利用个密钥对初始化向量进行机密

9.用当前分组和加密后的初始化向量进行异或加密

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image86.png){width="5.760416666666667in"
height="4.185119203849519in"}

**明文分组填充问题：**

1，分组数据填充和加密算法没关系，和加密算法用的分组模式有关系

2，只有ECB,CBC要填充，填充多少就看加密算法的需要的多少填充

**DES算法**

分组长度为64比特位，密钥长度为64位比特位，共16轮迭代Feistel结构的密码算法。

Feistel结构：加密和解密的流程是一样的只不过是加密和解密用的密钥顺序是要翻过来。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image87.png){width="5.760416666666667in"
height="8.015164041994751in"}

加密解说：

明文： 1234 5678

L0=1234 R0=5678

密钥： keys = Kn

第一次加密：

L1=R0=5678 R1=L0\^F(R0,K0)

第二次加密：

L2=R1 R2=L1\^F(R1,K1)

第n次加密\...\.....

**Feistel结构的题**

**RC4加密算法**

加密：原文和Keystream进行异或得到密文

解密：密文和Keystream进行异或得到原文

看似只需要和keystream进行异或就可以解密或加密，但是密钥流长度和明文长度是对应的，RC4算法的主要代码就是在于如何生成秘钥

密钥流的生成由两部分组成：

0.  KSA（the Key-Scheduling Algorithm)

    PRGA(the Pseudo-Random Generation Algorithm)

[首先进行初始化,然后就是生成]{.mark}随机数

利用Key生成S盒------The key-scheduling algorithm (KSA)

/\* 得到S-box \*/

int i = 0;

for (i = 0; i \< 256; i++) {

S\[i\] = i;

T\[i\] = puc_key\[i % key_length\];

}

for (i = 0; i \< 256; i++) {

j = (j + S\[i\] + T\[i\]) % 256;

swap_uchar(&S\[i\], &S\[j\]); //交换S\[i\]和S\[j\]

}

利用S盒生成密钥流------The pseudo-random generation algorithm(PRGA)

/\* 生成密钥流 Keystream \*/

int i = 0;

int j = 0;

int t = 0;

unsigned long k = 0;

for (k = 0; k \< ul_data_length; k++) {

i = (i + 1) % 256;

j = (j + puc_sbox\[i\]) % 256;

swap_uchar(&puc_sbox\[i\], &puc_sbox\[j\]);

t = (puc_sbox\[i\] + puc_sbox\[j\]) % 256;

puc_key_stream\[k\] = puc_sbox\[t\];

}

**RSA数学基础**

**RSA原理**

RSA
是一种非对称密码算法，它使用一对密钥，即公钥和私钥。公钥用于加密，私钥用于解密。RSA
算法的安全性基于两个数论问题：大整数分解和模幂运算。

以下是 RSA 解密的基本原理：

1\. 生成密钥对：

 - 随机选择两个大素数 p 和 q。

 - 计算 RSA 模数 n = p \* q。

 - 计算欧拉函数值 φ(n) = (p - 1) \* (q - 1)。

 - 选择一个私钥指数 d，满足 1 \< d \< φ(n) 且 d 与 φ(n) 互质。

 - 计算公钥指数 e，满足 e \* d ≡ 1 (mod φ(n))。

 - 公钥是 (n, e)，私钥是 (n, d)。

2\. 加密密文：

 - 将明文消息转换为整数形式 M，满足 0 ≤ M \< n。

 - 使用公钥 (n, e) 将明文消息 M 加密为密文 C，计算 C = M\^e (mod n)。

3\. 解密明文：

 - 使用私钥 (n, d) 将密文 C 解密为明文消息 M，计算 M = C\^d (mod n)。

在解密过程中，我们使用私钥指数 d 和 RSA 模数 n
来执行模幂运算，以还原密文为明文。

需要注意的是，安全性取决于保持私钥的机密性，因为知道私钥可以轻松地解密密文。因此，私钥应该妥善保管，只有授权的实体才能访问它。

这是 RSA 解密的基本原理。通过使用正确的私钥指数和 RSA
模数，我们可以解密密文并还原为明文。

**逆元**

[逆元是指两个元素相乘后对模数取模的结果等于 1。]{.mark}

在 RSA
解密过程中，使用私钥的指数 [d]{.mark} 对密文进行解密。因为 [d]{.mark} 和 [e]{.mark} 是互为逆元的，所以使用私钥解密后，得到的结果再次乘以公钥的指数 [e]{.mark}，并对模数 [n]{.mark} 取模，将会恢复成原始的明文。

逆元在 RSA
加密算法中起着重要的作用，确保了密文经过解密后能够正确还原为明文。

希望这个解释能够帮助你理解 RSA
中逆元的概念。如果你还有其他问题，请随时提问。

**模数取模**

当我们说对模数取模时，我们是在使用除法的概念。

初中数学中，我们学习了除法运算，例如将一个数除以另一个数，得到商和余数。对模数取模与此类似，但我们只关注余数部分。

举个例子，假设我们有一个数 17，我们想对它对模数 5
取模。我们进行除法运算，得到商 3 和余数 2。在这种情况下，对模数 5
取模的结果是 2。

所以，对模数取模就是将一个数除以模数，得到的余数部分。在 RSA
中，我们使用模运算来确保结果在指定的范围内。

希望这个解释能够帮助你理解对模数取模的概念。如果你还有其他问题，请随时提问。

**同余**

定义：余数相同就叫同余

(a mod n)=(b mod n)记作 a=b(mod n)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image88.png){width="5.760416666666667in"
height="1.416606517935258in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image89.png){width="5.760416666666667in"
height="3.2237970253718284in"}

同余性质：

当m大于或等于1情况下，a1的模m同余a2的模m，b1的模m同余b2的模m

那么a1加减b1同余a2加减b2, a1乘b1同余a2乘b2

乘法逆元性质：

当a乘b等于1的模m，那么gcd(a,m)=1也就是最小公因数是1

**平方剩余**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image90.png){width="5.760416666666667in"
height="1.0704516622922136in"}

当m是正整数，x平方同余a模m，并且gcd(a,m)=1也就是a和m的最小公因数是1

那么a就叫模m的平方剩余。

**欧拉定理**

[若N个整数的最大公因数是1，则称这N个整数互质或者叫互素]{.mark}

[只有1和它本身两个因数的自然数叫做质数或者叫素数]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image91.png){width="5.760416666666667in"
height="2.1697287839020123in"}

**费马定理**

**中国剩余定理**

**RSA加密系统**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image92.png){width="4.486111111111111in"
height="1.3041021434820648in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image93.png){width="1.25in"
height="0.2916666666666667in"}

**RSA加密类型**

python 和 rsa加密的函数解析：

libnum.modular.invmod (e,phi)：返回e模phi的逆元。

gmpy2.invert(e,phi)：返回e模phi的逆元。

m = pow(c, d, n) : m = c\^d mod n mod=%

0.  **普通解密**已知p、q、e、密文c，求明文m

import libnum

p=libnum.generate_prime(1024)

q=libnum.generate_prime(1024)

e=65537

m=\"NSSCTF{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}\"

m=libnum.s2n(m)

n=p\*q

phi=(p-1)\*(q-1)

d=libnum.invmod(e,phi)

c=pow(m,e,n)

print(\"p=\",p)

print(\"q=\",q)

print (\"e=\",e)

print (\"c=\",c)

#p=
122912801126049869009003839542545176400185213365268209105714006257803073428638629824801261702125287814910668428403367391355051987389837804474055637991864563803834741161217607848968821280710324766558457056004037592628178078680121173634128054936108782807954132605887275556228703383455969903056759874047110115433

#q=
120790113700754477830062212762518406876786376726996249661848284428829412089402183812692045970711341815805796005449714738748110749559462448861357011272792817313060401380148108517705435100103533857957024851181447994572972501120774586405811257420853542417275740953525627232008812587423053626515513859653865873671

#e= 65537

#c=
7094224488947659163318199615533819770556597977720767621640224798887506152292861133457571683713587909779712343346370719403811813233693263526316785431883833118583425528830238629831001255198236686372518770451273159769779374149881346761523688131115323441973953523582174059584087249568245044443295176738493785560215046375056269378223045128094953923926250055718405799885041115025529297362914403732661935017257507786348635366480744933193471899621592092711962814949533564454932121056035003021428158830645604347966849572981124877683317022116903132719663958775850982016292384237647664448371811915879714093710876989697939277005

exp：

```python
import gmpy2

from Crypto.Util.number import long_to_bytes

p =
122912801126049869009003839542545176400185213365268209105714006257803073428638629824801261702125287814910668428403367391355051987389837804474055637991864563803834741161217607848968821280710324766558457056004037592628178078680121173634128054936108782807954132605887275556228703383455969903056759874047110115433

q =
120790113700754477830062212762518406876786376726996249661848284428829412089402183812692045970711341815805796005449714738748110749559462448861357011272792817313060401380148108517705435100103533857957024851181447994572972501120774586405811257420853542417275740953525627232008812587423053626515513859653865873671

c =
7094224488947659163318199615533819770556597977720767621640224798887506152292861133457571683713587909779712343346370719403811813233693263526316785431883833118583425528830238629831001255198236686372518770451273159769779374149881346761523688131115323441973953523582174059584087249568245044443295176738493785560215046375056269378223045128094953923926250055718405799885041115025529297362914403732661935017257507786348635366480744933193471899621592092711962814949533564454932121056035003021428158830645604347966849572981124877683317022116903132719663958775850982016292384237647664448371811915879714093710876989697939277005

phi = (p-1) * (q-1)

e = 65537

n = p * q

d = gmpy2.invert(e, phi)

m = pow(c, d, n)

print('💌:',long_to_bytes(m))
```

1.  **公钥解析**

如果题目给了pem或者key后缀结尾的文件，用工具解出n和e，或者可以用kali自带的Openssl从公钥提取n和e.

题目：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image94.png){width="5.760416666666667in"
height="0.9245111548556431in"}

[命令：openssl rsa -pubin -text -modulus -in key.pem/key.key]{.mark}

[这里的Modulus是n的十六进制要转十进制]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image95.png){width="5.760416666666667in"
height="2.23661198600175in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image96.png){width="5.760416666666667in"
height="3.577280183727034in"}

SSL在线工具-公钥解析 (hiencode.com)

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image97.png){width="5.760416666666667in"
height="3.7083595800524933in"}

用python脚本跑flag

import rsa

import gmpy2

p=285960468890451637935629440372639283459

q=304008741604601924494328155975272418463

n=p\*q

e=65537

phi=(q-1)\*(p-1)

d=gmpy2.invert(e,phi)#用模逆求d

key=rsa.PrivateKey(n,e,d,q,p)
#在pkcs标准中，pkcs#1规定私钥保护（n,e,d,p,q）

with
open(\"D:\\\\迅雷下载\\\\0eaf8d6c-3fe5-4549-9e81-94ac42535e7b\\\\flag.enc\",\"rb\")
as f: #以二进制读取，密文

    f=f.read()

    print(rsa.decrypt(f,key)) #f:公钥加密结果 key:私钥

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image98.png){width="5.760416666666667in"
height="5.460503062117235in"}

2.  **模不互素**

求两个模n的最大公因数就可以得到其中的大素数

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image99.png){width="5.760416666666667in"
height="1.4490715223097113in"}

#!/usr/bin/python

\# coding:utf-8

import gmpy2

import libnum

c1 = int(

\'0x8BD7BF995BF9E16A0D04ADB49A2411C74FFDB0DB4F35DB3A79A1B44691947C9824085BC4CA5F7F4EFA3C8FD0BC3E870AA6D5E15307A63A2172C44C5903D35785B8D06B51651EE7106B070D5A6AABA089AB67609661265B74914C865F863DC1D2DC08CE0B026107A74EC3FDC62666B50110B9D15A243EAAD6F53646929A3369285404868E42DD0BBE92D956018E3C0B36EF5E9516E433228CFDD06D6E662EC0A9A31061EA11F61CA17EABF43D2D4977FC9D6FC53AB6DC01509401B8D9A46B59A9ADAA97D54CC50C27445E4C21B893510620EC3566AD6E8727FA147437B207505217E6F2DF009E2286C8354D281374D7802D08A2062FE48DBF135BBCAB120EBF84\',

16)

c2 = int(

\'0x8C3CF3161AA3E37831030985C60566A7604688B73E5B1D3B36E72EF06ED4F71289EFE80E0D94BD755034E6C210F17DA85B9D0388F3AD104C68BC514A8EB1569A109EB5F266F7C5FA4DDFA638258949B43D4CF1406720CCD4CA11E74FDF8AEB35C56A79781C87157FC4213573329C5B0FF411F8A4F34580AA103DB9FD403C0D409FA11860A7C4595FDC49DC2CF94E5112B772E5DEC8F17E24B10A7FD7A95DCB87BE5E27C32FC931574A7847BC506A61EFE9DB3D3F612143845FE80D7B3EA548B886A67A29CBDB2775B1F91178B6DA763F1A6ECFF46592E4C7FFAAB6C9FEF29D9CB9E035A3D98ECFFB26BA2EEAA56D1CD096E6A2CF9A58086CAD7718DDA5CB0C1B\',

16)

n1 = int(

18674375108313094928585156581138941368570022222190945461284402673204018075354069827186085851309806592398721628845336840532779579197302984987661547245423180760958022898546496524249201679543421158842103496452861932183144343315925106154322066796612415616342291023962127055311307613898583850177922930685155351380500587263611591893137588708003711296496548004793832636078992866149115453883484010146248683416979269684197112659302912316105354447631916609587360103908746719586185593386794532066034112164661723748874045470225129298518385683561122623859924435600673501186244422907402943929464694448652074412105888867178867357727)

n2 = int(

20071978783607427283823783012022286910630968751671103864055982304683197064862908267206049336732205051588820325894943126769930029619538705149178241710069113634567118672515743206769333625177879492557703359178528342489585156713623530654319500738508146831223487732824835005697932704427046675392714922683584376449203594641540794557871881581407228096642417744611261557101573050163285919971711214856243031354845945564837109657494523902296444463748723639109612438012590084771865377795409000586992732971594598355272609789079147061852664472115395344504822644651957496307894998467309347038349470471900776050769578152203349128951)

p1 = gmpy2.gcd(n1, n2)

assert (p1 != 1)

p2 = n1 / p1

p3 = n2 / p1

e = 0x10001

d1 = gmpy2.invert(e, (p1 - 1) \* (p2 - 1))

d2 = gmpy2.invert(e, (p1 - 1) \* (p3 - 1))

m1 = pow(c1, d1, n1)

m2 = pow(c2, d2, n2)

print libnum.n2s(m1) + libnum.n2s(m2)

3.  **分解 N 得到多个相同的 P**

[1.利用]{.mark}factordb[在线分解n]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image100.png){width="5.760416666666667in"
height="1.2889206036745406in"}

2  yafu

下载地址：

yafu download \| SourceForge.net

下载  yafu-x64.exe------windows系统

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image101.png){width="5.760416666666667in"
height="3.4204035433070867in"}

对该文件地址处输入  cmd  打开该文件终端

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image102.png){width="5.760416666666667in"
height="2.3656616360454943in"}

输入.\\yafu-x64.exe 按回车进入下一行

再输入factor(需要分解的素数)

得出结果。

4.  **dp、dq 泄露**

原理：

dp=d%(p-1)

dq=d%(q-1)

**攻击条件：**

已知p，q，dp，dq，c

**关系公式：**

![stickPicture.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image103.webp){width="0.0in"
height="0.0in"}

**解密公式：**

![stickPicture.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image104.jpeg){width="5.760416666666667in"
height="2.1169017935258094in"}

解密脚本：

import gmpy2

from Crypto.Util.number import \*

n=
118618954287615269695904875995489548511444940267622767094047739634494646358809304433978173495687678370406458702860536342785803753234702546219494665535864474652301862284591690673176769043630372899075883834606545174586348720993678078895654149136676023206963021215226128014757783383076786413359604861549162636747p=
12244425890527037559457450758199625345224440148602500121947513405940248134857180032689144921510099766782376592176091852775339372003558472079284757727362571q=
9687588078701625994967484476321431565856840411439788976614047902260935119170606128529184693304251663287418434325133814992945149670372082642015792984936257dp=
11661765341055037028213110243140762441891859947132976341835485861002039690412298548398000165827316261292160830963662695604031845480131372329938955617008307dq=
5330972108962230819517925352753760247189342573369390983643754562382224659226949816794659715545630171557328975020873518879918889149973698886977898856476183

c=
12374013610995935975987144573885493212459411904794697197903023715805777590324318665512805085245267803654557700689811822171219122398629103950576556025535606948328799420133553234348610960343249046259660281472602396406991408998707805300684186709474247145123999521260863968647240075574632249474210031448000004668InvQ
= gmpy2.invert(q,p)

p=
12244425890527037559457450758199625345224440148602500121947513405940248134857180032689144921510099766782376592176091852775339372003558472079284757727362571q=
9687588078701625994967484476321431565856840411439788976614047902260935119170606128529184693304251663287418434325133814992945149670372082642015792984936257dp=
11661765341055037028213110243140762441891859947132976341835485861002039690412298548398000165827316261292160830963662695604031845480131372329938955617008307dq=
5330972108962230819517925352753760247189342573369390983643754562382224659226949816794659715545630171557328975020873518879918889149973698886977898856476183c=
12374013610995935975987144573885493212459411904794697197903023715805777590324318665512805085245267803654557700689811822171219122398629103950576556025535606948328799420133553234348610960343249046259660281472602396406991408998707805300684186709474247145123999521260863968647240075574632249474210031448000004668

InvQ = gmpy2.invert(q,p)

mp = pow(c,dp,p)

mq = pow(c,dq,q)

m=(((mp-mq)\*InvQ)%p)\*q+mq

print(long_to_bytes(m))

5.  **dp 泄露**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image105.png){width="5.760416666666667in"
height="2.1364654418197726in"}

exp:

import gmpy2 as gp

from Crypto.Util.number import \*

e = 65537

n =
62950660589752377241535942010457460675378335694404721223426371627802159493655570041534480026979837056215567303530448462076388942749116962945931432723672826148999814815864738069663127706046027850586024555861960247057288826014343547293035737544457656904257388300461848219257240252715837662741274235378360898441

c =
26392919777656338278184497106215581599692023606797351841011065350738534402079717897589592521000832026751736045905247050532819571969784687491977953157313304550096179520376626220816081159472339787295872214912587497324709488986746768994907107727184468228540635002062232484115731701648311946527233449512543132274

dp =
7088497034630351463006975624795947102639056977565074157092915907376477955247769847204254053775159112398217033648894620506901638351932922911273150932128973

for i in range(1,e):

if(dp\*e-1)%i == 0:

if n%(((dp\*e-1)//i)+1) == 0:

p=((dp\*e-1)//i)+1

q=n//(((dp\*e-1)//i)+1)

phi=(q-1)\*(p-1)

d=gp.invert(e,phi)

m=pow(c,d,n)

print(long_to_bytes(m))

6.  **p/q接近类型**

题目：

from libnum import \*

from gmpy2 import \*

p=generate_prime(1024)

q=next_prime(p)

e=65537

m=\'NSSCTF{\*\*\*\*\*\*\*}\'

m=s2n(m)

n=p\*q

phi=(p-1)\*(q-1)

d=invmod(e,phi)

c=pow(m,e,n)

print(\"n=\",n)

print(\"e=\",e)

print(\"c=\",c)

\# n=
24981376790941538042242194741227892897407513396986731688877133454927442860995432316502739082570143505514748189761926835267759902439088795405888334103808204493954060044146586606969762154041793765844462081845490598211667272961234605967919438875499785814549051002289336390400088945736443426364361032870741024016549739096474413537901098157940458928277363388694717514323106251487767419607466664175936942972759711506228656400164583540573319572125036265662330306877811831045019686459493451558882811173136631573392182233161484350878695026357462290962322316959710815852914274474767115283825849610223430527125542218326259388501

\# e= 65537

\# c=
20159395346151098135636315342962498279920000537186367678734614295342297238729946157173169398141183795295342421626812913110784320710149318393656661582157610182569479131625808166266400522513050071081253869746865806961410702124426021839786686971490883603141916263075756918270160269956469968815381434371042453456185750940323619568741956243054983302281739844073931738335165924679149156513059772597287311150001080524533236565521881558592378167621577532597521749930820990533120461791013359786254216859344006298715497621642857727174896969485816794718062289736382736417151820935214824518306312811267158057425922650562544599188

[exp：]{.mark}

#p与q相近，可以费马分解。也可以直接开方求根附近的素数，即为p, q。

from Crypto.Util.number import \*

from gmpy2 import next_prime,iroot

e = 0x10001

n =
24981376790941538042242194741227892897407513396986731688877133454927442860995432316502739082570143505514748189761926835267759902439088795405888334103808204493954060044146586606969762154041793765844462081845490598211667272961234605967919438875499785814549051002289336390400088945736443426364361032870741024016549739096474413537901098157940458928277363388694717514323106251487767419607466664175936942972759711506228656400164583540573319572125036265662330306877811831045019686459493451558882811173136631573392182233161484350878695026357462290962322316959710815852914274474767115283825849610223430527125542218326259388501

c =
20159395346151098135636315342962498279920000537186367678734614295342297238729946157173169398141183795295342421626812913110784320710149318393656661582157610182569479131625808166266400522513050071081253869746865806961410702124426021839786686971490883603141916263075756918270160269956469968815381434371042453456185750940323619568741956243054983302281739844073931738335165924679149156513059772597287311150001080524533236565521881558592378167621577532597521749930820990533120461791013359786254216859344006298715497621642857727174896969485816794718062289736382736417151820935214824518306312811267158057425922650562544599188

t = iroot(n,2)\[0\]

q = next_prime(t)

p = n//q

assert(n==p\*q)

d = inverse(e,(p-1)\*(q-1))

print(long_to_bytes(pow(c,d,n)).decode())

7.  **大指数dp泄露**

e有点大，然后加dp泄露

from Crypto.Util.number import \*

flag = b\'NSSCTF{\*\*\*\*\*\*}\'

p = getPrime(512)

q = getPrime(512)

n = p\*q

e = getPrime(128)

d = inverse(e, (p-1)\*(q-1))

dp = d % (p-1)

m = bytes_to_long(flag)

c = pow(m, e, n)

print(f\'n = {n}\')

print(f\'e = {e}\')

print(f\'c = {c}\')

print(f\'dp = {dp}\')

\'\'\'

n =
92288362151232755164303382554034496430634785857894506752180261103500715219090974532177552845107426542175470207920267802066773828210866572070045093611090322738109527534622730588618668861998969946471756352024368486322527057077613762697792913167023012077178671066981439295386486943067698150993422039585259179729

e = 229991316986730339421575788374847647237

c =
66178170892880340054212366602556925884485962775832591797127163461420023986798822926684824340567060840259672460835004142425374706821346941926520921852009455818529825976414766339170445233789109526300838535719649346266975388774091834431039678689254534566870194580604694419819400454951059125553501095973278807456

dp =
8987556601717285362487353965045062789633142861774364363374961991445049127918653163458814169532860957264061203394944931114888144611267605606197232438332289

\'\'\'

exp:

from sage import \*

from Crypto.Util.number import long_to_bytes

from xenny.ctf.crypto.modern.asymmetric.rsa import dpleak

\# 大指数dp泄露

n =
92288362151232755164303382554034496430634785857894506752180261103500715219090974532177552845107426542175470207920267802066773828210866572070045093611090322738109527534622730588618668861998969946471756352024368486322527057077613762697792913167023012077178671066981439295386486943067698150993422039585259179729

e = 229991316986730339421575788374847647237

c =
66178170892880340054212366602556925884485962775832591797127163461420023986798822926684824340567060840259672460835004142425374706821346941926520921852009455818529825976414766339170445233789109526300838535719649346266975388774091834431039678689254534566870194580604694419819400454951059125553501095973278807456

dp =
8987556601717285362487353965045062789633142861774364363374961991445049127918653163458814169532860957264061203394944931114888144611267605606197232438332289

m = dpleak.attack(dp,c,e=e,n=n)

flag = long_to_bytes( m )

print(flag)

#b\'NSSCTF{D0_YoU_WAN1_TO_J0In_NsSCTf}111111111111111111111111111111111111111111111111111111111111111111111111111\'

8.  **Roll 按行加密**

    **共模攻击**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image106.png){width="5.760416666666667in"
height="1.963497375328084in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image107.png){width="5.760416666666667in"
height="2.5690135608048994in"}

import gmpy2

from Crypto.Util.number import \*

n=21058339337354287847534107544613605305015441090508924094198816691219103399526800112802416383088995253908857460266726925615826895303377801614829364034624475195859997943146305588315939130777450485196290766249612340054354622516207681542973756257677388091926549655162490873849955783768663029138647079874278240867932127196686258800146911620730706734103611833179733264096475286491988063990431085380499075005629807702406676707841324660971173253100956362528346684752959937473852630145893796056675793646430793578265418255919376323796044588559726703858429311784705245069845938316802681575653653770883615525735690306674635167111

e1=2767

e2=3659

c1=20152490165522401747723193966902181151098731763998057421967155300933719378216342043730801302534978403741086887969040721959533190058342762057359432663717825826365444996915469039056428416166173920958243044831404924113442512617599426876141184212121677500371236937127571802891321706587610393639446868836987170301813018218408886968263882123084155607494076330256934285171370758586535415136162861138898728910585138378884530819857478609791126971308624318454905992919405355751492789110009313138417265126117273710813843923143381276204802515910527468883224274829962479636527422350190210717694762908096944600267033351813929448599

c2=11298697323140988812057735324285908480504721454145796535014418738959035245600679947297874517818928181509081545027056523790022598233918011261011973196386395689371526774785582326121959186195586069851592467637819366624044133661016373360885158956955263645614345881350494012328275215821306955212788282617812686548883151066866149060363482958708364726982908798340182288702101023393839781427386537230459436512613047311585875068008210818996941460156589314135010438362447522428206884944952639826677247819066812706835773107059567082822312300721049827013660418610265189288840247186598145741724084351633508492707755206886202876227

g,s,t=gmpy2.gcdext(e1,e2)#欧里几得算法

m=pow(c1,s,n)\*pow(c2,t,n) %n

print(long_to_bytes(m))

10. **低加密指数攻击**

当e等于1，2，3的时候就可以达到低加密指数攻击的条件，枚举k，直到出现整数。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image108.png){width="5.152777777777778in"
height="3.289449912510936in"}

解密脚本

import gmpy2

from Crypto.Util.number import \*

e = 3

n =
18970053728616609366458286067731288749022264959158403758357985915393383117963693827568809925770679353765624810804904382278845526498981422346319417938434861558291366738542079165169736232558687821709937346503480756281489775859439254614472425017554051177725143068122185961552670646275229009531528678548251873421076691650827507829859299300272683223959267661288601619845954466365134077547699819734465321345758416957265682175864227273506250707311775797983409090702086309946790711995796789417222274776215167450093735639202974148778183667502150202265175471213833685988445568819612085268917780718945472573765365588163945754761

c =
150409620528139732054476072280993764527079006992643377862720337847060335153837950368208902491767027770946661

i = 0

while True:

    if gmpy2.iroot((c+i\*n),3)\[1\] == True:#gmpy2.iroot(x,n)
x开n次根求根为整数就停止

        m = gmpy2.iroot((c+i\*n),3)\[0\] \# gmpy2.iroot()开根号

        print(i)

        break

    i += 1

print(long_to_bytes(m))

11. **低加密指数广播攻击**

例题：

m = xxxxxxxx

e = 65537

========== n c ==========

n =
20474918894051778533305262345601880928088284471121823754049725354072477155873778848055073843345820697886641086842612486541250183965966001591342031562953561793332341641334302847996108417466360688139866505179689516589305636902137210185624650854906780037204412206309949199080005576922775773722438863762117750429327585792093447423980002401200613302943834212820909269713876683465817369158585822294675056978970612202885426436071950214538262921077409076160417436699836138801162621314845608796870206834704116707763169847387223307828908570944984416973019427529790029089766264949078038669523465243837675263858062854739083634207

c =
974463908243330865728978769213595400782053398596897741316275722596415018912929508637393850919224969271766388710025195039896961956062895570062146947736340342927974992616678893372744261954172873490878805483241196345881721164078651156067119957816422768524442025688079462656755605982104174001635345874022133045402344010045961111720151990412034477755851802769069309069018738541854130183692204758761427121279982002993939745343695671900015296790637464880337375511536424796890996526681200633086841036320395847725935744757993013352804650575068136129295591306569213300156333650910795946800820067494143364885842896291126137320

n =
20918819960648891349438263046954902210959146407860980742165930253781318759285692492511475263234242002509419079545644051755251311392635763412553499744506421566074721268822337321637265942226790343839856182100575539845358877493718334237585821263388181126545189723429262149630651289446553402190531135520836104217160268349688525168375213462570213612845898989694324269410202496871688649978370284661017399056903931840656757330859626183773396574056413017367606446540199973155630466239453637232936904063706551160650295031273385619470740593510267285957905801566362502262757750629162937373721291789527659531499435235261620309759

c =
15819636201971185538694880505120469332582151856714070824521803121848292387556864177196229718923770810072104155432038682511434979353089791861087415144087855679134383396897817458726543883093567600325204596156649305930352575274039425470836355002691145864435755333821133969266951545158052745938252574301327696822347115053614052423028835532509220641378760800693351542633860702225772638930501021571415907348128269681224178300248272689705308911282208685459668200507057183420662959113956077584781737983254788703048275698921427029884282557468334399677849962342196140864403989162117738206246183665814938783122909930082802031855

n =
25033254625906757272369609119214202033162128625171246436639570615263949157363273213121556825878737923265290579551873824374870957467163989542063489416636713654642486717219231225074115269684119428086352535471683359486248203644461465935500517901513233739152882943010177276545128308412934555830087776128355125932914846459470221102007666912211992310538890654396487111705385730502843589727289829692152177134753098649781412247065660637826282055169991824099110916576856188876975621376606634258927784025787142263367152947108720757222446686415627479703666031871635656314282727051189190889008763055811680040315277078928068816491

c =
4185308529416874005831230781014092407198451385955677399668501833902623478395669279404883990725184332709152443372583701076198786635291739356770857286702107156730020004358955622511061410661058982622055199736820808203841446796305284394651714430918690389486920560834672316158146453183789412140939029029324756035358081754426645160033262924330248675216108270980157049705488620263485129480952814764002865280019185127662449318324279383277766416258142275143923532168798413011028271543085249029048997452212503111742302302065401051458066585395360468447460658672952851643547193822775218387853623453638025492389122204507555908862

n =
21206968097314131007183427944486801953583151151443627943113736996776787181111063957960698092696800555044199156765677935373149598221184792286812213294617749834607696302116136745662816658117055427803315230042700695125718401646810484873064775005221089174056824724922160855810527236751389605017579545235876864998419873065217294820244730785120525126565815560229001887622837549118168081685183371092395128598125004730268910276024806808565802081366898904032509920453785997056150497645234925528883879419642189109649009132381586673390027614766605038951015853086721168018787523459264932165046816881682774229243688581614306480751

c =
4521038011044758441891128468467233088493885750850588985708519911154778090597136126150289041893454126674468141393472662337350361712212694867311622970440707727941113263832357173141775855227973742571088974593476302084111770625764222838366277559560887042948859892138551472680654517814916609279748365580610712259856677740518477086531592233107175470068291903607505799432931989663707477017904611426213770238397005743730386080031955694158466558475599751940245039167629126576784024482348452868313417471542956778285567779435940267140679906686531862467627238401003459101637191297209422470388121802536569761414457618258343550613

n =
22822039733049388110936778173014765663663303811791283234361230649775805923902173438553927805407463106104699773994158375704033093471761387799852168337898526980521753614307899669015931387819927421875316304591521901592823814417756447695701045846773508629371397013053684553042185725059996791532391626429712416994990889693732805181947970071429309599614973772736556299404246424791660679253884940021728846906344198854779191951739719342908761330661910477119933428550774242910420952496929605686154799487839923424336353747442153571678064520763149793294360787821751703543288696726923909670396821551053048035619499706391118145067

c =
15406498580761780108625891878008526815145372096234083936681442225155097299264808624358826686906535594853622687379268969468433072388149786607395396424104318820879443743112358706546753935215756078345959375299650718555759698887852318017597503074317356745122514481807843745626429797861463012940172797612589031686718185390345389295851075279278516147076602270178540690147808314172798987497259330037810328523464851895621851859027823681655934104713689539848047163088666896473665500158179046196538210778897730209572708430067658411755959866033531700460551556380993982706171848970460224304996455600503982223448904878212849412357

n =
21574139855341432908474064784318462018475296809327285532337706940126942575349507668289214078026102682252713757703081553093108823214063791518482289846780197329821139507974763780260290309600884920811959842925540583967085670848765317877441480914852329276375776405689784571404635852204097622600656222714808541872252335877037561388406257181715278766652824786376262249274960467193961956690974853679795249158751078422296580367506219719738762159965958877806187461070689071290948181949561254144310776943334859775121650186245846031720507944987838489723127897223416802436021278671237227993686791944711422345000479751187704426369

c =
20366856150710305124583065375297661819795242238376485264951185336996083744604593418983336285185491197426018595031444652123288461491879021096028203694136683203441692987069563513026001861435722117985559909692670907347563594578265880806540396777223906955491026286843168637367593400342814725694366078337030937104035993569672959361347287894143027186846856772983058328919716702982222142848848117768499996617588305301483085428547267337070998767412540225911508196842253134355901263861121500650240296746702967594224401650220168780537141654489215019142122284308116284129004257364769474080721001708734051264841350424152506027932

n =
25360227412666612490102161131174584819240931803196448481224305250583841439581008528535930814167338381983764991296575637231916547647970573758269411168219302370541684789125112505021148506809643081950237623703181025696585998044695691322012183660424636496897073045557400768745943787342548267386564625462143150176113656264450210023925571945961405709276631990731602198104287528528055650050486159837612279600415259486306154947514005408907590083747758953115486124865486720633820559135063440942528031402951958557630833503775112010715604278114325528993771081233535247118481765852273252404963430792898948219539473312462979849137

c =
19892772524651452341027595619482734356243435671592398172680379981502759695784087900669089919987705675899945658648623800090272599154590123082189645021800958076861518397325439521139995652026377132368232502108620033400051346127757698623886142621793423225749240286511666556091787851683978017506983310073524398287279737680091787333547538239920607761080988243639547570818363788673249582783015475682109984715293163137324439862838574460108793714172603672477766831356411304446881998674779501188163600664488032943639694828698984739492200699684462748922883550002652913518229322945040819064133350314536378694523704793396169065179

n =
22726855244632356029159691753451822163331519237547639938779517751496498713174588935566576167329576494790219360727877166074136496129927296296996970048082870488804456564986667129388136556137013346228118981936899510687589585286517151323048293150257036847475424044378109168179412287889340596394755257704938006162677656581509375471102546261355748251869048003600520034656264521931808651038524134185732929570384705918563982065684145766427962502261522481994191989820110575981906998431553107525542001187655703534683231777988419268338249547641335718393312295800044734534761692799403469497954062897856299031257454735945867491191

c =
6040119795175856407541082360023532204614723858688636724822712717572759793960246341800308149739809871234313049629732934797569781053000686185666374833978403290525072598774001731350244744590772795701065129561898116576499984185920661271123665356132719193665474235596884239108030605882777868856122378222681140570519180321286976947154042272622411303981011302586225630859892731724640574658125478287115198406253847367979883768000812605395482952698689604477719478947595442185921480652637868335673233200662100621025061500895729605305665864693122952557361871523165300206070325660353095592778037767395360329231331322823610060006

n =
23297333791443053297363000786835336095252290818461950054542658327484507406594632785712767459958917943095522594228205423428207345128899745800927319147257669773812669542782839237744305180098276578841929496345963997512244219376701787616046235397139381894837435562662591060768476997333538748065294033141610502252325292801816812268934171361934399951548627267791401089703937389012586581080223313060159456238857080740699528666411303029934807011214953984169785844714159627792016926490955282697877141614638806397689306795328344778478692084754216753425842557818899467945102646776342655167655384224860504086083147841252232760941

c =
5418120301208378713115889465579964257871814114515046096090960159737859076829258516920361577853903925954198406843757303687557848302302200229295916902430205737843601806700738234756698575708612424928480440868739120075888681672062206529156566421276611107802917418993625029690627196813830326369874249777619239603300605876865967515719079797115910578653562787899019310139945904958024882417833736304894765433489476234575356755275147256577387022873348906900149634940747104513850154118106991137072643308620284663108283052245750945228995387803432128842152251549292698947407663643895853432650029352092018372834457054271102816934

n =
28873667904715682722987234293493200306976947898711255064125115933666968678742598858722431426218914462903521596341771131695619382266194233561677824357379805303885993804266436810606263022097900266975250431575654686915049693091467864820512767070713267708993899899011156106766178906700336111712803362113039613548672937053397875663144794018087017731949087794894903737682383916173267421403408140967713071026001874733487295007501068871044649170615709891451856792232315526696220161842742664778581287321318748202431466508948902745314372299799561625186955234673012098210919745879882268512656931714326782335211089576897310591491

c =
9919880463786836684987957979091527477471444996392375244075527841865509160181666543016317634963512437510324198702416322841377489417029572388474450075801462996825244657530286107428186354172836716502817609070590929769261932324275353289939302536440310628698349244872064005700644520223727670950787924296004296883032978941200883362653993351638545860207179022472492671256630427228461852668118035317021428675954874947015197745916918197725121122236369382741533983023462255913924692806249387449016629865823316402366017657844166919846683497851842388058283856219900535567427103603869955066193425501385255322097901531402103883869

n =
22324685947539653722499932469409607533065419157347813961958075689047690465266404384199483683908594787312445528159635527833904475801890381455653807265501217328757871352731293000303438205315816792663917579066674842307743845261771032363928568844669895768092515658328756229245837025261744260614860746997931503548788509983868038349720225305730985576293675269073709022350700836510054067641753713212999954307022524495885583361707378513742162566339010134354907863733205921845038918224463903789841881400814074587261720283879760122070901466517118265422863420376921536734845502100251460872499122236686832189549698020737176683019

c =
1491527050203294989882829248560395184804977277747126143103957219164624187528441047837351263580440686474767380464005540264627910126483129930668344095814547592115061057843470131498075060420395111008619027199037019925701236660166563068245683975787762804359520164701691690916482591026138582705558246869496162759780878437137960823000043988227303003876410503121370163303711603359430764539337597866862508451528158285103251810058741879687875218384160282506172706613359477657215420734816049393339593755489218588796607060261897905233453268671411610631047340459487937479511933450369462213795738933019001471803157607791738538467

n =
27646746423759020111007828653264027999257847645666129907789026054594393648800236117046769112762641778865620892443423100189619327585811384883515424918752749559627553637785037359639801125213256163008431942593727931931898199727552768626775618479833029101249692573716030706695702510982283555740851047022672485743432464647772882314215176114732257497240284164016914018689044557218920300262234652840632406067273375269301008409860193180822366735877288205783314326102263756503786736122321348320031950012144905869556204017430593656052867939493633163499580242224763404338807022510136217187779084917996171602737036564991036724299

c =
21991524128957260536043771284854920393105808126700128222125856775506885721971193109361315961129190814674647136464887087893990660894961612838205086401018885457667488911898654270235561980111174603323721280911197488286585269356849579263043456316319476495888696219344219866516861187654180509247881251251278919346267129904739277386289240394384575124331135655943513831009934023397457082184699737734388823763306805326430395849935770213817533387235486307008892410920611669932693018165569417445885810825749609388627231235840912644654685819620931663346297596334834498661789016450371769203650109994771872404185770230172934013971

n =
20545487405816928731738988374475012686827933709789784391855706835136270270933401203019329136937650878386117187776530639342572123237188053978622697282521473917978282830432161153221216194169879669541998840691383025487220850872075436064308499924958517979727954402965612196081404341651517326364041519250125036424822634354268773895465698920883439222996581226358595873993976604699830613932320720554130011671297944433515047180565484495191003887599891289037982010216357831078328159028953222056918189365840711588671093333013117454034313622855082795813122338562446223041211192277089225078324682108033843023903550172891959673551

c =
14227439188191029461250476692790539654619199888487319429114414557975376308688908028140817157205579804059783807641305577385724758530138514972962209062230576107406142402603484375626077345190883094097636019771377866339531511965136650567412363889183159616188449263752475328663245311059988337996047359263288837436305588848044572937759424466586870280512424336807064729894515840552404756879590698797046333336445465120445087587621743906624279621779634772378802959109714400516183718323267273824736540168545946444437586299214110424738159957388350785999348535171553569373088251552712391288365295267665691357719616011613628772175

n =
27359727711584277234897157724055852794019216845229798938655814269460046384353568138598567755392559653460949444557879120040796798142218939251844762461270251672399546774067275348291003962551964648742053215424620256999345448398805278592777049668281558312871773979931343097806878701114056030041506690476954254006592555275342579529625231194321357904668512121539514880704046969974898412095675082585315458267591016734924646294357666924293908418345508902112711075232047998775303603175363964055048589769318562104883659754974955561725694779754279606726358588862479198815999276839234952142017210593887371950645418417355912567987

c =
3788529784248255027081674540877016372807848222776887920453488878247137930578296797437647922494510483767651150492933356093288965943741570268943861987024276610712717409139946409513963043114463933146088430004237747163422802959250296602570649363016151581364006795894226599584708072582696996740518887606785460775851029814280359385763091078902301957226484620428513604630585131511167015763190591225884202772840456563643159507805711004113901417503751181050823638207803533111429510911616160851391754754434764819568054850823810901159821297849790005646102129354035735350124476838786661542089045509656910348676742844957008857457

n =
27545937603751737248785220891735796468973329738076209144079921449967292572349424539010502287564030116831261268197384650511043068738911429169730640135947800885987171539267214611907687570587001933829208655100828045651391618089603288456570334500533178695238407684702251252671579371018651675054368606282524673369983034682330578308769886456335818733827237294570476853673552685361689144261552895758266522393004116017849397346259119221063821663280935820440671825601452417487330105280889520007917979115568067161590058277418371493228631232457972494285014767469893647892888681433965857496916110704944758070268626897045014782837

c =
14069112970608895732417039977542732665796601893762401500878786871680645798754783315693511261740059725171342404186571066972546332813667711135661176659424619936101038903439144294886379322591635766682645179888058617577572409307484708171144488708410543462972008179994594087473935638026612679389759756811490524127195628741262871304427908481214992471182859308828778119005750928935764927967212343526503410515793717201360360437981322576798056276657140363332700714732224848346808963992302409037706094588964170239521193589470070839790404597252990818583717869140229811712295005710540476356743378906642267045723633874011649259842

n =
25746162075697911560263181791216433062574178572424600336856278176112733054431463253903433128232709054141607100891177804285813783247735063753406524678030561284491481221681954564804141454666928657549670266775659862814924386584148785453647316864935942772919140563506305666207816897601862713092809234429096584753263707828899780979223118181009293655563146526792388913462557306433664296966331469906428665127438829399703002867800269947855869262036714256550075520193125987011945192273531732276641728008406855871598678936585324782438668746810516660152018244253008092470066555687277138937298747951929576231036251316270602513451

c =
17344284860275489477491525819922855326792275128719709401292545608122859829827462088390044612234967551682879954301458425842831995513832410355328065562098763660326163262033200347338773439095709944202252494552172589503915965931524326523663289777583152664722241920800537867331030623906674081852296232306336271542832728410803631170229642717524942332390842467035143631504401140727083270732464237443915263865880580308776111219718961746378842924644142127243573824972533819479079381023103585862099063382129757560124074676150622288706094110075567706403442920696472627797607697962873026112240527498308535903232663939028587036724

n =
23288486934117120315036919418588136227028485494137930196323715336208849327833965693894670567217971727921243839129969128783853015760155446770590696037582684845937132790047363216362087277861336964760890214059732779383020349204803205725870225429985939570141508220041286857810048164696707018663758416807708910671477407366098883430811861933014973409390179948577712579749352299440310543689035651465399867908428885541237776143404376333442949397063249223702355051571790555151203866821867908531733788784978667478707672984539512431549558672467752712004519300318999208102076732501412589104904734983789895358753664077486894529499

c =
10738254418114076548071448844964046468141621740603214384986354189105236977071001429271560636428075970459890958274941762528116445171161040040833357876134689749846940052619392750394683504816081193432350669452446113285638982551762586656329109007214019944975816434827768882704630460001209452239162896576191876324662333153835533956600295255158377025198426950944040643235430211011063586032467724329735785947372051759042138171054165854842472990583800899984893232549092766400510300083585513014171220423103452292891496141806956300396540682381668367564569427813092064053993103537635994311143010708814851867239706492577203899024

n =
19591441383958529435598729113936346657001352578357909347657257239777540424811749817783061233235817916560689138344041497732749011519736303038986277394036718790971374656832741054547056417771501234494768509780369075443550907847298246275717420562375114406055733620258777905222169702036494045086017381084272496162770259955811174440490126514747876661317750649488774992348005044389081101686016446219264069971370646319546429782904810063020324704138495608761532563310699753322444871060383693044481932265801505819646998535192083036872551683405766123968487907648980900712118052346174533513978009131757167547595857552370586353973

c =
3834917098887202931981968704659119341624432294759361919553937551053499607440333234018189141970246302299385742548278589896033282894981200353270637127213483172182529890495903425649116755901631101665876301799865612717750360089085179142750664603454193642053016384714515855868368723508922271767190285521137785688075622832924829248362774476456232826885801046969384519549385428259591566716890844604696258783639390854153039329480726205147199247183621535172450825979047132495439603840806501254997167051142427157381799890725323765558803808030109468048682252028720241357478614704610089120810367192414352034177484688502364022887

n =
19254242571588430171308191757871261075358521158624745702744057556054652332495961196795369630484782930292003238730267396462491733557715379956969694238267908985251699834707734400775311452868924330866502429576951934279223234676654749272932769107390976321208605516299532560054081301829440688796904635446986081691156842271268059970762004259219036753174909942343204432795076377432107630203621754552804124408792358220071862369443201584155711893388877350138023238624566616551246804054720492816226651467017802504094070614892556444425915920269485861799532473383304622064493223627552558344088839860178294589481899206318863310603

c =
6790553533991297205804561991225493105312398825187682250780197510784765226429663284220400480563039341938599783346724051076211265663468643826430109013245014035811178295081939958687087477312867720289964506097819762095244479129359998867671811819738196687884696680463458661374310994610760009474264115750204920875527434486437536623589684519411519100170291423367424938566820315486507444202022408003879118465761273916755290898112991525546114191064022991329724370064632569903856189236177894007766690782630247443895358893983735822824243487181851098787271270256780891094405121947631088729917398317652320497765101790132679171889

n =
26809700251171279102974962949184411136459372267620535198421449833298448092580497485301953796619185339316064387798092220298630428207556482805739803420279056191194360049651767412572609187680508073074653291350998253938793269214230457117194434853888765303403385824786231859450351212449404870776320297419712486574804794325602760347306432927281716160368830187944940128907971027838510079519466846176106565164730963988892400240063089397720414921398936399927948235195085202171264728816184532651138221862240969655185596628285814057082448321749567943946273776184657698104465062749244327092588237927996419620170254423837876806659

c =
386213556608434013769864727123879412041991271528990528548507451210692618986652870424632219424601677524265011043146748309774067894985069288067952546139416819404039688454756044862784630882833496090822568580572859029800646671301748901528132153712913301179254879877441322285914544974519727307311002330350534857867516466612474769753577858660075830592891403551867246057397839688329172530177187042229028685862036140779065771061933528137423019407311473581832405899089709251747002788032002094495379614686544672969073249309703482556386024622814731015767810042969813752548617464974915714425595351940266077021672409858645427346

exp:

from Crypto.Util.number import \*

from gmpy2 import \*

e = 65537

n1 =
20474918894051778533305262345601880928088284471121823754049725354072477155873778848055073843345820697886641086842612486541250183965966001591342031562953561793332341641334302847996108417466360688139866505179689516589305636902137210185624650854906780037204412206309949199080005576922775773722438863762117750429327585792093447423980002401200613302943834212820909269713876683465817369158585822294675056978970612202885426436071950214538262921077409076160417436699836138801162621314845608796870206834704116707763169847387223307828908570944984416973019427529790029089766264949078038669523465243837675263858062854739083634207

c1 =
974463908243330865728978769213595400782053398596897741316275722596415018912929508637393850919224969271766388710025195039896961956062895570062146947736340342927974992616678893372744261954172873490878805483241196345881721164078651156067119957816422768524442025688079462656755605982104174001635345874022133045402344010045961111720151990412034477755851802769069309069018738541854130183692204758761427121279982002993939745343695671900015296790637464880337375511536424796890996526681200633086841036320395847725935744757993013352804650575068136129295591306569213300156333650910795946800820067494143364885842896291126137320

n2 =
20918819960648891349438263046954902210959146407860980742165930253781318759285692492511475263234242002509419079545644051755251311392635763412553499744506421566074721268822337321637265942226790343839856182100575539845358877493718334237585821263388181126545189723429262149630651289446553402190531135520836104217160268349688525168375213462570213612845898989694324269410202496871688649978370284661017399056903931840656757330859626183773396574056413017367606446540199973155630466239453637232936904063706551160650295031273385619470740593510267285957905801566362502262757750629162937373721291789527659531499435235261620309759

c2 =
15819636201971185538694880505120469332582151856714070824521803121848292387556864177196229718923770810072104155432038682511434979353089791861087415144087855679134383396897817458726543883093567600325204596156649305930352575274039425470836355002691145864435755333821133969266951545158052745938252574301327696822347115053614052423028835532509220641378760800693351542633860702225772638930501021571415907348128269681224178300248272689705308911282208685459668200507057183420662959113956077584781737983254788703048275698921427029884282557468334399677849962342196140864403989162117738206246183665814938783122909930082802031855

n3 =
25033254625906757272369609119214202033162128625171246436639570615263949157363273213121556825878737923265290579551873824374870957467163989542063489416636713654642486717219231225074115269684119428086352535471683359486248203644461465935500517901513233739152882943010177276545128308412934555830087776128355125932914846459470221102007666912211992310538890654396487111705385730502843589727289829692152177134753098649781412247065660637826282055169991824099110916576856188876975621376606634258927784025787142263367152947108720757222446686415627479703666031871635656314282727051189190889008763055811680040315277078928068816491

c3 =
4185308529416874005831230781014092407198451385955677399668501833902623478395669279404883990725184332709152443372583701076198786635291739356770857286702107156730020004358955622511061410661058982622055199736820808203841446796305284394651714430918690389486920560834672316158146453183789412140939029029324756035358081754426645160033262924330248675216108270980157049705488620263485129480952814764002865280019185127662449318324279383277766416258142275143923532168798413011028271543085249029048997452212503111742302302065401051458066585395360468447460658672952851643547193822775218387853623453638025492389122204507555908862

n4 =
21206968097314131007183427944486801953583151151443627943113736996776787181111063957960698092696800555044199156765677935373149598221184792286812213294617749834607696302116136745662816658117055427803315230042700695125718401646810484873064775005221089174056824724922160855810527236751389605017579545235876864998419873065217294820244730785120525126565815560229001887622837549118168081685183371092395128598125004730268910276024806808565802081366898904032509920453785997056150497645234925528883879419642189109649009132381586673390027614766605038951015853086721168018787523459264932165046816881682774229243688581614306480751

c4 =
4521038011044758441891128468467233088493885750850588985708519911154778090597136126150289041893454126674468141393472662337350361712212694867311622970440707727941113263832357173141775855227973742571088974593476302084111770625764222838366277559560887042948859892138551472680654517814916609279748365580610712259856677740518477086531592233107175470068291903607505799432931989663707477017904611426213770238397005743730386080031955694158466558475599751940245039167629126576784024482348452868313417471542956778285567779435940267140679906686531862467627238401003459101637191297209422470388121802536569761414457618258343550613

n5 =
22822039733049388110936778173014765663663303811791283234361230649775805923902173438553927805407463106104699773994158375704033093471761387799852168337898526980521753614307899669015931387819927421875316304591521901592823814417756447695701045846773508629371397013053684553042185725059996791532391626429712416994990889693732805181947970071429309599614973772736556299404246424791660679253884940021728846906344198854779191951739719342908761330661910477119933428550774242910420952496929605686154799487839923424336353747442153571678064520763149793294360787821751703543288696726923909670396821551053048035619499706391118145067

c5 =
15406498580761780108625891878008526815145372096234083936681442225155097299264808624358826686906535594853622687379268969468433072388149786607395396424104318820879443743112358706546753935215756078345959375299650718555759698887852318017597503074317356745122514481807843745626429797861463012940172797612589031686718185390345389295851075279278516147076602270178540690147808314172798987497259330037810328523464851895621851859027823681655934104713689539848047163088666896473665500158179046196538210778897730209572708430067658411755959866033531700460551556380993982706171848970460224304996455600503982223448904878212849412357

n6 =
21574139855341432908474064784318462018475296809327285532337706940126942575349507668289214078026102682252713757703081553093108823214063791518482289846780197329821139507974763780260290309600884920811959842925540583967085670848765317877441480914852329276375776405689784571404635852204097622600656222714808541872252335877037561388406257181715278766652824786376262249274960467193961956690974853679795249158751078422296580367506219719738762159965958877806187461070689071290948181949561254144310776943334859775121650186245846031720507944987838489723127897223416802436021278671237227993686791944711422345000479751187704426369

c6 =
20366856150710305124583065375297661819795242238376485264951185336996083744604593418983336285185491197426018595031444652123288461491879021096028203694136683203441692987069563513026001861435722117985559909692670907347563594578265880806540396777223906955491026286843168637367593400342814725694366078337030937104035993569672959361347287894143027186846856772983058328919716702982222142848848117768499996617588305301483085428547267337070998767412540225911508196842253134355901263861121500650240296746702967594224401650220168780537141654489215019142122284308116284129004257364769474080721001708734051264841350424152506027932

n7 =
25360227412666612490102161131174584819240931803196448481224305250583841439581008528535930814167338381983764991296575637231916547647970573758269411168219302370541684789125112505021148506809643081950237623703181025696585998044695691322012183660424636496897073045557400768745943787342548267386564625462143150176113656264450210023925571945961405709276631990731602198104287528528055650050486159837612279600415259486306154947514005408907590083747758953115486124865486720633820559135063440942528031402951958557630833503775112010715604278114325528993771081233535247118481765852273252404963430792898948219539473312462979849137

c7 =
19892772524651452341027595619482734356243435671592398172680379981502759695784087900669089919987705675899945658648623800090272599154590123082189645021800958076861518397325439521139995652026377132368232502108620033400051346127757698623886142621793423225749240286511666556091787851683978017506983310073524398287279737680091787333547538239920607761080988243639547570818363788673249582783015475682109984715293163137324439862838574460108793714172603672477766831356411304446881998674779501188163600664488032943639694828698984739492200699684462748922883550002652913518229322945040819064133350314536378694523704793396169065179

n8 =
22726855244632356029159691753451822163331519237547639938779517751496498713174588935566576167329576494790219360727877166074136496129927296296996970048082870488804456564986667129388136556137013346228118981936899510687589585286517151323048293150257036847475424044378109168179412287889340596394755257704938006162677656581509375471102546261355748251869048003600520034656264521931808651038524134185732929570384705918563982065684145766427962502261522481994191989820110575981906998431553107525542001187655703534683231777988419268338249547641335718393312295800044734534761692799403469497954062897856299031257454735945867491191

c8 =
6040119795175856407541082360023532204614723858688636724822712717572759793960246341800308149739809871234313049629732934797569781053000686185666374833978403290525072598774001731350244744590772795701065129561898116576499984185920661271123665356132719193665474235596884239108030605882777868856122378222681140570519180321286976947154042272622411303981011302586225630859892731724640574658125478287115198406253847367979883768000812605395482952698689604477719478947595442185921480652637868335673233200662100621025061500895729605305665864693122952557361871523165300206070325660353095592778037767395360329231331322823610060006

n9 =
23297333791443053297363000786835336095252290818461950054542658327484507406594632785712767459958917943095522594228205423428207345128899745800927319147257669773812669542782839237744305180098276578841929496345963997512244219376701787616046235397139381894837435562662591060768476997333538748065294033141610502252325292801816812268934171361934399951548627267791401089703937389012586581080223313060159456238857080740699528666411303029934807011214953984169785844714159627792016926490955282697877141614638806397689306795328344778478692084754216753425842557818899467945102646776342655167655384224860504086083147841252232760941

c9 =
5418120301208378713115889465579964257871814114515046096090960159737859076829258516920361577853903925954198406843757303687557848302302200229295916902430205737843601806700738234756698575708612424928480440868739120075888681672062206529156566421276611107802917418993625029690627196813830326369874249777619239603300605876865967515719079797115910578653562787899019310139945904958024882417833736304894765433489476234575356755275147256577387022873348906900149634940747104513850154118106991137072643308620284663108283052245750945228995387803432128842152251549292698947407663643895853432650029352092018372834457054271102816934

n10 =
28873667904715682722987234293493200306976947898711255064125115933666968678742598858722431426218914462903521596341771131695619382266194233561677824357379805303885993804266436810606263022097900266975250431575654686915049693091467864820512767070713267708993899899011156106766178906700336111712803362113039613548672937053397875663144794018087017731949087794894903737682383916173267421403408140967713071026001874733487295007501068871044649170615709891451856792232315526696220161842742664778581287321318748202431466508948902745314372299799561625186955234673012098210919745879882268512656931714326782335211089576897310591491

c10 =
9919880463786836684987957979091527477471444996392375244075527841865509160181666543016317634963512437510324198702416322841377489417029572388474450075801462996825244657530286107428186354172836716502817609070590929769261932324275353289939302536440310628698349244872064005700644520223727670950787924296004296883032978941200883362653993351638545860207179022472492671256630427228461852668118035317021428675954874947015197745916918197725121122236369382741533983023462255913924692806249387449016629865823316402366017657844166919846683497851842388058283856219900535567427103603869955066193425501385255322097901531402103883869

n11 =
22324685947539653722499932469409607533065419157347813961958075689047690465266404384199483683908594787312445528159635527833904475801890381455653807265501217328757871352731293000303438205315816792663917579066674842307743845261771032363928568844669895768092515658328756229245837025261744260614860746997931503548788509983868038349720225305730985576293675269073709022350700836510054067641753713212999954307022524495885583361707378513742162566339010134354907863733205921845038918224463903789841881400814074587261720283879760122070901466517118265422863420376921536734845502100251460872499122236686832189549698020737176683019

c11 =
1491527050203294989882829248560395184804977277747126143103957219164624187528441047837351263580440686474767380464005540264627910126483129930668344095814547592115061057843470131498075060420395111008619027199037019925701236660166563068245683975787762804359520164701691690916482591026138582705558246869496162759780878437137960823000043988227303003876410503121370163303711603359430764539337597866862508451528158285103251810058741879687875218384160282506172706613359477657215420734816049393339593755489218588796607060261897905233453268671411610631047340459487937479511933450369462213795738933019001471803157607791738538467

n12 =
27646746423759020111007828653264027999257847645666129907789026054594393648800236117046769112762641778865620892443423100189619327585811384883515424918752749559627553637785037359639801125213256163008431942593727931931898199727552768626775618479833029101249692573716030706695702510982283555740851047022672485743432464647772882314215176114732257497240284164016914018689044557218920300262234652840632406067273375269301008409860193180822366735877288205783314326102263756503786736122321348320031950012144905869556204017430593656052867939493633163499580242224763404338807022510136217187779084917996171602737036564991036724299

c12 =
21991524128957260536043771284854920393105808126700128222125856775506885721971193109361315961129190814674647136464887087893990660894961612838205086401018885457667488911898654270235561980111174603323721280911197488286585269356849579263043456316319476495888696219344219866516861187654180509247881251251278919346267129904739277386289240394384575124331135655943513831009934023397457082184699737734388823763306805326430395849935770213817533387235486307008892410920611669932693018165569417445885810825749609388627231235840912644654685819620931663346297596334834498661789016450371769203650109994771872404185770230172934013971

n13 =
20545487405816928731738988374475012686827933709789784391855706835136270270933401203019329136937650878386117187776530639342572123237188053978622697282521473917978282830432161153221216194169879669541998840691383025487220850872075436064308499924958517979727954402965612196081404341651517326364041519250125036424822634354268773895465698920883439222996581226358595873993976604699830613932320720554130011671297944433515047180565484495191003887599891289037982010216357831078328159028953222056918189365840711588671093333013117454034313622855082795813122338562446223041211192277089225078324682108033843023903550172891959673551

c13=
14227439188191029461250476692790539654619199888487319429114414557975376308688908028140817157205579804059783807641305577385724758530138514972962209062230576107406142402603484375626077345190883094097636019771377866339531511965136650567412363889183159616188449263752475328663245311059988337996047359263288837436305588848044572937759424466586870280512424336807064729894515840552404756879590698797046333336445465120445087587621743906624279621779634772378802959109714400516183718323267273824736540168545946444437586299214110424738159957388350785999348535171553569373088251552712391288365295267665691357719616011613628772175

n14 =
27359727711584277234897157724055852794019216845229798938655814269460046384353568138598567755392559653460949444557879120040796798142218939251844762461270251672399546774067275348291003962551964648742053215424620256999345448398805278592777049668281558312871773979931343097806878701114056030041506690476954254006592555275342579529625231194321357904668512121539514880704046969974898412095675082585315458267591016734924646294357666924293908418345508902112711075232047998775303603175363964055048589769318562104883659754974955561725694779754279606726358588862479198815999276839234952142017210593887371950645418417355912567987

c14 =
3788529784248255027081674540877016372807848222776887920453488878247137930578296797437647922494510483767651150492933356093288965943741570268943861987024276610712717409139946409513963043114463933146088430004237747163422802959250296602570649363016151581364006795894226599584708072582696996740518887606785460775851029814280359385763091078902301957226484620428513604630585131511167015763190591225884202772840456563643159507805711004113901417503751181050823638207803533111429510911616160851391754754434764819568054850823810901159821297849790005646102129354035735350124476838786661542089045509656910348676742844957008857457

n15 =
27545937603751737248785220891735796468973329738076209144079921449967292572349424539010502287564030116831261268197384650511043068738911429169730640135947800885987171539267214611907687570587001933829208655100828045651391618089603288456570334500533178695238407684702251252671579371018651675054368606282524673369983034682330578308769886456335818733827237294570476853673552685361689144261552895758266522393004116017849397346259119221063821663280935820440671825601452417487330105280889520007917979115568067161590058277418371493228631232457972494285014767469893647892888681433965857496916110704944758070268626897045014782837

c15 =
14069112970608895732417039977542732665796601893762401500878786871680645798754783315693511261740059725171342404186571066972546332813667711135661176659424619936101038903439144294886379322591635766682645179888058617577572409307484708171144488708410543462972008179994594087473935638026612679389759756811490524127195628741262871304427908481214992471182859308828778119005750928935764927967212343526503410515793717201360360437981322576798056276657140363332700714732224848346808963992302409037706094588964170239521193589470070839790404597252990818583717869140229811712295005710540476356743378906642267045723633874011649259842

n16 =
25746162075697911560263181791216433062574178572424600336856278176112733054431463253903433128232709054141607100891177804285813783247735063753406524678030561284491481221681954564804141454666928657549670266775659862814924386584148785453647316864935942772919140563506305666207816897601862713092809234429096584753263707828899780979223118181009293655563146526792388913462557306433664296966331469906428665127438829399703002867800269947855869262036714256550075520193125987011945192273531732276641728008406855871598678936585324782438668746810516660152018244253008092470066555687277138937298747951929576231036251316270602513451

c16 =
17344284860275489477491525819922855326792275128719709401292545608122859829827462088390044612234967551682879954301458425842831995513832410355328065562098763660326163262033200347338773439095709944202252494552172589503915965931524326523663289777583152664722241920800537867331030623906674081852296232306336271542832728410803631170229642717524942332390842467035143631504401140727083270732464237443915263865880580308776111219718961746378842924644142127243573824972533819479079381023103585862099063382129757560124074676150622288706094110075567706403442920696472627797607697962873026112240527498308535903232663939028587036724

n17 =
23288486934117120315036919418588136227028485494137930196323715336208849327833965693894670567217971727921243839129969128783853015760155446770590696037582684845937132790047363216362087277861336964760890214059732779383020349204803205725870225429985939570141508220041286857810048164696707018663758416807708910671477407366098883430811861933014973409390179948577712579749352299440310543689035651465399867908428885541237776143404376333442949397063249223702355051571790555151203866821867908531733788784978667478707672984539512431549558672467752712004519300318999208102076732501412589104904734983789895358753664077486894529499

c17 =
10738254418114076548071448844964046468141621740603214384986354189105236977071001429271560636428075970459890958274941762528116445171161040040833357876134689749846940052619392750394683504816081193432350669452446113285638982551762586656329109007214019944975816434827768882704630460001209452239162896576191876324662333153835533956600295255158377025198426950944040643235430211011063586032467724329735785947372051759042138171054165854842472990583800899984893232549092766400510300083585513014171220423103452292891496141806956300396540682381668367564569427813092064053993103537635994311143010708814851867239706492577203899024

n18 =
19591441383958529435598729113936346657001352578357909347657257239777540424811749817783061233235817916560689138344041497732749011519736303038986277394036718790971374656832741054547056417771501234494768509780369075443550907847298246275717420562375114406055733620258777905222169702036494045086017381084272496162770259955811174440490126514747876661317750649488774992348005044389081101686016446219264069971370646319546429782904810063020324704138495608761532563310699753322444871060383693044481932265801505819646998535192083036872551683405766123968487907648980900712118052346174533513978009131757167547595857552370586353973

c18 =
3834917098887202931981968704659119341624432294759361919553937551053499607440333234018189141970246302299385742548278589896033282894981200353270637127213483172182529890495903425649116755901631101665876301799865612717750360089085179142750664603454193642053016384714515855868368723508922271767190285521137785688075622832924829248362774476456232826885801046969384519549385428259591566716890844604696258783639390854153039329480726205147199247183621535172450825979047132495439603840806501254997167051142427157381799890725323765558803808030109468048682252028720241357478614704610089120810367192414352034177484688502364022887

n19 =
19254242571588430171308191757871261075358521158624745702744057556054652332495961196795369630484782930292003238730267396462491733557715379956969694238267908985251699834707734400775311452868924330866502429576951934279223234676654749272932769107390976321208605516299532560054081301829440688796904635446986081691156842271268059970762004259219036753174909942343204432795076377432107630203621754552804124408792358220071862369443201584155711893388877350138023238624566616551246804054720492816226651467017802504094070614892556444425915920269485861799532473383304622064493223627552558344088839860178294589481899206318863310603

c19 =
6790553533991297205804561991225493105312398825187682250780197510784765226429663284220400480563039341938599783346724051076211265663468643826430109013245014035811178295081939958687087477312867720289964506097819762095244479129359998867671811819738196687884696680463458661374310994610760009474264115750204920875527434486437536623589684519411519100170291423367424938566820315486507444202022408003879118465761273916755290898112991525546114191064022991329724370064632569903856189236177894007766690782630247443895358893983735822824243487181851098787271270256780891094405121947631088729917398317652320497765101790132679171889

n20 =
26809700251171279102974962949184411136459372267620535198421449833298448092580497485301953796619185339316064387798092220298630428207556482805739803420279056191194360049651767412572609187680508073074653291350998253938793269214230457117194434853888765303403385824786231859450351212449404870776320297419712486574804794325602760347306432927281716160368830187944940128907971027838510079519466846176106565164730963988892400240063089397720414921398936399927948235195085202171264728816184532651138221862240969655185596628285814057082448321749567943946273776184657698104465062749244327092588237927996419620170254423837876806659

c20 =
386213556608434013769864727123879412041991271528990528548507451210692618986652870424632219424601677524265011043146748309774067894985069288067952546139416819404039688454756044862784630882833496090822568580572859029800646671301748901528132153712913301179254879877441322285914544974519727307311002330350534857867516466612474769753577858660075830592891403551867246057397839688329172530177187042229028685862036140779065771061933528137423019407311473581832405899089709251747002788032002094495379614686544672969073249309703482556386024622814731015767810042969813752548617464974915714425595351940266077021672409858645427346

for i in range(1,21):

for j in range(i+1,21):

ni=eval(\"n\"+str(i))

nj=eval(\"n\"+str(j))

p=gcd(ni,nj)

if p\>1:

c=eval(\"c\"+str(i))

q=ni//p

d=invert(e,(p-1)\*(q-1))

flag=long_to_bytes(pow(c,d,ni))

print(flag)

12. **RSAwiener攻击**

当e很大基本上就是wiener攻击就可以解出d

0.  注意：一定要将该py文件放在与github下载的文件的相同文件夹内，如下图，图中RSA维纳攻击.txt为我所编写的python脚本，将文件名后缀改为.py即可。

下载工具链接 https://github.com/pablocelayes/rsa-wiener-attack

例题

from Crypto.Util.number import \*

from gmpy2 import \*

from RSAwienerHacker import \*

import libnum

n=
639662333905190724963174274393118134850652056724765488685973275138948202602626008285649108873241886836533441901790252560580886492518792249844707754890068885294414947775869189660933854702732140888525369256213185908742658834741758334492843871934294115437721034834635565406377520933839418094457376057043593848401

e=
548564175098067125961375319851171259385596271876637657761522885808657855394647972481844447376596437557651275057610120865395646169671221375251081541213042646978655686531005856899936162320404991331623237305862913250487293880446994470841390688087392282045130633013139311548859962245908782253213294049851175315059

c=
266367266471585923035346980467315672043839080179258966276144775106482166900911004389808367589961536843898187180012055918063504477273067284037318171833017082239907978935274619109926579983150571298634653886980563681026116724117473808890951091279814434050754571460308728024448607359710055618866766919226511213734

d=hack_RSA(e,n)

flag=long_to_bytes(pow(c,d,n))

print(flag)

0.  **知道phi和n求p,q**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image109.png){width="5.760416666666667in"
height="1.6516951006124234in"}

p+q=n+1-phi

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image110.png){width="2.7777777777777777in"
height="4.803675634295713in"}

**知道n,e,d求q,p**

原理图

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Crypto/media/image111.png){width="5.760416666666667in"
height="2.887204724409449in"}

def getpq(n,e,d):

while True:

k = e \* d - 1

g = random.randint(0, n)

while k%2==0:

k=k//2

x=gmpy2.powmod(g,k,n)

y=gmpy2.gcd(x-1,n)

if y\>1 and x!=0:

return gmpy2.gcd(x,n)

print(getpq(n,e,d))
