# -*- coding:utf-8 -*-
#作者：少世
import base64
import pycipher
from urllib.parse import unquote
import json
#Unicode解码
def unicd():
	s=input("Unicode、输入密文:")
	print(json.loads('"%s"' % s))
#逆转字符串
def nizhuan():
	s=input("输入要逆转的字符串：")
	print(s[::-1])
#批量替换特定字符
def replace():
	m=input("输入要替换字符的字符串：")
	a=input("输入要替换的旧字符的字符：")
	b=input("输入要替换的新字符的字符：")
	print(m.replace(a, b))

# 栅栏解密
def zhalan():
	s=input("栅栏、输入密文：")
	l=int(input("输入栏数："))
	print(pycipher.Railfence(l).decipher(s))# 调用python自带的模块解密
# 仿射解密
def fanshe():
	s=input("仿射、输入密文：")
	a=int(input("输入a:"))
	b=int(input("输入b:"))
	m=1
	while True:
		if a*m%26==1:
			break
		m=m+1
	for p in s:
		if "a" <= p <= "z": # 判断是否为小写字母
			print(chr(ord("a")+(ord(p)-ord("a")-b)*m%26), end='')
		elif "A" <= p <= "Z": # 判断是否为大写字母
			print(chr(ord("A")+(ord(p)-ord("A")-b)*m%26), end='')
		else:
			print(p, end='') 
# 凯撒解密
def kaisa():
	s=input("凯撒、输入密文：")
	for i in range(1,30):
		print(i - 1,"")
		for p in s:
			if "a" <= p <= "z":
				print(chr(ord("a")+(ord(p)-ord("a")-i)%26), end='')
			elif "A" <= p <= "Z":
				print(chr(ord("A")+(ord(p)-ord("A")-i)%26), end='')
			else:
				print(p, end='')

# base85解码
def ba85():
	s=input("base85、输入密文：")
	print((base64.b85decode(s.encode('utf-8'))).decode()) # 调用python自带的模块解密
# base64解码
def ba64():
	s=input("base64、输入密文：")
	print((base64.b64decode(s.encode('utf-8'))).decode()) # 调用python自带的模块解密
# base32解码
def ba32():
	s=input("base32、输入密文：")
	print((base64.b32decode(s.encode('utf-8'))).decode()) # 调用python自带的模块解密
# base16解码
def ba16():
	s=input("base16、输入密文：")
	print((base64.b16decode(s.encode('utf-8'))).decode()) # 调用python自带的模块解密
# 十六进制转字符串
def hexs():
	s=input("十六进制转字符串、输入密文：")
	print(str(bytes.fromhex(s), 'utf-8'))
# url转字符串
def urls(): 
	s=input("url转字符串、输入密文：")
	print(unquote(s))

print("1、凯撒解密")
print("2、仿射解密")
print("3、base85解密:")
print("4、base64解密")
print("5、base32解密")
print("6、base16解密")
print("7、十六进制转字符串解密")
print("8、url编码解密")
print("9、栅栏解密")
print("10、替换字符串中旧字符解密")
print("11、逆转字符串解密")
print("12、Unicode编码解密")
s=input("根据上面对应的选项输入序号：")
if s == '1':
	kaisa()
elif s == '2':
	fanshe()
elif s == '3':
	ba85()
elif s == '4':
	ba64()
elif s == '5':
	ba32()
elif s == '6':
	ba16()
elif s == '7':
	hexs()
elif s == '8':
	urls()
elif s == '9':
	zhalan()
elif s == '10':
	replace()
elif s == '11':
	nizhuan()
elif s == '12':
	unicd()
else:
	print("输入提示的数字")
