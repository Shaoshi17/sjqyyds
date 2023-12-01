**逆向工程基础**

**逆向工程基础概述**

一般，题目的形式都是：程序接收用户的输入，并在系统中一系列的校验算法，如果通过算法则成功，输入的就是flag。这些算法可能是已经成熟的算法比如凯撒或者亦或这种经典的算法，还有一些是作者自己思考的算法，所以做这个题目需要我们，有一定的算法能力，和思维能力，甚至猜测，联想能力。

**汇编语言的认识**

**寄存器，内存寻址**

寄存器是CPU的组成部分是有限储量的高速存储部件，用来缓存指令，数据和地址，一般的IA-32(intel
32-bit),即x86架构的处理器中包含以下的寄存器：

通用寄存器EAX,EBX,ECX,EDX,ESI,EDI。

栈顶指针寄存器ESP，栈底指针寄存器EBP.

指令计数器EIP

段寄存器：CS,DS,ES,FS,GS

对于16位的CPU,是将E全部去掉,FS,GS都还没有，因为不是主流就不多写16位的。

对于64位的CPU，则是将前缀E改成R，同时增加了R8～R这八个同用寄存器。

标志寄存器：

AF：辅助进位标志，运算在第三位进位的时候置1

PF：奇偶校验标志，当运算结果的二进制的有偶数个1时置1

SF：符号标志，有符号整形的符合位为1时置1,表示这是一个负数

ZF：零标志，运算结果为全为0时置1

OF：溢出标志，运算结果在有符号数里面溢出置时1

CF：进位标志，运算结果在无符号数里进位置时1

**X86/X64汇编语言**

CTF和平时最常见的就是X86/X64架构

基本格式：操作码 \[操作数1\],\[操作数2\]

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image1.png){width="5.760416666666667in"
height="2.959413823272091in"}

汇编语言跳转指令有很多，它们会根据标志位的情况进行跳转，在条件跳转前往往存在cmp比较指令，cmp只比较不进行修改。只会对标志位进行影响。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image2.png){width="5.760416666666667in"
height="2.5993886701662294in"}

**反汇编**

我们将机械码翻译回汇编代码的过程叫做反汇编。

在反汇编的过程中我们必须知道在机械码中那些是数据那些是指令或者那些是跳转的标签或者跳转表再或者常量的数据甚至有故意影响反汇编的干扰数据,所以我们如果是一条一条的解析解析下去肯定会出问题,我们需要知道正确的指令起始位置和要跳转的标签等来指引反汇编工具正确解析代码.

即使有些信息会反汇编丢失,但是我们仍然可以通过算法来还原出来程序的流程,下面介绍两种以知的算法:线性反汇编算法和递归下降反汇编算法.

线性反汇编算法:简单粗暴,从代码段的起始位置一直一个接一个解析指令,直至结束,缺点就是一旦有数据插入到代码中则后需的所有的反汇编的都是错的无用的

递归下降反汇编算法:则是从从线性反汇编算法留下的种种问题后创造的新算法,不在是简单的一一解析并显示,而是尝试推测出每条指令执行后程序将如何进行下去,例如普通指令执行后还是直接执行下一条,无条件跳转指令会立即跳转到目标位置,函数会调用指令临时跳出再返回继续执行,返回指令则会终止当前执行流程,条件指令跳转则可能分出两条路径,在不同的位置,引擎会将一些已知的模式匹配到起始位置再根据指令的执行模式逐个对程序执行情况进行跟踪最后将程序完全反汇编.

**调用规定**

人们为了连接各程序员写的函数不出错,为编辑器创立了规定各函数之间的参数传递的约定,称为调用约定

（1）x86 32位架构的调用约定

❖ \_\_cdecl： 参 数从 右 向左 依 次压 入 栈中 ， 调用 完 毕， 由 调用 者
负责 将 这些 压 入的 参 数清 理

掉，返回值置于EAX中。绝大多数x86平台的C语言程序都在使用这种约定。

❖ \_\_stdcall： 参 数同 样 从 右 向 左 依次 压入 栈 中 ， 调 用 完毕
，由 被 调 用 者 负 责 清 理压 入的 参

数，返回值同样置于EAX中。Windows的很多API都是用这种方式提供的。

