**windows java搭建篇**

工具：

maven 3.6.1

idea 2020.2.4

jdk-14.0.2

![截图.png](    Java语言/media/image1.png){width="5.760416666666667in"
height="0.8142541557305337in"}

idea安装

就这个要注意

![截图.png](    Java语言/media/image2.png){width="5.305555555555555in"
height="4.148548775153106in"}

然后激活idea,选择代码激活

![截图.png](    Java语言/media/image3.png){width="5.760416666666667in"
height="3.46496719160105in"}

idea激活码经常更新：<https://www.yuque.com/yueryi/oldfish/bqrfq3?>

然后打开这个链接复制里面的代码进去就可以了

![截图.png](    Java语言/media/image4.png){width="5.760416666666667in"
height="4.479005905511811in"}

![截图.png](    Java语言/media/image5.png){width="5.760416666666667in"
height="3.457684820647419in"}

激活成功

![截图.png](    Java语言/media/image6.png){width="5.760416666666667in"
height="4.115788495188101in"}

（如果这个激活方面有问题可以看这个

![截图.png](    Java语言/media/image7.png){width="5.760416666666667in"
height="1.3659426946631672in"}

）

jdk的安装配置

.exe的安装没什么要详写的

环境变量配置

控制面板---系统和安全---系统---高级系统设置---环境变量

![截图.png](    Java语言/media/image8.png){width="5.760416666666667in"
height="6.3634930008748904in"}

新建系统变量JAVA_HOME 和CLASSPATH

　　变量名：JAVA_HOME

　　变量值：C:\\Program Files\\Java\\jdk-14.0.2 #jdk的安装目录

![截图.png](    Java语言/media/image9.png){width="4.097222222222222in"
height="4.201477471566054in"}

　　变量名：CLASSPATH

　　变量值：.;%JAVA_HOME%\\lib\\dt.jar;%JAVA_HOME%\\lib\\tools.jar;

然后修改系统变量名的Path也就是添加

　变量值：%JAVA_HOME%\\bin;%JAVA_HOME%\\jre\\bin;

win7是用分;号做分割符

win10是可以直接添加

![截图.png](    Java语言/media/image10.png){width="4.069444444444445in"
height="4.121482939632546in"}

然后打开cmd输入java \--version

如图就成功了

![截图.png](    Java语言/media/image11.png){width="5.760416666666667in"
height="0.888847331583552in"}

maven配置

先将下载好的压缩包解压到你自定义的盘符，然后，开始配置环境变量同jdk配置步骤一致。

变量名为MAVEN_HOME

变量值为Maven的安装路径

![截图.png](    Java语言/media/image12.png){width="4.277777777777778in"
height="4.66288167104112in"}

 配置完成后，通过cmd输入mvn -version验证是否安装成功。

![截图.png](    Java语言/media/image13.png){width="4.208333333333333in"
height="4.666666666666667in"}

成功

![截图.png](    Java语言/media/image14.png){width="5.760416666666667in"
height="1.5637937445319334in"}

进入idea内校验并配置maven本地路径

File\--\>Settings\--\>Maven，直接搜maven 更改下图的几个路径。

打开idea配置

![截图.png](    Java语言/media/image15.png){width="5.760416666666667in"
height="2.9795264654418196in"}

接下来就默认就可以了

![截图.png](    Java语言/media/image16.png){width="5.760416666666667in"
height="3.107823709536308in"}

等他转完

![截图.png](    Java语言/media/image17.png){width="5.760416666666667in"
height="3.222813867016623in"}

搭建成功

![截图.png](    Java语言/media/image18.png){width="5.760416666666667in"
height="3.1415288713910763in"}

要配置java环境就看这个<https://product.pconline.com.cn/itbk/software/rjwt/1505/6483358.html>

高博老师的gitee <https://gitee.com/gaobo1>

基础知识：

![截图.png](    Java语言/media/image19.png){width="4.486111111111111in"
height="1.0096347331583553in"}

java需要用javac来编译.java后缀的文件得到.class文件

.java是预编译文件就像C语言中的.c文件

.class是编译文件

![截图.png](    Java语言/media/image20.png){width="5.760416666666667in"
height="3.2402351268591425in"}

使用kali2.o的java编译，2021以上都没有javac编译工具

![截图.png](    Java语言/media/image21.png){width="5.760416666666667in"
height="3.8481474190726157in"}

**原理篇**

jdk jre jvm 三者的关系

一、JDK(Java Development Kit)

JDK(Java Development
Kit)，即Java开发工具包，是一个编写Java应用程序的开发环境，是java的**核心**所在。

bin里面的都是开发文件javac之类的

