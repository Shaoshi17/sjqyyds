for i in $(seq 101 109)
do
s="172.16.$i.250"
echo -e "\n\n$s\n\n"
gnome-terminal -e 'nc $s 6200'
done