❖ \_\_thiscall： 为 类方 法专 门优 化的 调用 约定 ，将 类方 法的 this指
针放 在ECX寄 存器 中， 然后

将其余参数压入栈中。

❖ \_\_fastcall： 为加速 调用而生的 调用 约定，将第 1个 参数放在 ECX中
，将 第2个 参数 放在EDX

中，然后将后续的参数从右至左压入栈中。

（2）x86 64位架构的调用约定

❖ Microsoft x64位（x 86-64 ）调用约定：在Windows上使用，依次
将前4个参数放入RDI、

RSI 、RDX、RCX 这4个寄存器，然后将剩下的参数从右至左压入栈中。

❖ SystemV x64 调用约定：在Linux 、MacOS上 使用，比Microsoft的版本多了两
个寄存器，

使用RDI、RSI、RDX、RCX
、R8、R9这6个寄存器传递前6个参数，剩下的从右至左压栈。

**局部变量**

在写程序的时候经常用到局部变量，局部变量有易失性，一旦程序返回就局部变量失效，考虑这个特性，人们把局部变量存放到栈上，每次函数被调用，程序从栈中分配一段空间，作为存储的的局部变量区域。

每个函数在被调用的 时候都会产生这样的局部 变量的区域、存储返回地 址的区
域和参数的区域 ,见图
程序一层层地深入调用函数,每个函数自己的区域就一层层地叠在栈上。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image3.png){width="5.194444444444445in"
height="7.1826990376202975in"}

人们把每个函数自己的一片区域叫帧，由于每帧的的都在栈上所以又叫栈帧，然而栈帧的位置不一定是固定的，而随着每次的调用的不同，栈帧的位置也会变化，那么怎么正确引导局部变量呢？

虽然 栈的内容随着进 栈和出栈 会一直不断变化 ，但是一 个函数中每个局
部变量 相对于该函数栈 帧的偏

移都 是固定的。 所以 可以引入一个 寄存 器来专门存 储当前 栈帧的位置 ，即
ebp， 称为 帧指针。程 序在

函 数初始化 阶段 赋值ebp为 栈帧中 间的 某个位置 ，这 样可以用 ebp引 用所
有的局部 变量 。由于上 一层

的 父函数 也要 使用ebp ，因 此要 在函数 开始 时先保 存 ebp， 再赋值ebp
为 自己 的栈帧 的值 ，这样 的流

程在汇编代码中便是经典的组合：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image4.png){width="5.760416666666667in"
height="0.4567169728783902in"}

现在 每个函数的 栈帧 便由局部变量 、父 栈帧的值、 返回地 址、参数四 部分
构成。可以看 出， ebp在 初

始化后实际上 指向的是父栈帧地址的存储位置。因此，\*
ebp形成了一个链表，代表一层 层的函数调用

链。

随着 编译技术的 发展 ，编译器也可 以通 过跟踪计算 每个指 令执行时栈 的位
置，从而直接 越过 ebp， 而

使 用栈指 针esp来 引用 局部 变量。 这样 可以节 省 每次保存 ebp时 需
要的时 间， 并增加 了一 个通用 寄存

器，从而提高了程序性能。

于 是现 在 有两 种 函数： 一 是有 帧指针的函数 ， 二是 经 过优化 后
没有帧指针的函数 。 现代 的 分析工 具

（ 如IDA Pro 等 ） 将 使 用高 级 的 栈 指针 跟 踪 方 法来 针 对 性 地处
理 这 两 种函 数 ， 从 而正确处理局部变量

**静态分析**

逆向中最基本的方法就是静态分析，工具以IDA为主

**IDA工具学习**

IDA是业界最成熟的反汇编工具，使用的是递归下降反汇编算法

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image5.png){width="5.760416666666667in"
height="3.2073239282589676in"}

**数据类型操作**

用户可以根据地址颜色来分辨某个位置的数据类型，被标注为代码的位置，其地址将会是黑色显示的，标注为数据的位置，为灰色的显示的，未定义数据类型位置标注为黄色

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image6.png){width="5.760416666666667in"
height="1.3536975065616799in"}

下面介绍一些定义数据的快捷键

U取消一个键已有的数据类型定义

D将某个位置变为数据

C将某个位置变为代码

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image7.png){width="5.760416666666667in"
height="0.6200448381452318in"}

**使用IDA Pro定位关键代码的方法：**

