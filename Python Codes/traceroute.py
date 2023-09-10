from scapy.all import *
import time


for i in range(1,900):
	a= IP()
	a.dst = '10.9.0.5'
	a.ttl = i
	b = ICMP()
	send(a/b)
	time.sleep(3)