for i in `cat 3306.txt`
do
echo $i
mysql -h $i -uroot -proot -e 'select version();'
done
for a in `cat 21.txt`
do
echo $a
ftp -n $a <<EOF
user root 123456
ls /
bye
EOF
done
