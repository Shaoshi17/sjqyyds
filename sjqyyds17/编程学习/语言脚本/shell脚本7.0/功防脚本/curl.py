#当bash的只能执行命令的时候启用python打印好命令使用：python curl.py >> curl.sh
for x in range(256):

    print("timeout 0.01 curl http://172.16.123."+str(x)+"/flag.txt")