二、JRE(Java Runtime Environment)

JRE(Java Runtime
Environment)，即Java运行环境，支持Java程序运行的标准环境，包含JVM标准实现及Java核心类库

bin里面是java可以运行java但是没有javac不能编译开发

三、JVM(Java Virtual Machine)

JVM(Java Virtual
Machine)，即[Java虚拟机](https://so.csdn.net/so/search?q=Java%E8%99%9A%E6%8B%9F%E6%9C%BA&spm=1001.2101.3001.7020)，运行在操作系统之上，存在于内存中，与内存打交道，与硬件没有直接交互，**是Java语言实现跨平台的核心。**

JV**M是Java程序跨平台的关键部分，只要为不同平台实现了相应的虚拟机，编译后的Java字节码就可以在该平台上运行**

**基础语言学习**

**效果图：**

![截图.png](    Java语言/media/image22.png){width="3.9444444444444446in"
height="1.1582895888013998in"}

```java
//要先定义类才能写方法

//如果是public class 那么类名字要和文件名字一样才能编译

//字节码文件不是一个文件一个，是一个类有一个

//每个类都存在方法

public class HelloWorld {   //这个类是public必须是和文件名一样

    public static void main(String[] args) { //方法

        System.out.println("Hello"); //类似printf输出文字

    }

}

class HelloWorld2{ //这个类可以任意名字

public static void main(String[] args){

        int s = 10; //赋值10给s的局部变量，就和shell中:s=10是一样的

        System.out.println(s);//使用打印s变量的值

        System.out.print("1234")

 //print默认是不换行的，println是换行的

    }

}

//后面接对应的是简化命令或描述

public class Hello {

    public static final String ADDRESS = "长沙"; //给常量赋值

    public static int i = 100;//给类变量（静态变量）赋值

    public static void main(String[] args) { //main

        System.out.println(ADDRESS+"i");//常量只能在最前面才能使用    

        for (int i = 0; i <5; i++) { //fori

            System.out.println(10); //10.sout

        }

    }

}
```

![截图.png](    Java语言/media/image23.png){width="5.760416666666667in"
height="3.1454910323709537in"}

java中的注释

// 行注释

\*/ xxx /\* 块注释

/\*\* xxx \*/ 文档注释

javac 默认是GBK，而win是utf-8所以如果java里面有中文就要用：java
\--encoding utf-8 xxx.java

给不认识的java未编译文件生成帮助手册：

javadoc -d myHello -author -version -encoding UTF-8 charset UTF-8
xxx.java

**-d 创建目录**

**-author 显示作者**

**-encoding UTF-8 -charset UTF-8 字符集修改为UTF-8**

![截图.png](    Java语言/media/image24.png){width="5.760416666666667in"
height="2.0278105861767277in"}

字符常量分类：

字符串常量：由\"\"括起来的

整型常量：程序中直接写数字，没有小数点

浮点数常量：程序中写小树

字符常量：由\'\'括起来的

布尔常量:只有true和false

空常量:null

![截图.png](    Java语言/media/image25.png){width="5.760416666666667in"
height="2.5690299650043746in"}

Java所有关键字

Java中的关键字一共包含48个，分别是：abstract、assert、boolean、break、byte、case、catch、char、vlass、continue、default、do、double、else、enum、extends、final、finally、float、for、implements、import、int、interface、instanceof、long、native、new、package、private、protected、public、return、short、static、strictfp、super、switch、synchronized、this、throw、throws、transient、try、void、volatile、while

3、需遵循的规范：

(1)、包名：所有字母一律小写。如：com.abc.demo。

(2)、类名和接口名：每个单词的首字母大写，其余小写。如：StudentDemo,HelloWorld。

(3)、常量名：所有字母都大写，单词间以下划线(\_)连接。如：DAY_OF_MONTH。

(4)、变量名和方法名：第一个单词首字母小写，从第二个单词开始每个单词首字母大写。即驼峰式命名法。如：chineseScore,getTotalMoney()。

(5)、在程序中，应尽量使用有意义的英文单词来定义标识符，即见名知义，这样便于阅读。如：password表示密码，name表示姓名等。

附上java关键字表

**if语句**
```java 
/**

 * if语句的三种语法

 * */

//if实现商品付款

import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("输入裤兜里的所有钱：");

        int coin = sc.nextInt();

        if (coin >= 600){

            System.out.println("付款成功");

        }else{

            System.out.println("付款失败");

        }

    }

}
```

```java
//if实现电影院100个座位奇数做左边偶数坐右边

class cinema {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("请输入你的座位号：");

        int number = sc.nextInt();

        if (number < 100 ) {

            if (number % 2 == 1) {

                System.out.println("请坐左边");

            } else {

                System.out.println("请做右边");

            }

        }else{

            System.out.println("座位号不对，请离开");

        }

    }

}

// if语句实现考试成绩的结果分配奖励

class examin {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("输入你的分数：");

        int result = sc.nextInt();

        if (result >-1 && result <101) {

            if (result >= 95 && result <= 100) {

                System.out.println("奖励单车");

            } else {

                if (result >= 90 && result <= 94) {

                    System.out.println("去游乐场玩");

                } else {

                    if (result >= 80 && result <= 89) {

                        System.out.println("买大黄蜂");

                    } else {

                        if (result <= 80) {

                            System.out.println("来找你谈谈理想");

                        }

                    }

                }

            }

        }else{

            System.out.println("成绩输入出错，重新运行JAVA脚本");

        }

    }

}
```

**Scanner类**

```java
//Scanner类实现键盘录入整数

import java.util.Scanner;

public class Hello {

    public static void main(String[] args){

        int k=10;

        double a=k;

        // 隐性数据类型转换，取值范围小转大

        double s= 10.0;

        int b = (int)k;

        //强制转换，取值范围大转小

        //创建对象

        Scanner sc = new Scanner(System.in);

        //接收数据

        //变量i记录了键盘录入的数据

        System.out.println("这是一个加法运算的计算器");

        System.out.println("请输入第一次整数:");

        int  i = sc.nextInt();

        System.out.println("请输入第二次整数:");

         //变量k记录了键盘录入的数据

        int  k = sc.nextInt();

        System.out.println(i+k);

        //进行加法运算，并输出

    }

// Scanner录入字符

    class Name{

        public static void main(String[] args)    {                    

        System.out.println("输入字符")

        int s = sc.nextLine();       

        System.out.println(s);

        // 打印s的值字符

        }

    }

}
```

```java
//switch实现多个选项

class He {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.println("想吃什么面");

        String face = sc.nextLine();

        switch(face){

            case "兰州拉面":

                System.out.println("吃兰州拉面");

                break;

            case "三鲜粉":

                System.out.println("吃三鲜粉");

                break;

            case "北京炸酱面":

                System.out.println("吃北京炸酱面");

                break;

            case "武汉热干面":

                System.out.println("吃武汉热干面");

                 break;

            default:

                System.out.println("想屁吃，吃泡面");

                break;

        }

    }

}
```

![截图.png](    Java语言/media/image26.png){width="5.760416666666667in"
height="1.5250120297462817in"}

**for循环**

```java
// 循环1~5并且相加

class She {

    public static int k=0;

    //定义变量用来进行累加

    public static void main(String[] args) {

        for(int i=1;i<=5;i++){

            k += i;

            // 开始逐渐累加到k

        }

        System.out.println(k);

    }

}

//判断1~100的偶数的和

class Xinag {

    public static void main(String[] args) {

        int a= 0;

        for (int i=0;i<=100;i++){

            if (i % 2 ==0){

                a = a+i;

            }

        }

        System.out.println(a);

    }

}

// 键盘录入两个数字表示一个范围

//既能被三整除又能被5整除

class keing {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("输入第一个数字");

        int number1 = sc.nextInt();

        System.out.println("输入第二个数字");

        int number2 = sc.nextInt();

        int count = 0;

        // 定义变量

        for (int i=number1;i<=number2;i++){

            if (i % 3 ==0&& i % 5 ==0){

                count++;

                //统计for里面的if执行成功了多少次，然后让上面定义的变量自增就可以统计执行的次数了。

            }

        }

        System.out.println(count);

    }

}
```

**witch循环**

// while

```java
class Qex {

    public static void main(String[] args) {

        int s = 1;

        while (s < 10) {

            System.out.println("ls");

            s++;

        }

    }

}
```

// 回文数：如果是回文树就打印true，反过来就是false

// int ge = x % 10 ; //获得个位

//先把值定义再方法里然后再局部调用更改，还是可以再另一个局部调用（一个变量是在当前的大括号里面实用）

```java
class Eshan {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("输入整数：");

        int number100 = sc.nextInt();

        int tmp = number100;

        int k = 0;

        while (number100 != 0) {

            int get = number100 % 10;

            //获取number100的个位

            number100 = number100 / 10;

           //把输入的数字除10就一定小于0就能再执行一次while循环

            k = k * 10 + get;

            //将获取的数字拼接到最右边

        }System.out.println(k);

        if (tmp==k){

            System.out.println("True");

        }else{

            System.out.println("False");

        }

    }

}
```