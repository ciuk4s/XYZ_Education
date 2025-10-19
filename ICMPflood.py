from scapy.all import *

icmp_request = IP(dst="10.0.2.5")/ICMP(type=8)

send(icmp_request, loop=1, verbose=False)
