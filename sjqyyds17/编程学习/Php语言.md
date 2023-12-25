# 7天理解掌握php基础

## day1

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

## day2
## day3
## day4
## day5
## day6
## day7





































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
