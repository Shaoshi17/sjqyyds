for i  in $(seq 254)
do
echo $i
masscan -p445 $i.0.0.0/8 --rate 100 >> /tmp/$i.txt
nmap -sS -T5 -p445  -script smb-vuln-ms17-010 -iL /tmp$i.txt
done