搜索特征字符串。具体操作为：

①快捷键Ctrl+S，打开搜索类型选择对话框--\>双击Strings，跳到字符串段--\>菜单项"Search--\>Text"；

②快捷键Alt+T，打开文本搜索对话框，在String文本框中输入要搜索的字符串点击OK即可；

**函数操作**

IDA有操作函数的方法：

删除函数：在函数窗口选中，按Delete键

定义函数：在反汇编窗口中选中后，按P键

修改函数：在函数窗口选中并按Ctrl+E组合键，或者在反汇编窗口按Alt+p组合键

这些定义修改有利于更加还原原始代码。

还有一些快捷键因为用的少，到时候在学和记。

对要进行反编译的函数点击，按F5即可获得反编译后的程序代码。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image8.png){width="5.760416666666667in"
height="3.120226377952756in"}

有的时候因为代码混淆等原因导致 IDA 无法建立函数：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image9.png){width="5.760416666666667in"
height="4.030181539807524in"}

当我们完成对函数识别的修复之后，我们可以在函数开头按下 [p]{.mark} 让 IDA
重新自动识别函数，或是框选属于该函数的汇编代码之后再按下 [p]{.mark} 让
IDA 重新自动识别函数：

**IDAPython**

在 IDA Pro 当中内置了一个 Python 及一个 IDC
模块，可以帮助我们快速地对二进制文件进行修改等工作。

我们可以通过 Alt+F7 或者 File → Script Command 直接编写运行 IDAPython
脚本按Shift+F2组合键，或选择"File→Script
command"菜单命令，可以打开脚本面板，将"Scripting
language"改为"Python"，即可获得一个简易的编辑器：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image10.png){width="5.527777777777778in"
height="3.733857174103237in"}

在使用之前需要先导入 ida 模块，比较常用的有以下 API：

idc.get_db_byte(addr) \# 返回 addr 处的 1 字节

idc.get_wide_word(addr) \# 返回 addr 处的 2 字节

idc.get_wide_dword(addr) \# 返回 addr 处的 4 字节

idc.get_qword(addr) \# 返回 addr 处的 8 字节

idc.get_bytes(addr, size, use_dbg) \# 返回 addr 处的 size 字节

idc.patch_byte(addr, value) \# 将 addr 处的 1 字节修改为 value（小端序）

idc.patch_word(addr, value) \# 将 addr 处的 2 字节修改为 value（小端序）

idc.patch_dword(addr, value) \# 将 addr 处的 4 字节修改为
value（小端序）

idc.patch_qword(addr, value) \# 将 addr 处的 8 字节修改为
value（小端序）

**IDA的其他功能**

IDA的菜单栏"View→Open subviews"下可以打开各种类型的窗口

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image11.png){width="5.760416666666667in"
height="4.010690069991251in"}

这些 窗口也有对应的快捷键调用出来

Ctrl+Shift+F12打开搜索框搜索关键字符

Ctrl+X 查看调用情况

a:数据转换为字符串

==n:更改变量名称==

==y:更改变量类型==

#### HexRays反编译器入门

HexRays作为IDA的插件运行，与IDA同为一家公司开发，与IDA有着紧密的联系。HexRays充分利用IDA确定的函数局部变量和数据类型，优化后生成类似C语言的伪代码。用户可以浏览生成的伪代码、添加注释、重命名其中的标识符，也可以修改变量类型、切换数据的显示格式等。

生成伪代码只需在反汇编窗口中定位到目标函数，按F5即可，插件运行完毕就会打开一个伪代码的窗口

当光标移动到标识符、关键字、常量上时，其他位置的相同内容也会被高亮，方便查看和操作。

很多常量没有以正确 的格式显示，如源代码中的0
x66变为十进制数102，\'a\'和\'A\'被转化为其ASCII编码对应的十进制数97和65,

十六进制显示就按H键,或者其他的各种数字的形式

将常量转换为'A'形式按R键

将常量转为枚举中的一个值，快捷键为M键。

将常量按照补码解析为负数，快捷键为_键。

将常量按位取反，形如C语言中的～0xF0，快捷键为～键。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image12.png){width="5.444444444444445in"
height="6.268412073490814in"}

HexRays的快捷键有时触发不了，可以在失败时尝试使用右键快捷菜单。

**修改变量类型**

