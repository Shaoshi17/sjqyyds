iptables -F
iptables -A INPUT -m multiport -p tcp  --dport 21,22,80,3306 -j ACCEPT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP
service iptables save
service iptables restart

