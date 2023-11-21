for i in $(seq 123 123) 

do
        fping -ag 172.16.$i.100 172.16.$i.120 >> ip.txt 

port=(21 22 23 80 445 873 1433 3306 2049 3389 6379 8080)
for i in ${port[*]}
do

masscan -p$i -iL ip.txt --rate 1000 > $i
done

done