本节使用GCC编译器开启的O3优化开关后编译的可执行文件和同样源代码经过复杂编译器优化过程，生成的伪代码有很大变化比如下面这个

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image13.png){width="5.760416666666667in"
height="4.191092519685039in"}

伪代码会对开头的一些常量进行显示格式转换，事实上原来的字符串复制操作已成为了
64位qword赋值+整形+16位dword赋值。HexRays因此将原来的字符串数组划分为了三个变量，\_int64
Str2,int v5,\_int16 v6,这样导致后面生成的伪代码阅读性差

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image14.png){width="5.625in"
height="2.7708333333333335in"}

变量str2,v5,v6实际上是一整个字符串数组，如果用户能正确的制定变量类型，则反编译的可读性将大大提高

所以HexRays利用了前面的类型分析系统，给了我们一个修改类型的方法，直接点击str2按Y键,调出对话框修改类型，对于这个程序，根据计算，实际上这三个变量应该以str2开头，长度为16的字符串数组，固修改为char\[16\]或者更大的也可以

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image15.png){width="5.760416666666667in"
height="4.601351706036746in"}

然后就出来了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image16.png){width="5.760416666666667in"
height="4.464108705161855in"}

[这样代码的可读性就大大提高了。]{.mark}

HexRays不只支持局部变量的类型修改，也支持修改参数类型、函数原型、全局变量类型等。实际上，HexRays不仅支持这些简单的类型，还支持结构体、枚举等C语言类型。按Shift+F1组合键，调出Local
Types窗口，从中可以操作C的各种类型:
按nsert键，或者单击右键，弹出添加类型的对话框，见图5-2-17，从中输入符合C语言简单语法的类型后，IDA会解析并存储其中的类型。此外，按Ctr+F9组合键或选择"File一Load
File一Parse C header file"菜单命令，可以加载C语言的头文

件。

添加自定义类型后，在设置变量类型时使用这些类型，HexRays会自动根据类型进行相应的解析操作，如显示结构体的访问、显示枚举等。

在逆向过程中可能出现各种类型识别错误的情况，我们需要利用C语言编程的经验，来正确地设置结构体、普通指针、结构体指针、整型等变量。

HexRays的类型变化一般情况下可以将一个变量的长度强行增加(如上文所说的改为char\[28\])，但是将一个长的变量改短时往往会报警"Sorry，can
not change variable type"
(如将上文的char\[的变量改回char\[27\]，则会报错)，所以将变量加长时需要谨慎。如果不慎修改错误，可以删除函数后，再定义函数，以重置该函数的各种信息。

[点击字符串Shift+e就可以提取数据]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image17.png){width="5.055555555555555in"
height="5.649713473315836in"}

[汇编代码和汇编代码流程图的切换用空格切换。]{.mark}

[汇编代码流程图的时候点击F5 进行反编译，伪代码]{.mark}

这个数字

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image18.png){width="3.6527777777777777in"
height="1.2001979440069992in"}

[对着按r就可以转字符串，]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image19.png){width="2.861111111111111in"
height="1.0404035433070866in"}

[按h就会转十六进制]{.mark}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image20.png){width="2.8194444444444446in"
height="1.1799901574803149in"}

大小端：

原理

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image21.png){width="5.760416666666667in"
height="3.810275590551181in"}

例题：这个很明显这个是翻过来了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image22.png){width="2.6805555555555554in"
height="0.9282863079615048in"}

还有一些高级的调试因为接触的少就不记录了，到时候碰到再深入了解

**动态分析**

IDA调试器虽然是静态分析调试工具，可以在感兴趣地方设置断点，使得程序中断，然后一行一行跟踪设置断点，进入或者略过，在跟踪过程中查看变量的值，从而了解程序的内部状态，方便找到问题。

动态分析就是让程序运行起来，观察程序运行的各种行为。

**OllyDBG和x64DBG调试**

OllyDBG和x64DBG都是调试windows平台可执行文件的调试器，x64DBG为后起之秀，支持32位和64位，而OllyDBG只支持32位并且停止更新

看似OD没什么存在的必要了但是，因为集成了大量的实现脱壳，对抗反调试等高级功能的脚步和插件，使得没有退出历史的舞台，仍然有一席之地。

OD和X64DBG有极其相似重合的快捷键，两个放一起学习更方便。

