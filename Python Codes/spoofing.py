from scapy.all import *

a = IP() 
a.dst = '10.9.0.5' #another machine IP in our network. we will run wireshark on this machine to capture the spoofed packet.
b = ICMP()
p = a/b
send(p)