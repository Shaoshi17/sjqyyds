**一天速成Excel**

![stickPicture.png](    Word_Excel/media/image1.png){width="5.760416666666667in"
height="4.693406605424322in"}

![stickPicture.png](    Word_Excel/media/image2.png){width="5.760416666666667in"
height="4.185471347331584in"}

![stickPicture.png](    Word_Excel/media/image3.png){width="5.760416666666667in"
height="3.2215660542432194in"}

![stickPicture.png](    Word_Excel/media/image4.png){width="5.760416666666667in"
height="3.8006878827646546in"}

![stickPicture.png](    Word_Excel/media/image5.png){width="5.760416666666667in"
height="5.201388888888889in"}

快捷键操作

函数公式

数据透视表

VBA

排版

**一、快捷键操作**

选择该列数据：Ctrl+Shift+上下/左右可以选择多列。

跳至表格最上或最下左右的话效果就是隔一个格子跳：Ctrl+上下，Ctrl+左右。

复制粘贴：Ctrl+C/V,复制/粘贴，Ctrl+Shift+V就是粘贴只粘贴值，也可以右键选择粘贴什么

设置单元格格式：

ctrl+shift+\~ 常规

ctrl+shift+1 数值

ctrl+shift+2 时间

ctrl+shift+3 日期

ctrl+shift+4 货币符号

ctrl+shift+5 百分比

ctrl+shift+6 科学计算

ctrl+shift+7 边框

查找替换：Ctrl+F查找，Ctrl+H替换

F4，重复上一个步骤，比如插入行，设置格式，等频繁操作

快速填充:取代大部分简单规律的分列、抽取、合并的工作。

**两列或列比较差异**

选择列或者行，Ctrl+G选择下面两个

![截图.png](    Word_Excel/media/image6.png){width="5.760416666666667in"
height="2.849349300087489in"}

**二、函数**

**1 公式if/countif/sumif/countifs/sumifs**

if、countif、sumif、countifs、sumifs，这几个一起学，用于条件计数、条件求和

**统计数字**

COUNT函数给定数据集合或者单元格区域中数据的个数进行计数，***COUNT函数只能对数字数据进行统计，对于空单元格、逻辑值或者文本数据将不统计。***

**案例**

![stickPicture.png](    Word_Excel/media/image7.png){width="5.760416666666667in"
height="4.331407480314961in"}

**统计非空单元格**

COUNTA函数是计算区域内非空单元格的个数。

**案例**

![stickPicture.png](    Word_Excel/media/image8.png){width="5.760416666666667in"
height="4.230715223097113in"}

**统计空白单元格**

COUNTBLANK函数是计算区域内空白单元格的个数。

**案例**

![stickPicture.png](    Word_Excel/media/image9.png){width="5.760416666666667in"
height="4.187010061242344in"}

**重复显示指定内容**

REPT函数是按照给定的次数重复显示文本的函数。

语法：=rept(需要重复显示的文本,重复显示的次数)

![截图.png](    Word_Excel/media/image10.png){width="5.760416666666667in"
height="1.3784831583552055in"}

**文本连接**

文本连接符&，把几个内容连接起来，可以是数字、单元格引用、字符等

![stickPicture.png](    Word_Excel/media/image11.png){width="5.760416666666667in"
height="2.584187445319335in"}

**计算文本长度**

LEN函数是计算字符串长度的函数。

![stickPicture.png](    Word_Excel/media/image12.png){width="5.760416666666667in"
height="3.689330708661417in"}

**计算文本长度**

LEN函数是计算字符串长度的函数。

![stickPicture.png](    Word_Excel/media/image12.png){width="5.760416666666667in"
height="3.689330708661417in"}

**查找函数2**

Find函数是从文本字符串中查找特定的字符位置，***区分大小写***

语法：=FIND(要查找的字符串、被查找的字符串、\[开始位置\])

案例：查找天在文本中的位置，查找C在文本中的位置，find区分大小写，所以最后一个会错误

![stickPicture.png](    Word_Excel/media/image13.png){width="5.760416666666667in"
height="3.4615048118985126in"}

FindB函数是从文本字符串中查找特定的字节位置，***区分大小写***

语法：=findb(要查找的字节、被查找的字节、\[开始位置\])

***一个汉字算1个字符，2个字节；数字和英文字母算1个字符，1个字节***

**1) countif函数**

统计某个单元格区域中符合指定条件的单元格数目。Countif(range, criteria)

range是单元格区域，criteria是指定的条件表达式。

例子：COUNTIF(E2:E17,\"\>30000\")

销售额大于30000的有5个。

**2) countifs函数**