打开文件：直接拖入

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image23.png){width="5.760416666666667in"
height="2.941412948381452in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image24.png){width="5.760416666666667in"
height="2.923410979877515in"}

**控制台运行**

按键Ctrl+G可以跳转到目标地址

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image25.png){width="5.760416666666667in"
height="3.3025470253718283in"}

在反汇编窗口按F2可以设置断点

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image26.png){width="5.760416666666667in"
height="3.2371916010498687in"}

F8是单步步过，F7为单步步入，F4为运行到光标处位置，F9为运行

**简单的脱壳**

**认识壳**

壳是在一些计算机软件里也有一段负责保护软件不被非法修改或反编译的程序，它们一般是先于程序运行，拿到控制权，然后完成他们的保护任务。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image27.png){width="5.208333333333333in"
height="3.53125in"}

由于这个和自然界的壳在功能上相似，所以命名这样的程序为壳。

**壳分类**

压缩壳

使用压缩壳，帮助缩小PE的大小，隐藏内部代码和资源，便于网络传输和保存

常见的压缩壳有：Upx,ASpack,PECompat

加密壳

使用加密壳，有多种防止代码逆向分析的技术，它的主要功能就是保护PE免受代码逆向分析。

常见的加密壳有：ASProtector,Armadillo,EXECrypto,Themida,VMProtect

**壳的加载过程**

保存入口参数：

加壳初始化的时候保存各寄存器的值

外壳执行完毕恢复各寄存器的值

最后跳到原程序执行

通常用 pushad / popad、pushfd / popfd 指令对来保存和恢复现场环境

获取所需函数 API

一般壳的输入表中只有 

GetProcAddress

GetModuleHandle  

LoadLibrary 

如果需要其他 API 函数，则通过 

LoadLibraryA(W)  

LoadLibraryExA(W) 

如果 DLL 文件已被映射到调用进程的地址空间里，就可以调用 

GetModuleHandleA(W) 

一旦 DLL 模块被加载，就可以调用 

GetProcAddress 

解密各区块数据 

处于保护源程序代码和数据的目的，一般会加密源程序文件的各个区块。在程序执行时外壳将这些区块数据解密，以让程序正常运行

外壳一般按区块加密，按区块解密，并将解密的数据放回在合适的内存位置

将这样的壳去掉就叫脱壳，由于加密壳的复杂性CTF一般不会出现，CTF最广泛的就是UPX压缩壳，支持各种平台，各种架构，使用广泛。

脱壳UPX两种办法：

静态，因为UPX本身就自带脱壳器，使用命令-d就可以了，不过有时会失败，需要切换到正确版本的UPX，Windows下内置多个UPX版本的第三方的图形化界面UPXShell工具，可以方便地切换版

动态，因为UPX开源并且修改调控的地方很多，导致官方的脱壳不了，只能自己手动脱壳，就需要详细讲讲了

可执行文件被操作系统载入后开始执行前，寄存器内会存放一些操作系统预先填充好的值，栈的数据也会被设置，壳程序要保留这些数据(状态)，以免其被壳段代码不经意间地破坏，在转交控制权前壳需要恢复这些数据，才能让原来的程序正常运行。

一般情况，以有的栈是不应发生更改的，简单的壳会将这些要保护的信息压入栈中（从栈中开辟新空间），X86的汇编指令中就有一个可以将所以32位通用寄存器的值压入栈中，那就是pushad指令，UPX也使用这个方法，这个方法叫做："保护现场"，

pushad: 将所有的32位通用寄存器压入堆栈

pusha:将所有的16位通用寄存器压入堆栈

pushfd:然后将32位标志寄存器EFLAGS压入堆栈

pushf::将的16位标志寄存器EFLAGS压入堆栈

popad:将所有的32位通用寄存器取出堆栈

popa:将所有的16位通用寄存器取出堆栈

popfd:将32位标志寄存器EFLAGS取出堆栈

popf:将16位标志寄存器EFLAGS取出堆栈

像这下面的代码，首先是将所有的通用寄存器和段寄存器的值都写入数据段中，然后执行pushfd将标志寄存器也压入栈中

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image28.png){width="5.760416666666667in"
height="2.6229352580927383in"}

