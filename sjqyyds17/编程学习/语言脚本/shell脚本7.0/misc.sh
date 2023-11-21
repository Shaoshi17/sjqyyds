strings $1 | grep fl
foremost -T $1
steghide extract -sf $1 -p " "
outguess -r $1 -t flag.txt
binwalk -e --run-as=root  $1
zsteg $1