多个条件. countifs(条件区域1，条件1，条件区域2，条件2）

COUNTIFS(B2:B17,\"苏州\",D2:D17,\"\>100\")

苏州销量大于100的记录数

**3) sumif函数**

计算指定条件的单元格区域内数值和

Sumif(range,criteria,sum_range)

range是判断条件的单元格区域，criteria是指定的条件表达式。Sum_range是需要计算的数值所在的单元格区域。

SUMIF(A2:A17,\"2007/02/13\",E2:E17)

2007/2/13的销售总额

**4) if函数**

=if(条件，条件为真返回值，条件为假返回值）

IF(E2\>10000,\"优秀\",IF(E2\>5000,\"良好\",\"及格\"))

如果销量\>10000,那么表现优秀；5000\<销量≤10000，那么表现良好，销量≤5000，及格。

**4) sum函数**

Alt+=键快速求和。

SUM函数是一个求和函数，以将单个值、单元格引用或是区域相加，或者将三者的组合相加。

语法：SUM(number1,\[number2\],\...)

number1 （必需参数）要相加的第一个数字。
可以是具体数字，也可以是单元格引用或者单元格区域。

number2，这是要相加的第二个数字。

**直接砍掉小数点**

TRUNC函数是将数字的小数部分直接截去，返回整数，不讲究四舍五入。

语法：=TRUNC(number, \[num_digits\])

TRUNC 函数语法具有下列参数：

number必需。 需要截尾取整的数字。

\[num_digits\]可选。一般都不需要第二个参数。

案例：

=trunk(9.99)，返回值9

=trunk(4.12)，返回值4

=trunk(0.32)，返回值0

=trunk(-8.43)，返回值-8

**四舍五入小数点**

**ROUND**函数将数字四舍五入到指定的位数。

语法：=ROUND(number, num_digits)

number必需参数。 要四舍五入的数字。

num_digits必需参数。 要进行四舍五入运算的位数。

![截图.png](    Word_Excel/media/image14.png){width="5.760416666666667in"
height="3.3112401574803147in"}

**随机整数**

RANDBETWEEN函数是返回指定的最小值和指定最大值之间的一个随机整数。

语法：RANDBETWEEN（bottom,top）

Bottom参数： 指定的最小整数。

Top参数： 指定的最大整数。

![截图.png](    Word_Excel/media/image15.png){width="5.760416666666667in"
height="2.487055993000875in"}

**奇偶数判断**

ISODD函数是一个奇数判断函数，如果数字为奇数则返回TRUE

![stickPicture.png](    Word_Excel/media/image16.png){width="5.760416666666667in"
height="2.320492125984252in"}

ISEVEN函数是一个偶数判断函数，如果数字为偶数则返回TRUE

![stickPicture.png](    Word_Excel/media/image17.png){width="5.760416666666667in"
height="2.320492125984252in"}

**多条件求平均**

AVERAGEIFS函数是求多重条件所有单元格的平均值。使用方法可参考SUMIFS函数

语法：=averageifs(average_range,criteria_range1,criteria1,criteria_range2,criteria2,\...)

案例

![截图.png](    Word_Excel/media/image18.png){width="5.760416666666667in"
height="3.7372036307961505in"}

**2 公式max/min/large**

这几个公式可以用于简单的数据分析，不进行赘述，但往往会跟其他函数混合使用

**match函数**

[Excel匹配函数：Match函数的10种用法！可直接套用
(baidu.com)](https://baijiahao.baidu.com/s?id=1748710102793626157)

**3 vlookup函数**

查找匹配

在数据表的首列查找指定的数值，并由此返回数据表当前行中指定列的数值。

vlookup(lookup_value,table_array,col_index_num,range_lookup)

其中，lookup_value代表需要查找的数值，table_array代表需要查找的单元格区域，col_index_num是返回的匹配值的列序号，range_lookup是true/false的逻辑值，精确\--FALSE，不精确---TRUE

如下表所示，查找学籍号对应的姓名。

Vlookup(I2,\$A:\$G,2,FALSE)

![截图.png](    Word_Excel/media/image19.png){width="5.760416666666667in"
height="3.1193591426071743in"}

**2) vlookup函数代替if函数**

IF(E4\>10000,\"优秀\",IF(E4\>5000,\"良好\",\"及格\"))

VLOOKUP(E4,\$K\$1:\$L\$4,2,TRUE)

![stickPicture.png](    Word_Excel/media/image20.png){width="5.760416666666667in"
height="1.6636581364829397in"}

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**公式的结构**

下面表达式是一个简单的公式实例。

=(C2+D2)\*5

从公式结构来看，构成公式的元素通常包括等号，引用，常量，运算符等元素，其中等号是不可缺的。公式还可以使用数组，Excel函数或名称，来进行运算。

![截图.png](    Word_Excel/media/image21.png){width="5.760416666666667in"
height="1.6929472878390202in"}

最简单，最常用的公式

![截图.png](    Word_Excel/media/image22.png){width="5.760416666666667in"
height="3.3306955380577428in"}

公式中的运算符

![截图.png](    Word_Excel/media/image23.png){width="5.760416666666667in"
height="2.7283475503062116in"}

运算符的优先级

![截图.png](    Word_Excel/media/image24.png){width="5.760416666666667in"
height="2.0114074803149604in"}

**怎么只复制粘贴Excel表格中公式算出的值而不是使用的公式?**

使用Ctrl+C复制，然后使用Ctrl+Shift+V只粘贴值。

![截图.png](    Word_Excel/media/image25.png){width="5.760416666666667in"
height="4.644762685914261in"}

当然还可以粘贴其他东西。

![截图.png](    Word_Excel/media/image26.png){width="3.861111111111111in"
height="3.902740594925634in"}

**在单元格快速使用公式参数弹出设置窗口**

快捷弹出参数设置公式的窗口的方法，通过快捷键来快速弹出参数设置界面。

首先在单元格输入函数，并输入左括号，然后按下CTRL+A键，呼出参数设置窗口！

![ca8c37d31d5d50178c4ee97a61326a13.gif](    Word_Excel/media/image27.gif){width="5.760416666666667in"
height="3.544307742782152in"}
