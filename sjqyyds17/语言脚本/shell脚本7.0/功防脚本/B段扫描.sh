for i  in $(seq 254)
do
echo $i
nmap -sS -T5 -p445  -script smb-vuln-ms17-010 172.16.$i.0/24
done
