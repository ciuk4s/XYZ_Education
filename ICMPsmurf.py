from scapy.all import * 

icmp_request = IP(src="10.0.2.5", dst="10.0.2.255")/ICMP(type=8)

send(icmp_request, count=100, verbose=1)
