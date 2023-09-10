#!/usr/bin/python

from scapy.all import *

def print_pkt(pkt): 
    pkt.show()


interfaces = ['br-387ba5533ef0','enp0s3','lo']
pkt = sniff(iface=interfaces, filter='icmp', prn=print_pkt)