于是，先单步执行pushad指令(按F8键)，再设置硬件读取断点。在OllyDBG中，右击寄存器区域，在弹出的快捷菜单中选择"Hw
break \[ESP\]"即可。x64DBG则可直接在栈窗口中利用右键快捷菜单设置。

设置完成，按F9键运行程序，再次中断在一个不同的地址，其原理就是将栈空间向上清零0x80长度，在紧跟着跳转到原代码。

详细解说看ctfer成长之路-nu1l战队.pdf。因为没遇到现在也不能实践理解不透彻。

**GDB调试器**

**IDA调试器**

**常见算法识别**

在CTF逆向中，成熟的算法是出现频率非常高的，所以如果能识别这些算法可以大大提高做逆向的速度

**特征值识别**

很多算法入TEA，Base,DES等，在运算中会使用一下有特征的常量，这些常量一般都是存在软件里，所以看到这些特征的常量就知道是什么加密算法在运算了

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image29.png){width="5.760416666666667in"
height="2.753478783902012in"}

当然那些分析工具也集成了函数和插件分析这些特征常量，如下图就是IDA用FindCrypt的KANNAL等分析出来的AES算法加密和MD5加密算法

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image30.png){width="5.760416666666667in"
height="1.6763549868766405in"}

**特征运算识别**

当特征值不足我们可以进入里面查看他们的运算特征是否符合某种算法的特征，从而分析出是使用了什么算法。

下表就是CTF中常见的算法运算特征表。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image31.png){width="5.760416666666667in"
height="3.6399759405074366in"}

**第三方库识别**

为了提升编程效率一般会使用常用的算法，选择现成的库和函数，如系统库或者第三方库，对于动态链接库，函数名的符号信息可以轻松识别出来，对于静态链接的第三方库，IDA设别起来比较困难。

字符串识别：很多第三方库有些特定的的版权信息和报错信息从而找到加密算法是什么

函数签名识别：就是看这些函数的签名，分析出

二进制对比识别：使用相同的一个库编译的二进制文件中的库函数也会存在许多相同之处。如果能够确定程序编写者使用了某个已

知库，并且我们能够获得一份含有符号且同样使用了该库的静态编译二进制文件，我们便可以利用对比的方法具体确定每个库函数

**二进制代码保护和混淆**

在显示中攻防无处不在，为了自己的程序不被逆向分析破解就要采取各种手段以防被轻松的逆向，干扰静态分析中的汇编过程。

**低于静态分析**

干扰反汇编的最简单方法就是在代码中加入花指令 所谓花指令就是:

**花指令**

隐藏掉不想被逆向分析出来的工程代码块，在真实代码中插入一下垃圾代码同时保证，原有程序正确执行，而程序无法很好的反编译出来，达到混淆的效果，花指令通常用来加大静态分析的难度。

从出题人角度构造花指令的关键思路就是使原程序逻辑不受影响，的内联代码，同时在内联代码中写入
jmp call
jet对应的机械码的汇编指令，使反汇编软件在识别的时候错误的识别为汇编指令，从而影响到反汇编的结果。

jn/jnz/jmp

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image32.png){width="5.760416666666667in"
height="2.433182414698163in"}

之前我们学过线性扫描和递归下降扫描两种，线性扫描代表就是OllyDBG和WinDBG，由于是一条一条的识别，我们可以简单的在第一条和第二条指令中插入jmp跳转指令并且加入0xE8字节。

push ebp

jmp addr1

db 0xE8

addr1:

mov ebp,esp

\...\.....

当识别完jmp addr1代码后会继续识别下面的db
0xE8,而0xE8是call指令的起始字节就会让反汇编器认为是从0xE8后开始的后面是5个字节为一条call指令从而让后续解析错误。

就是像 call \..... 原本mov ebp,esp 被拆开当做call mov
ebp什么的导致后面的正确代码都开始乱组合在一起。

对于递归下降扫描代表就是IDA，由于递归下降扫描遇到无条件跳转就会自己直接跳走，这样0xE8就会被忽略，所以我们修改一下

push ebp

jz addr1

jnz addr1

db 0xE8

addr1:

mov ebp,esp

sub esp,0x100

\...\...\...\....

递归下降扫描对于有条件跳转会进行两个都执行，所以将一条有无条件跳转改为两个有条件跳转，这样不仅不影响原来的程序也可以影响到反汇编工具分析，当反汇编工具运行完成jnz
addr1就会有一个分支来运行0xE8从而被识别成call导致后面的字节数据都乱组合起来。

