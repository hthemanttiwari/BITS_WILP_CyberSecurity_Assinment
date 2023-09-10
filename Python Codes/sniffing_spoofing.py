from scapy.all import *

def print_pkt(pkt):
	a = IP(dst=pkt[IP].src)
	a.src = pkt[IP].dst
	a.id = 0
	a.ttl = 200
	a.tos = 0xb8
	b = pkt[ICMP]
	b.type = 'echo-reply'
	p = a/b
	send(p)

pkt = sniff(filter='icmp and not src host 10.9.0.6',prn=print_pkt)