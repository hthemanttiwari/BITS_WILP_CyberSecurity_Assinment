#!/usr/bin/python
from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(filter='icmp',prn=print_pkt)
pkt = sniff(filter='tcp and src host 23.54.112.241 and dst port 23', prn=print_pkt) 
#23.54.112.241 is ip of ynet.co.il (at this time 08.09.2023  17:29)

pkt = sniff(filter='net 216.58.0.0/16',prn=print_pkt)
# this is subnet mask of some of google servers.