在实际这些跳转都会更加隐蔽，将跳转目标代码都打乱，即乱序，从而混淆，减少被反的可能性。

比如这种

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image33.png){width="5.319444444444445in"
height="1.5854035433070865in"}

**变形**

变形就是使用其他的指令实现相同的内容。

call addr1=push addr1 ; ret

当然还可以再复杂。但是如果影响到正在使用的寄存器就得不偿失了

例题：

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image34.png){width="5.760416666666667in"
height="2.2199890638670166in"}

**破解花指令的方法**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image35.png){width="5.760416666666667in"
height="2.91457895888014in"}

将E8修改为90,因为nop翻译为机械码是144，再转换为16进制就是90H.

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image36.png){width="4.722222222222222in"
height="1.4906791338582677in"}

修改成功

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image37.png){width="5.760416666666667in"
height="2.8215780839895013in"}

点击C重新运行代码

得到flag和原有的程序

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image38.png){width="5.760416666666667in"
height="2.3976126421697286in"}

**代码自修改**

代码自修改（SMC）就是程序在执行过程中，将自己可执行代码进行修改的手段，让真正代码不被识别。

**加密**

**\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--**

**要求 **

熟悉如操作系统，汇编语言，加解密等相关知识

具有丰富的多种高级语言的编程经验

熟悉多种编译器的编译原理

较强的程序理解和逆向分析能力

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image39.png){width="5.760416666666667in"
height="2.1677679352580927in"}

等工具收集信息，并根据这些静态信息进行使用
strings/file/binwalk/stracegoogle/github 搜索

研究程序的保护方法，检查是否存在代码混淆、壳、反调试等技术，:并设法破除或绕过保护根据平台/语言选择相应反汇编/反编译器对目标软件进行静态分析，并根据一些程序特征快速定位到关键代码进行分析

结合动态调试，验证自己的静态分析猜想，在动调过程中进一步熟悉程序功能理清程序流程，根据正向算法推理逆向算法写出解题脚本，求解
flag
#### Python 反编译：pyinstxtractor工具和uncompyle6库的使用
==`pyinstxtractor.py`== 工具的下载地址：[https://sourceforge.net/projects/pyinstallerextractor/](https://sourceforge.net/projects/pyinstallerextractor/)  
或[https://download.csdn.net/download/qq_63585949/86509791?spm=1001.2014.3001.5503](https://download.csdn.net/download/qq_63585949/86509791?spm=1001.2014.3001.5503)
> `uncompyle`库为第三方库，可以使用`pip`命令安装：

```python
pip install uncompyle6
```

> `uncompyle`库为第三方库，可以使用`pip`命令安装：

```python
pip install uncompyle6
```
![[Pasted image 20231125084630.png]]
> 进入该文件夹，里面有许许多多后缀为`.dll`和`.pyd`的文件，还有一个名为`PYZ-00.pyz_extracted`的文件夹，这个文件夹里放的是程序引入的**依赖库**，如果你引入过自己其他的`.py`文件，就可以用类似的方法将依赖的`.py`文件反编译出来。

> 目录中有两个带`.pyc`后缀的文件，我们要找到那个与你的`.exe`文件同名的文件：


> （`pyinstxtractor.py`工具在2.0以前的版本，会生成两个不带后缀的文件，我们仍然是要找到那个与自己的`.exe`文件同名的文件，手动为它添加`.pyc`后缀）

> 为它添加`.pyc`后缀并用Hex编辑器打开：  
![[Pasted image 20231125084646.png]]

> 这个`.pyc`文件是没有`Magic Number`的，我们需要根据Python版本自行补全：  
> ![[Pasted image 20231125084714.png]]  
> `Magic Number`补全相关的详细操作，请见：[Python Uncompyle6 反编译工具使用 与 Magic Number 详解](http://t.csdn.cn/Q8kD8)

> 然后回到目录下，打开控制台，输入命令`uncompyle6 文件名.pyc > 文件名.py`回车执行，就可以看到目录下生成了`.py`文件了：  
> ![[Pasted image 20231125084722.png]]


怎么变成字符串，直接全选这些字符然后右键按A。

![image.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image41.png){width="5.760416666666667in"
height="4.08761811023622in"}

就变成这样了

![image.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image42.png){width="5.760416666666667in"
height="0.3525349956255468in"}

**[异或字符串]{.mark}**

python

Str= b\"DH\~mqqvqxB\^\|\|zll@Jq\~jkwpmvez{\"

Str0=b\"\"

for i in Str:

Str0 +=bytes(\[i\^ 0x1F\])

print(Str0)

C语言
```

#include \<stdio.h\>

#include \<string.h\>

int main() {

char Str\[\] = \"DHmqqvqxB\";

for (int i = 0; i \< strlen(Str); i++) {

Str\[i\] = Str\[i\] \^ 0x1F;

}

printf(\"%s\", Str);

system(\"pause\");

return 0;

}
```

##### 自定义base64加密表

```python
python

import base64

import string

str1 = "5Mc58bPHLiAx7J8ocJIlaVUxaJvMcoYMaoPMaOfg15c475tscHfM8=="

string1 =
"qvEJAfHmUYjBac+u8Ph5n9Od17FrICLX0gVtM4Qk6T2z3wNSsyoebilxWKGZpRD"
#自定义base加密表

string2 =
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\"

print(base64.b64decode(str1.translate(str.maketrans(string1,string2))))
```

**[OllyGDB工具学习]{.mark}**

调试32位的程序，动态调试

**Ghidra**

**例题**

**控制台程序**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image43.png){width="3.361111111111111in"
height="1.0926213910761156in"}

控制台输入flag,或者是输入解密内容验证成功就输出flag

**Crackme**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image44.png){width="5.760416666666667in"
height="1.1085575240594925in"}

输入验证码得到flag

**游戏**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image45.png){width="5.760416666666667in"
height="2.459681758530184in"}

