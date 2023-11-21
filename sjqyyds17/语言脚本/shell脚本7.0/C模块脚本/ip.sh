masscan -p$1 172.16.123.0/24 --rate 1000 > $1
masscan -p$2 172.16.123.0/24 --rate 1000 > $2
masscan -p$3 172.16.123.0/24 --rate 1000 > $3
