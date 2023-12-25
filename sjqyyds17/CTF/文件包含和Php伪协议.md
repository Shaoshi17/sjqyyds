### php包含
php提供四个包含函数：include(),include_once(),require(),require_once();


## PHP伪协议
[PHP伪协议详解-CSDN博客](https://blog.csdn.net/cosmoslin/article/details/120695429)

####  php流过滤 php://filter
php://filter 是一种元封装器， 设计用于数据流打开时的筛选过滤应用。 这对于一体式（all-in-one）的文件函数非常有用，类似 readfile()、 file() 和 file_get_contents()， 在数据流内容读取之前没有机会应用其他过滤器。

简单通俗的说，==这是一个中间件，在读入或写入数据的时候对数据进行处理后输出的一个过程==
**php://filter**可以获取指定文件源码。当它与包含函数结合时，==php://filter流会被当作php文件执行。==所以我们一般对其进行编码，让其不执行。从而导致 任意文件读取。
协议参数

|名称|描述|
|---|---|
|`resource=<要过滤的数据流>`|这个参数是必须的。它指定了你要筛选过滤的数据流。|
|`read=<读链的筛选列表>`|该参数可选。可以设定一个或多个过滤器名称，以管道符（`\|`）分隔。|
|`write=<写链的筛选列表>`|该参数可选。可以设定一个或多个过滤器名称，以管道符（`\|`）分隔。|
|`<；两个链的筛选列表>`|任何没有以 `read=` 或 `write=` 作前缀 的筛选器列表会视情况应用于读或写链。|

常用：

```php
php://filter/read=convert.base64-encode/resource=index.php
php://filter/resource=index.php
```
利用filter协议读文件±，将index.php通过base64编码后进行输出。这样做的好处就是如果不进行编码，文件包含后就不会有输出结果，而是当做php文件执行了，==而通过编码后则可以读取文件源码。==
而使用的convert.base64-encode，就是一种过滤器。
#### PHP流输入 php://input



#### Data Url