完成游戏任务得到flag

**Android App**

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image46.png){width="3.8472222222222223in"
height="4.462361111111111in"}

就是验证用户名和密码是否正确，正确输出flag

**CTF逆向共同点**

就是用户输入x

然后进行数据处理

再判断是否正确

**Unity外挂攻防**

Unity引擎:

Unity是实施3D互动内容创作和运营的平台。

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image47.png){width="5.760416666666667in"
height="2.92871719160105in"}

引用场景：游戏，汽车，运输与制造，工程建设与数字城市。

**开发流程**

创建项目

导入资源

搭建场景

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image48.png){width="5.760416666666667in"
height="3.6860695538057744in"}

添加组件

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image49.png){width="5.760416666666667in"
height="2.7360837707786527in"}

编写逻辑

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image50.png){width="5.760416666666667in"
height="2.506804461942257in"}

程序测试

打包发布

1，Mono

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image51.png){width="5.760416666666667in"
height="2.7490693350831146in"}

打包的特性

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image52.png){width="5.760416666666667in"
height="1.9724146981627297in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image53.png){width="5.760416666666667in"
height="2.058581583552056in"}

2, JIT

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image54.png){width="5.760416666666667in"
height="2.592461723534558in"}

IL2CPP

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image55.png){width="5.760416666666667in"
height="2.5533934820647417in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image56.png){width="5.760416666666667in"
height="2.7979166666666666in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image57.png){width="5.760416666666667in"
height="1.7695997375328083in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image58.png){width="5.760416666666667in"
height="2.411563867016623in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image59.png){width="5.760416666666667in"
height="2.7692279090113736in"}

![截图.png](D:\tools\Tools\Obsidian\sjqyyds\sjqyyds17\附件\Reverse/media/image60.png){width="5.5in"
height="5.833333333333333in"}

**获取所需函数
API**[¶](https://yangtf.gitee.io/ctf-wiki/reverse/unpack/packer-introduction/#api)

一般壳的输入表中只有 

GetProcAddress

GetModuleHandle  

LoadLibrary 

如果需要其他 API 函数，则通过 

LoadLibraryA(W)  

LoadLibraryExA(W) 

如果 DLL 文件已被映射到调用进程的地址空间里，就可以调用 

GetModuleHandleA(W) 

一旦 DLL 模块被加载，就可以调用 

GetProcAddress 

解密各区块数据 

处于保护源程序代码和数据的目的，一般会加密源程序文件的各个区块。在程序执行时外壳将这些区块数据解密，以让程序正常运行

外壳一般按区块加密，按区块解密，并将解密的数据放回在合适的内存位置

